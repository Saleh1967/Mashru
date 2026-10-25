# أثرُ تشغيلٍ على حالات ضابط باب الفاء لم يُسجَّل (2026-10-25، نحو 05:20 بتوقيت UTC)

مخرجا أداتين في جلسة المراجع المستقلّ (سجلُّه: `/root/.claude/projects/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/subagents/agent-aa293ba901479cb02.jsonl`،
غيرُ مودَع)، قرأ بهما سجلَّ الجلسة الرئيس قبل ضغطه؛ والسجلُّ الرئيس بعد الضغط يبدأ بعدها، فهذا ما بقي منها. نقلهما البنّاءُ هنا **كاملين
بلا تعديل** من السطرين 219 و223 في سجلّ المراجع، ومعهما أمرا المراجع اللذان أخرجاهما (السطران 218 و222). **والبترُ فيهما من أمرَي المراجع**
(`[-1500:]` و`[:2500]` في الأوّل، و`[:6000]` و`[:1500]` في الثاني)، لا من هذا النقل. **والمخرجان يتداخلان** (كلاهما فيه أوامرُ من الفترة نفسها)،
وترتيبُهما ترتيبُ سجلّ المراجع لا ترتيبُ الوقت.
ترتيبُ الأحداث فيهما: 05:03:31 التشغيلُ الأوّل (`natija_1.json`)؛ 05:19:38 تعديلُ الشفرة؛ 05:20:16 التشغيلُ (43/48، والإخفاقاتُ بأسمائها)؛
05:20:25 قراءةُ F09 وF31 وF35؛ 05:20:49 السحبُ والتشغيلُ بعده (46/48، وهو `natija_2.json`).

## أمرُ المراجع (السطر 218)

````
cd /root/.claude/projects/-home-claude && python3 -I - <<'EOF'
import json
lines=open('/root/.claude/projects/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe.jsonl').read().splitlines()
ids={}
for l in lines:
    d=json.loads(l); ts=d.get('timestamp','')
    if d.get('type')=='assistant':
        for x in d['message'].get('content',[]):
            if isinstance(x,dict) and x.get('type')=='tool_use':
                s=json.dumps(x['input'],ensure_ascii=False)
                if ('ev3' in s and '/fa/' in s) or ('fa/ev' in s):
                    ids[x['id']]=ts; print('=====',ts, (x['input'].get('command') or s)[-1500:])
    if d.get('type')=='user':
        c=d['message'].get('content')
        if isinstance(c,list):
            for x in c:
                if isinstance(x,dict) and x.get('type')=='tool_result' and x.get('tool_use_id') in ids:
                    cc=x.get('content')
                    if isinstance(cc,list): cc=' '.join(y.get('text','') for y in cc if isinstance(y,dict))
                    print('--- result'); print(str(cc)[:2500])
EOF
````

## مخرجُه كاملًا (السطر 219، 2026-10-25T06:47:39.527Z)

````
===== 2026-10-25T05:03:31.659Z th
       | none => []
       | some x => [(h.ism, h.fia, Haql.shir, qarin x (shir h.jumla))])

structure Ihsa where
  sawab : Nat
  naqsTaghtiya : Nat
  tajawuz : Nat
  qabulKhati : Nat
  raddKhati : Nat
  ikhtilafDaraja : Nat
  ikhtiyar : Nat
  tawaqquf : Nat
  khata : Nat
  deriving DecidableEq, Repr

def ihsa (l : List (String × Fia × Haql × Natija)) : Ihsa :=
  let c (n : Natija) := (l.filter (fun x => x.2.2.2 == n)).length
  ⟨c .sawab, c .naqsTaghtiya, c .tajawuz, c .qabulKhati, c .raddKhati, c .ikhtilafDaraja, c .ikhtiyar, c .tawaqquf, c .khata⟩

def ihsaFia (f : Fia) : Ihsa := ihsa (natayij.filter (fun x => x.2.1 == f))

/-- الإخفاقاتُ بأسمائها: (الحالة، الحقل، النتيجة). -/
def akhta : List (String × Haql × Natija) :=
  (natayij.filter (fun x => x.2.2.2 != .sawab)).map (fun x => (x.1, x.2.2.1, x.2.2.2))

