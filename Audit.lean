import Jisr.Nabt
import Dal.Khaliya
import Dal.AqsamAllafz
import Madlul.Dalala
import Madlul.AqsamAlmadlul
import Madlul.Tayin
import Madlul.Tashfir
import Madlul.TashfirSullam
import Madlul.TashfirMadda
import Madlul.TashfirKhawass
import Madlul.TashfirNas
import Madlul.Wiratha
import Madlul.Jamad
import Madlul.Shabaka
import Madlul.Hawass
import Aql.Awwaliyyat
import Aql.TashfirAwwaliyyat
import Aql.Azmina
import Aql.TashfirAzmina
import Aql.Makan
import Aql.TashfirMakan
import Aql.Mirsat
import Aql.TashfirMirsat
import Aql.Isnad
import Jisr.JisrDal
import Jisr.JisrDalUtur
import Jisr.QiraaSimat
import Jisr.KhulasaIkhbar
import Jisr.NisabAsnaf
import Jisr.TartibMamul
import Jisr.AqsamDalMadlul
import Jisr.Tawafuq
import Dal.AqsamAlism
import Jisr.TasnifAlism
import Aql.Aqliyya
import Aql.Qaida
import Aql.Badiha
import Aql.SababShartMani
import Aql.AdawatMaani
import Aql.Mawsua
import Aql.Idaa
import Aql.QawaninDalala
import Aql.Naql
import Aql.Maratib
import Aql.AlaqaMajaz
import Aql.SalamaMaqbul
import Dal.Tamthil
import Dal.Makharij
import Dal.Qanun
import Dal.Jumla
import Jisr.Awamil
import Jisr.Tarkib
import SLGE.Kull
import SLGE.Awamil
import Jisr.Nisab
import Jisr.Ikhbar
import Jisr.AqsamAwamil
import Jisr.Mulhaqat
import Jisr.Utur
import Jisr.JadwalLuzum
import Madlul.JadwalLuzum
import Madlul.JadwalLuzumNaql
import Madlul.Naht
import Nizam.Asas
import Nizam.Talab
import Faahis.Lib
import Nizam.Damj
import Nizam.Aqd
import Nizam.Phi
import Madlul.Ishtirak
import Madlul.Tarjih
import Jisr.Iqtiran
import Jisr.MantuqMafhum
import Jisr.QaydMafhum
import Jisr.BabJaza
import Jisr.BabJazaQiyas
import Madlul.TashfirHawass
import Madlul.TashfirShabaka
import Madlul.Fard116Shawahid
import Jisr.QawaidSitta
import Dal.Adad
import Nizam.QawaidB
import Nizam.Baqi
import Aql.Waqi
import Aql.WaqiShawahid
import Nizam.Qiyas
import Jisr.NafyFil
import Jisr.NafyFilQiyas
import Jisr.BabFa
import Jisr.BabFaQiyas
import Jisr.MajariKalim
import Jisr.MajariKalimQiyas
import Dal.WaqfSibawayhi
import Dal.WaqfSibawayhiQiyas
import Jisr.BaqiJaza
import Jisr.BaqiJazaQiyas
import Jisr.NassItar
import Jisr.NassItarDabit
import Jisr.NassItarQiyas
import Jisr.SakkJumla
import Jisr.SakkJumlaQiyas
import SLGE.Core
import SLGE.Count
import SLGE.Hamza
import SLGE.Ladder
import SLGE.Law
import SLGE.Root
import SLGE.Syllable
import Madlul.TasisDalala
import Nizam.Shahada
import Dal.Tahsil
import Dal.QiraaTahsil
import Jisr.Abniya
import Jisr.AbniyaDabit
import Jisr.AbniyaQiyas
import Jisr.IntrubiyaShahada
import Jisr.TabaqatQawaid
import Jisr.IbdalAlfiyyaQiyas
import Jisr.Mawsul
import Jisr.MawsulDabit
import Jisr.MawsulQiyas
import Jisr.Ishara
import Jisr.IsharaDabit
import Jisr.IsharaQiyas
import Jisr.Khabar
import Jisr.KhabarDabit
import Jisr.KhabarQiyas
import Jisr.Damir
import Jisr.DamirDabit
import Jisr.DamirQiyas

-- المرحلة ١: الدال وحده
#print axioms Dal.n_injective
#print axioms Dal.n_surjective
#print axioms Dal.NawDalala.kull_hasir
#print axioms Dal.NawDalala.kull_nodup
#print axioms Dal.QismMufrad.kull_hasir
#print axioms Dal.QismMurakkab.kull_hasir
-- المرحلة ٢: المدلول وحده
#print axioms Madlul.QismMadlul.kull_hasir
#print axioms Madlul.QismMadlul.kull_nodup
#print axioms Madlul.QismMadlul.khamsa
#print axioms Dalala.dakhil_mutabaqa_or_tadammun
#print axioms Dalala.no_witness_no_dalala
-- الثلاث المأذونة في الجلسة 2026-10-25 (23:07): مبنيّةٌ ومسلّماتُها تُطبع في ملفّها، ولم تكن هنا
#print axioms Dalala.iltizam_needs_mutabaqa
#print axioms Dalala.iltizam_needs_luzum_table
#print axioms Dalala.mutabaqa_without_tadammun
-- المرحلة ٣: الدال والمدلول معًا
#print axioms Jisr.tasnif_fi_kull
#print axioms Jisr.tasnif_mustawfa
#print axioms Jisr.haqiqa_majaz_shart
#print axioms Jisr.tahaqquq_wahid
#print axioms Jisr.tahaqquq_hasir
#print axioms Jisr.mantuq_iff
#print axioms Jisr.mafhum_iff
#print axioms Jisr.mantuq_mafhum_la_yajtamian
#print axioms Jisr.la_tahaqquq_bila_madda
-- تقسيم الاسم (ج3 745–749)
#print axioms Dal.QismIsm.kull_hasir
#print axioms Dal.QismIsm.kull_nodup
#print axioms Dal.QismIsm.sitta
#print axioms Jisr.kulli_iff
#print axioms Jisr.mushtaq_iff
#print axioms Jisr.alam_iff
#print axioms Jisr.juzi_la_yaqra_sifat_kulli
#print axioms Jisr.kulli_la_yaqra_iftiqar
#print axioms Jisr.tasnifIsm_mustawfa
-- العقل والعقلية (التفكير 37–65؛ ج1 27–57)
#print axioms Aql.la_hukm_bila_waqi
#print axioms Aql.la_hukm_bila_hiss
#print axioms Aql.la_hukm_bila_dimagh
#print axioms Aql.la_hukm_bila_maalumat
#print axioms Aql.ghayr_mutaalliq_la_yufassir
#print axioms Aql.la_aql_bila_taalluq
#print axioms Aql.takrar_la_yunshi_fikran
#print axioms Aql.kull_hukm_min_alqaida
#print axioms Aql.ikhtilaf_alaqliyyat
#print axioms Aql.qaida_wahida_mutasiqa
#print axioms Aql.taaddud_alqawaid_la_lawn
#print axioms Aql.haqiqa_zanniyya
#print axioms Aql.la_mafhum_bila_shahid
-- مثالُ قاعدة العقليّة من فاحص المحرّك: إذا بُنيت به فلا حكمَ إلّا ما يقبله Qaida.maqbul، وأحكامُها تُعبَّأ في جوابٍ واحد (قرار المالك 2026-10-21)
#print axioms Aql.aqliyya_maqbula
#print axioms Aql.aqliyya_murakhkhasa
#print axioms Aql.aqliyya_jawab
#print axioms Aql.iqtirah_la_yahkum
#print axioms Aql.shahid_aqliyya_murakhkhasa
-- قاعدة المحرّك: الجبر المرخَّص (ج1 29، 57)
#print axioms Qaida.tatbiq_sahih
#print axioms Qaida.fahs_sahih
#print axioms Qaida.maqbul_murakhkhas
#print axioms Qaida.jawab_sahih
#print axioms Qaida.ziyada_la_tusqit
#print axioms Qaida.rutba_sifr_asl
#print axioms Qaida.shahid_maqbul
#print axioms Qaida.shahid_marfud_tartib
#print axioms Qaida.shahid_marfud_asl
-- الخطوةُ بمحتوى القانون: فاحصان متكافئان في اللقطة، والسلسلةُ تبقى مقبولةً بزيادة القوانين وإعادة ترتيبها (قرار المالك 2026-10-21)
#print axioms Qaida.tatbiqM_sahih
#print axioms Qaida.fahsM_sahih
#print axioms Qaida.maqbulM_murakhkhas
#print axioms Qaida.tatbiq_tarjama
#print axioms Qaida.fahs_tarjama
#print axioms Qaida.fahs_tarjama_none
#print axioms Qaida.maqbul_tarjama
#print axioms Qaida.tatbiqM_ihtiwa
#print axioms Qaida.fahsM_ihtiwa
#print axioms Qaida.maqbulM_ihtiwa
#print axioms Qaida.maqbulM_tartib
#print axioms Qaida.maqbul_naql
#print axioms Qaida.tatbiqM_min_tatbiq
#print axioms Qaida.fahsM_min_fahs
#print axioms Qaida.maqbulM_min_maqbul
#print axioms Qaida.maqbul_takafu
#print axioms Qaida.shahid_raqm_yabtul
#print axioms Qaida.shahid_muhtawa_yabqa
#print axioms Badiha.la_dhaka_bila_intibah
#print axioms Badiha.la_dhaka_bila_maalumat
#print axioms Badiha.la_badiha_fi_alahkam
#print axioms Badiha.aali_bila_dars
#print axioms Badiha.mufajaa_dayyiqa_badiha
#print axioms Badiha.masarSari_sahih
#print axioms Badiha.badiha_min_idrak
#print axioms Badiha.la_badiha_bila_rabt
#print axioms Badiha.tamiyat_alfil_mulahaza
#print axioms Badiha.saraTafkir_la_tastalzim
#print axioms Badiha.badiha_murakhkhas
-- السبب والشرط والمانع عند النبهاني، فوق ركن الواقع (Aql/SababShartMani.lean)
#print axioms SababShartMani.ghiyab_la_yunshi_hukm
#print axioms SababShartMani.la_yumkin_hukm_muayyan_maa_ghiyab
#print axioms SababShartMani.sabab_zahir_arkan_waqi
#print axioms SababShartMani.shahid_hummilat_aljibal
#print axioms SababShartMani.shart_wahdahu_la_yahkum
#print axioms SababShartMani.shartWudu
#print axioms SababShartMani.mani_yusqit_bisabab
#print axioms SababShartMani.maniDayn

