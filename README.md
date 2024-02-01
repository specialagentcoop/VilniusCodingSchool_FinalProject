# Vilnius-Tokyo-Vilnius SkyScanner May 2024 Flights Analysis

## Details
### Created by: Ugnė Petravičiūtė and Laura Budrytė

This code was developed for the final project of the Vilnius Coding School's Data Analytics and Fundamentals of Python Programming course.

### Project Goal

The goal of the project is to analyze data for the Vilnius-Tokyo-Vilnius flight route in May 2024, with a focus on identifying factors that influence flight prices. We selected four date ranges for the week-long trip analysis: May 03-10, May 10-17, May 17-24, and May 24-31, with a total of 2,582 flights.

We primaraly used Python programming language to complete the project, alongside Postgres and CSV for data storage. 

### Applied Knowledge

Used libraries: BeautifulSoup, Selenium, Pandas, Matplotlib, Seaborn, scikit-learn, psycopg2.

### Scraping

[scraping.pyscraping.py](https://github.com/specialagentcoop/VilniusCodingSchool_FinalProject/blob/23aac3d9f26254b4096146b71a2de4e652f6cf36/scraping.py)

1) We used the Selenium library to handle cookies as well as to create the visibility of all results on the page.
2) Then, we utilized the BeautifulSoup library to gather all required data.
3) Finally, the Pandas library was used to merge the collected data and create a dataframe.

Scraped URLs

- May 3-10:
https://www.skyscanner.net/transport/flights/vno/tyoa/240503/240510/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1
- May 10-17:
https://www.skyscanner.net/transport/flights/vno/tyoa/240510/240517/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1
- May 17-24:
https://www.skyscanner.net/transport/flights/vno/tyoa/240517/240524/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1
- May 24-31:
https://www.skyscanner.net/transport/flights/vno/tyoa/240524/240531/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=false&ref=home&rtn=1
