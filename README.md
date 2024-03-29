# UMBC DATA 606 Data Science Capstone Project
## Exploring Micromobility and Factors in Growth and Success of the Programs
## Spring 2022, Dr. Chaojie Wang
## David Fahnestock

Video Presentation: <a href='https://youtu.be/XDdARKZQE2w'>Video Link</a><br />
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
This project includes the detail micromobility usage data for each of the three cities [4].  The data is at the micromobility trip level, meaning each row of data represents one micromobility trip from one location to another location in the city. The data includes various elements, including the start and end date/time of each trip, the user's type (member or casual users), and other elements.  This project generally includes analysis of the period from 2019 through 2021, but expands the period in some instances during machine learning.  For the period from 2019 through 2021, there were approximately 90 million rows.

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
The project also uses supplemental economic (unemployment data) and historic weather data.  The source of these data are from the U.S. Bureau Labor Statistics (BLS) and the U.S. National Oceanic and Atmospheric Administration (NOAA) [5].  These data are considered to identify whether those factors also can be used to predict or obtain a better understanding of the features that impact micromobility usage.  Data elements include:

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
| Date |
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

The above general demographic information for each city was used to get a general initial understanding of the cities.  In consideration of this information, the factors of median household income and median age are useful for understanding general information.  However, these data elements do not appear to have specific use for this project given the relatively small period of time of analysis.  That is, these elements are slowly changing attributes of the cities that may be more useful over a long period of time (decades) at a macro-level.  Therefore, these will not be considered for our analysis purposes. 


### Micromobility Usage
See related Jupyter Notebook: https://github.com/dfdatascience/David_DATA606/blob/main/python/01_DATA606-Project-Master-EDA.ipynb

#### Total Usage by City
For the period from January 2019 through January 2022, New York City had the highest volume of trips, which totaled 70 million.  Chicago had 13 million trips and San Francisco had about 7 million trips.

   <img src='https://github.com/dfdatascience/David_DATA606/blob/main/images/eda_totalbycity_Jan2019toJan2022.png' width='50%'>
   
#### Trips by Year
There was a small decrease in usage in 2020.  This could be due to the onset of the Covid 19 pandemic.  It is also evident that there was a significant increase in usage in 2021 that far surpasses both 2019 and 2020.  Finally, San Francisco's usage remained relatively steady throughout the time period.

   <img src='https://github.com/dfdatascience/David_DATA606/blob/main/images/eda_totaltripsbyyear.png' width='50%'>

#### Seasonal Patterns in Usage
Usage was clearly seasonal for both New York and Chicago, and both had significant increases in 2021.  San Francisco is relatively consistent throughout the seasons. 

   <img src='https://github.com/dfdatascience/David_DATA606/blob/main/images/eda_seasonallinechart.png' width='50%'>
   
#### Type of Bikes Used
There was a large number of instances in the data where no type (nulls) was specified (see far left of the chart).  It is also noted that e-bike usage is minimal in New York City but is significant in San Francisco.  From review, New York City offers some e-bikes but it is very minimal at this point.  We note that classic bikes are predominant in New York City.  Due to the high number of nulls in this field, it does not appear it will be useful in our further machine learning work.

   <img src='https://github.com/dfdatascience/David_DATA606/blob/main/images/eda_bytypeofbike.png' width='50%'>
   
#### Types of Users
All three cities have more trips by members (monthly pass holders) than casual riders (day passes).  New York City's usage by members far exceeds casual riders.  San Francisco is nearly even between members and casual riders.

   <img src='https://github.com/dfdatascience/David_DATA606/blob/main/images/eda_bymembertype.png' width='50%'>


### Unemployment Data
See related Jupyter Notebook: https://github.com/dfdatascience/David_DATA606/blob/main/python/02_DATA606-Project-Master-EDA(b)_UnempAndWeather.ipynb

The unemployment data for each of the three related states (Illinois, New York, California) was obtained from the Bureau Labor Statistics website.  The data provides the actual unemployment rates at each state by month.  As can be seen below, there was a sharp spike in unemployment rates around March 2020.  This marks when Covid-19 shutdowns were largely implemented across the country.  As a result, we see the sharp spike in unemployment immediately in March 2020, increasing from about 4 percent to about 16 percent.

