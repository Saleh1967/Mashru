#!/bin/bash
# تثبيت Lean 4.34.1 (elan) إن لم يكن موجودًا. يصلح لسكربت إعداد البيئة السحابية ولـ CI ولجهاز المالك.
# المصدر الأوّل elan؛ والبديل عند تعذّره أرشيف GitHub الرسميّ ببصمة SHA-256 مثبتة قبل الاستخراج.
# التنزيل HTTPS فقط بمهلات ومحاولات محدودة، وملفّاته في مجلّد مؤقّت خاصّ يُنظَّف عند الخروج.
set -u
TC="leanprover/lean4:v4.34.1"
export PATH="$HOME/.elan/bin:$HOME/.lean/lean-4.34.1-linux/bin:$PATH"
ready() {
  timeout 30 lean --version 2>/dev/null | grep -Eq 'version 4\.34\.1([, )]|$)' &&
    timeout 30 lake --version >/dev/null 2>&1
}
if ready; then
  echo "Lean 4.34.1 موجود"; exit 0
fi
WORK=$(mktemp -d "${TMPDIR:-/tmp}/mashru-lean.XXXXXX") || exit 1
trap 'rm -rf -- "$WORK"' EXIT
trap 'exit 130' INT
trap 'exit 143' TERM
trap 'exit 129' HUP
download() {
  curl --proto '=https' --proto-redir '=https' --tlsv1.2 -fsSL \
    --connect-timeout 15 --max-time 900 --retry 2 --retry-max-time 1800 \
    "$1" -o "$2"
}
if command -v elan >/dev/null 2>&1; then
  timeout 180 elan toolchain install "$TC" && timeout 30 elan default "$TC" && ready && exit 0
fi
if download https://raw.githubusercontent.com/leanprover/elan/9605b24b08cf68b78dce0014b6fa01be1f8e2cee/elan-init.sh "$WORK/elan-init.sh"; then
  timeout 180 sh "$WORK/elan-init.sh" -y --default-toolchain "$TC" &&
    timeout 180 elan toolchain install "$TC" && timeout 30 elan default "$TC" && ready && exit 0
fi
echo "لم يجهز Lean عبر elan؛ البديل: أرشيف الإصدار من github.com" >&2
URL="https://github.com/leanprover/lean4/releases/download/v4.34.1/lean-4.34.1-linux.zip"
# digest المنشور للأصل lean-4.34.1-linux.zip في إصدار leanprover/lean4 v4.34.1.
SHA256="3013aba02bb8bf31b1cf8c9d956d60fb95bb1c10920dfe91abcaa59cb461ddac"
if ! download "$URL" "$WORK/lean.zip"; then
  echo "فشل تنزيل أرشيف Lean الرسمي" >&2; exit 1
fi
if ! printf '%s  %s\n' "$SHA256" "$WORK/lean.zip" | sha256sum --check --status; then
  echo "بصمة أرشيف Lean غير مطابقة؛ رُفض قبل الاستخراج" >&2; exit 1
fi
if mkdir -p "$HOME/.lean" && python3 - "$WORK/lean.zip" <<'PY'
import zipfile,os,sys
z=zipfile.ZipFile(sys.argv[1]); z.extractall(os.path.expanduser('~/.lean'))
for i in z.infolist():
    p=os.path.join(os.path.expanduser('~/.lean'), i.filename)
    if i.external_attr >> 16: os.chmod(p, (i.external_attr >> 16) & 0o777)
PY
then
  if command -v elan >/dev/null 2>&1; then
    timeout 30 elan toolchain link "$TC" "$HOME/.lean/lean-4.34.1-linux" &&
      timeout 30 elan default "$TC" || exit 1
  fi
  ready || exit 1
  echo 'export PATH="$HOME/.elan/bin:$HOME/.lean/lean-4.34.1-linux/bin:$PATH"' >> "$HOME/.bashrc" || exit 1
  echo "ثُبّت في ~/.lean"; exit 0
fi
echo "فشل تثبيت Lean" >&2; exit 1
