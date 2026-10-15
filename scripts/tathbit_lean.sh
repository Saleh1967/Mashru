#!/bin/bash
# تثبيت Lean 4.34.1 (elan) إن لم يكن موجودًا. يصلح لسكربت إعداد البيئة السحابية ولـ CI ولجهاز المالك.
# المصدر الأوّل elan (يحتاج raw.githubusercontent.com وrelease-assets.githubusercontent.com، وكلاهما في قائمة Trusted)،
# والبديل: أرشيف الإصدار من github.com مباشرة (يكفي إن حُجب raw.githubusercontent.com).
set -u
TC="leanprover/lean4:v4.34.1"
if command -v lake >/dev/null 2>&1 && lean --version 2>/dev/null | grep -q "4.34.1"; then
  echo "Lean 4.34.1 موجود"; exit 0
fi
export PATH="$HOME/.elan/bin:$PATH"
if command -v elan >/dev/null 2>&1; then
  elan toolchain install "$TC" && elan default "$TC" && exit 0
fi
if curl -fsSL --retry 2 https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -o /tmp/elan-init.sh; then
  sh /tmp/elan-init.sh -y --default-toolchain "$TC" && exit 0
fi
echo "elan غير متاح؛ البديل: أرشيف الإصدار من github.com" >&2
URL="https://github.com/leanprover/lean4/releases/download/v4.34.1/lean-4.34.1-linux.zip"
mkdir -p "$HOME/.lean" && curl -fsSL --retry 2 "$URL" -o /tmp/lean.zip && python3 -c "
import zipfile,os,sys
z=zipfile.ZipFile('/tmp/lean.zip'); z.extractall(os.path.expanduser('~/.lean'))
for i in z.infolist():
    p=os.path.join(os.path.expanduser('~/.lean'), i.filename)
    if i.external_attr >> 16: os.chmod(p, (i.external_attr >> 16) & 0o777)
" && echo 'export PATH="$HOME/.lean/lean-4.34.1-linux/bin:$PATH"' >> "$HOME/.bashrc" && echo "ثُبّت في ~/.lean" && exit 0
echo "فشل تثبيت Lean" >&2; exit 1