In comparing the unemployment chart (bottom) to the micromobility usage chart (top), it is clear that there is no noticeable correlation between this large spike in unemployment and micromobility usage.  Therefore, it does not appear that use of unemployment data, at least for the period of this project's review, will be useful in predicting micromobility usage.


   <img src='https://github.com/dfdatascience/David_DATA606/blob/main/images/eda_seasonallinechart.png' width='50%'>
   
   <img src='https://github.com/dfdatascience/David_DATA606/blob/main/images/eda_unemploymentovertime.png' width='50%'>

### Historic weather data
See related Jupyter Notebook: https://github.com/dfdatascience/David_DATA606/blob/main/python/02_DATA606-Project-Master-EDA(b)_UnempAndWeather.ipynb

In reviewing the high temperatures in each of the cities over the period of 2017 through 2021, it is clear that the temperatures follow a seasonal pattern as would be expected.  San Francisco fluctuates less than Chicago and New York City over the seasons.  

Overall, these patterns in high temperature follow a similar pattern as micromobility usage over the seasons.  The below chart shows the monthly average of the actual daily high temperatures.

   <img src='https://github.com/dfdatascience/David_DATA606/blob/main/images/eda_weatherhightemplinechart.png' width='50%'>
   
Precipitation levels fluctuate significantly in each city.  Chicago has the most snowfall.  San Francisco seems to have minimal precipitation in summers and no snow.  

   <img src='https://github.com/dfdatascience/David_DATA606/blob/main/images/eda_weatherprecipbymonth.png' width='50%'>
   <img src='https://github.com/dfdatascience/David_DATA606/blob/main/images/eda_weathersnowbymonth.png' width='50%'>
   
The below correlation matrix between micromobility usage and the various weather factors shows that there are strong positive correlations between micromobility usage (number of trips and duration) and the high temperature (TMAX).  As expected, there are negative correlations between micromobility usage and precipitation (PRCP), snow(SNWD), and wind (AWND, WSF5)

   <img src='https://github.com/dfdatascience/David_DATA606/blob/main/images/eda_weathertousagecorrelationmatrix.png' width='50%'>

   
## Feature Selection
Based on exploratory data analysis, the following feature determinations were made for consideration during machine learning:

| Feature(s) | To be Used for Machine Learning? | Reasoning |
| --- | --- | --- |
| Median Income Level | No | Changes in Median income occur over long periods of time.  This analysis is for a relatively short period of time.  Perhaps once there are decades of data, this would be suitable. | 
| Subscriber Type, Type of Bike, Age, Gender | No | A considerable portion of the data had nulls for these features or the features did not provide additional useful information for prediction.  Therefore, they will not be reliable for ML. |
| Unemployment Rates | No | The sharp increase in unemployment during the pandemic does not appear to impact micromobility usage.  Including this would likely negatively impact the accuracy of ML models. |
| Trip Date | Yes | The date of trips will be a key element in ML models for time series based predictions. |
| Trip Count and Duration | Yes | Focus will be on Trip count as the target feature for prediction. |
| Weather Conditions | Yes | Weather conditions appear to impact micromobility usage. |



## Machine Learning Models
In identifying appropriate machine learning models, the focus is on models that have been found to work well for time-series based predictions as they are suitable for this project in predicting future micromobility usage and growth. 

Based on review of various machine learning models, these two machine learning models were selected:
* <b>AutoRegressive Integrated Moving Average (ARIMA)</b> – This is an auto-regressive machine learning model that provides unique benefits for forecasting based on time series data.  For example, a research paper utilized ARIMA to effectively forecast inflation in Ireland [2].  Seasonal ARIMA (SARIMA) is a variation that accounts for seasonal patterns.  ARIMA is a univariate time-series analysis model.  
 
* <b>Long Short-Term Memory (LSTM) Neural Network</b> – LSTM uses a recurrent neural network and has been found to be suitable for time series based forecasting.  It was found in research to perform well for stock price prediction and where there are multivariate input [2].  LSTM provides for multi-variate analysis.  This will allow for multiple features to be used in the model to help improve performance of the predictions.


### Application of ARIMA Model
See related Jupyter Notebook: 
https://github.com/dfdatascience/David_DATA606/blob/main/python/04_DATA606-Project-Master-ARIMA.ipynb

In applying the ARIMA Model, we must consider whether there is a seasonal element to our data.  As determined during EDA, we noted strong seasonal patterns for New York City and Chicago.  San Francisco had less of a seasonal pattern.
  
