# UMBC DATA 606 Data Science Capstone Project
## Exploring Micromobility and Factors in Growth and Success of the Programs
## Spring 2022, Dr. Chaojie Wang
## David Fahnestock

Video Presentation: <a href='https://youtu.be/F80b0GESftU'>Video Link</a><br />
PowerPoint: <a href='https://github.com/dfdatascience/David_DATA606/blob/main/Presentations/CapstoneSpring2022_PowerPointPresentation-Micromobility.pdf'>Slides</a><br />

## Subject Overview
Micromobility is a growing way in cities for the public to travel from place to place quickly and easily.  This includes pedal bicycles, e-bikes, and scooters that are generally made available for small rental fees per trip or through periodic paid passes.  The global micromobility market is projected to grow from $44 billion in 2020 to over $214 billion by 2030 [3].  

Use of micromobility is not only a healthy way to travel but also can be beneficial to reduce city congestion and pollution from vehicular traffic.  It can also help reshape the way we think about travel in cities.  Many cities in the United States are implementing micromobility programs.  This project focuses on analysis of three large city micromobility programs: (1) Chicago, Illinois; (2) New York City, New York; and (3) San Francisco, California. 

The focus of this project is to explore factors that result in, or can be used to predict, the growth and success of micromobility programs by applying data science techniques.  The intent of this project is to better understand usage patterns of micromobility and which factors are most relevant to predict usage, growth, and the success of micromobility programs.  Ideally, the research results of this project could help in determining methods to evaluate and identify other cities that could benefit from micromobility programs.


## Research Questions
This project seeks to answer these questions:
- What factors impact usage and growth of micromobility?
- Can machine-learning be used to accurately:
	- Predict growth or usage patterns in micromobility?
	- Identify other cities where micromobility programs would have a high likelihood of success?

## About the Data Used

### Micromobility Usage Data
This project includes the detail micromobility usage data for each of the three cities [4].  The data is at the micromobility trip level, meaning each row of data represents one micromobility trip from one location to another location in the city. The data includes various elements, including the start and end date/time of each trip, the user's type (member or casual users), and other elements.  This project generally includes analysis of the period from 2019 through 2021, but expands the period in some instances during machine learning.  For the period from 2019 through 2021, there were over 90 million rows.

Data elements provided in the data include:
<table>
<tr><th>Standard Data Fields</th><th>Additional Data Fields (not always present)</th></tr>
<tr valign='top'><td>

| Field | 
| --- |
| Date/Time of Departure |
| Departure Station |
| Date/Time of Arrival at Destination |
| Destination Station |
| Type of Transport (docked bike, undocked bike, e-bike) |
| Type of Customer (daily, monthly pass) |

</td><td>
	
| Field | 
| --- |
| Departure Geocoordinates |
| Destination Geocoordinates |
| Gender |
| Year of Birth |

</td></tr> </table>

It is noted that the additional fields noted above are not always present in the data.  It was also found that some cities tracked the fields during a portion of the period analyzed but not the entire period.  These factors reduce the usefulness of these features for analysis purposes.

Derived fields were also calculated to be used for analysis purposes.  These allow for the trips to be grouped in different time dimensions.

| Derived Data Fields | 
| --- |
| Duration of Trip |
| Day of Trip |
| Month of Trip |
| Year of Trip |

### Historic Economic and Weather Data
The project also uses supplemental economic (unemployment data) and historic weather data.  The source of these data are from the U.S. Bureau Labor Statistics (BLS) and the U.S. National Oceanic and Atmospheric Administration (NOAA) [5].  These data are considered to identify whether those factors also contain useful features that can be used to predict or obtain a better understanding of the features that impact micromobility usage.  Data elements include:

<table>
<tr><th>Unemployment Data</th><th>NOAA Daily Historic Weather Data</th></tr>
<tr valign='top'><td>

| Field | 
| --- |
| State |
| Year |
| Month |
| Unemployment Rate |

</td><td>
	
| Field | 
| --- |
| City |
| High Temperature |
| Average and Peak 5 second Wind Speed|
| Precipitation and Snow Amounts |

</td></tr> </table>

These data sources are direct from the city websites (for usage data) or from governmental programs (unemployment and weather).  This helps ensure that the data are from reputable sources and are reliable.

## Unit of Analysis
The analysis focuses at the city level, through analysis of micromobility programs administered in multiple cities.  For this project, the focus is on cities within the United States for the purpose of this project.  However, the techniques used throughout this project could also be applied more globally to micromobility programs in other countries.

With regard to the underlying data, the lowest level unit of measure is on the trip detail.  That is, micromobility data is generally published in terms of one record per trip (from point A to point B). Therefore, the general unit of measure would be in terms of the volume of trips. 

