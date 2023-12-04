from django.shortcuts import render,redirect
import time
import asyncio
from django.http import JsonResponse
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []
list10 = []
list11 = []
list12 = []
list13 = []
list14 = []
list15 = []
list16 = []
def Trendyol(query,ara):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.trendyol.com/")
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, "V8wbcUhU")))
    current_url = driver.current_url
    driver.find_element(By.CLASS_NAME,"V8wbcUhU").send_keys(ara)
    driver.find_element(By.CLASS_NAME,"V8wbcUhU").send_keys(Keys.ENTER)
    WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME,"search-sort-container")))
    current_url=driver.current_url
    driver.get(f"{current_url}&sst=BEST_SELLER")





    WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME,"product-price")))
    trendyol_name=driver.find_elements(By.CSS_SELECTOR,f"h3.{"prdct-desc-cntnr-ttl-w"}")
    trendyol_price=driver.find_elements(By.CSS_SELECTOR,f"div.{"discounted-price-container"}")
    trendyol_img=driver.find_elements(By.CSS_SELECTOR,"img.p-card-img")
    trendyol_link=driver.find_elements(By.CSS_SELECTOR,f"div.{"p-card-chldrn-cntnr"} a")

    for k in trendyol_name :
        list4.append(k.text)

    for x in trendyol_price:
        list1.append(x.find_element(By.CLASS_NAME,"prc-box-dscntd").text)
    for y in trendyol_img :
        list2.append(y.get_attribute("src"))

    for z in trendyol_link :
        list3.append(z.get_attribute("href"))
    driver.quit()
def Amazon(query,ara):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.amazon.com.tr/")
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.ID,'twotabsearchtextbox')))

    driver.find_element(By.ID,'twotabsearchtextbox').send_keys(ara)
    driver.find_element(By.ID,"nav-search-submit-button").click()

    option_element = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//option[@value='review-rank']")))
    main_url="https://www.amazon.com.tr/"+option_element.get_attribute("data-url")
    driver.get(main_url)
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, "s-result-item")))
    amazon_name = driver.find_elements(By.CLASS_NAME, "a-size-base-plus")
    amazon_price = driver.find_elements(By.CLASS_NAME, "a-row")

    for k in amazon_name :
        list5.append(k.text)

    try:

        product_elements = driver.find_elements(By.CLASS_NAME, "s-price-instructions-style")


        for product_element in product_elements:

            try:
                product_element.find_element(By.CSS_SELECTOR, ".a-price-whole")
                product_element.find_element(By.CSS_SELECTOR, ".a-price-symbol")
                price_element=product_element.find_element(By.CSS_SELECTOR, ".a-price")
               
                
                product_price = price_element.text.replace("\n", ".")
            except:
                product_price = "Fiyat Yok"

            list6.append(product_price)




    except Exception as e:
        pass
    amazon_img = driver.find_elements(By.CLASS_NAME,"s-image")
    amazon_link = driver.find_elements(By.CSS_SELECTOR,'a.a-link-normal.s-no-outline')

    for y in amazon_img :
        
        list7.append(y.get_attribute("src"))
    for z in amazon_link :
        list8.append(z.get_attribute("href"))
    driver.quit()
def Hepsiburada(query,ara):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.hepsiburada.com/")
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME,'searchBoxOld-M1esqHPyWSuRUjMCALPK')))

    driver.find_element(By.CLASS_NAME,'searchBoxOld-M1esqHPyWSuRUjMCALPK').click()
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, 'theme-IYtZzqYPto8PhOx3ku3c')))
    driver.find_element(By.CLASS_NAME,"theme-IYtZzqYPto8PhOx3ku3c").send_keys(ara)
    driver.find_element(By.CLASS_NAME, "theme-IYtZzqYPto8PhOx3ku3c").send_keys(Keys.ENTER)
    current_url = driver.current_url
    driver.get(f"{current_url}&siralama=coksatan")
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, "moria-ProductCard-exfLof")))
    hepsiburada_name =driver.find_elements(By.CSS_SELECTOR,'h3[data-test-id="product-card-name"]')
    hepsiburada_price = driver.find_elements(By.CLASS_NAME,"moria-ProductCard-joawUM")
    hepsiburada_img = driver.find_elements(By.CSS_SELECTOR, "img.moria-ProductCard-dglYMa")
    hepsiburada_link=driver.find_elements(By.CLASS_NAME,"moria-ProductCard-gyqBb")


    for k in hepsiburada_name :
        list9.append(k.text)
    for x in hepsiburada_price:
        list10.append(x.find_element(By.CSS_SELECTOR,'div[data-test-id="price-current-price"]').text)
    for y in hepsiburada_img :
        list11.append(y.get_attribute("src"))
    for z in hepsiburada_link :
        list12.append(z.get_attribute("href"))
    driver.quit()