Our target feature for prediction will be the number of micromobility trips.  As ARIMA is a univariate analysis, the only input will be the time (month) and the number of trips

#### Determine Parameters
SARIMA will be used for predicting usage for New York City and Chicago.  We will apply ARIMA and SARIMA to San Francisco.  SARIMA requires 7 elements to train the model:
SARIMA (p,d,q)(P,D,Q)m

* p = Trend autoregression order
* d = Trend difference order
* q = Trend moving average order
* P = Seasonal autoregressive order
* D = Seasonal difference order
* Q = Seasonal moving average order
* m = The number of time steps for a single seasonal period

Below we use Chicago as the example of the process in determining the parameters.  This will describe the process for determining p, d, q, and m.  The seasonal parameters are not illustrated.  The other cities followed a similar process.  

For determining p, the ACF plot is used.  From review of the plot, we will approximate <b>p to be 2</b> as it is the maximum lag with a value in the ACF plot external to the confidence interval shaded in blue.

   <img src='https://github.com/dfdatascience/David_DATA606/blob/main/images/arima01_chicagoacfplot.png' width='50%'>

To determine d, the Dickey-Fuller test was used to test for Stationarity of the dataset.  For stationarity, the p value returned by the Dickey-Fuller test must be <= 0.05.  It was determined <b>d will be 0</b> as p was 5.94e-05 on the first test iteration.

To determine q, the PACF plot was used.  From the plot, we will approximate <b> q to be 2</b> as it is the maximum lag external to the confidence interval shaded in blue.  Additionally, <b>m will be 12</b> which is 12 months as that is when the seasonal pattern repeats.

   <img src='https://github.com/dfdatascience/David_DATA606/blob/main/images/arima02_chicagopacfplot.png' width='50%'>

#### ARIMA Training and Results

Using the parameters for each city, training of the model used the first 24 months of data and testing was done on the remaining 12 months of data for the period from 2019 through 2021.  The performance using this time period was poor.  For example, below shows a plot of the prediction for Chicago.  As can be seen, the prediction in 2021 was not accurate.  

   <img src='https://github.com/dfdatascience/David_DATA606/blob/main/images/arima03_chicagoprelimresults.png' width='50%'>
   
Upon further analysis, it was determined that a larger period of time was necessary to train the model.  Therefore, the time period was expanded back to 2017 through 2021, expanding from a three year to a five year period.  The model performed significantly better with the longer period of time.

For each city, the model was trained on the first 4 years of data and tested on the final year.  The results are shown below.

   <img src='https://github.com/dfdatascience/David_DATA606/blob/main/images/arima04_chicagofinalprediction.png' width='50%'>
   <img src='https://github.com/dfdatascience/David_DATA606/blob/main/images/arima05_nycfinalprediction.png' width='50%'>      
   <img src='https://github.com/dfdatascience/David_DATA606/blob/main/images/arima06_sffinalprediction.png' width='50%'>
  
Based on the Normalized Root Mean Squared Error (NRMSE) to assess performance, we noted the model performed relatively well for Chicago and New York City.  The model did not perform as well for San Francisco.  Of note, for San Francisco, both ARIMA and SARIMA were attempted and neither performed well.  The below for San Francisco represents the results of the SARIMA, which still performed a little better for San Francisco.  The below results represent those for the SARIMA model.

| Rank | City | NRMSE | Notes |
| --- | --- | --- | --- |
| 1 | Chicago | 0.2789 | Seasonal usage with growth in 2021 |
| 2 | New York City | 0.2849 | Similar usage pattern to Chicago |
| 3 | San Francisco | 0.5279 | Less seasonal pattern with unusual spike in usage in early 2020 |


### Application of LSTM Model
See related Jupyter Notebook: https://github.com/dfdatascience/David_DATA606/blob/main/python/05_DATA606-Project-Master-LSTM.ipynb

LSTM uses a recurrent neural network (RNN) and is useful time series multivariate analysis, in contrast with ARIMA which is univariate analysis.

Based on EDA, the following features will be used:
| Feature | Notes |
| --- | ---|
| Date of Trips | Analysis will be done with micromobility usage aggregated by day |
| Weather conditions | Weather conditions from NOAA on the same day within th city, including temperature, precipitation, and wind conditions. |
| Target Feature: Number of Trips | The model will be used to predict the number of trips |