## Research Process
This project follows this general research process
1. Obtain and Clean Micromobility Data for Multiple Cities
2. Perform Exploratory Data Analysis
3. Identify Key Features
4. Train and test machine learning models to predict usage and growth
5. Evaluate accuracy and develop conclusions

Python, with use of Jupyter Notebooks, was used significantly throughout all stages of the project.

## Data Cleansing and Preparation Challenges
This project included significant data cleaning and preparation challenges.  In general, each city publishes micromobility usage in monthly flat files.  Key challenges included:

* Merging data from different time periods
* Field layout changes within each city over time
* Cities each track different data elements
* Significant number of nulls in data fields impacting usefulness
* Joining disparate datasets (for example, micromobility data with weather data)
* Sheer volume of data, resulting in long processing times, and exceedingly high demands on computer resources

To help overcome these challenges, various helper functions were implemented.  Also, after exploratory data analysis, data was further pre-aggregated with only the features selected.

See Jupyter Notebook used for data cleaning and preparation: 
https://github.com/dfdatascience/David_DATA606/blob/main/python/03_DATA606-Project-Master-CleanForML.ipynb



## Exploratory Data Analysis

### Overview of City Demographics

| Metric | Chicago | New York City | San Francisco |
| --- | --- | --- | --- |
| Population (2020) | 2,746,388 | 8,804,190 | 873,965 |
| Median Household Income | $62,097 | $67,046 | $119,136 |
| Median Age | 34.8 | 36.9 | 38.3 |

Source: census.gov

The above general demographic information for each city was used to get a general initial understanding of the cities.  In consideration of this information, the factors of median household income and median age are useful for understanding general information.  However, these data elements do not appear to have specific use for this project given the relatively small period of time of analysis.  That is, these elements are slowly changing attributes of the cities that may be more useful over a long period of time (decades) at a macro-level.  Therefore, these will note be considered for our analysis purposes. 


### Micromobility Usage
See related Jupyter Notebook: https://github.com/dfdatascience/David_DATA606/blob/main/python/01_DATA606-Project-Master-EDA.ipynb

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


### Unemployment and Historic Weather Data
See related Jupyter Notebook: https://github.com/dfdatascience/David_DATA606/blob/main/python/02_DATA606-Project-Master-EDA(b)_UnempAndWeather.ipynb




## Feature Selection
Based on exploratory data analysis, the following feature determinations were made for consideration during machine learning:




## Machine Learning Models
In identifying appropriate machine learning models, the focus is on models that have been found to work well for time-series based predictions as they are suitable for this project in predicting future micromobility usage and growth. 

Based on review of various machine learning models, these two machine learning models were selected:
1. ARIMA – This is an auto-regressive machine learning model that provides unique benefits for forecasting based on time series data.  For example, a research paper utilized ARIMA to effectively forecast inflation in Ireland [2].  ARIMA is a univariate time-series analysis model.  
 
3. Long Short-Term Memory (LSTM) Neural Network – LSTM uses a recurrent neural network and has been found to be suitable for time series based forecasting.  It was found in research to perform well for stock price prediction and where there are multivariate input [2].  LSTM provides for multi-variate analysis.  This will allow for multiple features to be used in the model to help improve performance of the predictions.

For the purpose of this project, the target feature (what will be predicted) is usage for each city in terms of the number of micromobility trips.



## Conclusions


## References

<a id="1">[1]</a> 
J. Du, Q. Liu, K. Chen and J. Wang, "Forecasting stock prices in two ways based on LSTM neural network," 2019 IEEE 3rd Information Technology, Networking, Electronic and Automation Control Conference (ITNEC), 2019, pp. 1083-1086, doi: 10.1109/ITNEC.2019.8729026.

<a id="2">[2]</a> 
Meyler, Aidan, Geoff Kenny, and Terry Quinn. "Forecasting Irish inflation using ARIMA models." (1998): 1-48.

<a id="3">[3]</a>
"Micromobility Market Statistics 2022-2030", https://www.alliedmarketresearch.com/micro-mobility-market-A11372#:~:text=The%20global%20micromobility%20market%20was,17.4%25%20from%202021%20to%202030. Accessed 15 April 2022.

Data Sources: <br />
<a id="4">[4]</a>
Micromobility Usage Data
- Chicago Bikeshare: https://ride.divvybikes.com/system-data
- New York City Bikeshare: https://ride.citibikenyc.com/system-data
- San Francisco Bikeshare: https://www.lyft.com/bikes/bay-wheels/system-data

<a id="5">[5]</a>
Economic and Weather Data
- U.S. Bureau Labor Statistics (BLS) Unemployment data: https://www.bls.gov/bls/unemployment.htm.  This data includes historic unemployment rates by month at the State level.
- National Oceanic and Atmospheric Administration (NOAA) Historic Weather Data: https://www.noaa.gov.  This data includes historic weather conditions (such as high temperature, precipitation, snowfall, and wind speed) by city by day.