-- بروتوكول النقل من المعاجم: المهمّة الأولى (Aql/Naql.lean)
#print axioms Naql.la_mutawatir_min_al_add
#print axioms Naql.ahad_idha_wahid
#print axioms Naql.mutadhafir_idha_ithnan_faakthar
#print axioms Naql.la_asl_bila_qail
#print axioms Naql.la_asl_idha_kharij_al_hadd
#print axioms Naql.la_yasluhu_bila_qail_aw_kharij_al_hadd
#print axioms Naql.yasluhu_idha_qail_wa_la_nafy
#print axioms Naql.yasluhu_bool
-- أدواتُ المعاني بوّاباتِ المنطق: و/أو/لا.../إنْ لو، فوق سبب وشرط ومانع (Aql/AdawatMaani.lean)
#print axioms AdawatMaani.jam_yushhid_ibaha
#print axioms AdawatMaani.jam_yunafi_takhyir
#print axioms AdawatMaani.ibaha_tunaqid_takhyir
#print axioms AdawatMaani.takhyir_maa_asl_alaw_yuaddi_ila_xor
#print axioms AdawatMaani.xor_yastalzim_al_asl
#print axioms AdawatMaani.takhyirIkhtiyar
#print axioms AdawatMaani.ibahaMujalasa
#print axioms AdawatMaani.nafy_aljihatayn_yusawi_nafy_alaw
#print axioms AdawatMaani.nor_yastalzim_nand
#print axioms AdawatMaani.nand_la_yastalzim_nor
#print axioms AdawatMaani.wudu_shart_usuli_la_nahwi
#print axioms AdawatMaani.shartNahwiDaw
#print axioms AdawatMaani.daw_la_yakfi_lilshams
#print axioms AdawatMaani.shams_intifa_la_yulzim_daw_intifa
#print axioms AdawatMaani.musawi_yulzim_nafy_altarafayn
#print axioms AdawatMaani.shartNahwiNahar
#print axioms AdawatMaani.shartNahwiNaharAksan
#print axioms Mawsua.Tayy.injective
#print axioms Mawsua.la_tayy_maa_jam
#print axioms Mawsua.ilaBits_tul
#print axioms Mawsua.minBits_ilaBits
#print axioms Mawsua.sifrWahid_la_yudi
#print axioms Mawsua.udkhul_marfud
#print axioms Mawsua.istirja_murakhkhas
#print axioms Mawsua.wasm_la_yaalu_asl
#print axioms Mawsua.wasm_la_yaalu_qanun
#print axioms Mawsua.tarjih_some
#print axioms Mawsua.tarjih_min
#print axioms Mawsua.haqiqa_awla
#print axioms Mawsua.majaz_awla_min_naql
#print axioms Mawsua.asas_aqli
#print axioms Mawsua.ghayr_maddi_la_ilmi
#print axioms Mawsua.ilmi_zanni
#print axioms Mawsua.qayd_ilmi
#print axioms Mawsua.qayd_la_yarfa
#print axioms Mawsua.ilmi_fi_silsila
#print axioms Mawsua.sual_laHukm_iff
#print axioms Mawsua.sual_hukm_istirja
#print axioms Idaa.qaydMudaa_la_yarfa
#print axioms Idaa.la_burhan_min_mudaa
#print axioms Idaa.ahad_zanni
#print axioms Idaa.laysa_kull_lughawi_qati
#print axioms Idaa.tatwil_yajma
#print axioms Idaa.la_tanzif_bila_daya
#print axioms Idaa.aslMusajjal_sanad
#print axioms Idaa.sijill_faregh
#print axioms Idaa.basma_farigha_la_tuqbal
#print axioms Idaa.basma_farigha_khamila
#print axioms Idaa.sanad_farigh_marfud
#print axioms Idaa.aslMusajjal_shahid
#print axioms Qaida.mutadarrija_daifa
#print axioms Qaida.rutba_sifr_asl_daifa
#print axioms Mawsua.tartib_hasir
#print axioms Mawsua.tartib_nodup
#print axioms Mawsua.tartib_tanazuli
#print axioms Mawsua.quwwa_tafriq
#print axioms Dal.hala_min_ila
#print axioms Dal.hala_ila_min
#print axioms Dal.thalath_harakat
#print axioms Dal.hawamil_29
#print axioms Dal.hawamil_nodup
#print axioms Dal.makharij_15
#print axioms Dal.ahjam_sum
#print axioms Dal.ahjam_mawjaba
#print axioms Dal.alif_2
#print axioms Dal.ya_11
#print axioms Dal.waw_28
#print axioms Dal.makhraj_hamil
#print axioms Dal.hamil_makhraj
#print axioms Dal.illa_mukhtalifa
#print axioms Dal.madd_huruf_illa
#print axioms Dal.la_madd_lissukun
#print axioms QawaninDalala.shakl_sahih
#print axioms QawaninDalala.shakl_qawanin
#print axioms QawaninDalala.shakl_mutadarrija
#print axioms QawaninDalala.dalala_mutadarrija
#print axioms QawaninDalala.naql_la_aql
#print axioms QawaninDalala.juz_sawa
#print axioms QawaninDalala.kharij_sawa
#print axioms QawaninDalala.sawa_eq
#print axioms QawaninDalala.salama
#print axioms QawaninDalala.shahid_shakl
#print axioms QawaninDalala.shahid_mutadarrija
#print axioms QawaninDalala.shahid_tadammun
#print axioms QawaninDalala.shahid_iltizam
#print axioms QawaninDalala.shahid_la_iltizam_bila_luzum
#print axioms QawaninDalala.shahid_la_tadammun_bila_juz
#print axioms QawaninDalala.shariyya_awwalan
#print axioms QawaninDalala.wahida_tuhmal
#print axioms QawaninDalala.la_majaz_qabl_istinfad
#print axioms QawaninDalala.ghayr_yuqif
#print axioms QawaninDalala.majaz_bad_istinfad
#print axioms QawaninDalala.mushtarak_bila_qarina
#print axioms QawaninDalala.haml_rubai
#print axioms Maratib.qadiyya_min_haythu_hiya
#print axioms Maratib.la_mafhum_bila_shahid
#print axioms Maratib.mafhum_bishahid
#print axioms Maratib.takrar_la_yarfa
#print axioms Maratib.mujam_la_yasna_mafhum
#print axioms Maratib.la_mafhum_bila_waqi
#print axioms Maratib.waqi_yarfa
#print axioms Maratib.basma_farigha_la_tushhid
#print axioms Maratib.basma_farigha_la_tuthir
#print axioms Maratib.shuhudMutabara_shahid
#print axioms Maratib.shuhudMutabara_sanad
#print axioms Maratib.shahid_farigh_marfud
#print axioms Maratib.khatwa_majmu
#print axioms Maratib.foldl_majmu
#print axioms Maratib.ihsa_majmu
#print axioms Maratib.khatwa_maana_fst
#print axioms Maratib.mukhraj_wahid_min_haythu
#print axioms AlaqaMajaz.mashrua_bila_waqi_makhtum
#print axioms AlaqaMajaz.la_intiqal
#print axioms AlaqaMajaz.basma_farigha_la_tushri
#print axioms AlaqaMajaz.ghayr_mashrua_la_hukm
#print axioms AlaqaMajaz.ghayr_mashrua_la_tunshi_majaz
#print axioms AlaqaMajaz.alaqaOf_ghayr_mashrua_la_hukm
#print axioms AlaqaMajaz.alaqa_ghayr_mashrua_la_tunshi_majaz
#print axioms AlaqaMajaz.dawa_ukhra_la_hukm
#print axioms AlaqaMajaz.dawa_ukhra_la_majaz
#print axioms AlaqaMajaz.shahid_fard_awwal_muntafin
#print axioms AlaqaMajaz.shahid_intiqal
#print axioms SalamaMaqbul.maqbul_sadiq
#print axioms SalamaMaqbul.jawab_sadiq
#print axioms Dal.Tamthil.naql_yahfaz_tashghil
#print axioms Dal.Tamthil.naql_yahfaz_wazn
#print axioms Dal.Tamthil.naql_yahfaz_qubul
#print axioms Dal.Tamthil.khaliya_raqm_sawa
#print axioms Dal.Tamthil.raqm_khaliya_sawa
#print axioms Dal.ramz_eq_cellEnc
#print axioms Dal.ramz_lt
#print axioms Dal.ahjam_eq
#print axioms Dal.madd_eq
#print axioms Dal.makhraj_eq
#print axioms Dal.la_ibtida_bisakin
#print axioms Dal.khaliya_mufrada_84
#print axioms Dal.shahid_bint
#print axioms Dal.shahid_qaltu
#print axioms Dal.shahid_hajja
#print axioms Dal.harf_kharij_marfud
#print axioms Dal.akhudhSawakin_len
#print axioms Dal.qatta_sahih
#print axioms Dal.qatta_wahid
#print axioms Dal.anwa_sitta
#print axioms Dal.shahid_qatta
#print axioms Dal.judhur_thulathiyya
-- المرحلة ٣: الجملة في الوصل (Dal/Jumla.lean على Msent وHamza.lean)
#print axioms Dal.harakatIltiqa_lt
#print axioms Dal.rakkib_wahida
#print axioms Dal.ibtidaForm_lt
#print axioms Dal.ibtida_lt
#print axioms Dal.isqatHamza_lt
#print axioms Dal.rakkibAux_lt
#print axioms Dal.rakkib_abjadiyya
#print axioms Dal.jumla_murakhkhasa
#print axioms Dal.sentChain_eq_joinH
#print axioms Dal.splitH_ne_nil
#print axioms Dal.joinH_cons_nil
#print axioms Dal.joinH_cons_cons
#print axioms Dal.joinH_splitH
#print axioms Dal.qattaKull_sahih
#print axioms Dal.qattaJumla_sahih
#print axioms Dal.qattaJumla_wahid
#print axioms Dal.isqat_ghayr_sakin
#print axioms Dal.sakinAwwal_cons
#print axioms Dal.isqat_mover
#print axioms Dal.isqat_madd
#print axioms Dal.isqat_closed
#print axioms Dal.shahid_qala_uktub
#print axioms Dal.shahid_qalu_uktubu
#print axioms Dal.shahid_qum_allayla
#print axioms Dal.shahid_hadd
#print axioms Dal.shahid_idgham_hadd
-- المرحلة ٣: العوامل المئة وفق قانون الاستنفاد (Jisr/Awamil.lean على مودَع المالك)
#print axioms Jisr.Awamil.hala_injective
#print axioms Jisr.Awamil.ramz_arbaa
#print axioms Jisr.Awamil.jadwal_mia
#print axioms Jisr.Awamil.alfaz_96
#print axioms Jisr.Awamil.inghilaq
#print axioms Jisr.Awamil.nawasikh_thalatha
#print axioms Jisr.Awamil.istinfad
#print axioms Jisr.Awamil.bila_fard
#print axioms Jisr.Awamil.atf_yantashir
#print axioms Jisr.Awamil.majzum_qabl_hamzat_wasl
#print axioms Jisr.Awamil.shahid_lam_yaqum
-- ملفّات المالك المنقولة بنصّها (slge-closed-v13): المدلول أوّلًا، الأقسام الثلاثة، سلّم الضرورة لكلّ (وأدواته على الجنى الداني)، جبر العوامل على قطر الندى
#print axioms SLGE.Awwalan.la_wad_bila_madlul
#print axioms SLGE.Awwalan.madlul_bila_lafz
#print axioms SLGE.Awwalan.shams_kulli
#print axioms SLGE.Awwalan.kulli_la_bil_adad
#print axioms SLGE.Awwalan.hukm_bil_madlul
#print axioms SLGE.Awwalan.mutabaqa_qaim
#print axioms SLGE.Awwalan.shahid_la_yunshi
#print axioms SLGE.Cat.three_roles
#print axioms SLGE.Cat.no_fourth
#print axioms SLGE.Cat.kind_bij
#print axioms SLGE.Cat.three_structs
#print axioms SLGE.Cat.kindOfMadlul_spec
#print axioms SLGE.Cat.kindOfMadlul_onto
#print axioms SLGE.Law.licB_iff
#print axioms SLGE.Law.nec_order3B
#print axioms SLGE.Law.nec_order3
#print axioms SLGE.Law.perm_rev
#print axioms SLGE.Law.perm_swap
#print axioms SLGE.Law.stK_bound
#print axioms SLGE.Law.nec_position_all
#print axioms SLGE.Cat.nec_compose
#print axioms SLGE.Cat.ifada_pairs
#print axioms SLGE.Cat.fil_needs_ism
#print axioms SLGE.Cat.getD_harf
#print axioms SLGE.Cat.harf_never
#print axioms SLGE.Cat.harf_neutral
#print axioms SLGE.Law.harf_table
#print axioms SLGE.Law.augs_are_harf1
#print axioms SLGE.Wad.irab_marks
#print axioms SLGE.Wad.awamil_table
#print axioms SLGE.Wad.closure
#print axioms SLGE.Wad.exhaust
#print axioms SLGE.Wad.harf_governs
#print axioms SLGE.Wad.nawasikh_three
#print axioms SLGE.Wad.kalam_min_matches
#print axioms SLGE.Wad.wad_counts
#print axioms SLGE.Wad.nayta_augs
#print axioms SLGE.Wad.dha_two
-- بقيّة طبقة التركيب من حزمة المالك slge-closed-v13 بنصّها (13 ملفًّا، بإذنه 2026-10-16): المدلول، الضرورة، الجسر، التركيب، العوامل، المقام، الأطر المركّبة، السمات، الإطار الموحَّد، الجملة الكلّيّة
-- Madlul.lean (المالك، بنصّه)
#print axioms SLGE.Madlul.divs_complete
#print axioms SLGE.Madlul.divs_length
#print axioms SLGE.Madlul.codes
#print axioms SLGE.Madlul.code_inj
#print axioms SLGE.Madlul.no_maana_no_dal
#print axioms SLGE.Madlul.qism_none
#print axioms SLGE.Madlul.qism_never_maana
#print axioms SLGE.Madlul.hadhayan
#print axioms SLGE.Madlul.isnad_count
#print axioms SLGE.Madlul.isnad_harf
#print axioms SLGE.Madlul.no_third
#print axioms SLGE.Madlul.both_occur
#print axioms SLGE.Madlul.mafhum_iff_iltizam
#print axioms SLGE.Madlul.mukhalafa_closed
#print axioms SLGE.Madlul.takhsis_sub
#print axioms SLGE.Madlul.amal_bil_muqayyad
#print axioms SLGE.Madlul.amal_bil_mutlaq_la_yafi
#print axioms SLGE.Madlul.haml_iff
#print axioms SLGE.Madlul.shart_adam
#print axioms SLGE.Madlul.shart_la_yujib
#print axioms SLGE.Madlul.sabab_la_yujib
#print axioms SLGE.Madlul.mani_yamna
#print axioms SLGE.Madlul.wujud_tamm
-- Necessity.lean (المالك، بنصّه)
#print axioms SLGE.Law.nec_vowel
#print axioms SLGE.Law.nec_second
#print axioms SLGE.Law.two_complete
#print axioms SLGE.Law.nec_order
#print axioms SLGE.Law.nec_position
-- Bridge.lean (المالك، بنصّه)
#print axioms SLGE.Bridge.iqtiran_needs_madlul
#print axioms SLGE.Bridge.iqtiran_needs_dal
#print axioms SLGE.Bridge.no_single_cell
#print axioms SLGE.Bridge.dal_undetermines
#print axioms SLGE.Bridge.transition
#print axioms SLGE.Bridge.dal_complete_madlul_not
#print axioms SLGE.Bridge.irab_state_bij
#print axioms SLGE.Bridge.jazm_sukun_fil
#print axioms SLGE.Bridge.fariya_augs
#print axioms SLGE.Bridge.sent_min
#print axioms SLGE.Bridge.sent_two
-- Tarkib.lean (المالك، بنصّه)
#print axioms SLGE.Tarkib.keys_eq
#print axioms SLGE.Tarkib.chunk_0
#print axioms SLGE.Tarkib.chunk_1
#print axioms SLGE.Tarkib.chunk_2
#print axioms SLGE.Tarkib.chunk_3
#print axioms SLGE.Tarkib.chunk_4
#print axioms SLGE.Tarkib.chunk_5
#print axioms SLGE.Tarkib.chunk_6
#print axioms SLGE.Tarkib.chunk_7
#print axioms SLGE.Tarkib.chunk_8
#print axioms SLGE.Tarkib.chunk_9
#print axioms SLGE.Tarkib.chunk_10
#print axioms SLGE.Tarkib.chunk_11
#print axioms SLGE.Tarkib.chunk_12
#print axioms SLGE.Tarkib.chunk_13
#print axioms SLGE.Tarkib.chunk_14
#print axioms SLGE.Tarkib.chunk_15
#print axioms SLGE.Tarkib.chunk_16
#print axioms SLGE.Tarkib.chunk_17
#print axioms SLGE.Tarkib.chunk_18
#print axioms SLGE.Tarkib.lit_eq
#print axioms SLGE.Tarkib.frames_eq
#print axioms SLGE.Tarkib.frames_count
#print axioms SLGE.Tarkib.frames_nodup
#print axioms SLGE.Tarkib.map_decS_encS
#print axioms SLGE.Tarkib.idxOf_getD
#print axioms SLGE.Tarkib.s_dec_enc
#print axioms SLGE.Tarkib.frame_value
#print axioms SLGE.Tarkib.taqdim
#print axioms SLGE.Tarkib.mustatir
#print axioms SLGE.Tarkib.one_overt_five
#print axioms SLGE.Tarkib.adat
#print axioms SLGE.Tarkib.irab_by_position
#print axioms SLGE.Tarkib.state_in_proof
#print axioms SLGE.Tarkib.mustatir_value
#print axioms SLGE.Tarkib.ihala_between
-- Awamil.lean (المالك، بنصّه)
#print axioms SLGE.Awamil.table_classes
#print axioms SLGE.Awamil.eqs_closed
#print axioms SLGE.Awamil.nasikh_by_equation
#print axioms SLGE.Awamil.eqs_match_tarkib
#print axioms SLGE.Awamil.eqs_exhaust
#print axioms SLGE.Awamil.atf_propagates
#print axioms SLGE.Awamil.hidden_amil_value
-- Maqam.lean (المالك، بنصّه)
#print axioms SLGE.Maqam.maqam_three
#print axioms SLGE.Maqam.dal_underdetermines_maqam
#print axioms SLGE.Maqam.damair_in_muradi
#print axioms SLGE.Maqam.participants_free
#print axioms SLGE.Maqam.ghaib_needs_ante
#print axioms SLGE.Maqam.mutabaqa
#print axioms SLGE.Maqam.ishara_ref
#print axioms SLGE.Maqam.sila_aid
#print axioms SLGE.Maqam.featCode_inj
#print axioms SLGE.Maqam.maqam_value
-- TarkibExt.lean (المالك، بنصّه)
#print axioms SLGE.TarkibExt.fIdx_inj
#print axioms SLGE.TarkibExt.shart_frames
#print axioms SLGE.TarkibExt.shart_internal_ihala
#print axioms SLGE.TarkibExt.shart_count
#print axioms SLGE.TarkibExt.shart_value
#print axioms SLGE.TarkibExt.nida_heads
#print axioms SLGE.TarkibExt.nida_mukhatab
#print axioms SLGE.TarkibExt.nida_value
#print axioms SLGE.TarkibExt.istifham_sadara
#print axioms SLGE.TarkibExt.istifham_count
#print axioms SLGE.TarkibExt.shaan_frames
#print axioms SLGE.TarkibExt.mawsul_frames
#print axioms SLGE.TarkibExt.aid_value
-- Simat.lean (المالك، بنصّه)
#print axioms SLGE.Simat.tatabuq
#print axioms SLGE.Simat.rabit_tatabuq
#print axioms SLGE.Simat.zaman
#print axioms SLGE.Simat.tarif
#print axioms SLGE.Simat.mahall_exhaust
#print axioms SLGE.Simat.mahall_mabni
#print axioms SLGE.Simat.alaqa
#print axioms SLGE.Simat.attrCode_inj
#print axioms SLGE.Simat.map_inj
#print axioms SLGE.Simat.encS_inj
#print axioms SLGE.Simat.attr_value
#print axioms SLGE.Simat.ihala_ptr
#print axioms SLGE.Simat.ptr_value
-- Simat2.lean (المالك، بنصّه)
#print axioms SLGE.Simat.musawwigh
#print axioms SLGE.Simat.khabar_tatabuq
#print axioms SLGE.Simat.tanith
#print axioms SLGE.Simat.ptr_mafool
#print axioms SLGE.Simat.ptr_aid
#print axioms SLGE.Simat.extCode_inj
#print axioms SLGE.Simat.ext_value
-- Muwahhad.lean (المالك، بنصّه)
#print axioms SLGE.Muwahhad.u_conservative
#print axioms SLGE.Muwahhad.musawwigh_linked
#print axioms SLGE.Muwahhad.istithna_mufarragh
#print axioms SLGE.Muwahhad.amil_ala_amil
#print axioms SLGE.Muwahhad.amil_compose
#print axioms SLGE.Muwahhad.u_value
-- Kull.lean (المالك، بنصّه)
#print axioms SLGE.Kull.istithna_tamm
#print axioms SLGE.Kull.kull_conservative
#print axioms SLGE.Kull.containment
#print axioms SLGE.Kull.lan_not_shart
#print axioms SLGE.Kull.in_lam_yakun
#print axioms SLGE.Kull.tamm_in_jumla
#print axioms SLGE.Kull.bCode_inj
#print axioms SLGE.Kull.pair_zero
#print axioms SLGE.Kull.pair_ne0
#print axioms SLGE.Kull.istCode_inj
#print axioms SLGE.Kull.uK_mem
#print axioms SLGE.Kull.ud_value
#print axioms SLGE.Kull.fC_inj
#print axioms SLGE.Kull.opt_inj
#print axioms SLGE.Kull.j_value
-- المرحلة ٣: الجملة الاسمية والفعلية والظرفية بأقسام الكلم (Jisr/Tarkib.lean على المغني والقطر)
#print axioms Jisr.Tarkib.naw_thalatha
#print axioms Jisr.Tarkib.shawahid_mughni
#print axioms Jisr.Tarkib.azwaj_mufida
#print axioms Jisr.Tarkib.jadwal_yali
#print axioms Jisr.Tarkib.la_harf_bada_amil
-- النِّسَب الثلاث على أطر المالك، واستنفاد أساليب الإخبار (Jisr/Nisab.lean)
#print axioms Jisr.Nisab.kull_mawdi
#print axioms Jisr.Nisab.isnad_markaz
#print axioms Jisr.Nisab.ihsa_val
#print axioms Jisr.Nisab.uslub_istinfad
#print axioms Jisr.Nisab.ikhbar_82
-- أساليب الإخبار: جرد القطر، التغطية بأطر المالك، الحدّ الأدنى المكتمل (Jisr/Ikhbar.lean)
#print axioms Jisr.Ikhbar.kull_hasir
#print axioms Jisr.Ikhbar.istinfad
#print axioms Jisr.Ikhbar.adwar_tisa
#print axioms Jisr.Ikhbar.ghayr_mughatta
#print axioms Jisr.Ikhbar.adna_itar
#print axioms Jisr.Ikhbar.awamil_ikhbar
-- معجم أقسام الكلم: أقسام العوامل من القطر عبر عائلات المالك (Jisr/AqsamAwamil.lean)
#print axioms Jisr.AqsamAwamil.mujam_45
#print axioms Jisr.AqsamAwamil.bila_hukm
#print axioms Jisr.AqsamAwamil.shawahid
#print axioms Jisr.AqsamAwamil.naql_fi_jadwal
#print axioms Jisr.AqsamAwamil.mujam_98
#print axioms Jisr.AqsamAwamil.bila_hukm_2
#print axioms Jisr.AqsamAwamil.shawahid2
-- الأطر السبعة عشر المنتظرة على أطر المالك: الملحقات بأدوارها وشواهد القطر (Jisr/Mulhaqat.lean)
#print axioms Jisr.Mulhaqat.Dawr.hasir
#print axioms Jisr.Mulhaqat.Dawr.code_inj
#print axioms Jisr.Mulhaqat.khilaf_musajjal
#print axioms Jisr.Mulhaqat.itar_conservative
#print axioms Jisr.Mulhaqat.furui_eq
#print axioms Jisr.Mulhaqat.naib_shawahid
#print axioms Jisr.Mulhaqat.naib_ahkam
#print axioms Jisr.Mulhaqat.ishtighal_shawahid
#print axioms Jisr.Mulhaqat.tanazu_shawahid
#print axioms Jisr.Mulhaqat.mafail_shawahid
#print axioms Jisr.Mulhaqat.hal_shawahid
#print axioms Jisr.Mulhaqat.tamyiz_shawahid
#print axioms Jisr.Mulhaqat.idafa_shawahid
#print axioms Jisr.Mulhaqat.amil_ismi_shawahid
#print axioms Jisr.Mulhaqat.amil_ismi_istinfad
#print axioms Jisr.Mulhaqat.nat_shawahid
#print axioms Jisr.Mulhaqat.tawkid_shawahid
#print axioms Jisr.Mulhaqat.atf_bayan_shawahid
#print axioms Jisr.Mulhaqat.atf_nasaq_shawahid
#print axioms Jisr.Mulhaqat.badal_shawahid
#print axioms Jisr.Mulhaqat.adad_shawahid
#print axioms Jisr.Mulhaqat.halat_adwar
#print axioms Jisr.Mulhaqat.la_jazm
#print axioms Jisr.Mulhaqat.taghtiya_kamila
#print axioms Jisr.Mulhaqat.mulhaqCode_inj
#print axioms Jisr.Mulhaqat.itar_value
-- أطر الطبقات الثلاث على القانون العامّ: الدال وحده، المدلول وحده، معًا (Jisr/Utur.lean)
#print axioms Jisr.Utur.waqf_kama_yuqra
#print axioms Jisr.Utur.dal_waqf_kama_yuqra
#print axioms Jisr.Utur.wasl_yastalzim_ibtida
#print axioms Jisr.Utur.waqf_yastalzim_ibtida
#print axioms Jisr.Utur.wasl_waqf_mustaqillan
#print axioms Jisr.Utur.wasl_ghayr_Fwasl
#print axioms Jisr.Utur.la_itar_bisakin
#print axioms Jisr.Utur.dal_vs_complete
#print axioms Jisr.Utur.dal_yastalzim_complete
#print axioms Jisr.Utur.itar_dal_istinfad_2
#print axioms Jisr.Utur.itar_dal_anmat_2
#print axioms Jisr.Utur.itar_dal_shawahid
#print axioms Jisr.Utur.damm_murakhkhas
#print axioms Jisr.Utur.damm_mumtani
#print axioms Jisr.Utur.ofBool_murakhkhas
#print axioms Jisr.Utur.harf_la_yubtada
#print axioms Jisr.Utur.fil_la_yubtada
#print axioms Jisr.Utur.nisab_mahmul
#print axioms Jisr.Utur.wasl_thulathi
#print axioms Jisr.Utur.madlul_shawahid
#print axioms Jisr.Utur.ibtida3_of_hukm
#print axioms Jisr.Utur.hukmTarkib_murakhkhas
#print axioms Jisr.Utur.hukm3_murakhkhas
#print axioms Jisr.Utur.hukm_la_yusqit_tarkhis
#print axioms Jisr.Utur.fiHadd_of_hukm
#print axioms Jisr.Utur.kharij_alhadd
#print axioms Jisr.Utur.ofBool_ne_laHukm
#print axioms Jisr.Utur.damm_laHukm
#print axioms Jisr.Utur.asbabHadd_nil
#print axioms Jisr.Utur.laHukm_iff_sabab
#print axioms Jisr.Utur.fiHadd_shurut
#print axioms Jisr.Utur.la_hukm_ma_radda_itar
#print axioms Jisr.Utur.la_tamthil_la_hukm
#print axioms Jisr.Utur.mumtani_itarOK
#print axioms Jisr.Utur.shahid_asbab
#print axioms Jisr.Utur.shahid_hadd_asbab
#print axioms Jisr.Utur.shahid_qiraa
#print axioms Jisr.Utur.shahid_baqi
#print axioms Jisr.Utur.itar3_yahtawi
#print axioms Jisr.Utur.itar3_yahtawi_hukm
#print axioms Jisr.Utur.shahid_dhahaba_alwalad
#print axioms Jisr.Utur.shahid_fi_dar
#print axioms Jisr.Utur.shahid_hal
#print axioms Jisr.Utur.shahid_kana
#print axioms Jisr.Utur.shahid_hadd
#print axioms Jisr.Utur.kalimaCode_inj
#print axioms Jisr.Utur.madlulCode_inj
#print axioms Jisr.Utur.mahmulCode_inj
#print axioms Jisr.Utur.nisbaCode_inj
#print axioms Jisr.Utur.itarMadlulCode_inj
#print axioms Jisr.Utur.itar3_value
#print axioms SLGE.Law.ibtida
#print axioms SLGE.Law.cell_count
#print axioms SLGE.Law.qaltu
#print axioms SLGE.Law.hajja
#print axioms SLGE.Law.bint
#print axioms SLGE.Law.syl_law
#print axioms SLGE.Law.word_structure
#print axioms SLGE.Law.sent_structure
#print axioms SLGE.Law.wordChain_inj
#print axioms SLGE.Law.sentChain_inj
#print axioms SLGE.Law.word_levels
#print axioms SLGE.Law.word_levels_wasl
#print axioms SLGE.Law.syl_levels
#print axioms SLGE.Law.syl_numbering
#print axioms SLGE.Law.sukun_first_dead
#print axioms SLGE.Law.wasl_hamza_repair
#print axioms SLGE.Law.prefix_licenses
#print axioms SLGE.Law.tajawur
#print axioms SLGE.Law.tajawur_free
#print axioms SLGE.Law.root3
#print axioms SLGE.Law.root4
#print axioms SLGE.Law.root5
#print axioms SLGE.Law.wazn_counts
#print axioms SLGE.Law.root_numbering
#print axioms SLGE.Law.muj_numbering
#print axioms SLGE.Law.units1
#print axioms SLGE.Law.units2
#print axioms SLGE.carrier_dec_enc
#print axioms SLGE.carrier_enc_dec
#print axioms SLGE.cell_dec_enc
#print axioms SLGE.cell_enc_dec
#print axioms SLGE.syl_dec_enc
#print axioms SLGE.syl_enc_dec
#print axioms SLGE.makharij_count
#print axioms SLGE.syl_sizes