def t (i : Ihsa) : List Nat :=
  [i.sawab, i.naqsTaghtiya, i.tajawuz, i.qabulKhati, i.raddKhati, i.ikhtilafDaraja, i.ikhtiyar, i.tawaqquf, i.khata]

end Qiyas
end BabFa
end Jisr
EOF
export PATH="/root/.lean/lean-4.34.1-linux/bin:$PATH"; cd $S/wt-fa && python3 -I scripts/bina_dawabit_fa.py && timeout 1200 lake build Jisr.BabFaQiyas 2>&1 | grep -v '^info\|Replayed' | tail -4 && cat > $S/fa/ev.lean <<'EOF'
import Jisr.BabFaQiyas
open Jisr.BabFa Jisr.BabFa.Qiyas Jisr.BabFa.Dawabit
#eval t (ihsa natayij)
#eval [Fia.mujib, .hadd, .kharij, .umum, .ghumud].map (fun f => t (ihsaFia f))
#eval akhta
#eval (halat.length, natayij.length)
EOF
timeout 600 lake env lean $S/fa/ev.lean
--- result
كُتب Jisr/BabFaDawabit.lean
✔ [3/4] Built Jisr.BabFaDawabit (481ms)
✔ [4/4] Built Jisr.BabFaQiyas (544ms)
Build completed successfully (4 jobs).
[38, 4, 2, 0, 0, 0, 4, 0, 0]
[[21, 2, 1, 0, 0, 0, 0, 0, 0],
 [6, 1, 0, 0, 0, 0, 0, 0, 0],
 [4, 0, 1, 0, 0, 0, 0, 0, 0],
 [5, 1, 0, 0, 0, 0, 0, 0, 0],
 [2, 0, 0, 0, 0, 0, 4, 0, 0]]
[("F12", Jisr.BabFa.Qiyas.Haql.kalam, Jisr.BabFa.Qiyas.Natija.naqsTaghtiya),
 ("F15", Jisr.BabFa.Qiyas.Haql.kalam, Jisr.BabFa.Qiyas.Natija.naqsTaghtiya),
 ("F16", Jisr.BabFa.Qiyas.Haql.kalam, Jisr.BabFa.Qiyas.Natija.tajawuz),
 ("F24", Jisr.BabFa.Qiyas.Haql.kalam, Jisr.BabFa.Qiyas.Natija.naqsTaghtiya),
 ("F26", Jisr.BabFa.Qiyas.Haql.kalam, Jisr.BabFa.Qiyas.Natija.ikhtiyar),
 ("F28", Jisr.BabFa.Qiyas.Haql.kalam, Jisr.BabFa.Qiyas.Natija.ikhtiyar),
 ("F29", Jisr.BabFa.Qiyas.Haql.kalam, Jisr.BabFa.Qiyas.Natija.ikhtiyar),
 ("F30", Jisr.BabFa.Qiyas.Haql.kalam, Jisr.BabFa.Qiyas.Natija.ikhtiyar),
 ("F32", Jisr.BabFa.Qiyas.Haql.kalam, Jisr.BabFa.Qiyas.Natija.naqsTaghtiya),
 ("F38", Jisr.BabFa.Qiyas.Haql.kalam, Jisr.BabFa.Qiyas.Natija.tajawuz)]
