## UMBC DATA 606 Data Science Capstone Project
## Proposal -- Exploring Micromobility and Factors in Growth and Success of the Programs

### What is your issue of interest (provide sufficient background information)?
Micromobility is a growing way in cities for the public to travel from place to place quickly and easily.  This includes pedal bicycles, e-bikes, and scooters that are generally made available for small rental fees per trip or through periodic paid passes.  The focus of this project would be to explore the factors (economic, geographic, weather, demographic) that result in the growth and success of micromobility programs by applying data science techniques.  

*Note: This project’s focus is not specifically on the impacts of the Covid-19 pandemic on micromobility, but the pandemic may be one of many various factors that may be applicable to the broader factors explored.*  

### Why is this issue important to you and/or to others?
Many cities in the United States are implementing micromobility programs, including New York, Washington DC, and Austin, Texas.  It is not only a healthy way to travel but also can be beneficial to reduce city congestion and pollution from vehicular traffic.  It can also help reshape the way we think about travel in cities.

### What questions do you have in mind and would like to answer?
- Are there specific economic/socio-economic factors that impact the usage of micromobility?  Do unemployment rates, poverty rates, crime, and other economic factors have an impact?
- Does geographic location impact the likelihood of success of a micromobility program?   Do cities in warmer climates tend to have higher growth?  Does the terrain (hills, flat) of the area impact usage or success?
- Do demographics have an impact on growth and usage of micromobility?  Is usage higher in areas with younger populations?
- Are there seasonal patterns in the usage of micromobility?  
- Are there differences in usage patterns based on the types of micromobility (pedal bikes vs e-bikes vs scooters)?
- After identifying key features, can growth or usage patterns in micromobility be predicted through machine learning techniques?  Which models perform best?  
- Could machine learning be used to identify other cities where micromobility programs would have a high likelihood of success?


### Where do you get the data to analyze and help answer your questions (creditability of source, quality of data, size of data, attributes of data. etc.)?

Many of the cities with micromobility programs make their usage data publicly available.   For example:
- New York City: https://ride.citibikenyc.com/system-data 
- Austin, TX: https://data.austintexas.gov/Transportation-and-Mobility/Austin-MetroBike-Trips/tyfh-5r8s 
- U.S. Bureau of Transportation Statistics has various resources: https://data.bts.gov/stories/s/fseh-ipec 

The U.S. Bureau Labor Statistics publishes many datasets that could be useful:
- Unemployment data: https://www.bls.gov/bls/unemployment.htm 
- Demographic data: https://www.bls.gov/bls/demographics.htm 
- Wage information: https://www.bls.gov/bls/wages.htm 

The National Weather Service for general climate information: https://www.weather.gov/ 

These data sources are generally from governmental programs and directly published for use.  It is expected the total amount of data used throughout the project could be millions of records (trips).

### What will be your unit of analysis (for example, patient, organization, or country)? Roughly how many units (observations) do you expect to analyze?
The analysis will primarily focus at the city level, through analysis of micromobility programs administered in multiple cities.  The planned focus is on micromobility programs in the United States.  However, if time permits, the analysis may be expanded to compare different countries.

With regard to the underlying data, the lowest level unit of analysis is on the trip detail.  That is, micromobility data is generally published in terms of one record per trip (from point A to point B). Therefore, the general unit of measure would be in terms of the volume of trips. It is expected this project would analyze millions of trips across multiple city micromobility programs.


### What variables/measures do you plan to use in your analysis (variables should be tied to the questions in #3)?
These would include:
- Demographic information of the cities, such as age
- Climate information of the cities, such as average temperature, rainfall, snow
- Unemployment rates of the cities over time and in relation to the respective usage patterns of micromobility
- Wage information for the city, such as average or median salary
- Type of mobility used from the trip data, such as pedal bikes, e-bikes, and scooters

### What kinds of techniques/models do you plan to use (for example, clustering, NLP, ARIMA, etc.)?
Planned techniques include:
- Prior to application of machine learning models, there will be considerable exploratory data analysis (EDA), including basic time series analysis and comparative analysis between different cities micromobility programs.  This will help develop the necessary understanding of the data and potential limitations or strengths that may help inform next steps in applying machine learning.
- K-Nearest Neighbor (KNN) – KNN can be used for time series analysis and forecasting.  Research has been performed on the use of KNN for things like forecasting GDP growth (Jönsson).  KNN might have advantages in forecasting growth of micromobility.
- ARIMA – This model provides unique benefits for forecasting based on time series data.  For example, a research paper utilized ARIMA to help forecast inflation in Ireland (Mehler et al.)
- Random Forest – This has been shown to be beneficial with large datasets for things like predicting stock prices, whereby there are many attributes to be considered (Kumar et al.).
- Naïve Bayes – This is relatively simplistic model that has been found to be useful for prediction in a wide range of areas.  The plan is to use Naïve Bayes as a way to predict whether a micromobility program would be successful by developing targets for what would be considered success (this could be a percentage growth target range).
- Long Short-Term Memory (LSTM) Neural Network – LSTM has been found to be suitable for time series based forecasting.  It was found in research to perform well for stock price prediction and where there are multivariate input (Du et al.).
- Least Squares Support Vector Machine (LS-SVM) – This model has been found to be useful in various forecasting applications.  One research paper found it accurate for the purpose of traffic forecasting (Zhang and Lui).


### How do you plan to develop/apply ML and how you evaluate/compare the performance of the models?
For use in predicting the growth or future usage of micromobility in a given city, trying different combinations of features to be used in the model.  Then splitting the micromobility data into training and test sets to determine the accuracy of each different model applied.  In other words, after training each model, run it on the test set and evaluating the accuracy (within a range of bounds) based on the actual usage change.  For example, how accurate did the model predict micromobility usage (number of trips) from one Summer to the next Summer, etc.  Evaluation of the different models will include various comparisons within a given city's micromobility program (predicting growth within that city), but also comparisons between different cities.  For example, evaluating whether a model trained on one city's data can be accurate at prediction when tested on another city's data.


### What outcomes do you intend to achieve (better understanding of problems, tools to help solve problems, predictive analytics with practical applications, etc)?
I intend to better understand usage patterns of micromobility and which factors are most relevant to predict usage, growth, and the success of micromobility programs.  Ideally, the outcome would help in evaluating and identifying other cities that could benefit most from micromobility programs, and be successful with those programs.


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

