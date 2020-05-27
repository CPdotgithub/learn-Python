#from urllib import parse{}

# data = {
#     "wd":"刘德华",
#     "age":"18"
# }
# result = parse.urlencode(data)
# print(parse.parse_qs(result))

"""
内涵段子
"""
# -*- coding:utf-8 -*-

# from urllib import request

# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
#     ,"Referer":"http://www.budejie.com/"
#     ,"Cookie":"STM=1586234359; BAIDUID=8E102D9C15CD1368E01A1B5BF603E2C6:FG=1; BIDUPSID=8E102D9C15CD136831FBC36C7A418F1C; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=kVPNUdteWJ6QjluZ1lHNXZWMHF3NXZPeUVqUnFWby15eW9-fnY4UURIdEpFdEJlRVFBQUFBJCQAAAAAAAAAAAEAAADXruAkyq7UwtLduOoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEmFqF5JhaheZ; H_PS_PSSID=; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=7; BCLID=8080705441634025403; BDSFRCVID=4DKOJeC626VvPRouGaOOomSmYg_x9R7TH6aI2u9Cop1O2Rgf5OwlEG0PqM8g0Ku-NKziogKKLgOTHULF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tR4t_DLKtC83fP36q4vHbP40qxby26PJ3g39aJ5nJD_-S4QM04nhQP_gXUnLQ-rk5aOOVx_5QpP-HqI45jrThnOLXN5NK-KtB5vQKl0MLPjYbb0xyn_VXxPhMfnMBMnr52OnaU513fAKftnOM46JehL3346-35543bRTLnLy5KJYMDcnK4-Xj5cBDNbP"
# }
# url = "http://eclick.baidu.com/a.js?tu=u3057681&op=1&jk=3d110339be6a4056&word=http%3A%2F%2Fwww.budejie.com%2F&if=0&aw=135&ah=135&pt=13000&it=0&vt=0&csp=1536,960&bcl=1519,856&pof=1519,7112&top=6200&left=767&uid=u3057681_0&iw=false&total=2&ver=0426&rdm=1588346521313"

# req = request.Request(url=url,headers=headers,method="Get")
# resp = request.urlopen(req)
# print(resq.read())
# headers = {
#     "User-gent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
#     }
# url="http://www.budejie.com"
# req = request.Request(url=url,headers=headers)    
# resp = request.urlopen(req)
# result = resp.read().decode("utd-8")
# print(resp.read().decode("utf-8"),resp.getcode())