(39, 48)
Shell cwd was reset to /home/claude
===== 2026-10-25T05:20:16.657Z S=/tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad; cd $S/wt-fa && python3 - <<'EOF'
p='Jisr/BabFa.lean'; s=open(p,encoding='utf-8').read()
a='("laTakfur", 9023, 9025, "فلا تكفر فيتعلمون @QE@ فارتفعت لأنه لم يخبر عن الملكين أنهما قالا لا تكفر فيتعلمون")'
b='("laTakfur", 9024, 9025, "فارتفعت لأنه لم يخبر عن الملكين أنهما قالا لا تكفر فيتعلمون ليجعلا كفره سببا")'
assert s.count(a)==1; s=s.replace(a,b); open(p,'w',encoding='utf-8').write(s)
EOF
python3 -I ../chk_asanid.py Jisr/BabFa.lean 8914 9049; export PATH="/root/.lean/lean-4.34.1-linux/bin:$PATH"; timeout 900 lake build Jisr.BabFaDawabit 2>&1 | tail -1
python3 - <<'EOF'
S='/tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad'
q=open(f'{S}/wt-fa/Jisr/BabFaQiyas.lean',encoding='utf-8').read()
q=q[:q.index('/-! ## جدولُ المقارنة')].replace('namespace Qiyas','namespace QiyasEv')
q+='''
#eval t (ihsa natayij)
#eval [Fia.mujib, .hadd, .kharij, .umum, .ghumud].map (fun f => t (ihsaFia f))
#eval akhta
end QiyasEv
end BabFa
end Jisr
'''
open(f'{S}/fa/ev3.lean','w',encoding='utf-8').write(q)
EOF
cd $S/wt-fa && timeout 600 lake env lean $S/fa/ev3.lean
--- result
asanid 30 bad 0
Build completed successfully (3 jobs).
[43, 1, 2, 0, 0, 0, 1, 1, 0]
[[23, 0, 0, 0, 0, 0, 0, 1, 0],
 [7, 0, 0, 0, 0, 0, 0, 0, 0],
 [3, 0, 2, 0, 0, 0, 0, 0, 0],
 [5, 1, 0, 0, 0, 0, 0, 0, 0],
 [5, 0, 0, 0, 0, 0, 1, 0, 0]]
[("F09", Jisr.BabFa.QiyasEv.Haql.kalam, Jisr.BabFa.QiyasEv.Natija.tawaqquf),
 ("F30", Jisr.BabFa.QiyasEv.Haql.kalam, Jisr.BabFa.QiyasEv.Natija.ikhtiyar),
 ("F31", Jisr.BabFa.QiyasEv.Haql.kalam, Jisr.BabFa.QiyasEv.Natija.naqsTaghtiya),
 ("F35", Jisr.BabFa.QiyasEv.Haql.kalam, Jisr.BabFa.QiyasEv.Natija.tajawuz),
 ("F38", Jisr.BabFa.QiyasEv.Haql.kalam, Jisr.BabFa.QiyasEv.Natija.tajawuz)]
