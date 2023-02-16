"use strict";

const CACHE_NAME = 'static_machaneh_cache_v202302151901';

const CACHE_FILES = [
  "/",
  "/index.html",
  "DAG.jpg",
  "favicon.ico",
  "/camps/building_a_multiple_mega_church/BUILDING_A_MULTIPLE_MEGACHURCH.jpg",
  "/camps/building_a_multiple_mega_church/rss/podcast.rss",
  "/camps/building_a_multiple_mega_church/index.html",
  "/camps/loyalty_and_the_mega_church/LOYALTY_AND_THE_MEGACHURCH.jpg",
  "/camps/loyalty_and_the_mega_church/rss/podcast.rss",
  "/camps/loyalty_and_the_mega_church/index.html",
  "/camps/strive_lawfully_for_a_mega_church/STRIVE_LAWFULLY_FOR_A_MEGACHURCH.jpg",
  "/camps/strive_lawfully_for_a_mega_church/rss/podcast.rss",
  "/camps/strive_lawfully_for_a_mega_church/index.html",
  "/camps/double_mega_missionary_church/Double_Mega_Missionary__Church.jpg",
  "/camps/double_mega_missionary_church/rss/podcast.rss",
  "/camps/double_mega_missionary_church/index.html",
  "/camps/going_deeper_and_doing_more/GOING_DEEPER_AND_DOING_MORE.jpg",
  "/camps/going_deeper_and_doing_more/rss/podcast.rss",
  "/camps/going_deeper_and_doing_more/index.html",
  "/camps/love_and_the_mega_church/1544746436_love_and_the_mega_church.jpg",
  "/camps/love_and_the_mega_church/rss/podcast.rss",
  "/camps/love_and_the_mega_church/index.html",
  "/camps/the_dream_church/THE_DREAM_CHURCH.jpg",
  "/camps/the_dream_church/rss/podcast.rss",
  "/camps/the_dream_church/index.html",
  "/camps/advancing_in_pergamos/1499104733_ADVANCING_IN_PERGAMOS.jpg",
  "/camps/advancing_in_pergamos/rss/podcast.rss",
  "/camps/advancing_in_pergamos/index.html",
  "/camps/work_of_the_ministry/THE_WORK_OF_THE_MINISTRY.jpg",
  "/camps/work_of_the_ministry/rss/podcast.rss",
  "/camps/work_of_the_ministry/index.html",
  "/camps/pastors_of_thousands/PASTORS_OF_THOUSANDS.jpg",
  "/camps/pastors_of_thousands/rss/podcast.rss",
  "/camps/pastors_of_thousands/index.html",
  "/camps/the_message_of_sacrifice/1541043697_THE_MESSAGE_OF_SACRIFICE.jpg",
  "/camps/the_message_of_sacrifice/rss/podcast.rss",
  "/camps/the_message_of_sacrifice/index.html",
  "/camps/victory_in_laodicea/1503520278_VICTORY_IN_LAODICEA.jpg",
  "/camps/victory_in_laodicea/rss/podcast.rss",
  "/camps/victory_in_laodicea/index.html",
  "/camps/what_is_your_life/1544747222_what_is_your_life.jpg",
  "/camps/what_is_your_life/rss/podcast.rss",
  "/camps/what_is_your_life/index.html",
  "/camps/all_out/1544763117_all_out.jpg",
  "/camps/all_out/rss/podcast.rss",
  "/camps/all_out/index.html",
  "/camps/allos_-_another_of_the_kind/allos.jpg",
  "/camps/allos_-_another_of_the_kind/rss/podcast.rss",
  "/camps/allos_-_another_of_the_kind/index.html",
  "/camps/grace_n_peace/1541043525_grace_and_peace.jpg",
  "/camps/grace_n_peace/rss/podcast.rss",
  "/camps/grace_n_peace/index.html",
  "/camps/life_in_the_church/1544738187_life_in_the_church.jpg",
  "/camps/life_in_the_church/rss/podcast.rss",
  "/camps/life_in_the_church/index.html",
  "/camps/the_mega_church/1544746436_love_and_the_mega_church.jpg",
  "/camps/the_mega_church/rss/podcast.rss",
  "/camps/the_mega_church/index.html",
  "/camps/the_mysteries_of_god/the_mysteries_of_God.jpg",
  "/camps/the_mysteries_of_god/rss/podcast.rss",
  "/camps/the_mysteries_of_god/index.html",
  "/camps/zogreo/ZOGREO.jpg",
  "/camps/zogreo/rss/podcast.rss",
  "/camps/zogreo/index.html",
  "/camps/agree_on_the_way/1544747764_agree_on_the_way.jpg",
  "/camps/agree_on_the_way/rss/podcast.rss",
  "/camps/agree_on_the_way/index.html",
  "/camps/how_to_survive_in_ephesus/1544747746_how_to_survive_in_ephesus.jpg",
  "/camps/how_to_survive_in_ephesus/rss/podcast.rss",
  "/camps/how_to_survive_in_ephesus/index.html",
  "/camps/the_presence/Messages_On_The_Presence_Of_God.jpg",
  "/camps/the_presence/rss/podcast.rss",
  "/camps/the_presence/index.html",
  "/camps/kruptos_man/1504183235_Kruptos_Man.jpg",
  "/camps/kruptos_man/rss/podcast.rss",
  "/camps/kruptos_man/index.html",
  "/camps/gates_and_roads/1504183144_GATES_AND_ROADS.jpg",
  "/camps/gates_and_roads/rss/podcast.rss",
  "/camps/gates_and_roads/index.html",
  "/camps/bema/1544763067_bema.jpg",
  "/camps/bema/rss/podcast.rss",
  "/camps/bema/index.html",
  "/camps/victory_in_pergamos/VICTORY_IN_PERGAMOS.jpg",
  "/camps/victory_in_pergamos/rss/podcast.rss",
  "/camps/victory_in_pergamos/index.html",
  "/camps/barrenness_and_fruitfulness/BARRENNESS_AND_FRUITFULNESS.jpg",
  "/camps/barrenness_and_fruitfulness/rss/podcast.rss",
  "/camps/barrenness_and_fruitfulness/index.html",
  "/camps/preparation_of_the_gospel/PREPARATION_OF_THE_GOSPEL.jpg",
  "/camps/preparation_of_the_gospel/rss/podcast.rss",
  "/camps/preparation_of_the_gospel/index.html",
  "/camps/missions_and_missionaries/missions_and_missionaries.jpg",
  "/camps/missions_and_missionaries/rss/podcast.rss",
  "/camps/missions_and_missionaries/index.html",
  "/camps/others/1544763149_others.jpg",
  "/camps/others/rss/podcast.rss",
  "/camps/others/index.html",
  "/camps/church_planting/CHURCH_planting.jpg",
  "/camps/church_planting/rss/podcast.rss",
  "/camps/church_planting/index.html",
  "/camps/perfection/1544747842_perfection.jpg",
  "/camps/perfection/rss/podcast.rss",
  "/camps/perfection/index.html",
  "/camps/snake_junction/SNAKE_JUNCTION.jpg",
  "/camps/snake_junction/rss/podcast.rss",
  "/camps/snake_junction/index.html",
  "/camps/australia_1000/1544741114_australia_1000.jpg",
  "/camps/australia_1000/rss/podcast.rss",
  "/camps/australia_1000/index.html",
  "/camps/take_up_your_cross/1544741087_take_up_your_cross.jpg",
  "/camps/take_up_your_cross/rss/podcast.rss",
  "/camps/take_up_your_cross/index.html",
  "/camps/birthday_-_kee_waa/BIRTHDAY_(KEEWAA).jpg",
  "/camps/birthday_-_kee_waa/rss/podcast.rss",
  "/camps/birthday_-_kee_waa/index.html",
  "/camps/busselization/BUSSELISATION.jpg",
  "/camps/busselization/rss/podcast.rss",
  "/camps/busselization/index.html",
  "/camps/obedience_unto_death/OBEDIENCE_UNTO_DEATH.jpg",
  "/camps/obedience_unto_death/rss/podcast.rss",
  "/camps/obedience_unto_death/index.html",
  "/camps/become_who_you_can_become/rss/podcast.rss",
  "/camps/become_who_you_can_become/index.html",
  "/camps/spiritual_battles/1541042185_SPIRITUAL_BATTLES.jpg",
  "/camps/spiritual_battles/rss/podcast.rss",
  "/camps/spiritual_battles/index.html",
  "/camps/apocalypse/1541042155_APOCALYPSE.jpg",
  "/camps/apocalypse/rss/podcast.rss",
  "/camps/apocalypse/index.html",
  "/camps/the_lords_anointed/THE_LORDS_ANOINTED.jpg",
  "/camps/the_lords_anointed/rss/podcast.rss",
  "/camps/the_lords_anointed/index.html",
  "/camps/do_the_work_of_an_evangelist/DO_THE_WORK_OF_AN_EVANGELIST.jpg",
  "/camps/do_the_work_of_an_evangelist/rss/podcast.rss",
  "/camps/do_the_work_of_an_evangelist/index.html",
  "/camps/i_and_my_children/I_AND_THE_CHILDREN.jpg",
  "/camps/i_and_my_children/rss/podcast.rss",
  "/camps/i_and_my_children/index.html",
  "/camps/missions/INEXORABILITY_IN_THE_MISSIONS.jpg",
  "/camps/missions/rss/podcast.rss",
  "/camps/missions/index.html",
  "/camps/moses_and_associates/MOSES_AND_ASSOCIATES.jpg",
  "/camps/moses_and_associates/rss/podcast.rss",
  "/camps/moses_and_associates/index.html",
  "/camps/tell_them/1544764063_tell_them.jpg",
  "/camps/tell_them/rss/podcast.rss",
  "/camps/tell_them/index.html",
  "/camps/the_sufferings_of_christ/THE_SUFFERINGS_OF_CHRIST.jpg",
  "/camps/the_sufferings_of_christ/rss/podcast.rss",
  "/camps/the_sufferings_of_christ/index.html",
  "/camps/the_powers_of_a_cross/1504183776_POWERS_OF_A_CROSS.jpg",
  "/camps/the_powers_of_a_cross/rss/podcast.rss",
  "/camps/the_powers_of_a_cross/index.html",
  "/camps/warfare_keys/WARFARE__KEYS.jpg",
  "/camps/warfare_keys/rss/podcast.rss",
  "/camps/warfare_keys/index.html",
  "/camps/finish_what_you_started/FINISH_WHAT_YOU_STARTED.jpg",
  "/camps/finish_what_you_started/rss/podcast.rss",
  "/camps/finish_what_you_started/index.html",
  "/camps/mighty_foundations/MIGHTY_FOUNDATIONS_.jpg",
  "/camps/mighty_foundations/rss/podcast.rss",
  "/camps/mighty_foundations/index.html",
  "/camps/my_first_love/MY_FIRST_LOVE.jpg",
  "/camps/my_first_love/rss/podcast.rss",
  "/camps/my_first_love/index.html",
  "/camps/coming_out_of_obscurity/Coming_Out_Of_Obscurity_.jpg",
  "/camps/coming_out_of_obscurity/rss/podcast.rss",
  "/camps/coming_out_of_obscurity/index.html",
  "/camps/lay_power/1544764482_lay_power.jpg",
  "/camps/lay_power/rss/podcast.rss",
  "/camps/lay_power/index.html",
  "/camps/the_blessings_of_abraham/THE_BLESSING_OF_ABRAHAM.jpg",
  "/camps/the_blessings_of_abraham/rss/podcast.rss",
  "/camps/the_blessings_of_abraham/index.html",
  "/camps/predestination/1541041256_PREDESTINATION.jpg",
  "/camps/predestination/rss/podcast.rss",
  "/camps/predestination/index.html",
  "/camps/why_you_are_not_a_missionary/WHY_ARE_YOU_NOT_A_MISSIONARY.jpg",
  "/camps/why_you_are_not_a_missionary/rss/podcast.rss",
  "/camps/why_you_are_not_a_missionary/index.html",
  "/camps/tasters_or_partakers/Tasters__Partakers.jpg",
  "/camps/tasters_or_partakers/rss/podcast.rss",
  "/camps/tasters_or_partakers/index.html",
  "/camps/the_privilege/The_Priviledge.jpg",
  "/camps/the_privilege/rss/podcast.rss",
  "/camps/the_privilege/index.html",
  "/camps/the_bag_of_seeds/The_bag_of_Seeds.jpg",
  "/camps/the_bag_of_seeds/rss/podcast.rss",
  "/camps/the_bag_of_seeds/index.html",
  "/camps/if_you_love_the_lord/1544764629_if_you_love_the_lord.jpg",
  "/camps/if_you_love_the_lord/rss/podcast.rss",
  "/camps/if_you_love_the_lord/index.html",
  "/camps/that_my_house_may_be_filled/THAT_MY_HOUSE_MAY_BE_FILLED.jpg",
  "/camps/that_my_house_may_be_filled/rss/podcast.rss",
  "/camps/that_my_house_may_be_filled/index.html",
  "/camps/warnings_of_purpose/1544764740_Warnings_of_Purpose.jpg",
  "/camps/warnings_of_purpose/rss/podcast.rss",
  "/camps/warnings_of_purpose/index.html",
  "/camps/the_volante/THE_VOLANTE.jpg",
  "/camps/the_volante/rss/podcast.rss",
  "/camps/the_volante/index.html",
  "/camps/awake_o_sleeper/AWAKE_O_SLEEPER.jpg",
  "/camps/awake_o_sleeper/rss/podcast.rss",
  "/camps/awake_o_sleeper/index.html",
  "/camps/lord_i_know_you_need_somebody/72_-_LORD_I_KNOW_YOU_NEED_SOMEBODY.jpg",
  "/camps/lord_i_know_you_need_somebody/rss/podcast.rss",
  "/camps/lord_i_know_you_need_somebody/index.html",
  "/camps/inexorability_in_the_mission/INEXORABILITY_IN_THE_MISSIONS.jpg",
  "/camps/inexorability_in_the_mission/rss/podcast.rss",
  "/camps/inexorability_in_the_mission/index.html",
  "/camps/gods_banquet/GODS_BANQUET.jpg",
  "/camps/gods_banquet/rss/podcast.rss",
  "/camps/gods_banquet/index.html",
  "/camps/seigneur_ait_pitie/SEIGNEUR_AIT_PITIE.jpg",
  "/camps/seigneur_ait_pitie/rss/podcast.rss",
  "/camps/seigneur_ait_pitie/index.html",
  "/camps/the_word_of_my_patience/THE_WORD_OF_MY_PATIENCE.jpg",
  "/camps/the_word_of_my_patience/rss/podcast.rss",
  "/camps/the_word_of_my_patience/index.html",
  "/camps/be_thou_faithful_unto_death/BE_THOU_FAITHFUL_UNTO_DEATH.jpg",
  "/camps/be_thou_faithful_unto_death/rss/podcast.rss",
  "/camps/be_thou_faithful_unto_death/index.html",
  "/camps/the_sweet_influences_of_the_holy_spirit/sweet_influences.jpg",
  "/camps/the_sweet_influences_of_the_holy_spirit/rss/podcast.rss",
  "/camps/the_sweet_influences_of_the_holy_spirit/index.html",
  "/camps/secrets_of_the_anointing_and_his_anointing/1544765559_the_secret.jpg",
  "/camps/secrets_of_the_anointing_and_his_anointing/rss/podcast.rss",
  "/camps/secrets_of_the_anointing_and_his_anointing/index.html",
  "/camps/atmosphere/atmosphere.jpg",
  "/camps/atmosphere/rss/podcast.rss",
  "/camps/atmosphere/index.html",
  "/camps/one_hundred_million_souls/100-Million-Souls.jpg",
  "/camps/one_hundred_million_souls/rss/podcast.rss",
  "/camps/one_hundred_million_souls/index.html",
  "/camps/the_beautiful_job/1498918869_The-Beautiful-job.jpg",
  "/camps/the_beautiful_job/rss/podcast.rss",
  "/camps/the_beautiful_job/index.html",
  "/camps/principles_of_war/1498919053_principles_of_war.jpg",
  "/camps/principles_of_war/rss/podcast.rss",
  "/camps/principles_of_war/index.html",
  "/camps/fight_the_good_fight/fight_the_good_fight.jpg",
  "/camps/fight_the_good_fight/rss/podcast.rss",
  "/camps/fight_the_good_fight/index.html",
  "/camps/wise_as_serpents/1498919796_Wise-as-serpents.jpg",
  "/camps/wise_as_serpents/rss/podcast.rss",
  "/camps/wise_as_serpents/index.html",
  "/camps/give_thyself_wholly/give_thyself_.jpg",
  "/camps/give_thyself_wholly/rss/podcast.rss",
  "/camps/give_thyself_wholly/index.html",
  "/camps/mission_america_there_must_be_missions/mission_america.jpg",
  "/camps/mission_america_there_must_be_missions/rss/podcast.rss",
  "/camps/mission_america_there_must_be_missions/index.html",
  "/camps/mission_europe/MISSION_EUROPE.jpg",
  "/camps/mission_europe/rss/podcast.rss",
  "/camps/mission_europe/index.html",
  "/camps/mission_sa_prepare_the_way_of_the_lord/mission_south_africa.jpg",
  "/camps/mission_sa_prepare_the_way_of_the_lord/rss/podcast.rss",
  "/camps/mission_sa_prepare_the_way_of_the_lord/index.html",
  "/camps/mission_africa_the_ministry_of_the_sower/1498920239_Mission-Africa-Dag-Heward-Mills.jpg",
  "/camps/mission_africa_the_ministry_of_the_sower/rss/podcast.rss",
  "/camps/mission_africa_the_ministry_of_the_sower/index.html",
  "/camps/who_is_he_that_overcomes_the_world/1498920361_Who-Is-He-That-Overcomes-The-World.jpg",
  "/camps/who_is_he_that_overcomes_the_world/rss/podcast.rss",
  "/camps/who_is_he_that_overcomes_the_world/index.html",
  "/camps/god_requireth_that_which_is_past/God-Requireth-That-Which-Is-Past.jpg",
  "/camps/god_requireth_that_which_is_past/rss/podcast.rss",
  "/camps/god_requireth_that_which_is_past/index.html",
  "/camps/how_can_i_say_thanks/1498920635_how_can_i_say_thanks.jpg",
  "/camps/how_can_i_say_thanks/rss/podcast.rss",
  "/camps/how_can_i_say_thanks/index.html",
  "/camps/fulfil_your_ministry/1498920710_fulfil_your_ministry.jpg",
  "/camps/fulfil_your_ministry/rss/podcast.rss",
  "/camps/fulfil_your_ministry/index.html",
  "/camps/obligation_of_christians/Obligation__of_Christians.jpg",
  "/camps/obligation_of_christians/rss/podcast.rss",
  "/camps/obligation_of_christians/index.html",
  "/camps/attempt_great_things/1544740828_attempt_great_things.jpg",
  "/camps/attempt_great_things/rss/podcast.rss",
  "/camps/attempt_great_things/index.html",
  "/camps/expect_great_things/1544740782_expect_great_things.jpg",
  "/camps/expect_great_things/rss/podcast.rss",
  "/camps/expect_great_things/index.html",
  "/camps/ready_at_20/READY_AT_20.jpg",
  "/camps/ready_at_20/rss/podcast.rss",
  "/camps/ready_at_20/index.html",
  "/camps/let_my_people_go/LET_MY_PEOPLE_GO.jpg",
  "/camps/let_my_people_go/rss/podcast.rss",
  "/camps/let_my_people_go/index.html",
  "/camps/victory_in_laodecia/1503520278_VICTORY_IN_LAODICEA.jpg",
  "/camps/victory_in_laodecia/rss/podcast.rss",
  "/camps/victory_in_laodecia/index.html",
  "/camps/stir_it_up/STIR_IT_UP.jpg",
  "/camps/stir_it_up/rss/podcast.rss",
  "/camps/stir_it_up/index.html",
  "/camps/where_is_the_flock_that_was_given_thee/where_is_the_flock.jpg",
  "/camps/where_is_the_flock_that_was_given_thee/rss/podcast.rss",
  "/camps/where_is_the_flock_that_was_given_thee/index.html",
  "/camps/a_super_mega_church/A_SUPER_MEGA_CHURCH.jpg",
  "/camps/a_super_mega_church/rss/podcast.rss",
  "/camps/a_super_mega_church/index.html",
  "/camps/i_will_multiply_them_and_they_shall_not_be_few/I_WILL_MULTIPLY.jpg",
  "/camps/i_will_multiply_them_and_they_shall_not_be_few/rss/podcast.rss",
  "/camps/i_will_multiply_them_and_they_shall_not_be_few/index.html",
  "/camps/army_of_hard_followers/ARMY_OF_HARD_FOLLOWERS.jpg",
  "/camps/army_of_hard_followers/rss/podcast.rss",
  "/camps/army_of_hard_followers/index.html",
  "/camps/a_small_one_shall_become_a_strong_nation/1544740349_a_small_one_shall_become_a_strong_nation.jpg",
  "/camps/a_small_one_shall_become_a_strong_nation/rss/podcast.rss",
  "/camps/a_small_one_shall_become_a_strong_nation/index.html",
  "/camps/reasons_for_the_breakup/rss/podcast.rss",
  "/camps/reasons_for_the_breakup/index.html",
  "/camps/arise_and_shine/rss/podcast.rss",
  "/camps/arise_and_shine/index.html",
  "/camps/obligations_of_christian_workers/OBLIGATIONS_OF_CHRISTIAN_WORKERS.jpg",
  "/camps/obligations_of_christian_workers/rss/podcast.rss",
  "/camps/obligations_of_christian_workers/index.html",
  "/camps/the_church_must_send_or_it_will_end/THE_CHURCH__MUST_SEND_OR__IT_WILL_END.jpg",
  "/camps/the_church_must_send_or_it_will_end/rss/podcast.rss",
  "/camps/the_church_must_send_or_it_will_end/index.html",
  "/camps/no_city_shall_be_too_strong_for_you/NO_CITY_SHALL__BE_TOO_STRONG__FOR_YOU.jpg",
  "/camps/no_city_shall_be_too_strong_for_you/rss/podcast.rss",
  "/camps/no_city_shall_be_too_strong_for_you/index.html",
  "/camps/neutralize_the_curse/neutralise.jpg",
  "/camps/neutralize_the_curse/rss/podcast.rss",
  "/camps/neutralize_the_curse/index.html",
  "/camps/zealously_affected/ZEALOUSLY_AFFECTED.jpg",
  "/camps/zealously_affected/rss/podcast.rss",
  "/camps/zealously_affected/index.html",
  "/camps/everything_by_prayer_nothing_without_prayer/Everything_by_Prayer_Nothing_without_Prayer.jpg",
  "/camps/everything_by_prayer_nothing_without_prayer/rss/podcast.rss",
  "/camps/everything_by_prayer_nothing_without_prayer/index.html",
  "/camps/labour_to_be_blessed/labour_to_be_blessed.jpg",
  "/camps/labour_to_be_blessed/rss/podcast.rss",
  "/camps/labour_to_be_blessed/index.html",
  "/camps/make_yourself_a_saviour_of_men/make-yourself-a-saviour-of-men-565x318.jpg",
  "/camps/make_yourself_a_saviour_of_men/rss/podcast.rss",
  "/camps/make_yourself_a_saviour_of_men/index.html",
  "/camps/the_reward_for_hard_work_is_more_work/the_reward_for_hard.jpg",
  "/camps/the_reward_for_hard_work_is_more_work/rss/podcast.rss",
  "/camps/the_reward_for_hard_work_is_more_work/index.html",
  "/camps/no_weeping_no_gnashing/No-Weeping-No-Gnashing-565x318.jpg",
  "/camps/no_weeping_no_gnashing/rss/podcast.rss",
  "/camps/no_weeping_no_gnashing/index.html",
  "/camps/candle_in_the_dark/candle-in-the-dark-565x318.jpg",
  "/camps/candle_in_the_dark/rss/podcast.rss",
  "/camps/candle_in_the_dark/index.html",
  "/camps/twenty-five_to_fifty/twenty-five_to_fifty.jpg",
  "/camps/twenty-five_to_fifty/rss/podcast.rss",
  "/camps/twenty-five_to_fifty/index.html",
  "/camps/the_isles_shall_wait_for_me/the_isles_shall_wait_for_me.jpg",
  "/camps/the_isles_shall_wait_for_me/rss/podcast.rss",
  "/camps/the_isles_shall_wait_for_me/index.html",
  "/camps/attempt_great_things_for_god/ATTEMPT_GREAT_THINGS_FOR_GOD.jpg",
  "/camps/attempt_great_things_for_god/rss/podcast.rss",
  "/camps/attempt_great_things_for_god/index.html",
  "/camps/and_ye_shall_compass_the_city/and_ye_shall.jpg",
  "/camps/and_ye_shall_compass_the_city/rss/podcast.rss",
  "/camps/and_ye_shall_compass_the_city/index.html",
  "/camps/no_city_shall_be_too_strong_for_you_2018/no_city_shall_be_too_strong_for_you.jpg",
  "/camps/no_city_shall_be_too_strong_for_you_2018/rss/podcast.rss",
  "/camps/no_city_shall_be_too_strong_for_you_2018/index.html",
  "/camps/season_of_withdrawal/1550854868_season_of_withdrawal.jpg",
  "/camps/season_of_withdrawal/rss/podcast.rss",
  "/camps/season_of_withdrawal/index.html",
  "/camps/i_only_need_one_talent/one_talent.jpg",
  "/camps/i_only_need_one_talent/rss/podcast.rss",
  "/camps/i_only_need_one_talent/index.html",
  "/camps/make_yourself_a_saviour_of_men_-_harmattan_bible_seminar/1550945225_make_yourself.jpg",
  "/camps/make_yourself_a_saviour_of_men_-_harmattan_bible_seminar/rss/podcast.rss",
  "/camps/make_yourself_a_saviour_of_men_-_harmattan_bible_seminar/index.html",
  "/camps/i_come_seeking_fruit/i_come_looking_fruits.jpg",
  "/camps/i_come_seeking_fruit/rss/podcast.rss",
  "/camps/i_come_seeking_fruit/index.html",
  "/camps/am_i_good_for_nothing/128._Am_i_good.jpg",
  "/camps/am_i_good_for_nothing/rss/podcast.rss",
  "/camps/am_i_good_for_nothing/index.html",
  "/camps/jesus_saviour_of_the_world/JESUS_SAVIOUR_OF_THE_LORD.jpg",
  "/camps/jesus_saviour_of_the_world/rss/podcast.rss",
  "/camps/jesus_saviour_of_the_world/index.html",
  "/camps/choose_me_use_me/130._Choose_me_use_me.jpg",
  "/camps/choose_me_use_me/rss/podcast.rss",
  "/camps/choose_me_use_me/index.html",
  "/camps/eunuchs_in_the_palace/eunuchs_in_the_palace-min.jpg",
  "/camps/eunuchs_in_the_palace/rss/podcast.rss",
  "/camps/eunuchs_in_the_palace/index.html",
  "/camps/use_it_or_lose_it/rss/podcast.rss",
  "/camps/use_it_or_lose_it/index.html",
  "/enjoyhint/src/jquery.enjoyhint.js",
  "/enjoyhint/src/enjoyhint.js",
  "/enjoyhint/src/jquery.enjoyhint.css",
  "/enjoyhint/src/Casino_Hand/casino_hand-webfont.svg",
  "/enjoyhint/src/Casino_Hand/casino_hand-webfont.eot",
  "/enjoyhint/src/Casino_Hand/casino_hand-webfont.woff",
  "/enjoyhint/src/Casino_Hand/casino_hand-webfont.ttf",
  "/enjoyhint/enjoyhint.min.js",
  "/enjoyhint/enjoyhint.css",
  "/enjoyhint/package.json",
  "/enjoyhint/README.md",
  "/enjoyhint/enjoyhint.js",
  "/enjoyhint/bower.json",
  "/enjoyhint/index..html",
  "/enjoyhint/Gruntfile.js",
  "/enjoyhint/help.js",
  "/enjoyhint/LICENSE.md",
  "/images/android-icon-96x96.png",
  "/images/favicon-32x32.png",
  "/images/apple-icon-60x60.png",
  "/images/favicon-96x96.png",
  "/images/apple-icon-precomposed.png",
  "/images/ms-icon-310x310.png",
  "/images/favicon-16x16.png",
  "/images/apple-icon-152x152.png",
  "/images/apple-icon-120x120.png",
  "/images/apple-icon-57x57.png",
  "/images/apple-icon-144x144.png",
  "/images/apple-icon-76x76.png",
  "/images/ms-icon-144x144.png",
  "/images/android-icon-144x144.png",
  "/images/android-icon-48x48.png",
  "/images/android-icon-192x192.png",
  "/images/apple-icon-114x114.png",
  "/images/ms-icon-70x70.png",
  "/images/ms-icon-150x150.png",
  "/images/apple-icon-180x180.png",
  "/images/apple-icon-72x72.png",
  "/images/android-icon-36x36.png",
  "/images/android-icon-72x72.png",
  "/images/apple-icon.png",
  "/style/inline.css",
  "/style/help.css"
];


self.addEventListener("install", evt => {
  console.log("[ServiceWorker] install");
  evt.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      console.log("[ServiceWorker] caching");
      return cache.addAll(CACHE_FILES);
    })
  );
  self.skipWaiting();
});


self.addEventListener("activate", evt => {
  console.log("[ServiceWorker] activate");
  evt.waitUntil(
    caches.keys().then(keyList => {
      return Promise.all(
        keyList.map(key => {
	  if (key != CACHE_NAME) {
	    console.log("[ServiceWorker] cleaning up old caches", key);
            caches.delete(key);
	  }
	})
      );
    }) 
  );
  self.clients.claim();
});

self.addEventListener('fetch', event => {
    event.respondWith(
	    caches.match(event.request).then(response => {
		return response || fetch(event.request);
	    })
	);
});
