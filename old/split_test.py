a = "abc'=bcd"
g = a.split("=")
print(g)
d = {g[0]: g[-1]}
print(d)

cookies = "BAIDUID=0447A87C0E1B107462300D68B0A47020:FG=1; BIDUPSID=0447A87C0E1B107462300D68B0A47020; PSTM=1560825487; __cfduid=d3af605fdf36e40bbf224680b656665e81561534324; BDUSS=E3UVY2MFY4RkF6WnhWeVNwbVVISG5pWWV2eFREYWVQc0p6aWQ0Y3dleGlyVTFkSVFBQUFBJCQAAAAAAAAAAAEAAACtjioBbXVsYW5jaGVuAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGIgJl1iICZdRG; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=7; BDRCVFR[L2qdZltlrss]=aeXf-1x8UdYcs; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1564282067; FANYI_WORD_SWITCH=1; REALTIME_TRANS_SWITCH=1; SOUND_SPD_SWITCH=1; HISTORY_SWITCH=1; SOUND_PREFER_SWITCH=1; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; cflag=13%3A3; H_PS_PSSID=1432_21112_29519_28519_29098_29567_28833_29221_29459_22158; H_WISE_SIDS=130610_126126_132919_134417_114746_133737_120176_133017_132910_133043_131246_132440_130763_132378_131517_118888_118872_118846_118823_118796_133159_132780_134391_133351_129655_134434_132715_127025_128968_132540_133835_133472_131905_133838_133847_132552_133288_134461_134319_132544_134214_129643_131423_134236_133013_110085_134254_134155_127969_134094_127317_130597_128200_134150_134352; rsv_i=47896CzGMsC3YIbmVVTXMIUc8plnzTdbt5vt%2FhI4NebTDZCSeAaYkrkulhzrBqKW%2BAQ5M%2BrIYF09sZb3y%2FF8KB4fosOBvLY; FEED_SIDS=920211_0729_2; SE_LAUNCH=5%3A26072314_0%3A26072314_33%3A26072314; BD_BOXFO=_avui_ajvzGEC; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1564338927; yjs_js_security_passport=f5aeb9c367c153ca59c71d32ec06ea6a2cb011bf_1564338957_js; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D"
cookies_dic = {i.split("=")[0]: i.split("=")[-1] for i in cookies.split(";")}
print(cookies_dic)

for i in cookies.split(";"):
    cookies_dic2 = {i.split("=")[0]: i.split("=")[-1]}
print("*"*20)
print(cookies_dic2)

cookies_dic3 = dict()
for i in cookies.split(";"):
    # print(i.split(":")[0])
    # print(i.split(":")[-1])
    cookies_dic3[i.split(":")[0]] = i.split(":")[-1]
print("X"*20)
print(cookies_dic3)