Shell cwd was reset to /home/claude
===== 2026-10-25T05:20:49.090Z `shir`).''','''- **الدعاءُ مرفوعًا مستأنفًا** شعرٌ لا كلام: شاهدُه بيتٌ («ولا زال قبر …»، س9008–9012)، فهو «لا حكم» في الكلام ومقبولٌ في الشعر (المفتاح: ما
  يستشهد به البابُ من شعرٍ مقبولٌ في `shir`). والنصبُ بعده للسبب باقٍ مقبولًا بعموم «ما انتصب في باب الفاء» (س8915).'''),
('''- **الجزمُ بعد التمنّي والعرض والواجب** خطأ: «لا يكون في هذا إلا النصب» (س8979)، و«ولا يكون في هذا الباب إلا الرفع» (س9020–9021).''','''- **الجزمُ بعد التمنّي والواجب** خطأ: «لا يكون في هذا إلا النصب» (س8979)، و«ولا يكون في هذا الباب إلا الرفع» (س9020–9021).'''),
('''- **الشركةُ رفعًا** بعد التمنّي والعرض بديلان: في الأوّل فعلٌ يُضمّ إليه («ود لو تأتيه فتحدثه والرفع جيد»، س9000) أو لا فعل («لا يكون في هذا إلا
  النصب لأن الفعل لم تضمه إلى فعل»، س8979)؛''','''- **الشركةُ رفعًا** بعد التمنّي بديلان: في الأوّل فعلٌ يُضمّ إليه («ود لو تأتيه فتحدثه والرفع جيد»، س9000) أو لا فعل («لا يكون في هذا إلا النصب
  لأن الفعل لم تضمه إلى فعل»، س8979)؛ وبعد العرض مقبولةٌ («ألا تقع الماء فتسبح إذا جعلت الآخر على الأول»، س8979–8980) كما كانت؛'''),
('''    شعرٌ لا كلام، والجزمُ بعد التمنّي والواجب خطأ،''','''    مستأنفًا شعرٌ لا كلام، والجزمُ بعد التمنّي والواجب خطأ،'''),
]
for a,b in rep:
    assert s.count(a)==1,a[:60]; s=s.replace(a,b)
open(p,'w',encoding='utf-8').write(s)
EOF
grep -n 'والدعاءُ\|الدعاءُ$\|الدعاءُ ' Jisr/BabFa.lean | head; export PATH="/root/.lean/lean-4.34.1-linux/bin:$PATH"; timeout 900 lake build Jisr.BabFaDawabit 2>&1 | grep -v '^info\|Replayed'| tail -3; timeout 600 lake env lean $S/fa/ev3.lean
--- result
35:- **الدعاءُ مرفوعًا مستأنفًا** شعرٌ لا كلام: شاهدُه بيتٌ («ولا زال قبر …»، س9008–9012)، فهو «لا حكم» في الكلام ومقبولٌ في الشعر (المفتاح: ما
221:/-- **ما غُيّر بعد قراءة الحالات** (على الشاهد): الرفعُ مستأنفًا بعد النهي («فلا تكفر فيتعلمون»)، والرفعُ بعد استفهام التنبيه، والدعاءُ
✔ [2/3] Built Jisr.BabFa (1.4s)
✔ [3/3] Built Jisr.BabFaDawabit (481ms)
Build completed successfully (3 jobs).
[46, 0, 1, 0, 0, 0, 1, 0, 0]
[[24, 0, 0, 0, 0, 0, 0, 0, 0],
 [7, 0, 0, 0, 0, 0, 0, 0, 0],
 [4, 0, 1, 0, 0, 0, 0, 0, 0],
 [6, 0, 0, 0, 0, 0, 0, 0, 0],
 [5, 0, 0, 0, 0, 0, 1, 0, 0]]
[("F30", Jisr.BabFa.QiyasEv.Haql.kalam, Jisr.BabFa.QiyasEv.Natija.ikhtiyar),
 ("F38", Jisr.BabFa.QiyasEv.Haql.kalam, Jisr.BabFa.QiyasEv.Natija.tajawuz)]
Shell cwd was reset to /home/claude
````

## أمرُ المراجع (السطر 222)

````
cd /root/.claude/projects/-home-claude && python3 -I - <<'EOF'
import json
lines=open('/root/.claude/projects/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe.jsonl').read().splitlines()
for l in lines:
    d=json.loads(l); ts=d.get('timestamp','')
    if d.get('type')=='assistant' and ts.startswith(('2026-10-25T05:19:38','2026-10-25T05:20:49','2026-10-25T05:20:25')):
        for x in d['message'].get('content',[]):
            if isinstance(x,dict) and x.get('type')=='tool_use':
                print('=====',ts); print(x['input'].get('command')[:6000])
            if isinstance(x,dict) and x.get('type')=='text': print('TEXT',x['text'][:1500])
    if d.get('type')=='assistant' and '2026-10-25T05:03:41'<=ts<='2026-10-25T05:21:00':
        for x in d['message'].get('content',[]):
            if isinstance(x,dict) and x.get('type')=='text': print('TEXT',ts,x['text'][:1500])
EOF
````

## مخرجُه كاملًا (السطر 223، 2026-10-25T06:47:55.444Z)

````
===== 2026-10-25T05:19:38.173Z
S=/tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad; cd $S/wt-fa && python3 - <<'EOF'
p='Jisr/BabFa.lean'; s=open(p,encoding='utf-8').read()
rep=[
('''def rafShirka : Sadr → List Daraja
  | .nafyMaMudari | .nafyMaMadi | .wajib | .ard | .tamanni | .istifham | .zann => [.maqbul]''','''def rafShirka : Sadr → List Daraja
  | .nafyMaMudari | .wajib | .istifham | .zann => [.maqbul]
  | .nafyMaMadi => [.maqbul, .daif]
  | .ard | .tamanni => [.maqbul, .khata]'''),
('''def jazmShirka : Sadr → Daraja
  | .nahy | .istifham | .tashbihNafy | .nafyLam => .maqbul
  | .amr => .khata
  | _ => .laHukm''','''def jazmShirka : Sadr → Daraja
  | .nahy | .istifham | .tashbihNafy | .nafyLam => .maqbul
  | .amr | .ard | .tamanni | .wajib => .khata
  | _ => .laHukm'''),
('''def rafQat : Sadr → Daraja
  | .nafyMaMudari | .nafyMaMadi | .nafyLam | .nafyIsmi | .amr | .dua | .istifham | .wajib => .maqbul''','''def rafQat : Sadr → Daraja
  | .nafyMaMudari | .nafyMaMadi | .nafyLam | .nafyIsmi | .amr | .istifham | .wajib | .nahy => .maqbul'''),
('''def kalamMuallan (s : Sadr) : Mana → Irab → List Daraja
  | .sabab, .nasb => [nasbSabab s]''','''def kalamMuallan (s : Sadr) : Mana → Irab → List Daraja
  | .sabab, .nasb => if s = .zann then [.maqbul, .khata] else if s = .dua then [.laHukm] else [nasbSabab s]
  | .sabab, .raf => if s = .istifham then [.maqbul] else [.laHukm]'''),
('''  | _, .jazm => if s = .amr then [.khata] else [.laHukm]''','''  | _, .jazm => if s = .amr || s = .ard || s = .tamanni || s = .wajib then [.khata] else [.laHukm]'''),
('''  | .ghayrMuallan, .nasb => if j.sadr = .zann then [.maqbul, .khata] else kalamMuallan j.sadr .sabab .nasb''','''  | .ghayrMuallan, .nasb => kalamMuallan j.sadr .sabab .nasb'''),
('''def shir (j : Jumla) : List Daraja :=
  let k := kalam j
  if k.contains .maqbul then [.maqbul]
  else if j.sadr = .wajib && j.irab = .nasb && j.mana != .shirka && j.mana != .qat then [.maqbul]
  else [.laHukm]''','''def shir (j : Jumla) : List Daraja :=
  let k := kalam j
  if k.contains .maqbul then [.maqbul]
  else if j.sadr = .wajib && j.irab = .nasb && j.mana != .shirka && j.mana != .qat then [.maqbul]
  else if j.sadr = .dua && ((j.irab = .raf && (j.mana = .qat || j.mana = .ghayrMuallan)) ||
      (j.irab = .nasb && (j.mana = .sabab || j.mana = .ghayrMuallan))) then [.maqbul]
  else [.laHukm]'''),
]
for a,b in rep:
    assert s.count(a)==1,a[:60]; s=s.replace(a,b)
# theorems
a='''theorem ghamid_shawahid :
    kalam ⟨.zann, .ghayrMuallan, .nasb⟩ = [.maqbul, .khata] ∧
    kalam ⟨.nafyLa, .shirka, .raf⟩ = [.maqbul, .qabih] ∧
    ghamid ⟨.zann, .ghayrMuallan, .nasb⟩ = true := by
  decide'''
b='''theorem ghamid_shawahid :
    kalam ⟨.zann, .ghayrMuallan, .nasb⟩ = [.maqbul, .khata] ∧
    kalam ⟨.nafyLa, .shirka, .raf⟩ = [.maqbul, .qabih] ∧
    ghamid ⟨.zann, .ghayrMuallan, .nasb⟩ = true := by
  decide