def N11(query,ara):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.n11.com/")
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID,"searchData")))
    driver.find_element(By.ID, "searchData").click()
    driver.find_element(By.ID, "searchData").send_keys(ara)
    driver.find_element(By.ID, "searchData").send_keys(Keys.ENTER)
    current_url = driver.current_url
    driver.get(f"{current_url}&srt=SALES_VOLUME")
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, 'productName')))
    n11_name = driver.find_elements(By.CLASS_NAME, 'productName')
    n11_price = driver.find_elements(By.CLASS_NAME,"priceContainer ")
    n11_img = driver.find_elements(By.CSS_SELECTOR, "img.lazy.cardImage")
    n11_link = driver.find_elements(By.CSS_SELECTOR, "a.plink")
    for k in n11_name :
        list13.append(k.text)
    for x in n11_price:
        list14.append(x.text)
    for y in n11_img :
        list15.append(y.get_attribute("src"))

        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)

    for z in n11_link :
        list16.append(z.get_attribute("href"))
    driver.quit()
def comparee(ürün_adı):
    list1.clear()
    list2.clear()
    list3.clear()
    list4.clear()
    list5.clear()
    list6.clear()
    list7.clear()
    list8.clear()
    list9.clear()
    list10.clear()
    list11.clear()
    list12.clear()
    list13.clear()
    list14.clear()
    list15.clear()
    list16.clear()
    
    queries = ["product_1", "product_2"]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i, query in enumerate(queries):
            if i % 2 == 0:
                futures.append(executor.submit(Amazon,query,ürün_adı,))
            #elif i % 4== 1:
                #futures.append(executor.submit(Trendyol, query,ürün_adı,))
            #elif i % 4 == 2:
                #futures.append(executor.submit(Hepsiburada, query,ürün_adı,))
            else:
                futures.append(executor.submit(N11, query,ürün_adı,))

        # Tüm işlemleri bitirmesini bekle
        for future in concurrent.futures.as_completed(futures):
            future.result()



def home(request):
    if request.POST:
        trendyol=[]
        hepsiburada=[]
        n11=[]
        amazon=[]
        ürün_adı=str(request.POST["user_search"]).upper()
        comparee(ürün_adı)
        for fiyat,img,link,ad in zip(list1, list2, list3, list4):
                trendyol.append(list([ad, fiyat, img, link]))
        for ad, fiyat, img, link in zip(list5, list6, list7, list8):
                amazon.append(list([ad, fiyat, img, link]))
        for ad, fiyat, img, link in zip(list9, list10, list11, list12):
                hepsiburada.append(list([ad, fiyat, img, link]))
        for ad, fiyat, img, link in zip(list13, list14, list15, list16):
                n11.append(list([ad, fiyat, img, link]))
        listana=[len(amazon),len(n11)]
        referans=int(sorted(listana)[0])
        if 10>=referans>=5:
            my_data = {"trendyol": trendyol[0:referans],"amazon": amazon[0:referans],"hepsiburada": hepsiburada[0:referans],"n11": n11[0:referans],"ürün":ürün_adı}
        elif referans>10:
             my_data = {"trendyol": trendyol[0:10],"amazon": amazon[0:10],"hepsiburada": hepsiburada[0:10],"n11": n11[0:10],"ürün":ürün_adı}
        elif 5>referans>=0:
             my_data = {"trendyol": trendyol[0:5],"amazon": amazon[0:5],"hepsiburada": hepsiburada[0:5],"n11": n11[0:5],"ürün":ürün_adı}

        return render(request,"ilkapp/ilk.html",context=my_data)
        

    else:
        return render(request,"ilkapp/anasayfa.html")