-- المعلومات السابقة التأسيسية للتعيين والتمييز: induction FOR/ON على أركان ج1 ومنهج ابن سيده (Madlul/Tayin.lean)
#print axioms Madlul.Tayin.wa_naam
#print axioms Madlul.Tayin.wa_la
#print axioms Madlul.Tayin.hayat_naam
#print axioms Madlul.Tayin.hayat_la
#print axioms Madlul.Tayin.sannif_ghayr_jamad
#print axioms Madlul.Tayin.jamadiyya_hayat
#print axioms Madlul.Tayin.sannif_iff
#print axioms Madlul.Tayin.fusul_sannif
#print axioms Madlul.Tayin.sannif_fusul
#print axioms Madlul.Tayin.fasl_wahid
#print axioms Madlul.Tayin.aql_la_yumayyiz
#print axioms Madlul.Tayin.ghiyab_la_hukm
#print axioms Madlul.Tayin.shawahid_khuruj
#print axioms Madlul.Tayin.yuhassinQ_naam
#print axioms Madlul.Tayin.yuhassinQ_la
#print axioms Madlul.Tayin.hayat_tahsin
#print axioms Madlul.Tayin.tahsin_la_yughayyir
#print axioms Madlul.Tayin.qabiliyya_tabi_khassa
#print axioms Madlul.Tayin.shawahid

-- تشفير معجم الأجناس على قناة الدالّ وحده الثنائيّة نفسِها (Madlul/Tashfir.lean؛ ردًّا على طلب المالك
-- 2026-10-17 توظيف الـ binary والفكّ عبر Tayy على حدود الجسر)
#print axioms Madlul.Tashfir.qism_la_yudi
#print axioms Madlul.Tashfir.qismSifrWahid_la_yudi

-- تعميمُ Tayy على سلّم SLGE كلِّه بدرجةٍ n (Madlul/TashfirSullam.lean؛ طلب المالك 2026-10-17: دالّةٌ
-- واحدةٌ على unit = n، لا مثالٌ لكلّ انتقال، بقراءة مبرهنات SLGE/Ladder.lean مباشرةً)
#print axioms Madlul.TashfirSullam.fakkRaw_tawiRaw
#print axioms Madlul.TashfirSullam.fakkOf_tawiOf
#print axioms Madlul.TashfirSullam.tayyOf_la_yudi

-- قانون التوريث والوراثة على شجرة الأجناس (Madlul/Wiratha.lean)
#print axioms Madlul.Wiratha.battQ_yuhassin
#print axioms Madlul.Wiratha.warrith_yuhassin
#print axioms Madlul.Wiratha.battQ_yuhassinQ
#print axioms Madlul.Wiratha.tahsin_wiratha
#print axioms Madlul.Wiratha.battQ_la_yunaqid
#print axioms Madlul.Wiratha.warrith_la_yunaqid
#print axioms Madlul.Wiratha.battQ_yabutt
#print axioms Madlul.Wiratha.warrith_yabutt
#print axioms Madlul.Wiratha.mawruth_yabqa
#print axioms Madlul.Wiratha.battQ_laHukm
#print axioms Madlul.Wiratha.warrith_farigh
#print axioms Madlul.Wiratha.yuhassinQ_refl
#print axioms Madlul.Wiratha.yuhassinQ_trans
#print axioms Madlul.Wiratha.yuhassin_refl
#print axioms Madlul.Wiratha.yuhassin_trans
#print axioms Madlul.Wiratha.Shajara.wiratha
#print axioms Madlul.Wiratha.Shajara.jidhr_thabit
#print axioms Madlul.Wiratha.fusul_min_wiratha
#print axioms Madlul.Wiratha.aba_bila_hukm
#print axioms Madlul.Wiratha.ikhwan_bi_fasl

-- تصنيف الجماد: الكمّ والحالات والتحوّل وشروط الفيزياء والرياضيات والوحدة والكثرة (Madlul/Jamad.lean)
#print axioms Madlul.Jamad.dhawb_jumud
#print axioms Madlul.Jamad.tabakhkhur_takathuf
#print axioms Madlul.Jamad.tahawwul_yughayyir
#print axioms Madlul.Jamad.tahawwul_daraja
#print axioms Madlul.Jamad.muttasiqB_salim
#print axioms Madlul.Jamad.hala_ratiba
#print axioms Madlul.Jamad.sail_bayn
#print axioms Madlul.Jamad.tahawwul_la_yughayyir_haqiqa
#print axioms Madlul.Jamad.tahawwul_yahfaz_kutla
#print axioms Madlul.Jamad.kutla_majmu
#print axioms Madlul.Jamad.kathafa_la_tujma
#print axioms Madlul.Jamad.jism_kutla_la_hukm
#print axioms Madlul.Jamad.tartib_kathafa
#print axioms Madlul.Jamad.ifrad_madud
#print axioms Madlul.Jamad.ifrad_bila_ta
#print axioms Madlul.Jamad.shawahid_hala
#print axioms Madlul.Jamad.shawahid_muttasiq
#print axioms Madlul.Jamad.shawahid_muttasiq'
#print axioms Madlul.Jamad.thalj_ma
#print axioms Madlul.Jamad.thalj_yatfu
#print axioms Madlul.Jamad.kathafa_mushakkika
#print axioms Madlul.Jamad.haqiqa_mutawatia

-- شبكة العلاقات وأساليب الإخبار وسلسلة القرار المرخَّصة جبريًّا (Madlul/Shabaka.lean)
#print axioms Madlul.Shabaka.tawi_addi
#print axioms Madlul.Shabaka.tawi_lazim
#print axioms Madlul.Shabaka.tawi_fail
#print axioms Madlul.Shabaka.tawi_lazim_la_hukm
#print axioms Madlul.Shabaka.jahhil_naib
#print axioms Madlul.Shabaka.jahhil_lazim_la_hukm
#print axioms Madlul.Shabaka.sharik_tabadul
#print axioms Madlul.Shabaka.utlub_yahfaz
#print axioms Madlul.Shabaka.uslub_la_yakhtari
#print axioms Madlul.Shabaka.murakhkhas_salim
#print axioms Madlul.Shabaka.asl_sadiq
#print axioms Madlul.Shabaka.qaida_mutadarrija
#print axioms Madlul.Shabaka.asl_la_yurakhkhas_illa_mudaan
#print axioms Madlul.Shabaka.semB_qabiliyya
#print axioms Madlul.Shabaka.semB_mafooliyya
#print axioms Madlul.Shabaka.semB_sababiyya
#print axioms Madlul.Shabaka.semB_tasmiya
#print axioms Madlul.Shabaka.semB_qanunMujam
#print axioms Madlul.Shabaka.semB_nisba
#print axioms Madlul.Shabaka.s1
#print axioms Madlul.Shabaka.s2
#print axioms Madlul.Shabaka.s3
#print axioms Madlul.Shabaka.s4
#print axioms Madlul.Shabaka.s5
#print axioms Madlul.Shabaka.qawanin_salima
#print axioms Madlul.Shabaka.shabaka_salima
#print axioms Madlul.Shabaka.ghayr_thabit_la_yurakhkhas
#print axioms Madlul.Shabaka.jinsSifa_la_yurakhkhas
#print axioms Madlul.Shabaka.marfud
#print axioms Madlul.Shabaka.shawahid_maqbula
#print axioms Madlul.Shabaka.sail_sharab_marfud
#print axioms Madlul.Shabaka.sail_sharab_bil_mujam
#print axioms Madlul.Shabaka.salasil_marfuda
#print axioms Madlul.Shabaka.qaida_shahid_mutadarrija
#print axioms Madlul.Shabaka.adad_qawanin

-- الحواسّ الخمس وتشارك الخبرة رخصةً فوق الشبكة (Madlul/Hawass.lean)
#print axioms Madlul.Hawass.sawt_masmu
#print axioms Madlul.Hawass.hajm_malmus_mari
#print axioms Madlul.Hawass.tawhid
#print axioms Madlul.Hawass.la_mafhum_bila_mutabaqa
#print axioms Madlul.Hawass.la_mafhum_bila_mudaa_waqi
#print axioms Madlul.Hawass.mujam_la_yasna_mafhum
#print axioms Madlul.Hawass.tikrar_la_yarfa
#print axioms Madlul.Hawass.tasdiq_ratib
#print axioms Madlul.Hawass.rukhsa_la_tanzil
#print axioms Madlul.Hawass.sarakh_shadid
#print axioms Madlul.Hawass.sarakh_ratib
#print axioms Madlul.Hawass.malmas_la_hukm
#print axioms Madlul.Hawass.malmas_ratib
#print axioms Madlul.Hawass.tafdil_bila_tamyiz
#print axioms Madlul.Hawass.akbar_la_yanakis
#print axioms Madlul.Hawass.akbar_mutaaddi
#print axioms Madlul.Hawass.akbar_la_yufaddil_nafsah
#print axioms Madlul.Hawass.wajh_jins
#print axioms Madlul.Hawass.wajh_fard
#print axioms Madlul.Hawass.shawahid_malik
#print axioms Madlul.Hawass.mafhum_bi_tasharuk
#print axioms Madlul.Hawass.thalj_barid
#print axioms Madlul.Hawass.jabal_akbar
#print axioms Madlul.Hawass.khibrat_asma
#print axioms Madlul.Hawass.shahid_ghayr_mudaa_la_yuthir

-- أوّليات العقل: الأركان، التعيين، التمييز، المرفوع الثالث، الجزء والكلّ، الزمن والأزمنة الخمسة عند سيبويه (Aql/Awwaliyyat.lean)
#print axioms Aql.Awwaliyyat.la_fikr_bila_arkan
#print axioms Aql.Awwaliyyat.al_shay_huwa_huwa
#print axioms Aql.Awwaliyyat.tamyiz_bil_fasl
#print axioms Aql.Awwaliyyat.aqsam_mutamayiza
#print axioms Aql.Awwaliyyat.marfu_thalith
#print axioms Aql.Awwaliyyat.marfu_thalith_muqarrar
#print axioms Aql.Awwaliyyat.la_hukm_laysa_thalithan
#print axioms Aql.Awwaliyyat.juz_asghar_min_kull
#print axioms Aql.Awwaliyyat.kutlat_juz
#print axioms Aql.Awwaliyyat.adad_dun_majmuih
#print axioms Aql.Awwaliyyat.tawrith_intizam
#print axioms Aql.Awwaliyyat.taaqub_yurith
#print axioms Aql.Awwaliyyat.layl_nahar
#print axioms Aql.Awwaliyyat.azmina_thalatha_hasira
#print axioms Aql.Awwaliyyat.zaman_yurith_ma_kan
#print axioms Aql.Awwaliyyat.mustaqbal_la_hukm
#print axioms Aql.Awwaliyyat.ithbat_la_yukhallis
#print axioms Aql.Awwaliyyat.nafy_yukhallis
#print axioms Aql.Awwaliyyat.nafy_asma
#print axioms Aql.Awwaliyyat.zaman5_hasira
#print axioms Aql.Awwaliyyat.qasam_ala_zamanayn
#print axioms Aql.Awwaliyyat.qasam_yusqit_intizar
#print axioms Aql.Awwaliyyat.muhal_naqd
#print axioms Aql.Awwaliyyat.mustaqim_hasan
#print axioms Aql.Azmina.rutba_tartib
#print axioms Aql.Azmina.rutba_injective
#print axioms Aql.Azmina.al_an_muhayid
#print axioms Aql.Azmina.aks_yarudd
#print axioms Aql.Azmina.aks_aks
#print axioms Aql.Azmina.zaman_hasir
#print axioms Aql.Azmina.aks_yaqlib
#print axioms Aql.Azmina.al_an_hal
#print axioms Aql.Azmina.awwal_min_ams
#print axioms Aql.Azmina.qabl_ams_biyawm
#print axioms Aql.Azmina.ghad_thani_yawmik
#print axioms Aql.Azmina.awwalMin_bad
#print axioms Aql.Azmina.asma_azmina
#print axioms Aql.Azmina.markaz_sifr
#print axioms Aql.Azmina.markaz_markaz
#print axioms Aql.Azmina.markaz_yahfaz_farq
#print axioms Aql.Azmina.markaz_yahfaz_tartib
#print axioms Aql.Azmina.kull_yawm_yasir_amsan
#print axioms Aql.Azmina.kull_ams_mada_lan_yaud
#print axioms Aql.Azmina.usbu_sabat_ayyam
#print axioms Aql.Azmina.sana_ithna_ashar
#print axioms Aql.Azmina.yawm_24
#print axioms Aql.Azmina.shahr_tisa_aw_thalathun
#print axioms Aql.Azmina.shahr_bil_ayyam_la_hukm
#print axioms Aql.Azmina.zamanOf_ishara
#print axioms Aql.Azmina.tahwil_yahfaz_ishara
#print axioms Aql.Azmina.mustaqim_hasan_ams_ghad
#print axioms Aql.Azmina.muhal_ghad_ams
#print axioms Aql.Azmina.al_an_la_hukm
#print axioms Aql.Azmina.zaman3Of5_qalb5
#print axioms Aql.Azmina.qalb_injective
#print axioms Aql.Azmina.istiqama_aks
#print axioms Aql.Azmina.jisr_mustaqbal
#print axioms Aql.Azmina.jisr_madi
#print axioms Aql.Makan.naqid_naqid
#print axioms Aql.Makan.naqid_ghayr
#print axioms Aql.Makan.naqid_mihwar
#print axioms Aql.Makan.naqid_ishara
#print axioms Aql.Makan.jihat_sitt
#print axioms Aql.Makan.muradifat
#print axioms Aql.Makan.marja_muhayid
#print axioms Aql.Makan.aks_yarudd
#print axioms Aql.Makan.aks_aks
#print axioms Aql.Makan.mujab_ne_salib
#print axioms Aql.Makan.jiha_hasira
#print axioms Aql.Makan.jiha_ala_mihwarih
#print axioms Aql.Makan.aks_ala
#print axioms Aql.Makan.jihaOf_some
#print axioms Aql.Makan.aks_yunaqid
#print axioms Aql.Makan.nisba_marja_nafsih
#print axioms Aql.Makan.tanazur
#print axioms Aql.Makan.taaddi
#print axioms Aql.Makan.la_yajtami
#print axioms Aql.Makan.intiqal_marja
#print axioms Aql.Makan.jar_jiha
#print axioms Aql.Makan.jar_naqid
#print axioms Aql.Makan.jar_ala_mihwarih
#print axioms Aql.Makan.mujawir_tabadul
#print axioms Aql.Makan.mil_wa_farsakh
#print axioms Aql.Makan.farsakh_la_hukm
#print axioms Aql.Makan.shawahid_sibawayhi
#print axioms Aql.Makan.ghaya_tahfaz
#print axioms Aql.Makan.bila_marja_la_hukm
#print axioms Aql.Makan.jisr_wajhan
#print axioms Aql.Makan.wara_bil_qarina
#print axioms Aql.Makan.wara_wajhan
#print axioms Aql.Mirsat.an_hal
#print axioms Aql.Mirsat.huna_la_jiha
#print axioms Aql.Mirsat.thabat_naql_zaman
#print axioms Aql.Mirsat.thabat_naql_jiha
#print axioms Aql.Mirsat.thabat_naql_istiqama
#print axioms Aql.Mirsat.naql_mirsat_zaman
#print axioms Aql.Mirsat.naql_mirsat_jiha
#print axioms Aql.Mirsat.alyawm_bimanzilat_alan
#print axioms Aql.Mirsat.min_alan_ila_ghad
#print axioms Aql.Mirsat.huna_hadha
#print axioms Aql.Mirsat.taqrib_tabid
#print axioms Aql.Mirsat.bila_mirsat_la_hukm
#print axioms Aql.Mirsat.thabat_naql_mubham
#print axioms Aql.Mirsat.la_qabl_wa_bad
#print axioms Aql.Mirsat.mustaqim_min_kull_mirsat
#print axioms Aql.Isnad.ajza_ithnan
#print axioms Aql.Isnad.hakim_mahkum
#print axioms Aql.Isnad.sughra_kalam
#print axioms Aql.Isnad.wasf_bi_fail
#print axioms Aql.Isnad.zarfiyya_kalam
#print axioms Aql.Isnad.nasikh_yahfaz
#print axioms Aql.Isnad.kubra_kalam
#print axioms Aql.Isnad.kubra_bila_sabab_la_kalam
#print axioms Aql.Isnad.khabar_kalam
#print axioms Aql.Isnad.wasf_la_zaman
#print axioms Aql.Isnad.sughra_huna
#print axioms Aql.Isnad.thabat_naql_arad
#print axioms Aql.Isnad.thabat_naql_mawdi
#print axioms Aql.Isnad.mustaqarr_jiha
#print axioms Aql.Isnad.shawahid_kalam
#print axioms Aql.Isnad.sabab_yufarriq
#print axioms Aql.Isnad.hahuna_la_jiha
#print axioms Aql.Isnad.thamma_dhaka
#print axioms Jisr.JisrDal.harf_fakk
#print axioms Jisr.JisrDal.khaliya_malik
#print axioms Jisr.JisrDal.hawamil_huruf
#print axioms Jisr.JisrDal.asliyya_tuqabil
#print axioms Jisr.JisrDal.maqsur_la_yuayyin
#print axioms Jisr.JisrDal.mudaf_la_yuayyin
#print axioms Jisr.JisrDal.yayn_la_yufarriq
#print axioms Jisr.JisrDal.manqus_fatha_zahira
#print axioms Jisr.JisrDal.mamnu_fatha
#print axioms Jisr.JisrDal.mamnu_bi_al
#print axioms Jisr.JisrDal.amthila_nun
#print axioms Jisr.JisrDal.sitta_hamil
#print axioms Jisr.JisrDal.farIyaBab_malik
#print axioms Jisr.JisrDal.farIya_kull
#print axioms Jisr.JisrDal.shawahid_hukm
#print axioms Jisr.JisrDal.muwafiq_farIya
#print axioms Jisr.JisrDal.majhul_huruf
#print axioms Jisr.JisrDal.majhul_tul
#print axioms Jisr.JisrDal.majhul_dun_116
#print axioms Jisr.JisrDal.majhul_marfud
#print axioms Jisr.JisrDal.shawahid_majhul
#print axioms Jisr.JisrDal.intilaq_wasl
#print axioms Jisr.JisrDal.hukm_laHukm_sabab
#print axioms Jisr.JisrDal.majhul_none_iff
#print axioms Jisr.JisrDal.shawahid_sabab
#print axioms Jisr.JisrDal.shahid_anmat
#print axioms Jisr.JisrDal.majhul_namat
#print axioms Jisr.JisrDalUtur.mufrad_halaIrab
#print axioms Jisr.JisrDalUtur.mufrad_tanwin
-- خلاصةُ أسلوب الإخبار: الثمانيةُ بنودٍ الباقية (Jisr/KhulasaIkhbar.lean)
#print axioms Jisr.KhulasaIkhbar.bund_thamaniya
#print axioms Jisr.KhulasaIkhbar.bund_mutamayiza
#print axioms Jisr.KhulasaIkhbar.darajat_ilgha_thalath_mukhtalifa
#print axioms Jisr.KhulasaIkhbar.arbaa_asbab
#print axioms Jisr.KhulasaIkhbar.shawahid_arbaa_mustaqilla
#print axioms Jisr.KhulasaIkhbar.jamay_tashih_bila_jawaz
#print axioms Jisr.KhulasaIkhbar.yaslahu_khiyar_wahid
#print axioms Jisr.KhulasaIkhbar.laYaslahu_khiyaran
#print axioms Jisr.KhulasaIkhbar.bilaQarn_khas_bi_yaslahu
#print axioms Jisr.KhulasaIkhbar.ghaib_L115_khamsa
#print axioms Jisr.KhulasaIkhbar.ism_yataqaddam_laqab
#print axioms Jisr.KhulasaIkhbar.ism_yataqaddam_kunya
#print axioms Jisr.KhulasaIkhbar.laqab_la_yataqaddam_ism
#print axioms Jisr.KhulasaIkhbar.halatay_laqab_mustaqillatan
#print axioms Jisr.KhulasaIkhbar.mukhtassa_sabaa
#print axioms Jisr.KhulasaIkhbar.mushtaraka_sabaa
#print axioms Jisr.KhulasaIkhbar.qismat_jarr_tamma
#print axioms Jisr.KhulasaIkhbar.tasnif_al_bunud_tamm
#print axioms Jisr.NisabAsnaf.muwafiq_semOf
#print axioms Jisr.NisabAsnaf.jadwal_nisab
#print axioms Jisr.NisabAsnaf.kull_mamul_nisba
#print axioms Jisr.NisabAsnaf.idafiyya_jarr
#print axioms Jisr.NisabAsnaf.taqyidiyya_nida
#print axioms Jisr.NisabAsnaf.isnadiyya_asnaf
#print axioms Jisr.NisabAsnaf.ihsa_awamil
#print axioms Jisr.QiraaSimat.hawamil_malik
#print axioms Jisr.QiraaSimat.qiraa_salima
#print axioms Jisr.QiraaSimat.qiraaH_salima
#print axioms Jisr.QiraaSimat.hawamil_8
#print axioms Jisr.QiraaSimat.khalaya_10
#print axioms Jisr.QiraaSimat.anta_anti
#print axioms Jisr.QiraaSimat.huma_baqiya
#print axioms Jisr.QiraaSimat.ghayr_damir
#print axioms Jisr.QiraaSimat.qiraa_min_raqm
#print axioms Jisr.QiraaSimat.qiraa_min_annEnc
#print axioms Jisr.QiraaSimat.la_dalla_tasturidd
#print axioms Jisr.QiraaSimat.attrDec_attrCode
#print axioms Jisr.QiraaSimat.map_attrDec
#print axioms Jisr.QiraaSimat.fahs_min_raqm
#print axioms Jisr.QiraaSimat.kashf_tanaqud
#print axioms Jisr.QiraaSimat.faid
#print axioms Jisr.QiraaSimat.ihtizal
#print axioms Jisr.QiraaSimat.ihtizal_annEnc

