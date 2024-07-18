from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from azure.storage.blob import BlobServiceClient, BlobClient
import os
from datetime import datetime

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://google.com")
title = driver.title

driver.quit()

# Get the current date and time
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
file_name = f"file_{current_time}.txt"
directory = "scrape_results"

# Create directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

file_path = os.path.join(directory, file_name)

with open(file_path, "w") as f:
    f.write(title)

print(f"File saved to {file_path}")