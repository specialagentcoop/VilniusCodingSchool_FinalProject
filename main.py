from bs4 import BeautifulSoup
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 500)


def scrape_website(outbound_day, return_day):

    url = f'https://www.skyscanner.net/transport/flights/vno/tyoa/2405{outbound_day}/2405{return_day}/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1'
    overall_data = []
    outbound_flight_data = []
    return_flight_data = []

    # Start service
    service = Service(ChromeDriverManager().install())
    service.start()

    # Start driver
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    driver.implicitly_wait(10)

    # Handle cookies
    cookies = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#acceptCookieButton')))
    time.sleep(5)
    cookies.click()
    time.sleep(20)

    # Handle 'Show more results'
    show_more_results_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.BpkButton_bpk-button__YzJlY:nth-child(5)')))
    driver.execute_script('arguments[0].scrollIntoView();', show_more_results_button)
    time.sleep(5)
    show_more_results_button.click()

    # Scroll to the bottom
    for _ in range(65): #65
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(2)

    # Collect data
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # print(soup.prettify())

    flights = soup.find_all('div', class_='BpkTicket_bpk-ticket__NzNiO')
    outbound_flights = soup.find_all('div', class_='LegDetails_container__MTkyZ UpperTicketBody_leg__MmNkN')[0::2]
    return_flights = soup.find_all('div', class_='LegDetails_container__MTkyZ UpperTicketBody_leg__MmNkN')[1::2]

    for flight in flights:
        outbound_date = '2024-05-'+outbound_day
        return_date = '2024-05-'+return_day
        price = flight.find('span', class_='BpkText_bpk-text__MWZkY BpkText_bpk-text--lg__NjNhN').text.strip()

        overall_data.append({
            'Outbound Flight Date': outbound_date,
            'Return Flight Date': return_date,
            'Price': price,
        })

    for outbound_flight in outbound_flights:

        outbound_airlines_element = outbound_flight.find('img', class_='BpkImage_bpk-image__img__MDZkN')
        if outbound_airlines_element:
            outbound_airlines = outbound_airlines_element['alt']
        else:
            outbound_airlines = outbound_flight.find('span', class_='BpkText_bpk-text__MWZkY BpkText_bpk-text--xs__ZDJmY').text.strip()

        outbound_flight_times = outbound_flight.find_all('span', class_='BpkText_bpk-text__MWZkY BpkText_bpk-text--subheading__NzkwO')
        outbound_departure_time = [outbound_flight_time.text.strip() for outbound_flight_time in outbound_flight_times[0::2]]
        outbound_arrival_time = [outbound_flight_time.text.strip() for outbound_flight_time in outbound_flight_times[1::2]]

        outbound_arrival_date_element = outbound_flight.find('span', class_='BpkText_bpk-text__MWZkY BpkText_bpk-text--caption__MTIzM')
        outbound_arrival_date = outbound_arrival_date_element.text.strip() if outbound_arrival_date_element else '0'

        outbound_flight_duration = outbound_flight.find('span', class_='BpkText_bpk-text__MWZkY BpkText_bpk-text--xs__ZDJmY Duration_duration__NmUyM').text.strip()

        outbound_flight_stops_number = outbound_flight.find('span', class_='BpkText_bpk-text__MWZkY BpkText_bpk-text--xs__ZDJmY LegInfo_stopsLabelRed__NTY2Y').text.strip()

        outbound_airports = outbound_flight.find_all('span', class_='BpkText_bpk-text__MWZkY BpkText_bpk-text--body-default__Y2M3Z LegInfo_routePartialCityTooltip__NTE4Z')
        outbound_from_airport = [outbound_airport.text.strip() for outbound_airport in outbound_airports[0::2]]
        outbound_to_airport = [outbound_airport.text.strip() for outbound_airport in outbound_airports[1::2]]

        outbound_flight_stops_airports = outbound_flight.find_all('div', class_='LegInfo_stopsRow__MTUwZ')
        outbound_stops_airports = [airport.text.strip() for airport in outbound_flight_stops_airports]

        outbound_flight_data.append({
            'Outbound Flight Airlines': outbound_airlines,
            'Outbound Flight Departure Time': outbound_departure_time,
            'Outbound Flight Arrival Time': outbound_arrival_time,
            'Outbound Flight Arrival + Days': outbound_arrival_date,
            'Outbound Flight Duration': outbound_flight_duration,
            'Outbound Flight Stops': outbound_flight_stops_number,
            'Outbound Flight Connecting Airports': outbound_stops_airports,
            'Outbound Flight Departure Airport': outbound_from_airport,
            'Outbound Flight Arrival Airport': outbound_to_airport
        })

    for return_flight in return_flights:

        return_airlines_element = return_flight.find('img', class_='BpkImage_bpk-image__img__MDZkN')
        if return_airlines_element:
            return_airlines = return_airlines_element['alt']
        else:
            return_airlines = return_flight.find('span', class_='BpkText_bpk-text__MWZkY BpkText_bpk-text--xs__ZDJmY').text.strip()

        return_flight_times = return_flight.find_all('span', class_='BpkText_bpk-text__MWZkY BpkText_bpk-text--subheading__NzkwO')
        return_departure_time = [return_flight_time.text.strip() for return_flight_time in return_flight_times[0::2]]
        return_arrival_time = [return_flight_time.text.strip() for return_flight_time in return_flight_times[1::2]]

        return_arrival_date_element = return_flight.find('span', class_='BpkText_bpk-text__MWZkY BpkText_bpk-text--caption__MTIzM')
        return_arrival_date = return_arrival_date_element.text.strip() if return_arrival_date_element else '0'

        return_flight_duration = return_flight.find('span', class_='BpkText_bpk-text__MWZkY BpkText_bpk-text--xs__ZDJmY Duration_duration__NmUyM').text.strip()

        return_flight_stops_number = return_flight.find('span', class_='BpkText_bpk-text__MWZkY BpkText_bpk-text--xs__ZDJmY LegInfo_stopsLabelRed__NTY2Y').text.strip()

        return_airports = return_flight.find_all('span', class_='BpkText_bpk-text__MWZkY BpkText_bpk-text--body-default__Y2M3Z LegInfo_routePartialCityTooltip__NTE4Z')
        return_from_airport = [return_airport.text.strip() for return_airport in return_airports[0::2]]
        return_to_airport = [return_airport.text.strip() for return_airport in return_airports[1::2]]

        return_flight_stops_airports = return_flight.find_all('div', class_='LegInfo_stopsRow__MTUwZ')
        return_stops_airports = [airport.text.strip() for airport in return_flight_stops_airports]

        return_flight_data.append({
            'Return Flight Airlines': return_airlines,
            'Return Flight Departure Time': return_departure_time,
            'Return Flight Arrival Time': return_arrival_time,
            'Return Flight Arrival + Days': return_arrival_date,
            'Return Flight Duration': return_flight_duration,
            'Return Flight Stops': return_flight_stops_number,
            'Return Flight Connecting Airports': return_stops_airports,
            'Return Flight Departure Airport': return_from_airport,
            'Return Flight Arrival Airport': return_to_airport
        })

    # Stop service and driver
    service.stop()
    driver.quit()

    overall_df = pd.DataFrame(overall_data)
    outbound_data = pd.DataFrame(outbound_flight_data)
    return_data = pd.DataFrame(return_flight_data)
    df = pd.concat([overall_df, outbound_data, return_data], axis=1)
    df.to_csv(f'2405{outbound_day}-2405{return_day}_SkyScanner_Vilnius_Tokyo.csv', index=False)
    print(df)
    return df


scrape_website('03', '10')