-- ترتيبُ الفاعل والمفعول به مع عامله: قطر الندى L219–235 (Jisr/TartibMamul.lean؛ بعد تصحيح أرقام
-- السند وحذف قسمين غير مسنودين في مراجعة murajii 2026-10-17)
#print axioms TartibMamul.asl_yali_amilah
#print axioms TartibMamul.jawaz_taakhir_fail_an_maful
#print axioms TartibMamul.wujub_taakhir_fail_li_aid
#print axioms TartibMamul.wujub_taakhir_fail_li_damir_mamul
#print axioms TartibMamul.shahid_darabani_zayd
#print axioms TartibMamul.jawaz_taqdim_maful_ala_amil

-- جسرُ المعلومة المعمَّم: طيُّ وفكُّ Madlul.Jamad.Madda بـ SLGE.mixEnc/mixDec (Madlul/TashfirMadda.lean؛
-- طلب المالك 2026-10-17: «ابدا بالجسر اعمل lean» على المقترح ١ — جسر المعلومة/المفاهيم بالنمط المعمَّم)
#print axioms Madlul.TashfirMadda.optNat_dec_enc
#print axioms Madlul.TashfirMadda.zigzag_unzigzag
#print axioms Madlul.TashfirMadda.optInt_dec_enc
#print axioms Madlul.TashfirMadda.bound_pos
#print axioms Madlul.TashfirMadda.madda_dec_enc
#print axioms Madlul.TashfirMadda.fakkOf_tawiOf
#print axioms Madlul.TashfirMadda.tayyMadda_la_yudi
#print axioms Madlul.TashfirMadda.shawahid_sahih
#print axioms Madlul.TashfirMadda.madda_shawahid_tudi

-- جسرُ المعلومة المعمَّم: طيُّ وفكُّ Madlul.Tayin.Khawass بترميز قوائمَ عامّ فوق SLGE.mixEnc/mixDec
-- (Madlul/TashfirKhawass.lean؛ طلب المالك 2026-10-17 22:55: «Khawass … نفذ انت مفوض مني» — يغلق فجوة
-- القوائم التي أجّلتها TashfirMadda بالاسم؛ غيرُ مشروطٍ (بلا Subtype) لأنّ Qima/QabHaraka محدودان)
#print axioms Madlul.TashfirKhawass.qima_dec_enc
#print axioms Madlul.TashfirKhawass.qimaEnc_lt
#print axioms Madlul.TashfirKhawass.qab_dec_enc
#print axioms Madlul.TashfirKhawass.qabEnc_lt
#print axioms Madlul.TashfirKhawass.list_dec_enc
#print axioms Madlul.TashfirKhawass.khawass_l2_lt
#print axioms Madlul.TashfirKhawass.qabEnc_map_lt
#print axioms Madlul.TashfirKhawass.qab_list_roundtrip
#print axioms Madlul.TashfirKhawass.khawass_dec_enc
#print axioms Madlul.TashfirKhawass.tayyKhawass_la_yudi
#print axioms Madlul.TashfirKhawass.khawass_shawahid_tudi

-- جسرُ المعلومة المعمَّم (الثالث): طيُّ وفكُّ Aql.Mirsat.Mirsat بإعادة استعمال zigzag/BOUND من TashfirMadda
-- (Aql/TashfirMirsat.lean؛ نفس تفويض 2026-10-17 22:55؛ مشروطةٌ بـSahih — Subtype كـMaddaUnit، لا كـKhawass
-- غيرِ المشروطة — لأنّ حقول Mirsat الأربعة Int طليقةٌ لا أنواعًا محدودة)
#print axioms Aql.TashfirMirsat.mirsat_dec_enc
#print axioms Aql.TashfirMirsat.fakkOf_tawiOf
#print axioms Aql.TashfirMirsat.tayyMirsat_la_yudi
#print axioms Aql.TashfirMirsat.shawahid_sahih
#print axioms Aql.TashfirMirsat.mirsat_shawahid_tudi

-- جسرُ المعلومة المعمَّم (الرابع): طيُّ وفكُّ Aql.Azmina.Izaha؛ حقلٌ طليقٌ واحدٌ (adad) يكفيه موضعُ mixEnc
-- غيرُ المقيَّد فلا شرطَ Sahih هنا أصلًا (Aql/TashfirAzmina.lean؛ نفس تفويض 2026-10-17 22:55)
#print axioms Aql.TashfirAzmina.wahda_dec_enc
#print axioms Aql.TashfirAzmina.wahdaEnc_lt
#print axioms Aql.TashfirAzmina.izaha_dec_enc
#print axioms Aql.TashfirAzmina.tayyIzaha_la_yudi
#print axioms Aql.TashfirAzmina.izaha_asma_tudi

-- جسرُ المعلومة المعمَّم (الخامس): طيُّ وفكُّ Aql.Makan.Izaha3/Mawdi/Marja (Aql/TashfirMakan.lean؛ نفس
-- تفويض 2026-10-17 22:55). Marja نوعُ مجموعٍ: التاجُ محدودٌ في k₁، والحمولةُ طليقةٌ في o — لا blockEnc
-- (إخفاقانِ فعليّانِ موثَّقانِ في ترويسة الملفّ: تجسيدُ BOUND³ حوسوبيًّا OOM، ونداءُ simp جامعٌ يُعلِّق)
#print axioms Aql.TashfirMakan.izaha3_dec_enc
#print axioms Aql.TashfirMakan.izaha3FakkOf_tawiOf
#print axioms Aql.TashfirMakan.tayyIzaha3_la_yudi
#print axioms Aql.TashfirMakan.jiha_dec_enc
#print axioms Aql.TashfirMakan.jihaEnc_lt
#print axioms Aql.TashfirMakan.wahdaMakan_dec_enc
#print axioms Aql.TashfirMakan.wahdaMakanEnc_lt
#print axioms Aql.TashfirMakan.ojiha_dec_enc
#print axioms Aql.TashfirMakan.ojihaEnc_lt
#print axioms Aql.TashfirMakan.miq_dec_enc
#print axioms Aql.TashfirMakan.omiq_dec_enc
#print axioms Aql.TashfirMakan.mawdi_dec_enc
#print axioms Aql.TashfirMakan.tayyMawdi_la_yudi
#print axioms Aql.TashfirMakan.marja_dec_enc
#print axioms Aql.TashfirMakan.marjaTag_lt
#print axioms Aql.TashfirMakan.marjaFakkOf_tawiOf
#print axioms Aql.TashfirMakan.tayyMarja_la_yudi
#print axioms Aql.TashfirMakan.mawdi_shawahid_tudi
#print axioms Aql.TashfirMakan.marja_shawahid_sahih
#print axioms Aql.TashfirMakan.marja_shawahid_tudi

-- جسرُ المعلومة المعمَّم (السادس): طيُّ وفكُّ Aql.Awwaliyyat.Zaman5 (Aql/TashfirAwwaliyyat.lean؛ نفس تفويض
-- 2026-10-17 22:55). تعدادٌ محدودٌ بلا حمولة؛ ترميزٌ مباشرٌ بلا mixEnc أصلًا — أبسط من كلّ القطع 1–5.
#print axioms Aql.TashfirAwwaliyyat.zaman5_dec_enc
#print axioms Aql.TashfirAwwaliyyat.zaman5Enc_lt
#print axioms Aql.TashfirAwwaliyyat.tayyZaman5_la_yudi
#print axioms Aql.TashfirAwwaliyyat.zaman5_shawahid_tudi

