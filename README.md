## UMBC DATA 606 Data Science Capstone Project
## Draft Project Proposal -- Exploring Micromobility and Factors in Growth and Success of the Programs

### What is your issue of interest (provide sufficient background information)?
Micromobility is a growing way in cities for the public to travel from place to place quickly and easily.  This includes pedal bicycles, e-bikes, and scooters that are generally made available for small rental fees per trip or through periodic paid passes.  The focus of this project would be to explore the factors (economic, geographic, weather, demographic) that result in the growth and success of micromobility programs by applying data science techniques.  

Note: This project’s focus is not specifically on the impacts of the Covid-19 pandemic on micromobility, but the pandemic may be one of many various factors that may be applicable to the broader factors explored.   

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
Micromobility data is generally published in terms of one record per trip (from point A to point B).  Therefore, the general unit of measure would be in terms of the volume of trips.  It is expected this project would analyze millions of trips across multiple city micromobility programs.

### What variables/measures do you plan to use in your analysis (variables should be tied to the questions in #3)?
These would include:
- Demographic information of the cities, such as age
- Climate information of the cities, such as average temperature, rainfall, snow
- Unemployment rates of the cities over time and in relation to the respective usage patterns of micromobility
- Wage information for the city, such as average or median salary
- Type of mobility used from the trip data, such as pedal bikes, e-bikes, and scooters

### What kinds of techniques/models do you plan to use (for example, clustering, NLP, ARIMA, etc.)?
Naïve Bayes, Logistic Regression, SVM and Decision Tree.  Beyond ML models, this would also include general time series analysis techniques that can be used to help decipher aspects such as seasonal patterns.

### How do you plan to develop/apply ML and how you evaluate/compare the performance of the models?
For use in predicting the growth or future usage of micromobility in a given city, trying different combinations of features to be used in the model.  Then splitting the micromobility data into a training, test, and validation datasets to determine the accuracy of each different model applied.  In other words, after training each model, run it on the test set and evaluating the accuracy (within a range of bounds) based on the actual usage change.  For example, how accurate did the model predict micromobility usage (number of trips) from one Summer to the next Summer, etc.


### What outcomes do you intend to achieve (better understanding of problems, tools to help solve problems, predictive analytics with practical applications, etc)?
I intend to better understand usage patterns of micromobility and which factors are most relevant to predict usage and the success of micromobility programs.  Ideally, the outcome would help in evaluating and identifying other cities that could benefit most from micromobility programs, and be successful with those programs.

