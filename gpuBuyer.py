from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
import time
import datetime
import playsound

browser = webdriver.Chrome()

def send_email(product):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('', 'pgluytbbrxyszkyk') # recipient email goes in the single quote
    subject = 'RTX 3070 IN STOCK SOMEWHERE'
    body = 'This is the link: \n' + product

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('', '', msg) # recepient email goes in both quotes

    print('Email has been sent')
    server.quit()

inStock = False
available = 0

results = open("results.txt", "a+")

def times(avble, store):
    day = str(datetime.datetime.now())
    results.write(day + " " + avble + " at " + store + "\n")


while inStock == False or available == 0:
    prod = "https://www.microcenter.com/product/630035/gigabyte-geforce-rtx-3070-eagle-triple-fan-8gb-gddr6-pcie-40-graphics-card"
    browser.get("https://www.microcenter.com/product/630035/gigabyte-geforce-rtx-3070-eagle-triple-fan-8gb-gddr6-pcie-40-graphics-card")
    browser.find_element_by_class_name("close").click()
    site = browser.page_source

    if site.find(">Sold Out<") == -1:
        send_email(prod)
        playsound.playsound('ringtone.mp3', True)
        times("In stock", "Micro Center")
        inStock = True

    else:
        prod = "https://www.newegg.com/asus-geforce-rtx-3070-dual-rtx3070-8g/p/N82E16814126460?Item=N82E16814126460&Description=RTX%203070&cm_re=RTX_3070-_-14-126-460-_-Product&quicklink=true"
        browser.get("https://www.newegg.com/asus-geforce-rtx-3070-dual-rtx3070-8g/p/N82E16814126460?Item=N82E16814126460&Description=RTX%203070&cm_re=RTX_3070-_-14-126-460-_-Product&quicklink=true")
        time.sleep(.25)
        times("Out of stock", "Micro Center")
        site = browser.page_source
        
    if site.find(" OUT OF STOCK.") == -1:
        send_email(prod)
        playsound.playsound('ringtone.mp3', True)
        times("In stock", "Newegg")
        inStock = True
    
    else:
        browser.get("https://www.newegg.com/msi-geforce-rtx-3070-rtx-3070-ventus-2x/p/N82E16814137605?Item=N82E16814137605&Description=RTX%203070&cm_re=RTX_3070-_-14-137-605-_-Product&quicklink=true")
        prod = "https://www.newegg.com/msi-geforce-rtx-3070-rtx-3070-ventus-2x/p/N82E16814137605?Item=N82E16814137605&Description=RTX%203070&cm_re=RTX_3070-_-14-137-605-_-Product&quicklink=true"
        time.sleep(.25)
        times("Out of stock", "Newegg")
        site = browser.page_source

    if site.find(" OUT OF STOCK.") == -1:
        send_email(prod)
        playsound.playsound('ringtone', True)
        times("In stock", "Newegg")
        inStock = True

    else:
        browser.get("https://www.newegg.com/zotac-geforce-rtx-3070-zt-a30700e-10p/p/N82E16814500501?Item=N82E16814500501&Description=RTX%203070&cm_re=RTX_3070-_-14-500-501-_-Product&quicklink=true")
        prod = "https://www.newegg.com/zotac-geforce-rtx-3070-zt-a30700e-10p/p/N82E16814500501?Item=N82E16814500501&Description=RTX%203070&cm_re=RTX_3070-_-14-500-501-_-Product&quicklink=true"
        time.sleep(.25)
        times("Out of stock", "Newegg")
        site = browser.page_source
       
    if site.find(" OUT OF STOCK.") == -1:
        send_email(prod)
        playsound.playsound('ringtone.mp3', True)
        times("In stock", "Newegg")
        inStock = True

    else:
        print("Nothing in stock. Will check in 15 minutes")
        times("Out of stock", "Newegg")
        available = 1
    
    browser.quit()

results.close()
