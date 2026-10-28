#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""يربط الحالاتِ المجمَّدة (tahaqquq/dawabit/qabiliyya_jins/halat.json) ببرهان Jisr/QabiliyyaJins.lean:
(١) بصمةُ halat.json = المثبَّتة في tajmid.json (لم تُغيَّر بعد التجميد) ؛
(٢) كلُّ حالةٍ مجمَّدةٍ ممثَّلةٌ حرفيًّا في نظرية shawahid_jins (لا إسقاطَ صامت) — وصحّتُها يبرهنها `decide` في Lean.
لا يبني Lean هنا: البرهانُ في Audit/البوّابة ؛ هذا يحرس مطابقةَ المجمَّد للمعروض."""
import sys, json, hashlib, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HALAT = ROOT / 'tahaqquq' / 'dawabit' / 'qabiliyya_jins' / 'halat.json'
TAJMID = ROOT / 'tahaqquq' / 'dawabit' / 'qabiliyya_jins' / 'tajmid.json'
LEAN = ROOT / 'Jisr' / 'QabiliyyaJins.lean'

QMAP = {'insan': '.insan', 'hayawan': '.hayawan', 'nabat': '.nabat', 'jamad': '.jamad'}


def main():
    sha = hashlib.sha256(HALAT.read_bytes()).hexdigest()
    frozen = json.loads(TAJMID.read_text(encoding='utf-8'))['halat_sha256']
    if sha != frozen:
        print(f'HALAT_SHA_MISMATCH: {sha} != {frozen} (الحالاتُ المجمَّدة تغيّرت)'); return 1
    halat = json.loads(HALAT.read_text(encoding='utf-8'))['halat']
    src = LEAN.read_text(encoding='utf-8')
    m = re.search(r'theorem shawahid_jins\s*:(.*?):=\s*by\s*\n\s*decide', src, re.S)
    if not m:
        print('SHAWAHID_JINS_NOT_FOUND'); return 1
    block = m.group(1)
    missing = []
    for h in halat:
        line = f"hukmMadlul ⟨Tayin.ilaMadlul {QMAP[h['qism']]}, .qabiliyya {h['code']}, .{h['nisba']}⟩ = .{h['hukm']}"
        if line not in block:
            missing.append((h['id'], line))
    if missing:
        for i, l in missing[:5]:
            print(f'CASE_NOT_IN_PROOF: {i} :: {l}')
        return 1
    print(f'QABILIYYA_JINS_FROZEN_BOUND = YES ({len(halat)}/{len(halat)} حالة ممثَّلة ، البصمة مطابقة)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
