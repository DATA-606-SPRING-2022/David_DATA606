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
- Performed using Python in a Jupyter Notebook, found in file 'EDA.ipynb' in this folder
- For preliminary review, downloaded the most recent 12 months of data for the period from February 2021 through January 2022
- During this 1 year period, there were approximately 27.6 million trips
- Performed some cleaning of the data.  For example, certain fields had some null values.  These represented a relatively small portion of the total data (about 100 thousand of the 27.6 million records).  These nulls were replaced with 0's (for numeric fields) and "" for string fields.
- There were 1586 different Start Stations from which trips originated

- From review of the number of trips per month over the 12 month period, it is clear that the highest usage occurs in the summer months with the least usage in the winter months:
   <img src='https://github.com/dfdatascience/David_DATA606/blob/main/EDA/nyc_2021tripsbymonth.png?raw=true' width='75%'>

- Usage by Bike Type is dominated by Classic Bikes (not required to be docked) followed by Docked Bikes.  E-Bikes (that have electric motors) represent a miniscule portion of usage.  This appears to be due to the very limited number of e-bikes available.  From some online resources, it indicated e-bikes 250 e-bikes were introduced in early 2020.  Overall: 
    - classic_bike: 18,432,181 trips
	- docked_bike:   9,184,134 trips
	- electric_bike:       507 trips


- Usage by Member Type is predominately members rather than those who are casual, meaning they pay for each trip without joining:

   <img src='https://github.com/dfdatascience/David_DATA606/blob/main/EDA/nyc_2021tripsbymembertype.png?raw=true' width='75%'>


### Next Steps
This was just a preliminary exploratory analysis to get started and get some initial understanding of the data for the largest city (NYC).  The analysis will be expanded significantly from here, including:
- The time period will be expanded significantly from this single year period.  That is, the analysis will expand to at least 3 years of data.  Assuming the volume is consistent with this preliminary review, that will amount to about 80 million records just for NYC.
- I will be looking to include at least 3 other micromobility programs for other cities.  Depending on the types of data elements tracked by each different city, this could present challenges in being able to have consistent features for analysis and for applying machine learning modeling for prediction.
- Demographic data for each city reviewed will also be analyzed.  For example, this could include the average age, income level, population size, etc.
- Other data related to economic conditions (such as unemployment rates) will also be obtained and analyzed in conjunction with the micromobility data.
 





