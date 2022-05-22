# UMBC DATA 606 Data Science Capstone Project
## Exploring Micromobility and Factors in Growth and Success of the Programs
__Spring 2022, Dr. Chaojie Wang__ <br />
__David Fahnestock__ <br />

Video Presentation: https://youtu.be/F80b0GESftU 
PowerPoint: https://github.com/dfdatascience/David_DATA606/blob/main/Presentations/CapstoneSpring2022_PowerPointPresentation-Micromobility.pdf

## Subject Overview
Micromobility is a growing way in cities for the public to travel from place to place quickly and easily.  This includes pedal bicycles, e-bikes, and scooters that are generally made available for small rental fees per trip or through periodic paid passes.  The focus of this project is to explore factors that result in, or can be used to predict, the growth and success of micromobility programs by applying data science techniques.  

The global micromobility market is projected to grow from $44 billion in 2020 to over $214 billion by 2030 [1].  Use of micromobility is not only a healthy way to travel but also can be beneficial to reduce city congestion and pollution from vehicular traffic.  It can also help reshape the way we think about travel in cities.

Many cities in the United States are implementing micromobility programs.  This project focuses on analysis of three large city micromobility programs: (1) Chicago, Illinois; (2) New York City, New York; and (3) San Francisco, California. 

## Research Questions
This project seeks to answer these questions:
- What factors impact usage and growth of micromobility?
- Can machine-learning be used to accurately:
	- Predict growth or usage patterns in micromobility?
	- Identify other cities where micromobility programs would have a high likelihood of success?

## About the Data Used

### Micromobility Usage Data
- New York City: https://ride.citibikenyc.com/system-data 
- Austin, TX: https://data.austintexas.gov/Transportation-and-Mobility/Austin-MetroBike-Trips/tyfh-5r8s 

### Economic and Weather Data
- U.S. Bureau Labor Statistics (BLS) Unemployment data: https://www.bls.gov/bls/unemployment.htm 
- National Oceanic and Atmospheric Administration (NOAA) Historic Weather Data: https://www.noaa.gov

These data sources are generally from governmental programs and directly published for use.  It is expected the total amount of data used throughout the project could be millions of records (trips).

## Unit of Analysis
The analysis focuses at the city level, through analysis of micromobility programs administered in multiple cities.  Additionally, the focus is on cities within the United States for the purpose of this project.

With regard to the underlying data, the lowest level unit of analysis is on the trip detail.  That is, micromobility data is generally published in terms of one record per trip (from point A to point B). Therefore, the general unit of measure would be in terms of the volume of trips. It is expected this project would analyze millions of trips across multiple city micromobility programs.


## What variables/measures do you plan to use in your analysis (variables should be tied to the questions in #3)?
These would include:
- Demographic information of the cities, such as age
- Climate information of the cities, such as average temperature, rainfall, snow
- Unemployment rates of the cities over time and in relation to the respective usage patterns of micromobility
- Wage information for the city, such as average or median salary
- Type of mobility used from the trip data, such as pedal bikes, e-bikes, and scooters

## What kinds of techniques/models do you plan to use (for example, clustering, NLP, ARIMA, etc.)?
Planned techniques include:
- Prior to application of machine learning models, there will be considerable exploratory data analysis (EDA), including basic time series analysis and comparative analysis between different cities micromobility programs.  This will help develop the necessary understanding of the data and potential limitations or strengths that may help inform next steps in applying machine learning.
- K-Nearest Neighbor (KNN) – KNN can be used for time series analysis and forecasting.  Research has been performed on the use of KNN for things like forecasting GDP growth (Jönsson).  KNN might have advantages in forecasting growth of micromobility.
- ARIMA – This model provides unique benefits for forecasting based on time series data.  For example, a research paper utilized ARIMA to help forecast inflation in Ireland (Mehler et al.)
- Random Forest – This has been shown to be beneficial with large datasets for things like predicting stock prices, whereby there are many attributes to be considered (Kumar et al.).
- Naïve Bayes – This is relatively simplistic model that has been found to be useful for prediction in a wide range of areas.  The plan is to use Naïve Bayes as a way to predict whether a micromobility program would be successful by developing targets for what would be considered success (this could be a percentage growth target range).
- Long Short-Term Memory (LSTM) Neural Network – LSTM has been found to be suitable for time series based forecasting.  It was found in research to perform well for stock price prediction and where there are multivariate input (Du et al.).
- Least Squares Support Vector Machine (LS-SVM) – This model has been found to be useful in various forecasting applications.  One research paper found it accurate for the purpose of traffic forecasting (Zhang and Lui).


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
Jönsson, Kristian. "Machine learning and nowcasts of Swedish GDP." Journal of Business Cycle Research 16.2 (2020): 123-134.

<a id="3">[3]</a> 
I. Kumar, K. Dogra, C. Utreja and P. Yadav, "A Comparative Study of Supervised Machine Learning Algorithms for Stock Market Trend Prediction," 2018 Second International Conference on Inventive Communication and Computational Technologies (ICICCT), 2018, pp. 1003-1007, doi: 10.1109/ICICCT.2018.8473214.

<a id="4">[4]</a> 
Meyler, Aidan, Geoff Kenny, and Terry Quinn. "Forecasting Irish inflation using ARIMA models." (1998): 1-48.

<a id="5">[5]</a> 
Zhang, Yang, and Yuncai Liu. "Traffic forecasting using least squares support vector machines." Transportmetrica 5.3 (2009): 193-213.