/-- **ما غُيّر بعد قراءة الحالات** (على الشاهد): الرفعُ مستأنفًا بعد النهي («فلا تكفر فيتعلمون»)، والرفعُ بعد استفهام التنبيه، والدعاءُ
    شعرٌ لا كلام، والجزمُ بعد التمنّي والواجب خطأ، والظنُّ نصبًا للسبب بديلان، والشركةُ رفعًا بعد التمنّي وبعد «ما» والماضي بديلان. -/
theorem baad_qiraa :
    kalam ⟨.nahy, .qat, .raf⟩ = [.maqbul] ∧ kalam ⟨.istifham, .sabab, .raf⟩ = [.maqbul] ∧
    hukm ⟨.dua, .qat, .raf⟩ = ⟨[.laHukm], [.maqbul]⟩ ∧ kalam ⟨.tamanni, .ghayrMuallan, .jazm⟩ = [.khata] ∧
    kalam ⟨.wajib, .ghayrMuallan, .jazm⟩ = [.khata] ∧ kalam ⟨.zann, .sabab, .nasb⟩ = [.maqbul, .khata] ∧
    kalam ⟨.tamanni, .shirka, .raf⟩ = [.maqbul, .khata] ∧ kalam ⟨.nafyMaMadi, .shirka, .raf⟩ = [.maqbul, .daif] := by
  decide'''
assert s.count(a)==1; s=s.replace(a,b)
# nasb_ghayr_wajib now false for zann & dua: restrict
a='''/-- **النصبُ للسبب مقبولٌ في كلّ صدرٍ غيرِ واجب** (تعريفيّة). -/
theorem nasb_ghayr_wajib (s : Sadr) (h : wajib s = false) : kalam ⟨s, .sabab, .nasb⟩ = [.maqbul] := by
  cases s <;> simp_all [wajib, kalam, kalamMuallan, nasbSabab]'''
b='''/-- **النصبُ للسبب مقبولٌ في كلّ صدرٍ غيرِ واجب** إلّا الظنَّ (بديلان) والدعاءَ (شعرٌ لا كلام) (تعريفيّة؛ وكان قبل قراءة الحالات بلا
    استثناء). -/
