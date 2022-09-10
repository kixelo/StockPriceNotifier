from selenium import webdriver
import time
import yagmail
import os

def get_driver():
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  
  driver = webdriver.Chrome(options=options)
  driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
  return driver

def clean_text(text):
  output=float(text.replace("%", ""))
  return output

def main():
  driver=get_driver()
  print(driver)
  time.sleep(2)
  element = driver.find_element(by="xpath", value='//*[@id="app_indeks"]/section[1]/div/div/div[2]/span')
  return clean_text(element.text)

def notification():
  stock_price=main()
  sender = "pypip2022@gmail.com"
  receiver = "nebemof893@laluxy.com"
  subject = "This is the subject"
  contents = f"Stock price change notification, the current price drop is {stock_price} %"

  yag = yagmail.SMTP(user=sender, password=os.getenv("PASSWORD"))
  if stock_price < 0.10:
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email sent!")
  else:
    print("No significant change")
  return "{:.2f}".format(stock_price)

print(notification())