-- أداةُ طيّ String العامّة (Madlul/TashfirNas.lean؛ نفس تفويض 2026-10-17 22:55). تركيبٌ على listEnc/listDec
-- من TashfirKhawass + مبرهناتِ نواة Lean (Char.ofNat_toNat، UInt32.toNat_lt، String.ofList_toList) بلا
-- برهانٍ جديدٍ تقريبًا؛ تفتح جسري Hawass وShabaka(alaqat) اللذين يحملان حقول String.
#print axioms Madlul.TashfirNas.char_dec_enc
#print axioms Madlul.TashfirNas.charEnc_lt
#print axioms Madlul.TashfirNas.charList_dec_enc
#print axioms Madlul.TashfirNas.charList_map_lt
#print axioms Madlul.TashfirNas.string_dec_enc
#print axioms Madlul.TashfirNas.tayyString_la_yudi
#print axioms Madlul.TashfirNas.string_shawahid_tudi
#print axioms JadwalLuzum.qawaninOf_shakl
#print axioms JadwalLuzum.qaidaOf_shakl
#print axioms JadwalLuzum.qaidaOf_mutadarrija
#print axioms JadwalLuzum.asl_rutba_sifr
#print axioms JadwalLuzum.luzum_min_taalil
#print axioms JadwalLuzum.juz_min_hadd
#print axioms JadwalLuzum.aslB_iff
#print axioms JadwalLuzum.iltizam_min_taalil
#print axioms JadwalLuzum.tadammun_min_juz
#print axioms JadwalLuzum.la_iltizam_bila_taalil
#print axioms JadwalLuzum.fahm_marifa_tadammun
#print axioms JadwalLuzum.fahm_qalb_tadammun
#print axioms JadwalLuzum.fahm_ilm_mutabaqa
#print axioms JadwalLuzum.iqal_talab_iltizam
#print axioms JadwalLuzum.fahm_la_iltizam
#print axioms JadwalLuzum.silat_sitt
#print axioms JadwalLuzum.talab_la_mubashir
-- النقلُ لصفوف جدول اللزوم (Madlul/JadwalLuzumNaql.lean)
#print axioms JadwalLuzum.la_mutawatir
#print axioms JadwalLuzum.mutadhafir_iff
#print axioms JadwalLuzum.yashhad_saff
#print axioms JadwalLuzum.la_daraja_bila_saff
#print axioms JadwalLuzum.daraja_jisr
#print axioms JadwalLuzum.bila_saff
#print axioms JadwalLuzum.la_yaqra_lafz
#print axioms JadwalLuzum.yasluh_iff
#print axioms JadwalLuzum.naw_hadd
#print axioms JadwalLuzum.naw_ithnan
#print axioms JadwalLuzum.iltizam_saff
#print axioms JadwalLuzum.shahid_luzum_maqayis
#print axioms JadwalLuzum.iltizam_jadwal
#print axioms JadwalLuzum.shahid_hadd
#print axioms JadwalLuzum.shahid_daraja
#print axioms JadwalLuzum.shahid_qiraat
#print axioms JadwalLuzum.shahid_fahm_juz_lisan
#print axioms Naht.aakhidha_bihazz
#print axioms Naht.farid_nodup
#print axioms Naht.manhut_ithnan
#print axioms Naht.amthila_manhuta
#print axioms Naht.bulum_yukhalif
#print axioms Ishtirak.ishtirak_iff
#print axioms Ishtirak.taraduf_iff
#print axioms Ishtirak.alaqa_tanazur
#print axioms Ishtirak.alaqa_hasira
#print axioms Ishtirak.shawahid_sibawayhi
#print axioms Ishtirak.isqat_yahfaz
#print axioms Ishtirak.silat_malik_arba
#print axioms Ishtirak.isqat_khams
#print axioms Ishtirak.dars_la_yasil
#print axioms Ishtirak.katiba_laysat_kitaba
#print axioms Tarjih.ashara_awjuh
#print axioms Tarjih.kull_zawj_marra
#print axioms Tarjih.khayr_min_khayr
#print axioms Tarjih.awla_la_yaksis
#print axioms Tarjih.bila_qarina_haqiqa
#print axioms Tarjih.qarina_tusrif
#print axioms Tarjih.la_ishtirak_maa_alaqa
#print axioms Tarjih.mushtarak_bila_qarina
#print axioms Tarjih.dars_dirasa
#print axioms Tarjih.dars_bila_siyaq
#print axioms Tarjih.sibawayhi_nabhani
#print axioms Tarjih.dars_laysa_mushtarak
#print axioms Nizam.tarkib_huwiyya_yamin
#print axioms Nizam.tarkib_huwiyya_yasar
#print axioms Nizam.tarkib_tajmii
#print axioms Nizam.salama_tatarakkab
#print axioms Nizam.la_tarkhis_bila_ma_qablahu
#print axioms Nizam.la_hukm_yasri
#print axioms Nizam.mumtani_yasri
#print axioms Nizam.tasduq_iff
#print axioms Nizam.tasduq_bi_mukhalifat
#print axioms Nizam.mukhalifat_dunya
#print axioms Nizam.mukhalifat_mukhalif
#print axioms Nizam.la_ilhaq_bila_illa
-- اقترانُ الدالّ بالمدلول: مرشَّحون من الوضع تقطعهم قيود، لقراءة صيغة الفعل وجنسه من خلاياه، وقرينةٍ تحسم
-- ما بقي محتملًا (Jisr/Iqtiran.lean؛ تفويضُ المالك 2026-10-18 «إغلاق دَين الاقتران» — إغلاقٌ محلّيٌّ، في
-- Mashru نفسِه، لفراغ QUYUD_ARE_INPUT المعلَن في Alghanem ADR٩٨، ولفراغٍ من نوعه في JisrDal نفسِه
-- (بابُ الصرف معلَنٌ من المعجم لا من الدالّ)). الأربعةُ مبرهنةٌ لكلّ (iqtiran_iff/tartib_la_yughayyir/
-- qayd_la_yazid/tabaqat، مسلّماتُها propext/Quot.sound فقط)؛ البقيّة مبرهنةٌ على الشاهد (decide).
#print axioms Jisr.Iqtiran.iqtiran_iff
#print axioms Jisr.Iqtiran.tartib_la_yughayyir
#print axioms Jisr.Iqtiran.qayd_la_yazid
#print axioms Jisr.Iqtiran.tabaqat
#print axioms Jisr.Iqtiran.sigha_afal_tartib
#print axioms Jisr.Iqtiran.shahid_sigha
#print axioms Jisr.Iqtiran.shahid_jins
#print axioms Jisr.Iqtiran.shahid_qarina
#print axioms Jisr.MantuqMafhum.mem_mukhalafaOf
#print axioms Jisr.MantuqMafhum.mem_jisrMn
#print axioms Jisr.MantuqMafhum.mem_jisr
#print axioms Jisr.MantuqMafhum.mafhum_min_mantuq
#print axioms Jisr.MantuqMafhum.la_mafhum_bila_haml
#print axioms Jisr.MantuqMafhum.mukhalafa_min_mukhalafaOf
#print axioms Jisr.MantuqMafhum.mukhalafa_min_qayd
#print axioms Jisr.MantuqMafhum.mukhalafa_shurut
#print axioms Jisr.MantuqMafhum.mani_yamna_mukhalafa
#print axioms Jisr.MantuqMafhum.ism_la_mukhalafa
#print axioms Jisr.MantuqMafhum.mukhalafa_wahida
#print axioms Jisr.MantuqMafhum.iqtida_shart_lil_mutabaqa
#print axioms Jisr.MantuqMafhum.adad_mafahim
#print axioms Jisr.MantuqMafhum.tariq_mafhum
#print axioms Jisr.MantuqMafhum.shawahid_mafhum
#print axioms Jisr.MantuqMafhum.shawahid_la_mafhum
#print axioms Jisr.MantuqMafhum.muwafaqa_bila_awlawiyya
#print axioms Jisr.MantuqMafhum.shahid_la_haml
#print axioms Jisr.MantuqMafhum.muwafaqa_tabia
#print axioms Jisr.MantuqMafhum.shahid_tabia
-- شهادةُ القيد من البنية تحت bilBunya: قيدُ المنطوق من جدول العوامل وجرد القطر في Lean (Jisr/QaydMafhum.lean؛ قولُ المالك 2026-10-24، 19:14)
#print axioms Jisr.QaydMafhum.qayd_bilBunya
#print axioms Jisr.QaydMafhum.bilBunya_sawa
#print axioms Jisr.QaydMafhum.mukhalafa_mashuda
#print axioms Jisr.QaydMafhum.la_mukhalafa_bila_shahid
#print axioms Jisr.QaydMafhum.innama_bunya_yamna
#print axioms Jisr.QaydMafhum.ghayr_mukhalafa_baqi
#print axioms Jisr.QaydMafhum.ghayr_mukhalafa_yabqa
#print axioms Jisr.QaydMafhum.adawat_shart
#print axioms Jisr.QaydMafhum.adawat_ghaya
#print axioms Jisr.QaydMafhum.shahid_istifham
#print axioms Jisr.QaydMafhum.ghaib_la_yashhad
#print axioms Jisr.QaydMafhum.wasf_fi_bab_amal
#print axioms Jisr.QaydMafhum.shawahid_mashuda
#print axioms Jisr.QaydMafhum.shawahid_sawa
#print axioms Jisr.QaydMafhum.shahid_bila_bunya_wa_innama
#print axioms Jisr.QaydMafhum.ism_iff
#print axioms Jisr.QaydMafhum.innamaFi_iff
#print axioms Jisr.QaydMafhum.jard_qatr
-- «هذا باب الجزاء» عند سيبويه (الكتاب س9190–9304؛ Jisr/BabJaza.lean): الحكمُ على تركيب الجزاء في الكلام والشعر، والجسرُ إلى القطر وجدول العوامل
#print axioms Jisr.BabJaza.maqbul_kalam_maqbul_shir
#print axioms Jisr.BabJaza.ghayr_la_hukm
#print axioms Jisr.BabJaza.jawab_bifil_aw_bilfa
#print axioms Jisr.BabJaza.waw_thumma_khata
#print axioms Jisr.BabJaza.fa_majzum_la_yuqbal
#print axioms Jisr.BabJaza.ismiyya_bila_rabit
#print axioms Jisr.BabJaza.raf_baad_jazm
#print axioms Jisr.BabJaza.raf_baad_madi
#print axioms Jisr.BabJaza.jazm_haythu_idh
#print axioms Jisr.BabJaza.idha_jazm
#print axioms Jisr.BabJaza.adawat_qatr
#print axioms Jisr.BabJaza.adawat_jadwal
#print axioms Jisr.BabJaza.qarn_qatr_tawafuq
-- ضابطُ باب الجزاء المجمَّد، النتيجةُ على الشفرة الحاليّة (Jisr/BabJazaQiyas.lean؛ hawkama/منهج_الضوابط.md في طلبه)
#print axioms Jisr.BabJaza.Qiyas.qarin_jadwal
#print axioms Jisr.BabJaza.Qiyas.majal
#print axioms Jisr.BabJaza.Qiyas.natija
#print axioms Jisr.BabJaza.Qiyas.natija_fia
#print axioms Jisr.BabJaza.Qiyas.akhta_sifr
-- جسرُ المعلومة المعمَّم (السابع): طيُّ وفكُّ Madlul.Hawass (Hassa/Hukm/Shidda/Thubut/Bud/Tasmiya/Khibra)
-- وMaratib.ShahidWaqi (Madlul/TashfirHawass.lean؛ نفس تفويض 2026-10-17 22:55). أداةٌ جديدةٌ: splitAtSep
-- (الفصلُ بقيمةٍ محجوزة لا بحدٍّ مختار) تفتح الحقول المتعدّدة من String معًا بلا Sahih/Subtype إلّا على
-- mawdi وحده (شرطٌ خفيفٌ، لا يُغلَّف بـTayy/Subtype عمدًا).
#print axioms Madlul.TashfirHawass.splitAtSep_join
#print axioms Madlul.TashfirHawass.hassa_dec_enc
#print axioms Madlul.TashfirHawass.hassaEnc_lt
#print axioms Madlul.TashfirHawass.tayyHassa_la_yudi
#print axioms Madlul.TashfirHawass.hukm_dec_enc
#print axioms Madlul.TashfirHawass.hukmEnc_lt
#print axioms Madlul.TashfirHawass.tayyHukm_la_yudi
#print axioms Madlul.TashfirHawass.shidda_dec_enc
#print axioms Madlul.TashfirHawass.shiddaEnc_lt
#print axioms Madlul.TashfirHawass.tayyShidda_la_yudi
#print axioms Madlul.TashfirHawass.thubut_dec_enc
#print axioms Madlul.TashfirHawass.thubutEnc_lt
#print axioms Madlul.TashfirHawass.tayyThubut_la_yudi
#print axioms Madlul.TashfirHawass.charBound_ge5
#print axioms Madlul.TashfirHawass.charBound_notin_charCodes
#print axioms Madlul.TashfirHawass.charCodes_lt
#print axioms Madlul.TashfirHawass.charCodes_dec_enc
#print axioms Madlul.TashfirHawass.bud_dec_enc
#print axioms Madlul.TashfirHawass.tasmiya_dec_enc
#print axioms Madlul.TashfirHawass.tayyTasmiya_la_yudi
#print axioms Madlul.TashfirHawass.shahid_dec_enc
#print axioms Madlul.TashfirHawass.khibra_dec_enc
#print axioms Madlul.TashfirHawass.abad_tudi
#print axioms Madlul.TashfirHawass.mujam_tudi
#print axioms Madlul.TashfirHawass.qawlMalik_tudi
#print axioms Madlul.TashfirHawass.qawlMalik_shawahid
#print axioms Madlul.TashfirHawass.khibrat_tudi
#print axioms Madlul.TashfirHawass.khibrat_eq
-- جسرُ المعلومة المعمَّم (الثامن): طيُّ وفكُّ Madlul.Shabaka (Luzum/Uslub/Fil/Qawl/Shabaka) — قطعةُ alaqat
-- من الاسم الثمانيّ. أداتانِ جديدتان: splitAllSep/joinTrailing (تعميمُ splitAtSep من جزءٍ واحدٍ إلى عددٍ
-- غيرِ محدود، بفاصلٍ لاحق)، وstringsEnc/stringsListEnc (طيُّ List String وList(List String) بهما، غيرَ
-- مشروطين بتاتًا). Shabaka (ستّةُ حقول List(String×String)) وQawl (أحدَ عشرَ منشِئًا بحقولَ نصّيّة) كلاهما
-- غيرُ مشروطٍ — الأشملُ بين قطع هذه السلسلة، بلا استثناءٍ واحدٍ كـmawdi في القطعة السابقة (Hawass).
#print axioms Madlul.TashfirShabaka.splitAtSep_snd_lt
#print axioms Madlul.TashfirShabaka.splitAllSep_unfold
#print axioms Madlul.TashfirShabaka.splitAllSep_joinTrailing
#print axioms Madlul.TashfirShabaka.joinTrailing_mem
#print axioms Madlul.TashfirShabaka.stringsEnc_lt
#print axioms Madlul.TashfirShabaka.stringsEnc_notMem
#print axioms Madlul.TashfirShabaka.stringsRaw_dec_enc
#print axioms Madlul.TashfirShabaka.strings_dec_enc
#print axioms Madlul.TashfirShabaka.stringsListEnc_lt
#print axioms Madlul.TashfirShabaka.stringsListEnc_notMem
#print axioms Madlul.TashfirShabaka.stringsList_dec_enc
#print axioms Madlul.TashfirShabaka.luzum_dec_enc
#print axioms Madlul.TashfirShabaka.luzumEnc_lt
#print axioms Madlul.TashfirShabaka.tayyLuzum_la_yudi
#print axioms Madlul.TashfirShabaka.uslub_dec_enc
#print axioms Madlul.TashfirShabaka.uslubEnc_lt
#print axioms Madlul.TashfirShabaka.tayyUslub_la_yudi
#print axioms Madlul.TashfirShabaka.fil_dec_enc
#print axioms Madlul.TashfirShabaka.tayyFil_la_yudi
#print axioms Madlul.TashfirShabaka.tagOf_lt
#print axioms Madlul.TashfirShabaka.toStrings_ofStrings
#print axioms Madlul.TashfirShabaka.qawl_dec_enc
#print axioms Madlul.TashfirShabaka.tayyQawl_la_yudi
#print axioms Madlul.TashfirShabaka.stringsToPairs_pairsToStrings
#print axioms Madlul.TashfirShabaka.shabaka_dec_enc
#print axioms Madlul.TashfirShabaka.tayyShabaka_la_yudi
#print axioms Madlul.TashfirShabaka.shabaka_tudi
#print axioms Madlul.TashfirShabaka.shabakaP_tudi
#print axioms Madlul.TashfirShabaka.qawl_shawahid
#print axioms Madlul.TashfirShabaka.fil_shahid
#print axioms Madlul.Fard116.licB_iff
#print axioms Madlul.Fard116.runL_imtina
#print axioms Madlul.Fard116.runL_qabul
#print axioms Madlul.Fard116.licB_iff_spaced
#print axioms Madlul.Fard116.illa_la_tajawur
#print axioms Madlul.Fard116.tajB_eq
#print axioms Madlul.Fard116.spacedB_iff
#print axioms Madlul.Fard116.licF_eq
#print axioms Madlul.Fard116.illa_sawa
#print axioms Madlul.Fard116.licN3_eq
#print axioms Madlul.Fard116.harf3_arqam
#print axioms Madlul.Fard116.maanN3_eq
#print axioms Madlul.Fard116.azwajQanun_kulluha
#print axioms Madlul.Fard116.tamathul_mujaz
#print axioms Madlul.Fard116.jumhur_atwal
#print axioms Madlul.Fard116.kharita3
#print axioms Madlul.Fard116.kharita4
#print axioms Madlul.Fard116.ramz_arqam3
#print axioms Madlul.Fard116.Shawahid.mukhalif_lisan3
#print axioms Madlul.Fard116.Shawahid.mukhalif_maqayis3
#print axioms Madlul.Fard116.Shawahid.mukhalif_lisan4
#print axioms Madlul.Fard116.Shawahid.mukhalif_lisan5
#print axioms Madlul.Fard116.Shawahid.jiwar_0_1
#print axioms Madlul.Fard116.Shawahid.jiwar_3_4
#print axioms Madlul.Fard116.Shawahid.jiwar_5_6
#print axioms Madlul.Fard116.Shawahid.jiwar_9_10
#print axioms Madlul.Fard116.Shawahid.jiwar_16_17
#print axioms Madlul.Fard116.Shawahid.jiwar_16_18
#print axioms Madlul.Fard116.Shawahid.jiwar_17_18
#print axioms Madlul.Fard116.Shawahid.jiwar_19_20
#print axioms Madlul.Fard116.Shawahid.jiwar_19_21
#print axioms Madlul.Fard116.Shawahid.jiwar_20_21
#print axioms Madlul.Fard116.Shawahid.jiwar_22_23
#print axioms Madlul.Fard116.Shawahid.jiwar_22_24
#print axioms Madlul.Fard116.Shawahid.jiwar_23_24
#print axioms Madlul.Fard116.Shawahid.jiwar_26_27
#print axioms Madlul.Fard116.Shawahid.jiwar_0_3
#print axioms Madlul.Fard116.Shawahid.jiwar_3_5
#print axioms Madlul.Fard116.Shawahid.jiwar_4_6
#print axioms Madlul.Fard116.Shawahid.jiwar_7_8
#print axioms Madlul.Fard116.Shawahid.jiwar_20_24
#print axioms Madlul.Fard116.Shawahid.jiwar_25_26
#print axioms Madlul.Fard116.Shawahid.jiwar_7_9
#print axioms Madlul.Fard116.Shawahid.jiwar_1_4
#print axioms Madlul.Fard116.Shawahid.jiwar_1_6
#print axioms Madlul.Fard116.Shawahid.jiwar_8_9
#print axioms Madlul.Fard116.Shawahid.jiwar_25_27
#print axioms Madlul.Fard116.Shawahid.jiwar_8_16
#print axioms Madlul.Fard116.Shawahid.jiwar_9_16
#print axioms Madlul.Fard116.Shawahid.jiwar_13_15
#print axioms Madlul.Fard116.Shawahid.jiwar_6_8
#print axioms Madlul.Fard116.Shawahid.tamathul_12
#print axioms Madlul.Fard116.Shawahid.tamathul_23
#print axioms Madlul.Fard116.Shawahid.tamathul_13
#print axioms Madlul.Fard116.Shawahid.qayd_3_4
#print axioms Madlul.Fard116.Shawahid.qayd_4_1
#print axioms Madlul.Fard116.Shawahid.qayd_21_20
#print axioms Madlul.Fard116.Shawahid.qayd_21_19
#print axioms Madlul.Fard116.Shawahid.qayd_9_7
#print axioms Madlul.Fard116.Shawahid.qayd_21_9
#print axioms Madlul.Fard116.Shawahid.qayd_16_9
#print axioms Madlul.Fard116.Shawahid.qayd_0_5
#print axioms Madlul.Fard116.Shawahid.qayd_6_3
#print axioms Madlul.Fard116.Shawahid.qayd_21_16
#print axioms Madlul.Fard116.Shawahid.tawlid4_G1
#print axioms Madlul.Fard116.Shawahid.tawlid4_G2
#print axioms Madlul.Fard116.Shawahid.tawlid4_Gr
#print axioms Madlul.Fard116.Shawahid.tawlid5
-- قرار المالك ٢ (Nizam/Talab.lean؛ ج3 س415): الأمر والالتماس والسؤال لا حكم بلا مقام
#print axioms Nizam.Talab.la_qisma_bila_maqam
#print axioms Nizam.Talab.qisma_bil_maqam
#print axioms Nizam.Talab.la_dalla_min_sigha
#print axioms Nizam.Talab.qismBiRutba_mutabayin
-- العقد الواحد (Nizam/Aqd.lean؛ قول المالك 2026-10-19 «البرهان المغلق لا يتجزأ…» و«حلل وقارن ثم  يُبنى طلبُ الدمج الواحد بهذا العقد موافق»)
#print axioms Nizam.Aqd.iqtiranB_iff
#print axioms Nizam.Aqd.tarkib_iff
#print axioms Nizam.Aqd.bit_wahid
#print axioms Nizam.Aqd.mustawa_iff
#print axioms Nizam.Aqd.kull_ma_kull
#print axioms Nizam.Aqd.la_shahid_la_hukm
#print axioms Nizam.Aqd.mumtani_asbab
#print axioms Nizam.Aqd.fahras
#print axioms Nizam.Aqd.madkhal_fakk
#print axioms Nizam.Aqd.khatwa_qanun
#print axioms Nizam.Aqd.runB_run
#print axioms Nizam.Aqd.fakk_ramz
#print axioms Nizam.Aqd.qina_illa
#print axioms Nizam.Aqd.nayta_qina
#print axioms Nizam.Aqd.siyagh_sawa
#print axioms Nizam.Aqd.run_kabir
#print axioms Nizam.Aqd.kama_sawa
#print axioms Nizam.Aqd.baad_sawa
#print axioms Nizam.Aqd.dalOK_taqatu
#print axioms Nizam.Aqd.jidhr_salim
#print axioms Nizam.Aqd.wahid_la_yakfi
#print axioms Nizam.Aqd.farq_dalLic
#print axioms Nizam.Aqd.irabMin_irabState
#print axioms Nizam.Aqd.irabMurashshah_la_jazm
#print axioms Nizam.Aqd.kataba_ilm_taraduf
#print axioms Nizam.Aqd.kataba_luzum_la_hukm
#print axioms Nizam.Aqd.qaltu_mumtani
#print axioms Nizam.Aqd.qala_la_hukm
#print axioms Nizam.Aqd.shawahid_sigha
#print axioms Nizam.Aqd.kataba_haal
-- Φ: التركيبُ الجامعُ المانع بالمنطق الثلاثيّ (Nizam/Phi.lean؛ قرار المالك 2026-10-20 00:23 «(ب) Φ العامّة في Lean مع المنطق الثلاثيّ، تُعمِّم kull_ma_kull. موافق»)
#print axioms Nizam.Phi.tabaqat_wa
#print axioms Nizam.Phi.tabaqat_aw
#print axioms Nizam.Phi.tabaqat_la_taarud
#print axioms Nizam.Phi.wa_P
#print axioms Nizam.Phi.wa_N
#print axioms Nizam.Phi.aw_P
#print axioms Nizam.Phi.aw_N
#print axioms Nizam.Phi.yujad_P
#print axioms Nizam.Phi.yujad_N
#print axioms Nizam.Phi.yujad_map_P
#print axioms Nizam.Phi.yujad_map_N
#print axioms Nizam.Phi.yujadMaftuh_P
#print axioms Nizam.Phi.yujadMaftuh_ne_N
#print axioms Nizam.Phi.yujadMaftuh_U
#print axioms Nizam.Phi.yujadN_P
#print axioms Nizam.Phi.yujadN_N
#print axioms Nizam.Phi.la_N_bila_istinfad
#print axioms Nizam.Phi.istinfad_shawahid
#print axioms Nizam.Phi.shahada_nisbiyya
#print axioms Nizam.Phi.tarkib_P
#print axioms Nizam.Phi.tarkib_N
#print axioms Nizam.Phi.zanjir_P
#print axioms Nizam.Phi.zanjir_N
#print axioms Nizam.Phi.zanjir_U
#print axioms Nizam.Phi.ghayruhuma_U
#print axioms Nizam.Phi.wa_tabadul
#print axioms Nizam.Phi.wa_aw_tawzi
#print axioms Nizam.Phi.yujad_map_wa
#print axioms Nizam.Phi.tahdith_nafsuhu
#print axioms Nizam.Phi.tahdith_ghayr
#print axioms Nizam.Phi.tahdith_nafs
#print axioms Nizam.Phi.tahdith_tabadul
#print axioms Nizam.Phi.yujadV_append
#print axioms Nizam.Phi.yujadV_la_yataallaq
#print axioms Nizam.Phi.yujadV_wa
#print axioms Nizam.Phi.awraq_la_yataallaq
#print axioms Nizam.Phi.phi_awd
#print axioms Nizam.Phi.imtidad_cons
#print axioms Nizam.Phi.yujadV_P
#print axioms Nizam.Phi.yujadV_N
#print axioms Nizam.Phi.kullAwamil_P
#print axioms Nizam.Phi.kullAwamil_N
#print axioms Nizam.Phi.shajara_P
#print axioms Nizam.Phi.shajara_N
#print axioms Nizam.Phi.shajara_U
#print axioms Nizam.Phi.wajiha_daruriyya
#print axioms Nizam.Phi.mithal_miftah
#print axioms Nizam.Phi.rutba_P
#print axioms Nizam.Phi.rutba_N
#print axioms Nizam.Phi.rutba_U
#print axioms Nizam.Phi.amilQanun_P
#print axioms Nizam.Phi.amilQanun_N
#print axioms Nizam.Phi.amilMani_P
#print axioms Nizam.Phi.amilMani_N
#print axioms Nizam.Phi.amilJidhr_P
#print axioms Nizam.Phi.amilJidhr_ghayr_N
#print axioms Nizam.Phi.amilShahid_P
#print axioms Nizam.Phi.amilShahid_ghayr_N
#print axioms Nizam.Phi.amil_sawa
#print axioms Nizam.Phi.phiAqdB_sawa
#print axioms Nizam.Phi.phiAqd_shajara
#print axioms Nizam.Phi.hukmB_phiB
#print axioms Nizam.Phi.aqd_phi
#print axioms Nizam.Phi.phiAqd_P
#print axioms Nizam.Phi.phiAqd_N
#print axioms Nizam.Phi.phiAqd_farigh
#print axioms Nizam.Phi.kull_ma_kull_min_phi
#print axioms Nizam.Phi.jidhr_hadd
#print axioms Nizam.Phi.aqd_phi_mashru
#print axioms Nizam.Phi.hukmB_shajara_mashru
#print axioms Nizam.Phi.kataba_phi

