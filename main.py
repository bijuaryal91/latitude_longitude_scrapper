from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.common.exceptions import NoSuchElementException

# Read hospital names from the hospital_list.txt file
with open('hospital_list.txt', 'r') as file:
    hospital_names = file.read().splitlines()

# Initialize the Firefox browser using Selenium
driver = webdriver.Firefox()

# Open Google Maps
driver.get('https://www.google.com/maps')

# Define a function to search for a hospital and get its latitude and longitude
def search_hospital_and_get_coordinates(hospital_name):
    search_box = driver.find_element(By.NAME, 'q')
    search_box.clear()
    search_box.send_keys(hospital_name)
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results to load
    driver.implicitly_wait(5)

    # Click on the marker to get its latitude and longitude
    marker_xpath = "//div[contains(@aria-label, '{}')]".format(hospital_name.replace("'", "\\'"))
    marker = driver.find_element(By.XPATH, marker_xpath)
    marker.click()

    try:
        # Get latitude and longitude from the info box
        info_box_xpath = "//div[contains(@aria-label, 'Information about {}')]".format(hospital_name.replace("'", "\\'"))
        info_box = driver.find_element(By.XPATH, info_box_xpath)
        location_text = info_box.text
        lat, lng = location_text.split("\n")[0].split(",")
        latitude, longitude = lat.split(":")[1].strip(), lng.split(":")[1].strip()
    except NoSuchElementException:
        # If information box is not found, get latitude and longitude from the URL
        url = driver.current_url
        query_params = url.split("@")[1].split(",")
        latitude, longitude = query_params[0], query_params[1]

    return latitude, longitude

    search_box = driver.find_element(By.NAME, 'q')
    search_box.clear()
    search_box.send_keys(hospital_name)
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results to load
    driver.implicitly_wait(5)

    # Click on the marker to get its latitude and longitude
    marker = driver.find_element(By.XPATH, "//div[contains(@aria-label, '{}')]".format(hospital_name))
    marker.click()

    try:
        # Get latitude and longitude from the info box
        info_box = driver.find_element(By.XPATH, "//div[contains(@aria-label, 'Information about {}')]".format(hospital_name))
        location_text = info_box.text
        lat, lng = location_text.split("\n")[0].split(",")
        latitude, longitude = lat.split(":")[1].strip(), lng.split(":")[1].strip()
    except NoSuchElementException:
        # If information box is not found, get latitude and longitude from the URL
        url = driver.current_url
        query_params = url.split("@")[1].split(",")
        latitude, longitude = query_params[0], query_params[1]

    return latitude, longitude
# Create lists to store latitude and longitude data
latitudes = []
longitudes = []

# Search and get coordinates for each hospital
for hospital_name in hospital_names:
    latitude, longitude = search_hospital_and_get_coordinates(hospital_name)
    latitudes.append(latitude)
    longitudes.append(longitude)

# Close the browser
driver.quit()

# Combine hospital names, latitudes, and longitudes into a dictionary
data = {
    'Hospital Name': hospital_names,
    'Latitude': latitudes,
    'Longitude': longitudes
}

# Convert the dictionary into a DataFrame using pandas
df = pd.DataFrame(data)

# Save the data to an Excel file
df.to_excel('hospital_coordinates.xlsx', index=False)

print("Coordinates saved to hospital_coordinates.xlsx successfully.")
