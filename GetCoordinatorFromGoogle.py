from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep

# Download Chrome Webdriver (https://chromedriver.chromium.org/downloads), unzip to a folder
# then change the link of the Chrome Webdriver here.
chrome_webdriver = "D:/Projects/Python/Get Coordinator from Google/chromedriver_win32/chromedriver.exe"

# change the link of the input & output file here
input_link = "D:/Projects/Python/Get Coordinator from Google/Data/source_file.xlsx"
output_link = "D:/Projects/Python/Get Coordinator from Google/Data/result_file.xlsx"

# change the default point on Google map here:
default_point = "https://www.google.com/maps/@21.0182634,105.8241991,17z"

# Read data from excel
source_file = pd.read_excel(input_link)
row_num = len(source_file)

# Open Chrome
driver = webdriver.Chrome(chrome_webdriver)
driver.get("https://www.google.com/maps/")
# Wait 10 secs for user to click "I agree"
sleep(10)

# Loop over the addresses to search on Google Maps
for i in range(0, row_num):

    # driver.get(default_point) # Uncomment this line to use the default map point
    # Find search box & click
    input_area = driver.find_element(By.ID, "searchboxinput")
    input_area.click()
    input_area.clear()
    # Search for the address
    address = source_file["ADDRESS"][i]
    input_area.send_keys(address)
    # Find search button & click
    search_button = driver.find_element(By.ID, "searchbox-searchbutton")
    search_button.click()
    # Wait 2 secs to retrieve the result
    sleep(2)
    current_link = driver.current_url

    # Split the link to get the coordinator
    if current_link[0:35] == "https://www.google.com/maps/search/":
        latitude = "Cannot be found"
        longitude = "Cannot be found"
    else:
        if len(current_link.split("/")[1]) < 50:
            latitude = current_link.split('/')[-2].split(',')[0][1:]
            longitude = current_link.split('/')[-2].split(',')[1]
        else:
            latitude = current_link.split('/')[-1].split('!')[-2][2:]
            longitude = current_link.split('/')[-1].split('!')[-1][2:]
    source_file.loc[i, "LAT"] = latitude
    source_file.loc[i, "LNG"] = longitude

# Export to Excel file
source_file.to_excel("D:/Projects/Python/Get Coordinator from Google/Data/result_file.xlsx")
print("Done!")
