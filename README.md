# Vilnius-Tokyo-Vilnius SkyScanner May 2024 Flights Analysis

## Details
### Created by: Ugnė Petravičiūtė and Laura Budrytė

This code was developed for the final project of the Vilnius Coding School's Data Analytics and Fundamentals of Python Programming course.

### Project Goal

The goal of the project is to analyze data for the Vilnius-Tokyo-Vilnius flight route in May 2024, with a focus on identifying factors that influence flight prices. We selected four date ranges for the week-long trip analysis: May 03-10, May 10-17, May 17-24, and May 24-31, with a total of 2,582 flights.

We primaraly used Python programming language to complete the project, alongside Postgres and CSV for data storage. 

### Applied Knowledge

_Used imports_: BeautifulSoup, Selenium, Pandas, Matplotlib, Seaborn, scikit-learn, psycopg2.

### Scraping

[scraping.pyscraping.py](https://github.com/specialagentcoop/VilniusCodingSchool_FinalProject/blob/23aac3d9f26254b4096146b71a2de4e652f6cf36/scraping.py)

1) We used the Selenium library to handle cookies as well as to create the visibility of all results on the page.
2) Then, we utilized the BeautifulSoup library to gather all required data.
3) Finally, the Pandas library was used to merge the collected data and create CSV files to store scraped data.
4) We designed the scraping as a function to have the flexibility in indicating dates we want to collect data for.

_Scraped URLs_

- May 3-10:
https://www.skyscanner.net/transport/flights/vno/tyoa/240503/240510/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1
- May 10-17:
https://www.skyscanner.net/transport/flights/vno/tyoa/240510/240517/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1
- May 17-24:
https://www.skyscanner.net/transport/flights/vno/tyoa/240517/240524/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1
- May 24-31:
https://www.skyscanner.net/transport/flights/vno/tyoa/240524/240531/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1

### Data Cleaning

[data_cleaning.py](https://github.com/specialagentcoop/VilniusCodingSchool_FinalProject/blob/69b4a19ab97208fc83d0326cbf580e7f7fccb72b/data_cleaning.py)

1) The Pandas library was used to concatenate four files containing scraped data. Additionally, Pandas was used for data cleaning and convertion (to_datetime, to_numeric, apply, replace, rename, dropna, drop_duplicates).
2) We designed a function to convert time to minutes which is essential for mathematical calculations.

### Moving Data to SQL

[move_to_sql.py](https://github.com/specialagentcoop/VilniusCodingSchool_FinalProject/blob/08fc12f9022a7b0058dfa89e3dddc3bb3e0f2cee/move_to_sql.py)

- We utilized Pandas and psycopg2 libraries to securely store our data in Postgres.

### Data Analysis and Depiction

[tables.py](https://github.com/specialagentcoop/VilniusCodingSchool_FinalProject/blob/e94c6ae277b3316ada600109e15edbe4ff29ef43/tables.py)

* **Vilnius-Tokyo-Vilnius Flight Price vs Time and Predicted Flight Prices**

This visualization illustrates the correlation between flight prices and flight time in the analyzed data, along with the predicted trend.

![Screenshot 2024-01-31 204245](https://github.com/specialagentcoop/VilniusCodingSchool_FinalProject/assets/156001901/30eed034-00f6-4273-831f-4b81ce39a3e2)

* **Average Vilnius-Tokyo-Vilnius Flight Price by Date**

In this visualization, the average prices of flights are presented for each flight date.

![Screenshot 2024-01-31 204518](https://github.com/specialagentcoop/VilniusCodingSchool_FinalProject/assets/156001901/4f088e92-cd31-4509-bdd2-70a240caf70b)

* **Average Price by Airlines**

This visualization displays the average prices for each airline when both outbound and return flights are operated by the same airline.

![Screenshot 2024-01-31 204439](https://github.com/specialagentcoop/VilniusCodingSchool_FinalProject/assets/156001901/e93bccc2-0f3a-4956-93d1-d014350ac181)

* **Correlation Between Price and Departure Time From VNO**

This visualization depicts the correlation between departure time of outbound flights from Vilnius and their corresponding prices. Additionally, it illustrates the frequency of flights for each departure time.

![Screenshot 2024-01-31 204549](https://github.com/specialagentcoop/VilniusCodingSchool_FinalProject/assets/156001901/dd5b3af8-b7bb-492a-9ef6-19405fcb8526)

* **Top 10 Connecting Airports**

This visualization shows most common connecting international airports for Vilnius-Tokyo-Vilnius route.

![Screenshot 2024-01-31 204626](https://github.com/specialagentcoop/VilniusCodingSchool_FinalProject/assets/156001901/95439d35-531d-476e-a4fa-183ddefadac7)

### Conclusion

- The analysis of flights shows that the longer the flight takes, the cheaper it is. This prediction is only applicable for near future.
- In terms of dates, it is cheapest to fly on May 10-17 (average price is 1,698 Euros), possibly due to national celebrations in Japan. May 3-5 encompass Constitution Memorial Day, Greenery Day, and Children's Day. Therefore, flights for May 03-10 have the highest average price (2,099 Euros).
- Additionally, the most cost-effective airline is Scandinavian Airlines. The average price for a flight with Scandinavian Airlines is 970 Euros. Meanwhile, the most expensive airline is Air France, where a flight costs an average of 2,808 Euros. 
- When considering the departure time from VNO in relation to the price, the earliest and latest departures offer the lowest prices, while the highest prices are for midday departures at 11 am. 
- Additionally, we examined the top airports through which one can travel to Tokyo, and the most popular routes lead through Helsinki, Frankfurt, and Istanbul.
