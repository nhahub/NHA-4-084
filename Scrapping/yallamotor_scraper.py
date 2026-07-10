import sys
import subprocess
subprocess.run([sys.executable, '-m', 'pip', 'install', 'selenium', 'pandas', 'requests', 'undetected-chromedriver', '-q'])

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import pandas as pd
import re

driver = uc.Chrome()
driver.maximize_window()
print('Browser opened!')

try:
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD', timeout=10)
    usd_rate = response.json()['rates']['EGP']
    print(f'USD → EGP Rate: {usd_rate}')
except:
    usd_rate = 51.8
    print(f'Could not fetch rate. Using fallback: {usd_rate}')

test_url = 'https://egypt.yallamotor.com/used-cars/kia/cerato/2014/used-kia-cerato-2014-6th-of-october-city-2103935'
driver.get(test_url)
time.sleep(4)

body_text = driver.find_element(By.TAG_NAME, 'body').text
print(body_text[:3000])

NUM_PAGES = 230

all_links = []

for page in range(1, NUM_PAGES + 1):
    url = 'https://egypt.yallamotor.com/used-cars' if page == 1 else f'https://egypt.yallamotor.com/used-cars?page={page}'
    driver.get(url)
    time.sleep(4)

    links = set()

    all_anchors = driver.find_elements(By.TAG_NAME, 'a')
    for a in all_anchors:
        try:
            href = a.get_attribute('href') or ''
            if re.search(r'/used-cars/[^/]+/[^/]+/\d{4}/', href):
                links.add(href.split('?')[0])
        except:
            pass

    all_links.extend(list(links))
    print(f'Page {page}: {len(links)} car links found')
    time.sleep(2)

all_links = list(set(all_links))
print(f'\nTotal unique car links: {len(all_links)}')

Cars = []

for i, url in enumerate(all_links):
    driver.get(url)
    time.sleep(2)

    try:
        try:
            title = driver.find_element(By.CSS_SELECTOR, 'h1').text.strip()
            title = re.sub(r'^(Used|New)\s+', '', title).strip()
        except:
            title = 'N/A'

        page_text = driver.find_element(By.TAG_NAME, 'body').text

        year = 'N/A'
        year_match = re.search(r'\b(199\d|200\d|201\d|202[0-7])\b', page_text)
        if year_match:
            year = year_match.group(1)

        mileage = 'N/A'
        mileage_match = re.search(r'([\d,]+)\s*KM', page_text, re.IGNORECASE)
        if mileage_match:
            mileage = mileage_match.group(0).strip()

        transmission = 'N/A'
        if re.search(r'\bAutomatic\b', page_text, re.IGNORECASE):
            transmission = 'Automatic'
        elif re.search(r'\bManual\b', page_text, re.IGNORECASE):
            transmission = 'Manual'

        engine_cc = 'N/A'
        cc_match = re.search(r'([\d,]+)\s*CC', page_text, re.IGNORECASE)
        if cc_match:
            engine_cc = cc_match.group(0).strip()
        else:
            l_match = re.search(r'(\d+\.\d+)\s*L\b', page_text)
            if l_match:
                engine_cc = l_match.group(0).strip()

        date_posted = 'N/A'
        date_match = re.search(
            r'(\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4}|'
            r'(?:Today|Yesterday|\d+\s+(?:hour|day|week|month)s?\s+ago))',
            page_text, re.IGNORECASE
        )
        if date_match:
            date_posted = date_match.group(0).strip()
        else:
            try:
                date_posted = driver.find_element(By.TAG_NAME, 'time').get_attribute('datetime') or 'N/A'
            except:
                pass

        Cars.append({
            'Brand & Model'    : title,
            'Year'             : year,
            'Mileage'          : mileage,
            'Transmission'     : transmission,
            'Date Posted'      : date_posted,
            'USD Exchange Rate': usd_rate,
            'Engine CC'        : engine_cc
        })

        print(f'[{i+1}/{len(all_links)}] ✓ {title} | {year} | {mileage} | {transmission} | {engine_cc}')

    except Exception as e:
        print(f'[{i+1}/{len(all_links)}] ✗ Error: {e}')

    time.sleep(1.5)

driver.quit()
print(f'\nDone! {len(Cars)} cars scraped.')

df = pd.DataFrame(Cars, columns=[
    'Brand & Model', 'Year', 'Mileage', 'Transmission',
    'Date Posted', 'USD Exchange Rate', 'Engine CC'
])

df = df[~df['Brand & Model'].str.contains('Cars For Sale', case=False, na=False)]

df = df.drop_duplicates(subset=['Brand & Model'])
df = df.reset_index(drop=True)

df.to_csv('yallamotor_cars.csv', index=False, encoding='utf-8-sig')
print(f'Saved {len(df)} cars to yallamotor_cars.csv')

print(df.head(10))
