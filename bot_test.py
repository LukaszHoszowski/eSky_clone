from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

trip_type = 'roundtrip'
search_airport_type = 'ap'
departure = 'krk'
arrival = 'lon'
arrival_date = '2022-02-26'
departure_date = '2022-02-26'

pax_adult = '1'
pax_young = '0'
pax_children = '0'
pax_infant = '0'
flight_standard = 'economy'

def cookie_down():
    btn_cookie_agreement = driver.find_element(By.CSS_SELECTOR,
                                               'div[class$="summary-buttons"] button[size="large"]:last-child')
    btn_cookie_agreement.click()

url = f'https://www.esky.pl/flights/select/{trip_type}/{search_airport_type}/{departure}/{search_airport_type}/{arrival}' \
      f'?departureDate={departure_date}&returnDate={arrival_date}&pa={pax_adult}&py={pax_young}&pc={pax_children}&pi={pax_infant}&sc={flight_standard}'

driver = webdriver.Chrome('./drivers/chromedriver')
driver.get(url)

cookie_down()

# departure = driver.find_element(By.ID, 'departureRoundtrip0')
# departure.send_keys('Kraków, Balice, małopolskie, Polska (KRK)')
# departure.click()
# departure.send_keys(Keys.RETURN)
# arrival = driver.find_element(By.ID, 'arrivalRoundtrip0')
# arrival.send_keys('Wrocław, Strachowice, dolnośląskie, Polska (WRO)')
# arrival.click()
# arrival.send_keys(Keys.RETURN)
# arrival.send_keys(Keys.RETURN)
# arrival.click()
# btn_search = driver.find_element(By.CSS_SELECTOR,
#                                            '#multiQsfFlights > form > section.main > div.right-data > fieldset.trip-search > button')


# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
