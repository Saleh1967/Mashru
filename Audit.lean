import Dal.Khaliya
import Dal.AqsamAllafz
import Madlul.Dalala
import Madlul.AqsamAlmadlul
import Madlul.Tayin
import Madlul.Wiratha
import Madlul.Jamad
import Jisr.AqsamDalMadlul
import Jisr.Tawafuq
import Dal.AqsamAlism
import Jisr.TasnifAlism
import Aql.Aqliyya
import Aql.Qaida
import Aql.Badiha
import Aql.Mawsua
import Aql.Idaa
import Aql.QawaninDalala
import Aql.Maratib
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
#print axioms Maratib.khatwa_majmu
#print axioms Maratib.foldl_majmu
#print axioms Maratib.ihsa_majmu
#print axioms Maratib.khatwa_maana_fst
#print axioms Maratib.mukhraj_wahid_min_haythu
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
