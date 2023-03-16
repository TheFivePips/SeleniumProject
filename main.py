
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# chrome_driver_path = "/home/sam/development/chromedriver"
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.amazon.com/iFixit-Pro-Tech-Toolkit-Electronics/dp/B01GF0KV6G/ref=sxin_17_ac_d_hl?ac_md=3-1-UmVwYWlyIGtpdHM%3D-ac_d_hl_hl_rf&content-id=amzn1.sym.ea5a3043-3172-4e81-bcc4-eb7524db4f7c%3Aamzn1.sym.ea5a3043-3172-4e81-bcc4-eb7524db4f7c&crid=2MWURPBYYLJ5V&cv_ct_cx=ifixit&keywords=ifixit&pd_rd_i=B01GF0KV6G&pd_rd_r=9288fd88-0a19-484c-8eaf-6e0726fe0e98&pd_rd_w=50Ac2&pd_rd_wg=V1IQV&pf_rd_p=ea5a3043-3172-4e81-bcc4-eb7524db4f7c&pf_rd_r=SP14ZQPC5FB33DNJVESZ&qid=1678978566&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=ifixit%2Caps%2C144&sr=1-2-25fd44b4-555a-4528-b40c-891e95133f20")
title = driver.title
# print(title)
Whole_price = driver.find_element(By.CLASS_NAME, "a-price-whole").text
Cents_price = driver.find_element(By.CLASS_NAME, "a-price-fraction").text
full_price = f"${Whole_price}.{Cents_price}"
print(full_price)