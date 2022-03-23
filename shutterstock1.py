import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests



os.environ['PATH'] += r"/home/umair/Documents/python/driver"

driver = webdriver.Chrome()
header={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'max-age=0',
'cookie': 'sstk_anonymous_id=b5dee432-ac33-4574-9ed0-f278e715549d; sstk_session_id=82a0a795-7614-45c2-92ba-e6a9b875aee4; visitor_id=67953217152; sstk.sid=s%3A-LDPukSVCo2V6XxZSNNOzZPk5czvTnvb.wd6u6viSp%2FTER3PnOYta91kH7zAe05GcLG0ruBDo1pw; locale=en-US; _gcl_au=1.1.1701746165.1643549696; __ssid=1bc8df08f66e80608f3379af3f58a9f; _cs_c=1; _rdt_uuid=1643549707299.dcf4bc34-6a0f-45d8-b7df-7bc4cb656651; _ym_uid=16435497078280354; _ym_d=1643549707; C3UID-924=2857409171643549707; C3UID=2857409171643549707; _fbp=fb.1.1643549707744.424528412; _CEFT=Q%3D%3D%3D; _ga=GA1.2.497598542.1643549708; sstk_anonymous_id=b5dee432-ac33-4574-9ed0-f278e715549d; _gid=GA1.2.367936603.1643646151; go_lihp=image; next.sid=s%3ArxLX68aaByIBf4XuFjmV6MDmIdRp-H5Q.z%2F5STjoG7%2Bafb6znvKJIQb0HUklwyAwK%2FEueqL9ECLI; did=_dBUgl9gWg9xCpt_CI8gwhPRAu0dm9GSZTAr; ajs_anonymous_id=b5dee432-ac33-4574-9ed0-f278e715549d; _gaexp=GAX1.2.Ca9ldO_iQiKNDjpwKWK3Hw.19106.0; tracking_id=7bcb3cf0-7255-4940-b507-a351876c1cf3; footage_search_tracking_id=7bcb3cf0-7255-4940-b507-a351876c1cf3; n_v=a5fbb81d319-prod; NEXT_LOCALE=en; hl=en; IR_gbd=shutterstock.com; _ym_isad=2; _clck=1l6yph|1|eyn|0; ssnext=true; visit_id=74302051011; _actts=1643549689.1643805601.1643828672; _actmr=https%3A%2F%2Fwww.google.com%2F; _actvc=9; OptanonConsent=isIABGlobal=false&datestamp=Thu+Feb+03+2022+00%3A04%3A35+GMT%2B0500+(Pakistan+Standard+Time)&version=6.24.0&hosts=&consentId=c0981f67-ddea-4bdc-b990-220f4cc3e7fc&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CSPD_BG%3A1%2CC0002%3A1%2CC0005%3A1%2CC0004%3A1%2CC0007%3A1&AwaitingReconsent=false; _dc_gtm_UA-32034-1=1; _gcl_aw=GCL.1643828679.Cj0KCQiA9OiPBhCOARIsAI0y71DZ0wTdA2deHqgsJPNil2G182B5o2HqyH0Sjftepr4nPrXeUKL2jrEaApHiEALw_wcB; _gcl_dc=GCL.1643828679.Cj0KCQiA9OiPBhCOARIsAI0y71DZ0wTdA2deHqgsJPNil2G182B5o2HqyH0Sjftepr4nPrXeUKL2jrEaApHiEALw_wcB; _cs_mk=0.13455454898700214_1643828678778; _uetsid=fcd790a082b111ecb3a7ab8dbe49e4f9; _uetvid=701f62f081d111ecbf91f93d2cda99e3; IR_1305=1643828679306%7C76199%7C1643828679306%7C%7C; IR_PI=7a4af2ce-81d2-11ec-88a4-472039357661%7C1643915079306; stc114920=env:1643828679%7C20220305190439%7C20220202193439%7C1%7C1044410:20230202190439|uid:1643549707264.860225411.8935657.114920.1526502327.:20230202190439|srchist:1044410%3A1%3A20220302133507%7C1044418%3A1643653430%3A20220303182350%7C1044417%3A1643694171%3A20220304054251%7C1044418%3A1643719954%3A20220304125234%7C1044410%3A1643727244%3A20220304145404%7C1044418%3A1643805601%3A20220305124001%7C1044410%3A1643828679%3A20220305190439:20230202190439|tsa:0:20220202193439; _cs_id=9c534d58-bffc-ad02-ea01-41ee97781e49.1643549707.20.1643828679.1643828679.1639756028.1677713707162; _cs_s=1.0.0.1643830479536; AMP_TOKEN=%24NOT_FOUND; _gac_UA-32034-1=1.1643828680.Cj0KCQiA9OiPBhCOARIsAI0y71DZ0wTdA2deHqgsJPNil2G182B5o2HqyH0Sjftepr4nPrXeUKL2jrEaApHiEALw_wcB; _ce.s=v11.rlc~1643828680435~v11slnt~1643736781721; _clsk=ukpba7|1643828680656|1|0|f.clarity.ms/collect; cto_bundle=58Xb119iUXZIcWR6NFU0aTh4MGxhd0xlTVFDd3VMQUFYS3hvaXdzMncwU3F2eXo5NFpkODNmSUc3UzZ3STU5YXdwbE5aRUphTGlmNlJkU09TM0VOcURSR1VmR3NHRzE4RDJqU1lxMlJFT0NTZHhLMGE1ZmZ2dFdlTnMzajhWejNjU0VJU1g2Tm1XaWRPa1hOM3JtUm1jNDlsbXclM0QlM0Q; C3S-924=on; _actcc=4.1.193.80; _actmu=7af474cd-225c-44a6-83fd-f0b0cc408eaa; _actms=6bba71e2-e9a2-48ff-b1b4-fd86d01495cf; _4c_=fVJdb9QwEPwrKBJ9qq%2B2Yyd2pQpdr4gWKigUJMRLldibO%2FfSJNhO0wP1v7O%2BaymiiDxYnvHO7Ef2ZzatoMsOWSFyxVXJRM7lfraGTcgOf2ZmSOdtOkbfZofZKsYhHB4cTNM0C6sxRvAh9mY9M%2F3NAdwNbe%2FhYNn2ddWS7QOpQoAYCGWcv1pPRyh8yemfUoQo3jN5NTgbjwYmS8W55qJQe0vTBm%2BOqmlmQwLOHi2u6bvFRzfXH9zF8WrxYf7pLMzP6KZkJ9%2Fo9NnOuYXT78vw9uK9a%2Fkbpvix7Pnp980pvbxuIgxedBf%2BK3x5d86v%2FetqPpy61%2FPz6Woyx9l%2BBh12mw3e4j2EuA4uAhLuplpCosY6GO%2BG6Pru82ZIT2NnoXEdJMUYwF%2FGKo44vWw5QohImn7sot8k2zXCquu7zU0%2FhjOLVC0tAA6dVCbPiZClIBosJQ0vFZRMSqHt1sOmXEzPGJtxJOIPhDmleB18b0cTr%2BKungnqF8GmTBZunYGrCce6SuK8KJ7YFbjlKiJdFiqxg08heJtcZ%2FvpScW1eGJ%2Fq4pCI1v7fsKWES9Wvr%2BBFzo59Kn7c9eNdwg8NOD9NibNbzfOv1fn4QXX7q%2FH1F76IanwtjdVm9S4sBgPJv0EhMd8gfjN%2FOrL2QlCoUuplRR8lpYa51dSld3vZ3e7LddM0lJjAM4w4kqrQtD0YYR39mHdM61KDow3BApaEVEXktRaKcJroExaLXiTStp6SiYVKyjTUtzvyt16FM9SiucpdwMk2AKB7j%2FSf1R76x6LpTbPa005sU1liKCgSW0UI3ljjRTUSF022W9LlVNR6kI8WjL16Di0D47sKVjkmL%2BQ%2BWOweMh%2Ff%2F8L',
'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
'sec-ch-ua-mobile': '?0',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'none',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}
url='https://www.shutterstock.com'

driver.get(url)

driver.implicitly_wait(5)

serch=driver.find_element_by_css_selector('input[aria-label= "Search for images"]')
s = str(input('what you want to search: '))
serch.send_keys(s)

def closeAds():
    try:
        close=driver.find_element_by_id('usi_close')
        close.click()
    except:
        print('no add come this time')

closeAds()

enter=driver.find_element_by_css_selector('button[aria-label = "Search"]')
enter.click()

closeAds()


img=driver.find_elements_by_tag_name('img')
for count,all_src in enumerate(img):
    src=all_src.get_attribute('src')
    print(src)
    src1 = str(src)
    if src1!=None :
        if '.jpg' in src1:
            r = requests.get(src1, headers = header) 
            with open(f'{count}.jpg', 'wb') as f: 
                for chunk in r.iter_content(chunk_size = 1024*1024): 
                    if chunk: 
                        f.write(chunk)





