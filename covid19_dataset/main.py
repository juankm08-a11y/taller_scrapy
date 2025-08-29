import os 
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Directory_Downloads
download_dir = os.path.join(os.getcwd(),"datasets")
os.makedirs(download_dir,exist_ok=True)

# Configuration browser

chrome_options = Options()
prefs = {
    "download.default_directory":download_dir,
    "download.prompt_for_download":False,
    "download.directory_upgrade":True,
    "safebrowsing.enabled":True
}
chrome_options.add_experimental_option("prefs",prefs)

#Initialization Selenium
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    
  driver.get("https://www.stats.govt.nz/large-datasets/csv-files-for-download/")
  
 
  time.sleep(3)
  link = driver.find_element(By.LINK_TEXT,"2013 Census meshblock data")
  csv_url = link.get_attribute("href")
  
  response = requests.get(csv_url)
  output_file = os.path.join(download_dir,"meshblock_data.csv")
  with open(output_file,"wb") as f:
      f.write(response.content)  
  
  print(f"Archivaod descargado en: {output_file}")
  
finally:
  time.sleep(5)
  driver.quit()