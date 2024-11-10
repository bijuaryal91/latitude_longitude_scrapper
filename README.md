# Hospital Latitude and Longitude Scraper

A Python-based scraper that uses Selenium to retrieve latitude and longitude coordinates for a list of hospitals. The script reads hospital names from a `.txt` file, scrapes the coordinates from an online geolocation service, and saves the results to a `.csv` file. This tool is useful for healthcare data mapping, geographic analysis, and visualization.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
---

## Features

- **Automated Geolocation with Selenium**: Uses Selenium to scrape latitude and longitude data for each hospital.
- **Batch Processing**: Reads hospital names from a `.txt` file and outputs data to a `.csv` file.
- **Error Handling**: Handles invalid entries and logs errors for unsuccessful lookups.
- **Configurable and Extendable**: Designed to be easily modified to work with different websites.

---

## Tech Stack

- **Language**: Python
- **Libraries**: `selenium` (for web scraping), `pandas` (for CSV handling)
- **Browser Automation**: Selenium with ChromeDriver or GeckoDriver (Firefox)

---

## Installation

### Prerequisites

- **Python**: Python 3.6 or higher
- **Selenium WebDriver**: ChromeDriver or GeckoDriver (Firefox) installed and added to your system PATH
- **Browser**: Chrome or Firefox

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/bijuaryal91/latitude_longitude_scrapper.git
   cd latitude_longitude_scrapper
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
3. **Run the script**
   ```bash
   python main.py
4. **View Result**: The output CSV will contain hospital_name, latitude, and longitude columns.


## Configuration
1. **Modify Scraping Logic**: In `main.py`, adjust the Selenium script to target the correct elements based on the geolocation service you are scraping.
2. Error Handling: Ensure your geolocation source does not have rate limiting or CAPTCHA restrictions, which can interrupt Selenium scraping.