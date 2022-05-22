# UMBC DATA 606 Data Science Capstone Project
## Exploring Micromobility and Factors in Growth and Success of the Programs
## Spring 2022, Dr. Chaojie Wang
## David Fahnestock

Video Presentation: <a href='https://youtu.be/F80b0GESftU'>Video Link</a><br />
PowerPoint: <a href='https://github.com/dfdatascience/David_DATA606/blob/main/Presentations/CapstoneSpring2022_PowerPointPresentation-Micromobility.pdf'>Slides</a><br />

## Subject Overview
Micromobility is a growing way in cities for the public to travel from place to place quickly and easily.  This includes pedal bicycles, e-bikes, and scooters that are generally made available for small rental fees per trip or through periodic paid passes.  The global micromobility market is projected to grow from $44 billion in 2020 to over $214 billion by 2030 [1].  

Use of micromobility is not only a healthy way to travel but also can be beneficial to reduce city congestion and pollution from vehicular traffic.  It can also help reshape the way we think about travel in cities.  Many cities in the United States are implementing micromobility programs.  This project focuses on analysis of three large city micromobility programs: (1) Chicago, Illinois; (2) New York City, New York; and (3) San Francisco, California. The focus of this project is to explore factors that result in, or can be used to predict, the growth and success of micromobility programs by applying data science techniques.

## Research Questions
This project seeks to answer these questions:
- What factors impact usage and growth of micromobility?
- Can machine-learning be used to accurately:
	- Predict growth or usage patterns in micromobility?
	- Identify other cities where micromobility programs would have a high likelihood of success?

## About the Data Used
This project includes the detail micromobility usage data for each of the three cities [4].  The data is at the micromobility trip level, meaning each row of data represents one micromobility trip from one location to another location in the city. The data includes various elements, including the start and end date/time of each trip, the user's type (member or casual users), and other elements.  This project generally includes analysis of the period from 2019 through 2021, but expands the period in some instances during machine learning.  For the period from 2019 through 2021, there were over 90 million rows.

The project also uses supplemental economic and historic weather data [5].  This is considered to identify whether those factors also contain useful features that can be used to predict or obtain a better understanding of the features that impact micromobility usage.

These data sources are direct from the city websites (for usage data) or from governmental programs (unemployment and weather).  This helps ensure that the data are from reputable sources and are reliable.

## Unit of Analysis
The analysis focuses at the city level, through analysis of micromobility programs administered in multiple cities.  Additionally, the focus is on cities within the United States for the purpose of this project.

With regard to the underlying data, the lowest level unit of measure is on the trip detail.  That is, micromobility data is generally published in terms of one record per trip (from point A to point B). Therefore, the general unit of measure would be in terms of the volume of trips. 

## Exploratory Data Analysis



## Feature Selection
Based on exploratory data analysis, the following feature determinations were made for consideration during machine learning:




## Machine Learning Models
Two machine learning models were used:
1. ARIMA – This is an auto-regressive machine learning model that provides unique benefits for forecasting based on time series data.  For example, a research paper utilized ARIMA to effectively forecast inflation in Ireland [2].  ARIMA is a univariate time-series analysis model.  For the purpose of this project, it will be used to predict micromobility usage at each city in terms of number of trips.
 
3. Long Short-Term Memory (LSTM) Neural Network – LSTM uses a recurrent neural network and has been found to be suitable for time series based forecasting.  It was found in research to perform well for stock price prediction and where there are multivariate input [3].


## How do you plan to develop/apply ML and how you evaluate/compare the performance of the models?
For use in predicting the growth or future usage of micromobility in a given city, trying different combinations of features to be used in the model.  Then splitting the micromobility data into training and test sets to determine the accuracy of each different model applied.  In other words, after training each model, run it on the test set and evaluating the accuracy (within a range of bounds) based on the actual usage change.  For example, how accurate did the model predict micromobility usage (number of trips) from one Summer to the next Summer, etc.  Evaluation of the different models will include various comparisons within a given city's micromobility program (predicting growth within that city), but also comparisons between different cities.  For example, evaluating whether a model trained on one city's data can be accurate at prediction when tested on another city's data.


## What outcomes do you intend to achieve (better understanding of problems, tools to help solve problems, predictive analytics with practical applications, etc)?
I intend to better understand usage patterns of micromobility and which factors are most relevant to predict usage, growth, and the success of micromobility programs.  Ideally, the outcome would help in evaluating and identifying other cities that could benefit most from micromobility programs, and be successful with those programs.


# Preliminary Exploratory Data Analysis

