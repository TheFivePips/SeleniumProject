
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.amazon.com/iFixit-Pro-Tech-Toolkit-Electronics/dp/B01GF0KV6G/ref=sxin_17_ac_d_hl?ac_md=3-1-UmVwYWlyIGtpdHM%3D-ac_d_hl_hl_rf&content-id=amzn1.sym.ea5a3043-3172-4e81-bcc4-eb7524db4f7c%3Aamzn1.sym.ea5a3043-3172-4e81-bcc4-eb7524db4f7c&crid=2MWURPBYYLJ5V&cv_ct_cx=ifixit&keywords=ifixit&pd_rd_i=B01GF0KV6G&pd_rd_r=9288fd88-0a19-484c-8eaf-6e0726fe0e98&pd_rd_w=50Ac2&pd_rd_wg=V1IQV&pf_rd_p=ea5a3043-3172-4e81-bcc4-eb7524db4f7c&pf_rd_r=SP14ZQPC5FB33DNJVESZ&qid=1678978566&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=ifixit%2Caps%2C144&sr=1-2-25fd44b4-555a-4528-b40c-891e95133f20")

Whole_price = driver.find_element(By.CLASS_NAME, "a-price-whole").text
Cents_price = driver.find_element(By.CLASS_NAME, "a-price-fraction").text
full_price = f"${Whole_price}.{Cents_price}"
print(full_price)

total_ratings = driver.find_element(By.XPATH, '//*[@id="acrCustomerReviewText"]').text

star_ratings = driver.find_element(By.XPATH, '//*[@id="reviewsMedley"]/div/div[1]/span[1]/span/div[2]/div/div[2]/div/span/span').text

print(f"{star_ratings} stars out of {total_ratings}")