-- جدولُ اللزوم من مقاييس اللغة ولسان العرب (Jisr/JadwalLuzum.lean؛ تفويض المالك 2026-10-18، مهمّة #87):
-- سبعةُ جذوعٍ ثلاثيّةٍ بشهاداتٍ معجميّةٍ حرفيّة، شبكةٌ ومركزيّةُ «علم» مبرهنةٌ من الدرجة، وغرسٌ في
-- Madlul/Dalala.lean وAql/QawaninDalala.lean (مطابقة/تضمّن/التزام حقيقيّةً ثمّ مرخَّصةً جبريًّا).
#print axioms Jisr.JadwalLuzum.judhur_markhasa
#print axioms Jisr.JadwalLuzum.qaidaL_mutadarrija
#print axioms Jisr.JadwalLuzum.shahid_kataba_ilm_murtabit
#print axioms Jisr.JadwalLuzum.shahid_talab_ilm_murtabit
#print axioms Jisr.JadwalLuzum.murtabit_qalam_ilm_la_murakhkhas
#print axioms Jisr.JadwalLuzum.qalam_ilm_marfud
#print axioms Jisr.JadwalLuzum.ilm_markaz
#print axioms Jisr.JadwalLuzum.darajat_baqiya
#print axioms Jisr.JadwalLuzum.masafat_kataba
#print axioms Jisr.JadwalLuzum.masafat_talab
#print axioms Jisr.JadwalLuzum.masafat_ilm
#print axioms Jisr.JadwalLuzum.kull_mutabaqa_nafsiha
#print axioms Jisr.JadwalLuzum.ilm_tadammun_fahm
#print axioms Jisr.JadwalLuzum.kataba_iltizam_qalam
#print axioms Jisr.JadwalLuzum.shahidLuzum_shakl
#print axioms Jisr.JadwalLuzum.shahidLuzum_mutadarrija
#print axioms Jisr.JadwalLuzum.shahid_ilm_tadammun_fahm
#print axioms Jisr.JadwalLuzum.shahid_kataba_iltizam_qalam
-- الفاحص التنفيذيّ: نوعُ مودَع السند لا يأخذه قيدٌ فارغ (Faahis/Lib.lean؛ سدّ البصمة الفارغة 2026-10-19)
#print axioms nawSanad_basma_farigha
#print axioms nawSanad_aslMusajjal
#print axioms nawSanad_sanad
#print axioms nawSanad_sanad_farigh
-- التحميل المحقَّق: السلطة من سجلّ المودَعات وحده، وخطأ التحميل يُسلَّم باسمه (Faahis/Lib.lean؛ خطّة الإطلاق P1-أ)
#print axioms qira_mudaat
#print axioms khata_mudaat
#print axioms muhtawa_la_yudif_mudaa
#print axioms tahmil_muhtawa_mudaat
#print axioms tahmil_mudaat
#print axioms bila_sijill_la_mudaa
#print axioms muhaqqaq_salim
#print axioms qira_mudaa_muhtawa
#print axioms sijill_la_yahmil_muhtawa
#print axioms tahmil_sijill_muhtawa
#print axioms sijill_la_muhtawa
-- س1 (قولُ المالك 2026-10-24، 18:07): التنفيذُ السريع مكافئٌ للفاحص — القوانينُ مصفوفةً والأصولُ جدولًا، والقبولُ والمخزنُ والأصلُ هي هي
#print axioms Qaida.tatbiqA_eq
#print axioms Qaida.fahsA_eq
#print axioms Qaida.maqbulA_eq
#print axioms Mawsua.udkhulA_eq
#print axioms jadwalUsul_foldl
#print axioms jadwalUsul_find
#print axioms bina_asl
#print axioms bina_aslB
#print axioms bina_aslW
#print axioms bina_q
-- جبرُ الدمج المبرهن (مرحلة الدمج الأولى، سمّاها عرضُ الدمج «م1» وليست م1 البروتوكول؛ Nizam/Damj.lean؛ إذن المالك 2026-10-19 16:16)
#print axioms Nizam.Damj.bahth_mawjud
#print axioms Nizam.Damj.bahth_ghaib
#print axioms Nizam.Damj.ghayr_farigh
#print axioms Nizam.Damj.sahih_iff
#print axioms Nizam.Damj.damj1_tanazur
#print axioms Nizam.Damj.damj1_tikrar
#print axioms Nizam.Damj.damj1_janib_wahid
#print axioms Nizam.Damj.damj1_taarud_iff
#print axioms Nizam.Damj.damj1_la_ikhtira
#print axioms Nizam.Damj.damj1_ghaib
#print axioms Nizam.Damj.damj1_tajmii
#print axioms Nizam.Damj.ray_ghaib_sahih
#print axioms Nizam.Damj.ray_ghaib
#print axioms Nizam.Damj.ray_qima
#print axioms Nizam.Damj.ray_hadir
#print axioms Nizam.Damj.ray_asas
#print axioms Nizam.Damj.mem_farid
#print axioms Nizam.Damj.farid_nodup
#print axioms Nizam.Damj.jam_taarud
#print axioms Nizam.Damj.jam_juz
#print axioms Nizam.Damj.jam_mafatih
#print axioms Nizam.Damj.jam_sahih
#print axioms Nizam.Damj.jam_some
#print axioms Nizam.Damj.mem_mafatih
#print axioms Nizam.Damj.damjMiftah_kharij
#print axioms Nizam.Damj.damj_some
#print axioms Nizam.Damj.damj_nuqta
#print axioms Nizam.Damj.damj_bilaTakrar
#print axioms Nizam.Damj.damj_maqbul_iff
#print axioms Nizam.Damj.mem_mutaarida
#print axioms Nizam.Damj.takrarFi_nil_iff
#print axioms Nizam.Damj.bilaTakrar_iff
#print axioms Nizam.Damj.damj_marfud_iff
#print axioms Nizam.Damj.taarud_yamna
#print axioms Nizam.Damj.ray_damj
#print axioms Nizam.Damj.hadhf_yabqa
#print axioms Nizam.Damj.hadhfMaadhun_damj
#print axioms Nizam.Damj.ray_tasawi
#print axioms Nizam.Damj.damj_tanazur
#print axioms Nizam.Damj.damj_tikrar
#print axioms Nizam.Damj.damj_janib_wahid
#print axioms Nizam.Damj.la_faqd
#print axioms Nizam.Damj.la_faqd_janib
#print axioms Nizam.Damj.la_faqd_janib_b
#print axioms Nizam.Damj.la_ikhtira
#print axioms Nizam.Damj.damj_tajmii
#print axioms Nizam.Damj.mutakafi_inikas
#print axioms Nizam.Damj.mutakafi_tanazur
#print axioms Nizam.Damj.mutakafi_taaddi
#print axioms Nizam.Damj.mutakafi_natija
#print axioms Nizam.Damj.damj_tawafuq
#print axioms Nizam.Damj.damj_tikrar_mutakafi
#print axioms Nizam.Damj.damj_tanazur_mutakafi
#print axioms Nizam.Damj.damj_tajmii_mutakafi
#print axioms Nizam.Damj.shahid_hadhf_mahmul
#print axioms Nizam.Damj.salamat_damj
#print axioms Nizam.Damj.shahid_hadith_35
#print axioms Nizam.Damj.shahid_hadith_767e09b
#print axioms Nizam.Damj.shawahid_hadhf
#print axioms Nizam.Damj.shahid_hadhf_la_yaud
#print axioms Nizam.Damj.shawahid_taarud
#print axioms Nizam.Damj.shahid_la_yuhmal_min_hadir
#print axioms Nizam.Damj.musawat_harfiyya_la_tasihh
#print axioms Nizam.Damj.shawahid_mubarhanat
#print axioms Jisr.QawaidSitta.kullMawdi_mono
#print axioms Jisr.QawaidSitta.qiraaSitta_min_qiraa
#print axioms Jisr.QawaidSitta.hukmSitta_murakhkhas_thabit
#print axioms Jisr.QawaidSitta.hukm3_shakl
#print axioms Jisr.QawaidSitta.hukmSitta_shakl
#print axioms Jisr.QawaidSitta.shakl_mumtani
#print axioms Jisr.QawaidSitta.shakl_laHukm_mumtani
#print axioms Jisr.QawaidSitta.shakl_murakhkhas
#print axioms Jisr.QawaidSitta.hukmQiraa_ne_mumtani
#print axioms Jisr.QawaidSitta.hukmSitta_mumtani_thabit
#print axioms Jisr.QawaidSitta.hukmSitta_kharij
#print axioms Jisr.QawaidSitta.raf_bi_qiraa
#print axioms Jisr.QawaidSitta.mumtani_bi_qiraa
#print axioms Jisr.QawaidSitta.natija_murab
#print axioms Jisr.QawaidSitta.silsila_maqbula
#print axioms Jisr.QawaidSitta.rukhsa_murakhkhasa
#print axioms Jisr.QawaidSitta.la_tamdid
#print axioms Jisr.QawaidSitta.suwar_sitta
#print axioms Jisr.QawaidSitta.sahib_la_yathbut
#print axioms Jisr.QawaidSitta.sahib_muqaddima
#print axioms Jisr.QawaidSitta.dhu_la_rukhsa
#print axioms Jisr.QawaidSitta.qanun_raf_fi
#print axioms Jisr.QawaidSitta.ghayr_sitta
#print axioms Jisr.QawaidSitta.jadwal_jisrdal
#print axioms Jisr.QawaidSitta.shawahid_jisrdal
#print axioms Jisr.QawaidSitta.abuK_jadwal
#print axioms Jisr.QawaidSitta.shawahid_sitta
#print axioms Jisr.QawaidSitta.daraja_wujuh
#print axioms Jisr.QawaidSitta.shartMawdi_shurut
#print axioms Jisr.QawaidSitta.fiMawdi_shartan
#print axioms Jisr.QawaidSitta.mawadi_shawahid
#print axioms Jisr.QawaidSitta.fiMawdi_wujud
#print axioms Jisr.QawaidSitta.isdar_basma
#print axioms Jisr.QawaidSitta.asl_mawdi
#print axioms Dal.Adad.adadR_append
#print axioms Dal.Adad.adad_wasl
#print axioms Dal.Adad.adadR_inj
#print axioms Dal.Adad.adad_inj
#print axioms Dal.Adad.fakkR_adadR
#print axioms Dal.Adad.adadR_fakkR
#print axioms Dal.Adad.fakkR_majal
#print axioms Dal.Adad.fakk_adad
#print axioms Dal.Adad.adad_fakk
#print axioms Dal.Adad.fakk_majal
#print axioms Dal.Adad.adad_tabdil
#print axioms Dal.Adad.kataba_wasl
#print axioms Dal.Adad.kataba_kutiba
#print axioms Dal.Adad.bila_tul_yajma
#print axioms Dal.Adad.majmuAwwal_succ
#print axioms Dal.Adad.jam_darb
#print axioms Dal.Adad.qima_snoc
#print axioms Dal.Adad.adad_sigha
#print axioms Dal.Adad.kharij_majal
#print axioms Nizam.QawaidB.fahsM_usul
#print axioms Nizam.QawaidB.maqbul_silsila
#print axioms Nizam.QawaidB.rukhsa_usul
#print axioms Nizam.QawaidB.ramz_majal
#print axioms Nizam.QawaidB.ramz_sawa
#print axioms Nizam.QawaidB.qawaninB_qiyam
#print axioms Nizam.QawaidB.qinaHalat_bit
#print axioms Nizam.QawaidB.qinaHalat_sifr
#print axioms Nizam.QawaidB.alamat_bitat
#print axioms Nizam.QawaidB.qanun_bitat
#print axioms Nizam.QawaidB.rukhsaB_sawa
#print axioms Nizam.QawaidB.mawqufB_sawa
#print axioms Nizam.QawaidB.qiraaB_sawa
#print axioms Nizam.QawaidB.hukmB_sawa
#print axioms Nizam.QawaidB.mawadi_bitat
#print axioms Nizam.QawaidB.naqs_shawahid
#print axioms Nizam.Baqi.dimn_iff
#print axioms Nizam.Baqi.dimn_nafs
#print axioms Nizam.Baqi.dimn_trans
#print axioms Nizam.Baqi.dimn_asghar
#print axioms Nizam.Baqi.dimn_sifr
#print axioms Nizam.Baqi.dimn_aw
#print axioms Nizam.Baqi.adna_min
#print axioms Nizam.Baqi.adna_kamil
#print axioms Nizam.Baqi.adna_silsila
#print axioms Nizam.Baqi.qima_ratiba
#print axioms Nizam.Baqi.qima_dharrat
#print axioms Nizam.Baqi.baqi_sahih
#print axioms Nizam.Baqi.baqi_kamil
#print axioms Nizam.Baqi.baqi_adna
#print axioms Nizam.Baqi.P_iff
#print axioms Nizam.Baqi.qinaMin_bit
#print axioms Nizam.Baqi.N_iff
#print axioms Nizam.Baqi.k3_P
#print axioms Nizam.Baqi.k3_N
#print axioms Nizam.Baqi.hukm_k3
#print axioms Nizam.Baqi.natija_hukm
#print axioms Nizam.Baqi.taarud_yukhfa
#print axioms Nizam.Baqi.baqi_talab
#print axioms Nizam.Baqi.usulB_sghir
#print axioms Nizam.Baqi.naqsB_baqi
#print axioms Nizam.Baqi.rukhsaB_k3
#print axioms Nizam.Baqi.mithal_badilan
#print axioms Nizam.Baqi.mithal_tasghir
#print axioms Nizam.Baqi.mithal_dhu

-- الواقع المختوم: المشاهدة والحكم بشرط الختم والنموّ (Aql/Waqi.lean)، وشواهدُ الدفعة الأولى (Aql/WaqiShawahid.lean)
#print axioms Waqi.la_hukm_bila_mushahada
#print axioms Waqi.laHukm_iff
#print axioms Waqi.la_mafhum_bila_khatm
#print axioms Waqi.qiyas_makhtum_mafhum
#print axioms Waqi.riwayatan_mafhum
#print axioms Waqi.masdar_wahid_la_yarfa
#print axioms Waqi.mutabiq_append
#print axioms Waqi.numuw_la_yunzil
#print axioms Waqi.khatm_la_yunzil
#print axioms Waqi.akhir_numuw
#print axioms Waqi.jisr_iff
#print axioms Waqi.Shawahid.adad
#print axioms Waqi.Shawahid.ihsa
#print axioms Waqi.Shawahid.python_yahsub
#print axioms Waqi.Shawahid.lean_yaqbal_wa_yarud
#print axioms Waqi.Shawahid.basma_bihassatayn
#print axioms Waqi.Shawahid.isdar_ahad
#print axioms Waqi.Shawahid.github_riwaya
#print axioms Waqi.Shawahid.jisr_haqiqi
#print axioms Waqi.Shawahid.hukm_ala_kull_sijill
#print axioms Waqi.Shawahid.ihsa_ala_kull_sijill
-- عقدُ القياس (Nizam/Qiyas.lean؛ hawkama/معايير_القياس.md؛ قول المالك 2026-10-22 16:10)
#print axioms Nizam.Qiyas.diqqa_none_iff
#print axioms Nizam.Qiyas.adad_imtina_sahih
#print axioms Nizam.Qiyas.adad_imtina_khata
#print axioms Nizam.Qiyas.kull_imtina_la_diqqa
#print axioms Nizam.Qiyas.adad_append
#print axioms Nizam.Qiyas.imtina_la_yughayyir_diqqa
#print axioms Nizam.Qiyas.imtina_taghtiya_sifr
#print axioms Nizam.Qiyas.khata_dun_imtina
#print axioms Nizam.Qiyas.imtina_dun_sahih
#print axioms Nizam.Qiyas.majmu_eq
#print axioms Nizam.Qiyas.jawab_afdal_iff
#print axioms Nizam.Qiyas.majmuBunud_eq
#print axioms Nizam.Qiyas.jawab_afdal_bunud
#print axioms Nizam.Qiyas.tahwil_khata_imtina
#print axioms Nizam.Qiyas.khata_la_yarfa
#print axioms Nizam.Qiyas.shahid_diqqa_taghtiya

-- الجسر المحلي المثبت إلى NABT؛ حدود المصدر والتمثيل والرتبة محفوظة.
#print axioms Jisr.NabtBridge.cell_roundtrip
#print axioms Jisr.NabtBridge.atom_roundtrip
#print axioms Jisr.NabtBridge.cell_transport_injective
#print axioms Jisr.NabtBridge.carrier_names
#print axioms Jisr.NabtBridge.cell_decode_native
#print axioms Jisr.NabtBridge.cell_preserves_mark
#print axioms Jisr.NabtBridge.cell_preserves_name
#print axioms Jisr.NabtBridge.numeric_identity_is_wrong
#print axioms Jisr.NabtBridge.cells_roundtrip
#print axioms Jisr.NabtBridge.atoms_roundtrip
#print axioms Jisr.NabtBridge.cells_length
#print axioms Jisr.NabtBridge.cells_append
#print axioms Jisr.NabtBridge.cells_injective
#print axioms Jisr.NabtBridge.little_number_native
#print axioms Jisr.NabtBridge.number_native
#print axioms Jisr.NabtBridge.number_transport
#print axioms Jisr.NabtBridge.source_roundtrip
#print axioms Jisr.NabtBridge.canonical_source_roundtrip
#print axioms Jisr.NabtBridge.source_metadata
#print axioms Jisr.NabtBridge.source_injective
#print axioms Jisr.NabtBridge.valid_span_iff
#print axioms Jisr.NabtBridge.span_atoms
#print axioms Jisr.NabtBridge.certificate_source
#print axioms Jisr.NabtBridge.certificate_reconstruct
#print axioms Jisr.NabtBridge.certificate_bounds
#print axioms Jisr.NabtBridge.certificate_transport_reconstruct
#print axioms Jisr.NabtBridge.no_composite_without_evidence
#print axioms Jisr.NabtBridge.certificate_join_boundary
#print axioms Jisr.NabtBridge.inquiry_rank_bounded
#print axioms Jisr.NabtBridge.experimental_rank_bounded
#print axioms Jisr.NabtBridge.inquiry_requires_scope
#print axioms Jisr.NabtBridge.inquiry_requires_provenance
#print axioms Jisr.NabtBridge.inquiry_exhaustion_not_license
#print axioms Jisr.NabtBridge.no_meaning_promotion_without_world_witness
#print axioms Jisr.NabtBridge.empty_registry_stays_information
#print axioms Jisr.NabtBridge.kataba_transport
#print axioms Jisr.NabtBridge.atom_does_not_license_join
#print axioms Jisr.NabtBridge.filtered_gap_is_invalid
#print axioms Jisr.NabtBridge.same_ids_different_source_is_invalid
#print axioms Jisr.NabtBridge.insufficient_budget_stays_exhausted
#print axioms Jisr.NabtBridge.supplied_numeric_rank_does_not_override_mashru
-- نفيُ الفعل وحروفُ الفعل عند سيبويه (الكتاب س9755–9787؛ Jisr/NafyFil.lean): النفيُ والإثباتُ على Awwaliyyat.Zaman5، وما يلي الحرف
#print axioms Jisr.NafyFil.jawab_ghayr_farigh
#print axioms Jisr.NafyFil.nafy_khamsa
#print axioms Jisr.NafyFil.yafal_bila_hal
#print axioms Jisr.NafyFil.qasam_shawahid
#print axioms Jisr.NafyFil.sin_wa_hal
#print axioms Jisr.NafyFil.la_hukm_shawahid
#print axioms Jisr.NafyFil.la_yufsal_khata
#print axioms Jisr.NafyFil.maqbul_kalam_maqbul_shir
-- ضابطُ نفي الفعل المجمَّد، النتيجةُ على الشفرة الحاليّة (Jisr/NafyFilQiyas.lean؛ hawkama/منهج_الضوابط.md)، ومبرهنةُ «رب» و«قل» بعد قراءة الحالات
#print axioms Jisr.NafyFil.rubba_bila_ma
#print axioms Jisr.NafyFil.hal_tusaffi_qasam
#print axioms Jisr.NafyFil.huruf_jadwal
#print axioms Jisr.NafyFil.Qiyas.qarin_jadwal
#print axioms Jisr.NafyFil.Qiyas.qarin_suwar
#print axioms Jisr.NafyFil.Qiyas.majal
#print axioms Jisr.NafyFil.Qiyas.natija
#print axioms Jisr.NafyFil.Qiyas.natija_fia
#print axioms Jisr.NafyFil.Qiyas.akhta_sifr
-- «هذا باب الفاء» عند سيبويه (الكتاب س8914–9049؛ Jisr/BabFa.lean): الفعلُ بعد الفاء في الواجب وغير الواجب، بالمعنى والإعراب
#print axioms Jisr.BabFa.kalam_ghayr_farigh
#print axioms Jisr.BabFa.wajib_la_nasb
#print axioms Jisr.BabFa.amr_la_jazm
#print axioms Jisr.BabFa.nasb_ghayr_wajib
#print axioms Jisr.BabFa.maqbul_kalam_maqbul_shir
#print axioms Jisr.BabFa.ijab_yufarriq
#print axioms Jisr.BabFa.ghamid_shawahid
-- ضابطُ باب الفاء المجمَّد، النتيجةُ على الشفرة الحاليّة (Jisr/BabFaQiyas.lean؛ hawkama/منهج_الضوابط.md)، وشاهدُ ما غُيّر بعد قراءة الحالات
#print axioms Jisr.BabFa.baad_qiraa
#print axioms Jisr.BabFa.Qiyas.qarin_jadwal
#print axioms Jisr.BabFa.Qiyas.qarin_badil
#print axioms Jisr.BabFa.Qiyas.majal
#print axioms Jisr.BabFa.Qiyas.natija
#print axioms Jisr.BabFa.Qiyas.natija_fia
#print axioms Jisr.BabFa.Qiyas.akhta_2
-- مجاري أواخر الكلم عند سيبويه (الكتاب س111–233؛ Jisr/MajariKalim.lean): علامةُ الآخر بالصنف والموضع، إعرابًا أو بناءً
#print axioms Jisr.MajariKalim.la_jazm_fi_asma
#print axioms Jisr.MajariKalim.la_jarr_fi_mudari
#print axioms Jisr.MajariKalim.mabni_la_yataghayyar
#print axioms Jisr.MajariKalim.irab_bil_harf
#print axioms Jisr.MajariKalim.la_yansarif
#print axioms Jisr.MajariKalim.haythu_wa_ghayruha
-- ضابطُ مجاري أواخر الكلم المجمَّد، النتيجةُ على الشفرة الحاليّة (Jisr/MajariKalimQiyas.lean؛ hawkama/منهج_الضوابط.md)، و«ليس للفعل في الجر نصيب» بعد قراءة الحالات
#print axioms Jisr.MajariKalim.la_jarr_fi_fil
#print axioms Jisr.MajariKalim.Qiyas.qarin_jadwal
#print axioms Jisr.MajariKalim.Qiyas.majal
#print axioms Jisr.MajariKalim.Qiyas.natija
#print axioms Jisr.MajariKalim.Qiyas.natija_fia
#print axioms Jisr.MajariKalim.Qiyas.akhta_sifr
-- الوقفُ على أواخر الكلم المتحرّكة في الوصل عند سيبويه (الكتاب س17782–17859؛ Dal/WaqfSibawayhi.lean): وجهُ الوقف بالآخر والتنوين وما قبله والحركة
#print axioms Dal.WaqfSibawayhi.la_ishmam
#print axioms Dal.WaqfSibawayhi.tadif_baad_sakin
#print axioms Dal.WaqfSibawayhi.maqbul_kalam_maqbul_shir
#print axioms Dal.WaqfSibawayhi.munawwan_nasb_kull
#print axioms Dal.WaqfSibawayhi.hadhf_wa_qawafi
#print axioms Dal.WaqfSibawayhi.mumkin_shawahid
#print axioms Dal.WaqfSibawayhi.shawahid
-- ضابطُ الوقف عند سيبويه المجمَّد، النتيجةُ على الشفرة الحاليّة (Dal/WaqfSibawayhiQiyas.lean؛ hawkama/منهج_الضوابط.md)، وشواهدُ ما أُضيف بعد قراءة الحالات
#print axioms Dal.WaqfSibawayhi.munawwan_nasb_shawahid
#print axioms Dal.WaqfSibawayhi.Qiyas.qarin_jadwal
#print axioms Dal.WaqfSibawayhi.Qiyas.majal
#print axioms Dal.WaqfSibawayhi.Qiyas.natija
#print axioms Dal.WaqfSibawayhi.Qiyas.natija_fia
#print axioms Dal.WaqfSibawayhi.Qiyas.akhta_2
-- بقيّةُ أبواب الجزاء عند سيبويه (الكتاب س9305–9652؛ Jisr/BaqiJaza.lean) وضابطُها المجمَّد (Jisr/BaqiJazaQiyas.lean؛ hawkama/منهج_الضوابط.md)
#print axioms Jisr.BaqiJaza.mutlaq_salim
#print axioms Jisr.BaqiJaza.hukmSila_salim
#print axioms Jisr.BaqiJaza.hukmRafMudari_salim
#print axioms Jisr.BaqiJaza.hukmAsl_salim
#print axioms Jisr.BaqiJaza.hukmJaza_salim
#print axioms Jisr.BaqiJaza.maqbul_kalam_maqbul_shir
#print axioms Jisr.BaqiJaza.tamm
#print axioms Jisr.BaqiJaza.harf_la_sila
#print axioms Jisr.BaqiJaza.jazm_yadhhab
#print axioms Jisr.BaqiJaza.jazm_yabqa
#print axioms Jisr.BaqiJaza.nazir
#print axioms Jisr.BaqiJaza.bayn_la_raf
#print axioms Jisr.BaqiJaza.thumma_la_nasb
#print axioms Jisr.BaqiJaza.awail_kulluha
#print axioms Jisr.BaqiJaza.wajib_la_jaza
#print axioms Jisr.BaqiJaza.la_jazm_bighayr
#print axioms Jisr.BaqiJaza.badal_wa_ghalat
#print axioms Jisr.BaqiJaza.waw_hal_badilan
#print axioms Jisr.BaqiJaza.lakin_badilan
#print axioms Jisr.BaqiJaza.rabit_la_hukm
#print axioms Jisr.BaqiJaza.Qiyas.qarin_jadwal
#print axioms Jisr.BaqiJaza.Qiyas.qarin_badil
#print axioms Jisr.BaqiJaza.Qiyas.majal
#print axioms Jisr.BaqiJaza.Qiyas.natija
#print axioms Jisr.BaqiJaza.Qiyas.natija_fia
#print axioms Jisr.BaqiJaza.Qiyas.akhta_2
#print axioms Jisr.NassItar.hurufJarr_wad
#print axioms Jisr.NassItar.itarat_mem
#print axioms Jisr.NassItar.itarat_kalimat
#print axioms Jisr.NassItar.jamaa_murakhkhas
#print axioms Jisr.NassItar.jamaa_mumtani
#print axioms Jisr.NassItar.hukmNass_murakhkhas
#print axioms Jisr.NassItar.hukmNass_mumtani
#print axioms Jisr.NassItar.la_itar_la_hukm
#print axioms Jisr.NassItar.maqbula_iff
#print axioms Jisr.NassItar.fard_madlul
#print axioms Jisr.NassItar.yuid_shawahid
#print axioms Jisr.NassItar.haraka_tughayyir
#print axioms Jisr.NassItar.itar_min_hukm
#print axioms Jisr.NassItar.haykal_fil_la_itar
#print axioms Jisr.NassItar.Dabit.qarin_hukm
#print axioms Jisr.NassItar.Dabit.qarin_itar
#print axioms Jisr.NassItar.Dabit.rafd_ikhfaq
#print axioms Jisr.NassItar.Dabit.itar_tabi_hukm
#print axioms Jisr.NassItar.Qiyas.majal
#print axioms Jisr.NassItar.Qiyas.natija
#print axioms Jisr.NassItar.Qiyas.natija_fia
#print axioms Jisr.NassItar.Qiyas.akhta_1
#print axioms Jisr.NassItar.Qiyas.azwaj_1
#print axioms Jisr.NassItar.Qiyas.asbab_akhta
#print axioms Jisr.NassItar.Qiyas.waslBase_khanat
#print axioms Jisr.NassItar.Qiyas.khana_hala
#print axioms Jisr.NassItar.Qiyas.khalalKhana_nil
#print axioms Jisr.NassItar.Qiyas.waslBase_khalal
-- صكُّ الجملة (Jisr/SakkJumla.lean): القوّةُ والسببُ المذكورُ والمرجعُ من صورة التركيب، والواقعُ بعد القوّة؛ وتشخيصٌ على مرجع NABT
#print axioms Jisr.SakkJumla.taliq_la_yukhbar
#print axioms Jisr.SakkJumla.thani_la_ikhbar
#print axioms Jisr.SakkJumla.awwal_khabar_iff
#print axioms Jisr.SakkJumla.qala_amma_la_zann
#print axioms Jisr.SakkJumla.illa_bi_dall
#print axioms Jisr.SakkJumla.zarf_laysa_sabab
#print axioms Jisr.SakkJumla.lamma_wajhan
#print axioms Jisr.SakkJumla.hatta_wa_fa
#print axioms Jisr.SakkJumla.muayyan_iff
#print axioms Jisr.SakkJumla.ithnan_la_yataayyan
#print axioms Jisr.SakkJumla.ishara_ithnan_la_hukm
#print axioms Jisr.SakkJumla.la_marji_bila_siyaq
#print axioms Jisr.SakkJumla.la_waqi_bila_ikhbar
#print axioms Jisr.SakkJumla.thani_la_mafhum
#print axioms Jisr.SakkJumla.la_waqi_bila_mushahada
#print axioms Jisr.SakkJumla.la_dafi_bila_dall
#print axioms Jisr.SakkJumla.waqiNabt_iff
#print axioms Jisr.SakkJumla.nabt_quwwa
#print axioms Jisr.SakkJumla.nabt_marji
#print axioms Jisr.SakkJumla.nabt_marji_C05
#print axioms Jisr.SakkJumla.marjiNabt_huwa_mufassiran
#print axioms Jisr.SakkJumla.nabt_la_tarqiya
#print axioms Jisr.SakkJumla.taliq_iff_jaza
#print axioms Jisr.SakkJumla.lam_nafy_madi
#print axioms Jisr.SakkJumla.mafulLahu_qatr
-- ضابطُ صكّ الجملة المجمَّد، النتيجةُ على الشفرة الحاليّة (Jisr/SakkJumlaQiyas.lean؛ hawkama/منهج_الضوابط.md)
#print axioms Jisr.SakkJumla.Qiyas.qarin_shawahid
#print axioms Jisr.SakkJumla.Qiyas.majal
#print axioms Jisr.SakkJumla.Qiyas.natija
#print axioms Jisr.SakkJumla.Qiyas.natija_fia
#print axioms Jisr.SakkJumla.Qiyas.akhta_5

-- تمامُ التدقيق (tahaqquq/test_tadqiq_tamm.py، 2026-10-26): مبرهناتٌ عامّةٌ مبنيّةٌ لم تكن هنا، بترتيبها في ملفّاتها.
-- SLGE.Core
#print axioms SLGE.blockDec_enc
#print axioms SLGE.blockEnc_dec
#print axioms SLGE.blockEnc_lt
#print axioms SLGE.mixDec_enc
#print axioms SLGE.mixEnc_dec
#print axioms SLGE.mixDec_lt
#print axioms SLGE.decAux_enc
#print axioms SLGE.decL_encL
#print axioms SLGE.encL_decAux
#print axioms SLGE.encL_decL
#print axioms SLGE.decAux_lt
#print axioms SLGE.geo_succ_sub
#print axioms SLGE.encL_range
#print axioms SLGE.decL_length_iff
#print axioms SLGE.tri_zero
#print axioms SLGE.tri_succ
#print axioms SLGE.pair_unpair
#print axioms SLGE.tri_mono
#print axioms SLGE.pair_injective
#print axioms SLGE.unpair_pair
#print axioms SLGE.unpair_le
#print axioms SLGE.decSAux_enc
#print axioms SLGE.decS_encS
#print axioms SLGE.encS_decSAux
#print axioms SLGE.encS_decS
-- SLGE.Count
#print axioms SLGE.Machine.runL_append
#print axioms SLGE.Machine.wtL_append
#print axioms SLGE.Machine.C_succ
#print axioms SLGE.Machine.sizes_length
#print axioms SLGE.Machine.sizes_getD
#print axioms SLGE.Machine.base_le_C
#print axioms SLGE.Machine.base_eq_one
#print axioms SLGE.Machine.base_lt_iff
#print axioms SLGE.Machine.acc_nil
#print axioms SLGE.Machine.acc_iff
#print axioms SLGE.Machine.rank_lt
#print axioms SLGE.Machine.unrank_rank
#print axioms SLGE.Machine.unrank_spec
#print axioms SLGE.Machine.tab_eq
#print axioms SLGE.Machine.blockEnc_levels
#print axioms SLGE.Machine.levels_length
#print axioms SLGE.Machine.levels_getD
#print axioms SLGE.Machine.levels_sum
#print axioms SLGE.Machine.offFrom_snoc
#print axioms SLGE.Machine.offFrom_ge
#print axioms SLGE.Machine.offFrom_ge0
#print axioms SLGE.Machine.graded
#print axioms SLGE.Machine.level_count
#print axioms SLGE.Machine.gradedFin
#print axioms SLGE.Machine.mix2_lt
#print axioms SLGE.Machine.bsizes_getD
#print axioms SLGE.Machine.getD_eq
#print axioms SLGE.Machine.bNum
-- SLGE.Hamza
#print axioms SLGE.Law.fin_start_mover
#print axioms SLGE.Law.fin_free_suk_mov'
#print axioms SLGE.Law.fin_free_suk_mov
#print axioms SLGE.Law.hamza_least
#print axioms SLGE.Law.waslHaraka_lt
#print axioms SLGE.Law.fin_junction4
#print axioms SLGE.Law.fin_junction5
#print axioms SLGE.Law.fin_madd_edit
#print axioms SLGE.Law.fin_closed_edit'
#print axioms SLGE.Law.fin_closed_edit
#print axioms SLGE.Law.wasl_after_mover
#print axioms SLGE.Law.wasl_after_madd
#print axioms SLGE.Law.wasl_after_closed
#print axioms SLGE.Law.seat_range
-- SLGE.Ladder
#print axioms SLGE.cell_range
#print axioms SLGE.radix_pos
#print axioms SLGE.sylSizes_getD
#print axioms SLGE.mix_lt
#print axioms SLGE.skip_ne
#print axioms SLGE.unskip_skip
#print axioms SLGE.skip_lt
#print axioms SLGE.onset
#print axioms SLGE.syl_of_cells
#print axioms SLGE.sylEnc_lt
#print axioms SLGE.word_dec_enc
#print axioms SLGE.word_enc_dec
#print axioms SLGE.sent_dec_enc
#print axioms SLGE.sent_enc_dec
#print axioms SLGE.cellsOf_shape
#print axioms SLGE.take_drop
#print axioms SLGE.wordCells_head
#print axioms SLGE.grp_wordCells
#print axioms SLGE.foldr_syls
#print axioms SLGE.word_of_cells
#print axioms SLGE.ladder
-- SLGE.Law
#print axioms SLGE.Law.mk_run
#print axioms SLGE.Law.mk_wt
#print axioms SLGE.Law.run_append
#print axioms SLGE.Law.wt_append
#print axioms SLGE.Law.δ_big
#print axioms SLGE.Law.run_dead
#print axioms SLGE.Law.dead_not
#print axioms SLGE.Law.fin_mover
#print axioms SLGE.Law.mover_step
#print axioms SLGE.Law.mover_wt
#print axioms SLGE.Law.fin_nuc
#print axioms SLGE.Law.fin_afterK
#print axioms SLGE.Law.fin_afterC
#print axioms SLGE.Law.fin_afterJ
#print axioms SLGE.Law.fin_after
#print axioms SLGE.Law.fin_alif
#print axioms SLGE.Law.alif_mover_dead
#print axioms SLGE.Law.madd_ok
#print axioms SLGE.Law.fin_term
#print axioms SLGE.Law.terminal
#print axioms SLGE.Law.fin_hash
#print axioms SLGE.Law.fin_hashF
#print axioms SLGE.Law.fin_start
#print axioms SLGE.Law.fin_close
#print axioms SLGE.Law.fin_pot
#print axioms SLGE.Law.δ_le
#print axioms SLGE.Law.sym_eq_cellEnc
#print axioms SLGE.Law.chain0
#print axioms SLGE.Law.chain1
#print axioms SLGE.Law.chain2
#print axioms SLGE.Law.chain3
#print axioms SLGE.Law.chain4
#print axioms SLGE.Law.chain5
#print axioms SLGE.Law.maddOf_lt
#print axioms SLGE.Law.syl_run
#print axioms SLGE.Law.blockEnc_take
#print axioms SLGE.Law.syl_bounds
#print axioms SLGE.Law.syl_graded
#print axioms SLGE.Law.unskip_lt
#print axioms SLGE.Law.skip_unskip
#print axioms SLGE.Law.kill
#print axioms SLGE.Law.split
#print axioms SLGE.Law.chainOf_ne
#print axioms SLGE.Law.sentChain_cons
#print axioms SLGE.Law.run_lt68
#print axioms SLGE.Law.structure_aux
#print axioms SLGE.Law.mem_sentChain_116
#print axioms SLGE.Law.cellsOf_bounds
#print axioms SLGE.Law.chainCells_append
#print axioms SLGE.Law.chainCells_syl
#print axioms SLGE.Law.chainCells_word
#print axioms SLGE.Law.wordChain_lt
#print axioms SLGE.Law.splitH_word
#print axioms SLGE.Law.splitH_join
#print axioms SLGE.Law.splitH_sent
#print axioms SLGE.Law.map_inj_valid
#print axioms SLGE.Law.bound_aux
#print axioms SLGE.Law.bound
#print axioms SLGE.Law.live_of_F
#print axioms SLGE.Law.hK
#print axioms SLGE.Law.chain_ba
#print axioms SLGE.Law.hpos
#print axioms SLGE.Law.closure68
#print axioms SLGE.Law.sent_levels
#print axioms SLGE.Law.word_graded
#print axioms SLGE.Law.sent_graded
#print axioms SLGE.Law.word_count
#print axioms SLGE.Law.sent_count
-- SLGE.Root
#print axioms SLGE.Law.wazn_char
#print axioms SLGE.Law.root_wt
#print axioms SLGE.Law.root_hK
#print axioms SLGE.Law.root_close
#print axioms SLGE.Law.root_lev_tab
#print axioms SLGE.Law.tajawur_root
#print axioms SLGE.Law.fin_shape
#print axioms SLGE.Law.fin_shapeF
#print axioms SLGE.Law.Rs_lt
#print axioms SLGE.Law.shape_run
#print axioms SLGE.Law.wazn_from
#print axioms SLGE.Law.mizan_ok
#print axioms SLGE.Law.wazn_any_root
#print axioms SLGE.Law.idx_ok
#print axioms SLGE.Law.W_pos
#print axioms SLGE.Law.root_acc
#print axioms SLGE.Law.muj_size3
#print axioms SLGE.Law.aug_close
#print axioms SLGE.Law.aug_lev_tab
#print axioms SLGE.Law.unitList1_ok
#print axioms SLGE.Law.δa_dead
#print axioms SLGE.Law.aug_dead
#print axioms SLGE.Law.aug_live
#print axioms SLGE.Law.fin_pot2
#print axioms SLGE.Law.len_bound2
#print axioms SLGE.Law.units1_small
#print axioms SLGE.Law.units1_complete
#print axioms SLGE.Law.mazidU1_count
#print axioms SLGE.Law.unit_end_all
#print axioms SLGE.Law.unit_end
#print axioms SLGE.Law.fin_madd_mover
#print axioms SLGE.Law.fin_mc_mover
#print axioms SLGE.Law.from_madd
#print axioms SLGE.Law.mazid_any_root
-- SLGE.Syllable
#print axioms SLGE.Law.δ1_dead
#print axioms SLGE.Law.run1_dead
#print axioms SLGE.Law.δ1_eq
#print axioms SLGE.Law.run1_live
#print axioms SLGE.Law.live_of
#print axioms SLGE.Law.fin_maxw
#print axioms SLGE.Law.fin_close1
#print axioms SLGE.Law.δ1_le
#print axioms SLGE.Law.wt_bound1
#print axioms SLGE.Law.hK1
#print axioms SLGE.Law.hW1
#print axioms SLGE.Law.hFwaqf
#print axioms SLGE.Law.hFwasl
#print axioms SLGE.Law.lev_tab
#print axioms SLGE.Law.sl0
#print axioms SLGE.Law.sl1
#print axioms SLGE.Law.sl2
#print axioms SLGE.Law.sl3
#print axioms SLGE.Law.slw1
#print axioms SLGE.Law.slw2
#print axioms SLGE.Law.slw3
#print axioms SLGE.Law.offFrom_four
#print axioms SLGE.Law.eoff
#print axioms SLGE.Law.syl_structure
-- Dal.AqsamAllafz
#print axioms Dal.NawDalala.kull_length
#print axioms Dal.QismMufrad.kull_nodup
#print axioms Dal.QismMurakkab.kull_nodup
#print axioms Dal.QismMurakkab.kull_length
-- Dal.Khaliya
#print axioms Dal.fakk_n
#print axioms Dal.n_fakk
#print axioms Dal.card_116
-- Madlul.AqsamAlmadlul
#print axioms Madlul.QismMadlul.hadhayan_ghayr_mawdu
-- Madlul.Dalala
#print axioms Dalala.tadammun_needs_mutabaqa
#print axioms Dalala.mutabaqa_not_tadammun
#print axioms Dalala.mutabaqa_not_iltizam
#print axioms Dalala.tadammun_not_iltizam
#print axioms Dalala.kharij_only_iltizam
#print axioms Dalala.basit_no_juz
-- Jisr.AqsamDalMadlul
#print axioms Jisr.QismDalMadlul.kull_nodup
#print axioms Jisr.QismDalMadlul.kull_length
-- Jisr.JisrDal
#print axioms Jisr.JisrDal.harf_kh
#print axioms Jisr.JisrDal.hala_kh
#print axioms Jisr.JisrDal.akhir_append
#print axioms Jisr.JisrDal.akhir_append2
#print axioms Jisr.JisrDal.qablAkhir_append
#print axioms Jisr.JisrDal.kh_lt
#print axioms Jisr.JisrDal.hukm_append
#print axioms Jisr.JisrDal.hukm_append2
#print axioms Jisr.JisrDal.badilHala_harf
#print axioms Jisr.JisrDal.badilHala_lt
#print axioms Jisr.JisrDal.badilInda_harf
#print axioms Jisr.JisrDal.badilInda_tul
#print axioms Jisr.JisrDal.badilInda_lt
#print axioms Jisr.JisrDal.musharik_harf
#print axioms Jisr.JisrDal.musharik_tul
#print axioms Jisr.JisrDal.musharik_lt
-- Aql.Aqliyya
#print axioms Aql.mafhum_bishahid

-- شبكةُ الدلالة: الدورُ والتأسيس (Madlul/TasisDalala.lean)
#print axioms TasisDalala.dawr_mawqufa
#print axioms TasisDalala.mawqufa_la_yuarraf
#print axioms TasisDalala.dawr_la_yuarraf
#print axioms TasisDalala.ghayr_muarraf_mawqufa
#print axioms TasisDalala.muarraf_iff
#print axioms TasisDalala.la_tarif_bila_asl
#print axioms TasisDalala.bila_madkhal
#print axioms TasisDalala.asl_kafin_iff
#print axioms TasisDalala.iqfal_sahih
#print axioms TasisDalala.asl_fi_iqfal
#print axioms TasisDalala.thabit_tamm
#print axioms TasisDalala.iqfal_iff
#print axioms TasisDalala.dawrB_sahih
#print axioms TasisDalala.kharij_thabit
#print axioms TasisDalala.Jadwal.defJ_madakhil
#print axioms TasisDalala.Jadwal.defJ_ghayr_farigh
#print axioms TasisDalala.Jadwal.la_tarif_bila_asl_defJ
#print axioms TasisDalala.Jadwal.dawr_fahm_aql
#print axioms TasisDalala.Jadwal.fahm_aql_la_yuarraf
#print axioms TasisDalala.Jadwal.min_kataba
#print axioms TasisDalala.Jadwal.asasAdna_kafin
#print axioms TasisDalala.Jadwal.kafin_yahwi
#print axioms TasisDalala.Jadwal.asasAdna_asghar
#print axioms TasisDalala.Jadwal.asasAdna_adna
#print axioms TasisDalala.Jadwal.maqal_aql_kafin
#print axioms TasisDalala.Jadwal.maqal_dawr

-- عقدُ الشهادة على الانتقال (Nizam/Shahada.lean): الفاحصُ ونتائجُه المنفصلة، والقاعدةُ بمعناها، وسلامةُ الشهادة
#print axioms Nizam.Shahada.hal_thalath
#print axioms Nizam.Shahada.awwalNaqid_none
#print axioms Nizam.Shahada.naqisa_nil
#print axioms Nizam.Shahada.naqisaMadkhal_nil
#print axioms Nizam.Shahada.hukmMarbut_murakhkhas
#print axioms Nizam.Shahada.hukmMarbut_muallaq
#print axioms Nizam.Shahada.hukmMarbut_mumtani
#print axioms Nizam.Shahada.hukmMarbut_laTantabiq
#print axioms Nizam.Shahada.ghayrMarbut_awwalan
#print axioms Nizam.Shahada.madkhal_mashhud
#print axioms Nizam.Shahada.murakhkhas_iff
#print axioms Nizam.Shahada.ghayrMafhus_la_yurakhkhis
#print axioms Nizam.Shahada.hukm_bi_madkhal_mashhud
#print axioms Nizam.Shahada.madkhal_ghayrMafhus_yuallaq
#print axioms Nizam.Shahada.bila_madkhal_yuallaq
#print axioms Nizam.Shahada.la_shahada_bila_sanad
#print axioms Nizam.Shahada.madkhal_awwalan
#print axioms Nizam.Shahada.mani_mashhud_yamna
#print axioms Nizam.Shahada.muallaq_asma
#print axioms Nizam.Shahada.shahada_salima
#print axioms Nizam.Shahada.shahid_mani

-- تحصيلُ النصّ ومحاذاتُه بشهادةٍ على كلّ مقطع (Dal/Tahsil.lean): القطعُ بلا فقد، والمواضعُ بنقاط الرمز، والتصنيفُ وسلامتُه، والعقدُ مطبَّقًا
#print axioms Dal.Tahsil.harf_sifr
#print axioms Dal.Tahsil.hamilOf_harf
#print axioms Dal.Tahsil.qatta_flatten
#print axioms Dal.Tahsil.qatta_ghayr_farigh
#print axioms Dal.Tahsil.qatta_alamat
#print axioms Dal.Tahsil.qatta_ras
#print axioms Dal.Tahsil.filterMap_hala_le
#print axioms Dal.Tahsil.fakk_khaliyaMin
#print axioms Dal.Tahsil.harfMaddOf_salim
#print axioms Dal.Tahsil.harfHarakaOf_salim
#print axioms Dal.Tahsil.tasnif_salim
#print axioms Dal.Tahsil.binaMin_nass
#print axioms Dal.Tahsil.tahsil_nass
#print axioms Dal.Tahsil.tahsil_flatten
#print axioms Dal.Tahsil.mem_tahsil_qatta
#print axioms Dal.Tahsil.binaMin_hukm
#print axioms Dal.Tahsil.tahsil_hukm
#print axioms Dal.Tahsil.binaMin_tughatti
#print axioms Dal.Tahsil.tahsil_tughatti
#print axioms Dal.Tahsil.binaMin_muhadha
#print axioms Dal.Tahsil.tahsil_muhadha
#print axioms Dal.Tahsil.tughatti_mem
#print axioms Dal.Tahsil.mawdi_sahih
#print axioms Dal.Tahsil.tahsil_salim
#print axioms Dal.Tahsil.ismSinf_ne
#print axioms Dal.Tahsil.shahada_hukm
#print axioms Dal.Tahsil.shahada_tahsil_salima
#print axioms Dal.Tahsil.khalaya_muhadhat
#print axioms Dal.Tahsil.shahid_kataba
#print axioms Dal.Tahsil.shahid_shams
#print axioms Dal.Tahsil.shahid_muallaq
#print axioms Dal.QiraaTahsil.mem_khalayaTahsil
#print axioms Dal.QiraaTahsil.juzOf_khalaya
#print axioms Dal.QiraaTahsil.juzOf_fasid
#print axioms Dal.QiraaTahsil.ajza_cons
#print axioms Dal.QiraaTahsil.ajza_tahsil
#print axioms Dal.QiraaTahsil.ajza_asl
#print axioms Dal.QiraaTahsil.ajza_la_fasid
#print axioms Dal.QiraaTahsil.tamm_khalaya
#print axioms Dal.QiraaTahsil.qiraa_ajza
#print axioms Dal.QiraaTahsil.qiraa_tahsil
#print axioms Dal.QiraaTahsil.qiraa_la_fasid
#print axioms Dal.QiraaTahsil.qiraa_asl
#print axioms Dal.QiraaTahsil.qiraa_shahada
#print axioms Dal.QiraaTahsil.ajza_L
#print axioms Dal.QiraaTahsil.qiraa_murakhkhasa
#print axioms Dal.QiraaTahsil.shahid_fata
#print axioms Dal.QiraaTahsil.shahid_shams
#print axioms Dal.QiraaTahsil.shahid_rafd_tatwil
#print axioms Dal.QiraaTahsil.shahid_tatwil_maqta
#print axioms Dal.QiraaTahsil.shahid_jamaa
-- أبنيةُ اسمَي الفاعل والمفعول في الألفية (س594–607) والقطر (س358، س365) (Jisr/Abniya.lean): حكمُ صوغ الصيغة للمطلوب ودرجتُه
#print axioms Jisr.Abniya.ghayr_thulathi_fail
#print axioms Jisr.Abniya.ghayr_thulathi_mafool
#print axioms Jisr.Abniya.mafool_thulathi
#print axioms Jisr.Abniya.fail_min_fataha
#print axioms Jisr.Abniya.taaddi_la_yughayyir
#print axioms Jisr.Abniya.fail_mafool_la_yashtarikan
#print axioms Jisr.Abniya.ghayr_maqbul_bila
#print axioms Jisr.Abniya.amal_wad
#print axioms Jisr.Abniya.shawahid
-- مقارنةُ ضابط الأبنية قبل الحالات (Jisr/AbniyaDabit.lean؛ hawkama/منهج_الضوابط.md)
#print axioms Jisr.Abniya.Dabit.qarin_hukm
#print axioms Jisr.Abniya.Dabit.qarin_daraja
-- ضابطُ الأبنية المجمَّد، النتيجةُ على الشفرة الحاليّة (Jisr/AbniyaQiyas.lean؛ hawkama/منهج_الضوابط.md)
#print axioms Jisr.Abniya.Qiyas.majal
#print axioms Jisr.Abniya.Qiyas.natija
#print axioms Jisr.Abniya.Qiyas.natija_fia
#print axioms Jisr.Abniya.Qiyas.akhta_sifr
#print axioms Jisr.Abniya.Qiyas.azwaj_1

-- هيكلُ الإنتروبيا على الشيفرة (Jisr/Intrubiya.lean، Jisr/IntrubiyaShahada.lean).
#print axioms Jisr.Intrubiya.sum_replicate
#print axioms Jisr.Intrubiya.sum_map_le
#print axioms Jisr.Intrubiya.sum_map_mul
#print axioms Jisr.Intrubiya.sum_perm
#print axioms Jisr.Intrubiya.exactWords_length
#print axioms Jisr.Intrubiya.mem_exactWords
#print axioms Jisr.Intrubiya.lenCount_eq_spec
#print axioms Jisr.Intrubiya.lenCount_le
#print axioms Jisr.Intrubiya.lenCount_naql
#print axioms Jisr.Intrubiya.lenCount_perm
#print axioms Jisr.Intrubiya.off_succ_sub
#print axioms Jisr.Intrubiya.little_bounds
#print axioms Jisr.Intrubiya.encode_bounds
#print axioms Jisr.Intrubiya.off_mono
#print axioms Jisr.Intrubiya.decode_length
#print axioms Jisr.Intrubiya.qanatan
#print axioms Jisr.Intrubiya.lawVec_length
#print axioms Jisr.Intrubiya.lawVec_eq
#print axioms Jisr.Intrubiya.lawCount_eq
#print axioms Jisr.Intrubiya.lawCount_le
#print axioms Jisr.Intrubiya.naql_tabdil
#print axioms Jisr.Intrubiya.intrubiya_la_tataghayyar_bil_tamthil
#print axioms Jisr.Intrubiya.lenCount_succ
#print axioms Jisr.Intrubiya.hadd_aala
#print axioms Jisr.Intrubiya.hadd_adna
#print axioms Jisr.Intrubiya.qanun_nabt_huwa_slge
#print axioms Jisr.Intrubiya.kulfa_nabt_huwa_slge
#print axioms Jisr.Intrubiya.nihaya_nabt_huwa_slge
#print axioms Jisr.Intrubiya.tartib_dal_huwa_slge
#print axioms Jisr.Intrubiya.alaMashru_step
#print axioms Jisr.Intrubiya.shahadaV_T
#print axioms Jisr.Intrubiya.shahadaV_final
#print axioms Jisr.Intrubiya.shahadaU_T
#print axioms Jisr.Intrubiya.shahadaU_qaida
#print axioms Jisr.Intrubiya.lawCount_aala
#print axioms Jisr.Intrubiya.lawCount_adna
#print axioms Jisr.Intrubiya.adad_waqf
#print axioms Jisr.Intrubiya.adad_wasl
#print axioms Jisr.Intrubiya.wasl_adyaq_3

-- طبقةُ القواعد بين القانون والاستعمال (Jisr/TabaqatQawaid.lean).
#print axioms Jisr.TabaqatQawaid.run_maan
#print axioms Jisr.TabaqatQawaid.qabul_maan
#print axioms Jisr.TabaqatQawaid.length_filter_and_le
#print axioms Jisr.TabaqatQawaid.adad_maan_le
#print axioms Jisr.TabaqatQawaid.adad_maan_eq
#print axioms Jisr.TabaqatQawaid.length_filter_and_eq_iff
#print axioms Jisr.TabaqatQawaid.adad_maan_eq_iff
#print axioms Jisr.TabaqatQawaid.mayyit_yabqa
#print axioms Jisr.TabaqatQawaid.ala_baad
#print axioms Jisr.TabaqatQawaid.ala_iff
#print axioms Jisr.TabaqatQawaid.tasmahBaad_mamnu
#print axioms Jisr.TabaqatQawaid.tasmah_mamnu
#print axioms Jisr.TabaqatQawaid.sira_mahalli
#print axioms Jisr.TabaqatQawaid.tasmah_zawj
#print axioms Jisr.TabaqatQawaid.maan_tasmah
#print axioms Jisr.TabaqatQawaid.tasmah_ithnan
#print axioms Jisr.TabaqatQawaid.tasmahBaad_fargh
#print axioms Jisr.TabaqatQawaid.tasmah_fargh
#print axioms Jisr.TabaqatQawaid.adad_fargh
#print axioms Jisr.TabaqatQawaid.hadd_aala_amm
#print axioms Jisr.TabaqatQawaid.hadd_adna_amm
#print axioms Jisr.TabaqatQawaid.qanun_qaida_le
#print axioms Jisr.TabaqatQawaid.qanun_qaida_eq_iff

-- الإبدالُ في الواو والياء من الألفيّة على آلة القانون (Jisr/IbdalAlfiyya.lean، Jisr/IbdalAlfiyyaDabit.lean).
#print axioms Jisr.IbdalAlfiyya.ghayrMamnu_iff
#print axioms Jisr.IbdalAlfiyya.mamnu_iff
#print axioms Jisr.IbdalAlfiyya.run_sawa
#print axioms Jisr.IbdalAlfiyya.run_lt
#print axioms Jisr.IbdalAlfiyya.qanun_sawa
#print axioms Jisr.IbdalAlfiyya.ghayrMamnu_maan
#print axioms Jisr.IbdalAlfiyya.la_wahid_baad_haraka
#print axioms Jisr.IbdalAlfiyya.alif_mayyit
#print axioms Jisr.IbdalAlfiyya.run_le
#print axioms Jisr.IbdalAlfiyya.alif_baad_ghayr_fatha
#print axioms Jisr.IbdalAlfiyya.sira_snoc
#print axioms Jisr.IbdalAlfiyya.tasmah_mamnu_hukm
#print axioms Jisr.IbdalAlfiyya.tasmahBaad_khatima
#print axioms Jisr.IbdalAlfiyya.sinf_muqin_damma
#print axioms Jisr.IbdalAlfiyya.yaBadDamma_yamna
#print axioms Jisr.IbdalAlfiyya.yaBadDamma_akhir
#print axioms Jisr.IbdalAlfiyya.sinf_wawYa_haraka
#print axioms Jisr.IbdalAlfiyya.wawYa_yamna
#print axioms Jisr.IbdalAlfiyya.sinf_wawYa_fatha_damma
#print axioms Jisr.IbdalAlfiyya.yaWaw_yamna
#print axioms Jisr.IbdalAlfiyya.akhir_mamnu
#print axioms Jisr.IbdalAlfiyya.akhir_sinf_haraka
#print axioms Jisr.IbdalAlfiyya.akhir_sinf_khatima
#print axioms Jisr.IbdalAlfiyya.tasmahBaad_akhir
#print axioms Jisr.IbdalAlfiyya.tasmah_akhir
#print axioms Jisr.IbdalAlfiyya.akhir_yamna
#print axioms Jisr.IbdalAlfiyya.haraka_sinfIshtibah
#print axioms Jisr.IbdalAlfiyya.madd_la_ghayrMamnu
#print axioms Jisr.IbdalAlfiyya.shawahid_hukm
#print axioms Jisr.IbdalAlfiyya.fakkN_mem
#print axioms Jisr.IbdalAlfiyya.yahdhif
#print axioms Jisr.IbdalAlfiyya.muqin_yahdhif
#print axioms Jisr.IbdalAlfiyya.wawYa_yahdhif
#print axioms Jisr.IbdalAlfiyya.akhirWaw_yahdhif
#print axioms Jisr.IbdalAlfiyya.akhirYa_yahdhif
#print axioms Jisr.IbdalAlfiyya.Dabit.qarin_jadwal
#print axioms Jisr.IbdalAlfiyya.Dabit.rafd_ikhfaq
#print axioms Jisr.IbdalAlfiyya.Dabit.muharrik_kalima
#print axioms Jisr.IbdalAlfiyya.Qiyas.majal
#print axioms Jisr.IbdalAlfiyya.Qiyas.natija
#print axioms Jisr.IbdalAlfiyya.Qiyas.natija_fia
#print axioms Jisr.IbdalAlfiyya.Qiyas.akhta_1
#print axioms Jisr.IbdalAlfiyya.Qiyas.azwaj_1
-- الموصولُ وصلتُه في القطر (س137–143) والألفية (س146–157) (Jisr/Mawsul.lean): حكمُ الاستعمال ودرجتُه، والصلةُ بقراءة كلّ مصدر، والربطُ بـ Nizam.Phi.K3.wa
#print axioms Jisr.Mawsul.bawwaba_la_hukm
#print axioms Jisr.Mawsul.wa_k3
#print axioms Jisr.Mawsul.jawab_k3
#print axioms Jisr.Mawsul.khata_yakfi
#print axioms Jisr.Mawsul.bila_sila
#print axioms Jisr.Mawsul.silat_al
#print axioms Jisr.Mawsul.silat_ghayriha
#print axioms Jisr.Mawsul.ikhtilaf_masdarayn
#print axioms Jisr.Mawsul.la_aid_khata
#print axioms Jisr.Mawsul.tashdid_la_yughayyir
#print axioms Jisr.Mawsul.tashdid_ghayr_muthanna
#print axioms Jisr.Mawsul.lugha_la_tughayyir
#print axioms Jisr.Mawsul.qayd_khata
#print axioms Jisr.Mawsul.ghayr_maqbul_bila
#print axioms Jisr.Mawsul.asma_qatr
#print axioms Jisr.Mawsul.maqam_khass
#print axioms Jisr.Mawsul.shawahid
#print axioms Jisr.Mawsul.khilaf_mawsulOK_amm
#print axioms Jisr.Mawsul.khilaf_mawsulOK
#print axioms Jisr.Mawsul.khilaf_silaOK
#print axioms Jisr.Mawsul.la_qalil
-- مقارنةُ ضابط الموصول قبل الحالات (Jisr/MawsulDabit.lean؛ hawkama/منهج_الضوابط.md)
#print axioms Jisr.Mawsul.Dabit.qarin_hukm
#print axioms Jisr.Mawsul.Dabit.qarin_daraja
-- ضابطُ الموصول المجمَّد، النتيجةُ على الشفرة الحاليّة (Jisr/MawsulQiyas.lean؛ hawkama/منهج_الضوابط.md)
#print axioms Jisr.Mawsul.Qiyas.majal
#print axioms Jisr.Mawsul.Qiyas.natija
#print axioms Jisr.Mawsul.Qiyas.natija_fia
#print axioms Jisr.Mawsul.Qiyas.akhta_sifr
#print axioms Jisr.Mawsul.Qiyas.azwaj_1
-- أسماءُ الإشارة في القطر (س132–135) والألفية (س137–144) (Jisr/Ishara.lean): حكمُ الاستعمال بالأصل والمشار إليه والموضع والمسافة و«ها» واللام والكاف
#print axioms Jisr.Ishara.ghayr_muwafiq_khata
#print axioms Jisr.Ishara.lam_bila_kaf_khata
#print axioms Jisr.Ishara.la_hukm_iff
#print axioms Jisr.Ishara.ha_lam_khata
#print axioms Jisr.Ishara.muthanna_lam_khata
#print axioms Jisr.Ishara.madd_lam_khata
#print axioms Jisr.Ishara.kaf_lil_baid
#print axioms Jisr.Ishara.ha_baid_la_yughayyir
#print axioms Jisr.Ishara.mawdi_la_yughayyir
#print axioms Jisr.Ishara.muthanna_bila_jins
#print axioms Jisr.Ishara.asma_qatr
#print axioms Jisr.Ishara.maqam_ishara
#print axioms Jisr.Ishara.mirsat_maqbul
#print axioms Jisr.Ishara.shawahid
#print axioms Jisr.Ishara.shahid_qasr
-- مقارنةُ ضابط أسماء الإشارة قبل الحالات (Jisr/IsharaDabit.lean؛ hawkama/منهج_الضوابط.md)
#print axioms Jisr.Ishara.Dabit.qarin_hukm
-- ضابطُ أسماء الإشارة المجمَّد، النتيجةُ على الشفرة الحاليّة (Jisr/IsharaQiyas.lean؛ hawkama/منهج_الضوابط.md)
#print axioms Jisr.Ishara.Qiyas.majal
#print axioms Jisr.Ishara.Qiyas.natija
#print axioms Jisr.Ishara.Qiyas.natija_fia
#print axioms Jisr.Ishara.Qiyas.akhta_sifr
#print axioms Jisr.Ishara.Qiyas.azwaj_1
-- الخبرُ في القطر (س157–162) والألفية (س177–188) (Jisr/Khabar.lean): حكمُ الخبر ودرجتُه، والوصفُ ومرفوعُه، بقول كلّ مصدرٍ والجمع بينهما
#print axioms Jisr.Khabar.bawwaba_la_hukm
#print axioms Jisr.Khabar.jumla_bila_rabit
#print axioms Jisr.Khabar.rawabit
#print axioms Jisr.Khabar.zarf_maqbul
#print axioms Jisr.Khabar.zaman_dhat
#print axioms Jisr.Khabar.zaman_maana
#print axioms Jisr.Khabar.mushtaq_ibraz
#print axioms Jisr.Khabar.jamid_farigh
#print axioms Jisr.Khabar.wasf_tabaq
#print axioms Jisr.Khabar.bila_itimad
#print axioms Jisr.Khabar.ikhtilaf_la_hukm
#print axioms Jisr.Khabar.hukm_min_masdar
#print axioms Jisr.Khabar.ghayr_maqbul_bila
#print axioms Jisr.Khabar.ibtida_wad
#print axioms Jisr.Khabar.isnad_kubra
#print axioms Jisr.Khabar.hadd_isnad_rabit
#print axioms Jisr.Khabar.isnad_wasf
#print axioms Jisr.Khabar.tarkib_rabit
#print axioms Jisr.Khabar.simat2_jamid
#print axioms Jisr.Khabar.shawahid
-- مقارنةُ ضابط الخبر قبل الحالات (Jisr/KhabarDabit.lean؛ hawkama/منهج_الضوابط.md)
#print axioms Jisr.Khabar.Dabit.qarin_hukm
#print axioms Jisr.Khabar.Dabit.qarin_daraja
-- ضابطُ الخبر المجمَّد، النتيجةُ على الشفرة الحاليّة (Jisr/KhabarQiyas.lean؛ hawkama/منهج_الضوابط.md)
#print axioms Jisr.Khabar.Qiyas.majal
#print axioms Jisr.Khabar.Qiyas.natija
#print axioms Jisr.Khabar.Qiyas.natija_fia
#print axioms Jisr.Khabar.Qiyas.akhta_sifr
#print axioms Jisr.Khabar.Qiyas.azwaj_1
-- الضميرُ البارز في القطر (س124–128) والألفية (س105–119) (Jisr/Damir.lean): الاتّصالُ والانفصال والترتيب ودرجتُها
#print axioms Jisr.Damir.muttasiq_iff
#print axioms Jisr.Damir.ibtida_muttasil
#print axioms Jisr.Damir.ibtida_munfasil_la_hukm
#print axioms Jisr.Damir.illa_muttasil
#print axioms Jisr.Damir.illa_munfasil_la_hukm
#print axioms Jisr.Damir.fasl_maa_imkan
#print axioms Jisr.Damir.fasl_jadwal
#print axioms Jisr.Damir.tartib_munfasil_maqbul
#print axioms Jisr.Damir.tartib_muttasil_iff
#print axioms Jisr.Damir.darura_la_tughayyir_illa_ikhtiyar
#print axioms Jisr.Damir.ghayr_maqbul_bila_daraja
#print axioms Jisr.Damir.la_hukm_iff
#print axioms Jisr.Damir.akhass_shakhs
#print axioms Jisr.Damir.awwal_maarif
#print axioms Jisr.Damir.damair_rutab
#print axioms Jisr.Damir.shawahid
-- مقارنةُ ضابط الضمير قبل الحالات (Jisr/DamirDabit.lean؛ hawkama/منهج_الضوابط.md)
#print axioms Jisr.Damir.Dabit.qarin_hukm
#print axioms Jisr.Damir.Dabit.qarin_daraja
-- ضابطُ الضمير المجمَّد، النتيجةُ على الشفرة الحاليّة (Jisr/DamirQiyas.lean؛ hawkama/منهج_الضوابط.md)
#print axioms Jisr.Damir.Qiyas.majal
#print axioms Jisr.Damir.Qiyas.natija
#print axioms Jisr.Damir.Qiyas.natija_fia
#print axioms Jisr.Damir.Qiyas.akhta_sifr
#print axioms Jisr.Damir.Qiyas.azwaj_1