## Review of New York City (NYC) Bikeshare Trip Data

### Data Description
- This data is published here: https://ride.citibikenyc.com/system-data
- The data is provided in csv format by month
- Each record represents one trip, meaning a bike trip from one station to another station within the city
- Data Elements for the period reviewed are:
    - Ride ID
    - Rideable type
    - Started at
    - Ended at
    - Start station name
    - Start station ID
    - End station name
    - End station ID
    - Start latitude
    - Start longitude
    - End latitude
    - End longitude
    - Member or casual ride
- Each monthly csv file ranged from about 100MB to 600MB

### Review and Preliminary Observations
- Performed using Python in a Jupyter Notebook, found here: https://github.com/dfdatascience/David_DATA606/blob/main/python/DATA606-Project-EDA-Combined.ipynb
- For preliminary review, downloaded the most recent 12 months of data for the period from February 2021 through January 2022
- During this 1 year period, there were approximately 27.6 million trips
- Performed some cleaning of the data.  For example, certain fields had some null values.  These represented a relatively small portion of the total data (about 100 thousand of the 27.6 million records).  These nulls were replaced with 0's (for numeric fields) and "" for string fields.
- There were 1586 different Start Stations from which trips originated

- From review of the number of trips per month over the 12 month period, it is clear that the highest usage occurs in the summer months with the least usage in the winter months:
   <img src='https://github.com/dfdatascience/David_DATA606/blob/main/EDA/nyc_2021tripsbymonth.png?raw=true' width='75%'>

- Usage by Bike Type is dominated by Classic Bikes (not required to be docked) followed by Docked Bikes.  E-Bikes (that have electric motors) represent a miniscule portion of usage.  This appears to be due to the very limited number of e-bikes available.  From some online resources, it indicated about 250 e-bikes were introduced in early 2020.  Overall: 
    - classic_bike: 18,432,181 trips
	- docked_bike:   9,184,134 trips
	- electric_bike:       507 trips


- Usage by Member Type is predominately members rather than those who are casual, meaning they pay for each trip without joining:

   <img src='https://github.com/dfdatascience/David_DATA606/blob/main/EDA/nyc_2021tripsbymembertype.png?raw=true' width='75%'>


### Next Steps in Exploratory Data Analysis
This was just a preliminary exploratory analysis to get started and get some initial understanding of the data for the largest city (NYC).  The analysis will be expanded significantly from here, including:
- The time period will be expanded significantly from this single year period.  That is, the analysis will expand to at least 3 years of data.  Assuming the volume is consistent with this preliminary review, that will amount to about 80 million records just for NYC.
- I will be looking to include at least 3 other micromobility programs for other cities.  Depending on the types of data elements tracked by each different city, this could present challenges in being able to have consistent features for analysis and for applying machine learning modeling for prediction.
- Demographic data for each city reviewed will also be analyzed.  For example, this could include the average age, income level, population size, etc.
- Other data related to economic conditions (such as unemployment rates) will also be obtained and analyzed in conjunction with the micromobility data.
 



## References

<a id="1">[1]</a> 
J. Du, Q. Liu, K. Chen and J. Wang, "Forecasting stock prices in two ways based on LSTM neural network," 2019 IEEE 3rd Information Technology, Networking, Electronic and Automation Control Conference (ITNEC), 2019, pp. 1083-1086, doi: 10.1109/ITNEC.2019.8729026.

<a id="2">[2]</a> 
Meyler, Aidan, Geoff Kenny, and Terry Quinn. "Forecasting Irish inflation using ARIMA models." (1998): 1-48.

<a id="3">[3]</a>
Market background: https://www.alliedmarketresearch.com/micro-mobility-market-A11372#:~:text=The%20global%20micromobility%20market%20was,17.4%25%20from%202021%20to%202030

Data Sources:
<a id="4">[4]</a>
Micromobility Usage Data
- Chicago Bikeshare: https://ride.divvybikes.com/system-data
- New York City Bikeshare: https://ride.citibikenyc.com/system-data
- San Francisco Bikeshare: https://www.lyft.com/bikes/bay-wheels/system-data

<a id="5">[5]</a>
Economic and Weather Data
- U.S. Bureau Labor Statistics (BLS) Unemployment data: https://www.bls.gov/bls/unemployment.htm.  This data includes historic unemployment rates by month at the State level.
- National Oceanic and Atmospheric Administration (NOAA) Historic Weather Data: https://www.noaa.gov.  This data includes historic weather conditions (such as high temperature, precipitation, snowfall, and wind speed) by city by day.




