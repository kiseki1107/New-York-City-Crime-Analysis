# New York City Crime Analysis
![Title Image](https://raw.githubusercontent.com/kiseki1107/New-York-City-Crime-Analysis/master/Images/nyc_crime.png)
## Table of Contents
* [Introduction](#Introduction)
  * [Methods](#Methods)
  * [Technologies](#Technologies)
  * [Dependencies](#Dependencies)
* [Data Collection](#DataCollection)
* [Data Cleaning](#DataCleaning)
* [Data Visualization](#DataVisualization)
* [Machine Learning](#MachineLearning)
* [Further Notes](#PresentationSlides)

<a name="Introduction"></a>
## Introduction
The city of New York is one of the most populous city in the United States. Provided publically by New York City agencies, the NYC crime open data can be found [here](https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i). The purpose of this project is to analyze how the crime rate in New York City has changed within a decade since 2006. Additonally, this project seeks to utilize machine learning to predict crime rate occurences based on incident location.

<a name="Methods"></a>
### Methods
* Data Cleaning
* Data Manipulation
* Data Analysis
* Data Visualization
* ETL
* Machine Learning
* Web Application Deployment

<a name="Technologies"></a>
### Technologies
* Python
* HTML5
* Excel
* Flask
* Tableau

<a name="Dependencies"></a>
### Dependencies 
The following python libraries are used in this project:
```python
# For general python dataFrame manipulation, aggregations, and plots.
import warnings
warnings.simplefilter('ignore')
# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
```

<a name="DataCollection"></a>
## Data Collection
[Click here](https://github.com/kiseki1107/New-York-City-Crime-Analysis/blob/master/nycrime_pre-ML/nycrime_age.ipynb) for code reference.

The crime dataset contains roughly 6.5 million NYPD reports/complaints throughout the five boroughs mostly from 2006 to 2017.

Pandas is a wonderful python library when working with dataFrames for data analysis, but it has limitations when it comes to large datasets. With 6.5 million rows of crime data, loading the csv file and displaying the entire dataset on pandas will take some time. This issue can be resolved by loading the dataset into relational SQL servers such as MySQL to query the data. Another solution is to load the data into big data platforms such as Hadoop.

<a name="DataCleaning"></a>
## Data Cleaning
[Click here](https://github.com/kiseki1107/New-York-City-Crime-Analysis/blob/master/nycrime_pre-ML/nycrime_5mil.ipynb) for code reference.

To clean up the large crime data, the dataset was filtered out within three categories:

1. New York Police Department (NYPD) jurisdiction only

![jurisdiction image](https://raw.githubusercontent.com/kiseki1107/New-York-City-Crime-Analysis/master/Images/NYPD_filter.png)

2. Dates of crime occurences strictly from 2006 to 2017

The dataset provides the dates in the form of strings, so the strings must be converted into datetime data types.

![date image](https://raw.githubusercontent.com/kiseki1107/New-York-City-Crime-Analysis/master/Images/date_filter.png)

3. Proper age groups.

The age groups were defined for the age of crime victims and suspects. The NYC crime dataset includes complaints not only by individuals but also by large groups of people such as businesses, residents, and communities. There are also numbers within the age data that did not make sense, so, for this reason, the age groups were chosen within the lifespan of an individual. The 'Unknown' was also selected due to the fact that, sometimes, reported crimes do not document or even know the age of the victim/suspect.

![age image](https://raw.githubusercontent.com/kiseki1107/New-York-City-Crime-Analysis/master/Images/age_filter.png)

Additionally, further cleaning was performed on the NYC crime data to make the data more coherent and accessible. These include dropping unnecessary columns, renaming short-handed nomenclature into more comprehensible column names, and consolidating identical crime types.

![same crime](https://raw.githubusercontent.com/kiseki1107/New-York-City-Crime-Analysis/master/Images/similar_crime.png)

The above image is an example of converting similar crimes such as "CONSPIRACY 2, 1", "CONSPIRACY, 4, 3", and "CONSPIRACY 6, 5" into simply, "CONSPIRACY".

<a name="DataVisualization"></a>
## Data Visualization

The following visualizations are created with [Tableau](https://public.tableau.com/en-us/s/). These visualizations for the NYC crime data can also be viewed [here](https://public.tableau.com/profile/clarence.li#!/vizhome/nycrime/TotalCrime_OverTime).

![crime over time](https://raw.githubusercontent.com/kiseki1107/New-York-City-Crime-Analysis/master/Tableau/crime_by_year.png)

The total number of crimes reported over a decade from 2006 to 2017. There is an apparent declining trend over time.

![crime by year](https://raw.githubusercontent.com/kiseki1107/New-York-City-Crime-Analysis/master/Tableau/YearlyCrimesBoro.png)

The total number of crimes reported per year from each of the five boroughs. The declining trend here is less noticeable but there is a falling pattern. Also, note the great difference between crimes reported in Brooklyn versus crimes reported in Staten Island.  

![crime by month](https://raw.githubusercontent.com/kiseki1107/New-York-City-Crime-Analysis/master/Tableau/CrimesMonth.png)

Crimes reported per month displays seasonal crime patterns where crimes are more frequent during the summer, and less frequent during the winter.

![crime type by boro](https://raw.githubusercontent.com/kiseki1107/New-York-City-Crime-Analysis/master/Tableau/crime_level_by_boro.png)

A more descriptive visualization of the level of crimes committed by borough.

![crime suspect](https://raw.githubusercontent.com/kiseki1107/New-York-City-Crime-Analysis/master/Tableau/suspect_crime_data.png)

A detailed demographic visualization of reported perpetrators.

![crime victim](https://raw.githubusercontent.com/kiseki1107/New-York-City-Crime-Analysis/master/Tableau/victim_crime_data.png)

A detailed demographic visualization of reported victims.

![top crime](https://raw.githubusercontent.com/kiseki1107/New-York-City-Crime-Analysis/master/Tableau/top%20offense.png)

The top five types of crimes reported in New York City with larceny and theft being the most committed criminal offense.

For additional and more interactive visualizations, visit the project's tableau link [here](https://public.tableau.com/profile/clarence.li#!/vizhome/nycrime/TotalCrime_OverTime).

<a name="MachineLearning"></a>
## Machine Learning

<a name="PresentationSlides"></a>
## Further Notes
More descriptive and visual information can be found in the presentation slides provided [here](https://github.com/kiseki1107/New-York-City-Crime-Analysis/blob/master/CrimeProject.pdf).