theorem nasb_ghayr_wajib (s : Sadr) (h : wajib s = false) (hz : s ≠ .zann) (hd : s ≠ .dua) :
    kalam ⟨s, .sabab, .nasb⟩ = [.maqbul] := by
  cases s <;> simp_all [wajib, kalam, kalamMuallan, nasbSabab]'''
assert s.count(a)==1; s=s.replace(a,b)
open(p,'w',encoding='utf-8').write(s)
EOF
export PATH="/root/.lean/lean-4.34.1-linux/bin:$PATH"; timeout 1200 lake build Jisr.BabFa 2>&1 | grep -v '^info\|Replayed' | tail -15
===== 2026-10-25T05:20:25.656Z
S=/tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad; python3 -c "
import json
for x in json.load(open('$S/wt-fa/tahaqquq/dawabit/fa/cases.json')):
  if x['id'] in ('F09','F31','F35'): print(x['id'],x['fia'],x['mithal'],json.dumps(x['dakhil'],ensure_ascii=False),json.dumps(x['kharij'],ensure_ascii=False),[q['satr'] for q in x['sanad']],x['taliq'])
"
===== 2026-10-25T05:20:49.090Z
S=/tmp/claude-0/-home-claude/9fe1b599-e71e-5040-b7e8-33e9d9b2fbfe/scratchpad; cd $S/wt-fa && python3 - <<'EOF'
p='Jisr/BabFa.lean'; s=open(p,encoding='utf-8').read()
rep=[
('''  | .nafyMaMudari | .wajib | .istifham | .zann => [.maqbul]
  | .nafyMaMadi => [.maqbul, .daif]
  | .ard | .tamanni => [.maqbul, .khata]''','''  | .nafyMaMudari | .wajib | .istifham | .zann | .ard => [.maqbul]
  | .nafyMaMadi => [.maqbul, .daif]
  | .tamanni => [.maqbul, .khata]'''),
('''  | .amr | .ard | .tamanni | .wajib => .khata''','''  | .amr | .tamanni | .wajib => .khata'''),
('''  | .sabab, .nasb => if s = .zann then [.maqbul, .khata] else if s = .dua then [.laHukm] else [nasbSabab s]''','''  | .sabab, .nasb => if s = .zann then [.maqbul, .khata] else [nasbSabab s]'''),
('''  | _, .jazm => if s = .amr || s = .ard || s = .tamanni || s = .wajib then [.khata] else [.laHukm]''','''  | _, .jazm => if s = .amr || s = .tamanni || s = .wajib then [.khata] else [.laHukm]'''),
('''  else if j.sadr = .dua && ((j.irab = .raf && (j.mana = .qat || j.mana = .ghayrMuallan)) ||
      (j.irab = .nasb && (j.mana = .sabab || j.mana = .ghayrMuallan))) then [.maqbul]''','''  else if j.sadr = .dua && j.irab = .raf && (j.mana = .qat || j.mana = .ghayrMuallan) then [.maqbul]'''),
('''theorem nasb_ghayr_wajib (s : Sadr) (h : wajib s = false) (hz : s ≠ .zann) (hd : s ≠ .dua) :''','''theorem nasb_ghayr_wajib (s : Sadr) (h : wajib s = false) (hz : s ≠ .zann) :'''),
('''/-- **النصبُ للسبب مقبولٌ في كلّ صدرٍ غيرِ واجب** إلّا الظنَّ (بديلان) والدعاءَ (شعرٌ لا كلام) (تعريفيّة؛ وكان قبل قراءة الحالات بلا
    استثناء). -/''','''/-- **النصبُ للسبب مقبولٌ في كلّ صدرٍ غيرِ واجب** إلّا الظنَّ (بديلان) (تعريفيّة؛ وكان قبل قراءة الحالات بلا استثناء). -/'''),
('''- **الدعاء** شعرٌ لا كلام: شاهدُه بيتٌ («ولا زال قبر …»، س9008–9012)، فالرفعُ مستأنفًا والنصبُ «لا حكم» في الكلام ومقبولان في الشعر (المفتاح:
  ما يستشهد به البابُ من شعرٍ مقبولٌ في `shir`).''','''- **الدعاءُ مرفوعًا مستأنفًا** شعرٌ لا كلام: شاهدُه بيتٌ («ولا زال قبر …»، س9008–9012)، فهو «لا حكم» في الكلام ومقبولٌ في الشعر (المفتاح: ما
  يستشهد به البابُ من شعرٍ مقبولٌ في `shir`). والنصبُ بعده للسبب باقٍ مقبولًا بعموم «ما انتصب في باب الفاء» (س8915).'''),
('''- **الجزمُ بعد التمنّي والعرض والواجب** خطأ: «لا يكون في هذا إلا النصب» (س8979)، و«ولا يكون في هذا الباب إلا الرفع» (س9020–9021).''','''- **الجزمُ بعد التمنّي والواجب** خطأ: «لا يكون في هذا إلا النصب» (س8979)، و«ولا يكون في هذا الباب إلا الرفع» (س9020–9021).'''),
('''- **الشركةُ رفعًا** بعد التمنّي والعرض بديلان: في الأوّل فعلٌ يُضمّ إليه («ود لو تأتيه فتحدثه والرفع جيد»، س9000) أو لا فعل («لا يكون في هذا إلا
  النصب لأن الفعل لم تضمه إلى فعل»، س8979)؛''','''- **الشركةُ رفعًا** بعد التمنّي بديلان: في الأوّل فعلٌ يُضمّ إليه («ود لو تأتيه فتحدثه والرفع جيد»، س9000) أو لا فعل («لا يكون في هذا إلا النصب
  لأن الفعل لم تضمه إلى فعل»، س8979)؛ وبعد العرض مقبولةٌ («ألا تقع الماء فتسبح إذا جعلت الآخر على الأول»، س8979–8980) كما كانت؛'''),
('''    شعرٌ لا كلام، والجزمُ بعد التمنّي والواجب خطأ،''','''    مستأنفًا شعرٌ لا كلام، والجزمُ بعد التمنّي والواجب خطأ،'''),
]
for a,b in rep:
    assert s.count(a)==1,a[:60]; s=s.replace(a,b)
open(p,'w',encoding='utf-8').write(s)
EOF
grep -n 'والدعاءُ\|الدعاءُ$\|الدعاءُ ' Jisr/BabFa.lean | head; export PATH="/root/.lean/lean-4.34.1-linux/bin:$PATH"; timeout 900 lake build Jisr.BabFaDawabit 2>&1 | grep -v '^info\|Replayed'| tail -3; timeout 600 lake env lean $S/fa/ev3.lean
````
