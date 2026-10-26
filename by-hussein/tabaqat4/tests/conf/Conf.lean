import Jisr.Utur
import Aql.Isnad
import Jisr.BabJaza
import Jisr.BabJazaDawabit
open Jisr.Utur Aql.Isnad Aql.Mirsat Aql.Azmina Aql.Makan
namespace Conf
-- ١) إطارنا المبنيّ من خلايا المدخل = شاهد المستودع نفسه بنيةً ، وحكمه هو حكم نظرية المستودع
def ours : Itar3 := { jisr := { ud := Jisr.Mulhaqat.darabaZayd }, kalimat := [⟨[92, 4, 104], false, false⟩, ⟨[55, 112, 52, 69], true, true⟩], maani := [dhahab, walad], isnad := ⟨walad, .qabiliyya 10, .isnadiyya⟩ }
theorem ours_eq_repo : ours = dhahabaAlWalad := by decide
def ours2 : Itar3 := { jisr := { ud := Jisr.Mulhaqat.jaaRajul }, kalimat := [⟨[92, 4, 104], false, false⟩, ⟨[112, 52, 69, 59], false, false⟩], maani := [dhahab, walad], isnad := ⟨walad, .qabiliyya 10, .isnadiyya⟩ }
theorem ours2_eq_repo : ours2 = dhahabaWaladun := by decide
-- ٢) الحكم ممتنع على الولدَ كما في Utur.lean:958 — من نظرية المستودع لا من تشغيلنا
theorem mumtani_from_repo : hukm3 { dhahabaAlWalad with kalimat := [dhahaba, ⟨[55, 112, 52, 68], true, true⟩] } = .mumtani := by decide +kernel
-- والنظرية نفسها واردة في المستودع (Utur.lean:958) ضمن shahid_dhahaba_alwalad ؛ هنا أُعيد إثباتها مستقلّةً
-- ٣) الطبقة الرابعة: قيمنا = قيم Shahid_Ahmad (المرساة والعَرَض نفسهما)
def mirsat : Mirsat := ⟨0, ⟨0, 0, 0⟩⟩
def arad : Arad := .fiil 10 (-1) .saa none
def jumla4 : Jumla := .sughra ⟨20, none⟩ arad
theorem t4 : (ajza jumla4).map rutba = [.mahkum, .hakim] ∧ yastaghni jumla4 = true ∧ zamanArad mirsat arad = some .madi ∧ mawdiInda mirsat jumla4 = ⟨0, 0, 0⟩ := by decide
-- ٤) باب الجزاء: حالتا T9/T10 مقابل الضابط المجمَّد
open Jisr.BabJaza in
#eval (Jisr.BabJaza.Dawabit.halat.find? (fun h => h.jumla == (⟨"إن", .shartAwwalan, false, .mudariMajzum, .mudariMajzum⟩ : Jisr.BabJaza.Jumla))).map (fun h => (h.ism, h.kalam, h.shir))
open Jisr.BabJaza in
#eval (Jisr.BabJaza.Dawabit.halat.find? (fun h => h.jumla == (⟨"إن", .shartAwwalan, false, .mudariMajzum, .mudariMarfu⟩ : Jisr.BabJaza.Jumla))).map (fun h => (h.ism, h.fia, h.kalam, h.shir))
open Jisr.BabJaza in
#eval ((hukm ⟨"إن", .shartAwwalan, false, .mudariMajzum, .mudariMajzum⟩).kalam, (hukm ⟨"إن", .shartAwwalan, false, .mudariMajzum, .mudariMajzum⟩).shir, (hukm ⟨"إن", .shartAwwalan, false, .mudariMajzum, .mudariMarfu⟩).kalam, (hukm ⟨"إن", .shartAwwalan, false, .mudariMajzum, .mudariMarfu⟩).shir)
-- ٥) كلّ حالات الضابط الـ39 يوافقها hukm العامّ (اتساق المستودع نفسه ، نقيسه لا نفترضه)
open Jisr.BabJaza in
#eval (Jisr.BabJaza.Dawabit.halat.filter (fun h => (hukm h.jumla).kalam != h.kalam)).map (·.ism)
end Conf
#print axioms Conf.ours_eq_repo
#print axioms Conf.mumtani_from_repo
#print axioms Conf.t4