To prepare the data for this model, the micromobility usage data aggregated by day was merged with the NOAA weather data by day.  The final dataframe (example below) was then used to train and test the LSTM model.
      
   <img src='https://github.com/dfdatascience/David_DATA606/blob/main/images/lstm07_dataframe.png' width='50%'>
   
 * AWND = Average Wind Speed
 * PRCP = Amount of precipitation
 * SNWD = Amount of snow
 * TMAX = High Temperature
 * WSF5 = Max 5 second wind speed

#### Training the LSTM Model

Training was done on the first 4 years and testing was on the final year.  This was chosen to be consistent with the training done on the ARIMA model for comparison purposes.  In training, 50 epochs were used for each city.  The below image shows the loss per epoch for each of the three cities.  These follow the expected curve with the loss being reduced with each epoch.

<table><tr>
<td align="center">Chicago<br /><img src='https://github.com/dfdatascience/David_DATA606/blob/main/images/lstm01_chicagoloss.png' width='100%'></td>
<td align="center">NYC<br /><img src='https://github.com/dfdatascience/David_DATA606/blob/main/images/lstm02_nycloss.png' width='100%'></td>
<td align="center">San Francisco<br /><img src='https://github.com/dfdatascience/David_DATA606/blob/main/images/lstm03_sfloss.png' width='100%'></td>
</tr>
</table>

#### LSTM Results

The performance of LSTM far exceeded the performance of ARIMA.  Below shows the prediction for the test portion of the data for each city.  In each, it follows the actual very closely.  
   
<table><tr>
<td align="center">Chicago<br /><img src='https://github.com/dfdatascience/David_DATA606/blob/main/images/lstm04_chicagoprediction.png' width='100%'></td>
<td align="center">NYC<br /><img src='https://github.com/dfdatascience/David_DATA606/blob/main/images/lstm05_nycprediction.png' width='100%'></td>
<td align="center">San Francisco<br /><img src='https://github.com/dfdatascience/David_DATA606/blob/main/images/lstm06_sfprediction.png' width='100%'></td>
</tr>
</table>

Using Normalized Root Mean Squared Error (NRMSE) to evaluate performance, we found the following.  This shows strong performance for all three cities.  

| Rank | City | NRMSE |
| --- | --- | --- |
| 1 | San Francisco | 0.0807 |
| 2 | Chicago | 0.0847 |
| 3 | New York City | 0.1095 |

Based on these results, the following are considerations:
* There is a risk of overfitting.  Additional train/tests could be done to reduce the portion of the data used for training versus testing.  
* The portion used in this case (4 of the 5 years for training and 1 year for testing) was consistent with that used for ARIMA for comparative purposes.  LSTM performed far better than ARIMA.
* LSTM as a multivariate analysis was able to utilize many features for training (primarily weather related) that seem to have contributed to the higher performance of the LSTM model over the ARIMA model.


## Conclusions
In conclusion, through the work on this project, we note the following with regard to the original questions:
- What factors impact usage and growth of micromobility?
	- Past usage can be used to predict future usage.  This was demonstrated through the results of ARIMA and LSTM analysis.
	- Weather conditions are correlated with usage.  Generally, warmer and nicer weather results in higher usage.  This was evident in the better performance in the LSTM model (which was able to factor in weather conditions) as compared to the ARIMA model.
	- Unemployment rates do not appear to significantly impact usage, at least during the period of this project's review.  However, this appears largely due to the Covid-19 pandemic that resulted in a sharp increase in unemployment rates.

- Can machine-learning be used to accurately:
	- Predict growth or usage patterns in micromobility?
		- Yes, application of ARIMA and LSTM have demonstrated that machine learning can be used effectively to predict usage or growth of micromobility.  Note that LSTM's strong performance appears to be related to use of weather-related factors.  Therefore, it should be noted that the ability for long-range forecasts in micromobility usage using similar approaches to this project would require that weather forecasting also be highly accurate far into the future.  This may be a limiting factor.  Future work could expand on the work of this project to identify additional features that would improve the ability to do long-range forecasting.

	- Identify other cities where micromobility programs would have a high likelihood of success?
		- From the scope of the machine learning models applied, it cannot be definitively concluded whether machine learning could accurately identify cities where micromobility programs would be successful.  Certain factors, such as cities that have warmer or nicer climates may be a general indicator that micromobility may be successful.   



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




