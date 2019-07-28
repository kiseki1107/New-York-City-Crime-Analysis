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

NYPD jurisdiction only,

![jurisdiction image](https://raw.githubusercontent.com/kiseki1107/New-York-City-Crime-Analysis/master/Images/NYPD_filter.png)

dates of crime occurences strictly from 2006 to 2017,

`Note: the dataset provides the dates in the form of strings, so the strings must be converted into datetime data types.` 

![date image](https://raw.githubusercontent.com/kiseki1107/New-York-City-Crime-Analysis/master/Images/date_filter.png)

and proper age groups.

``Note: the age groups were defined for the age of crime victims and suspects. The NYC crime dataset includes complaints not only by individuals but also by large groups of people such as businesses, residents, and communities. There are also numbers within the age data that did not make sense, so, for this reason, the age groups were chosen within the lifespan of an individual. The 'Unknown' was also selected due to the fact that, sometimes, reported crimes do not document or even know the age of the victim/suspect.``

![age image](https://raw.githubusercontent.com/kiseki1107/New-York-City-Crime-Analysis/master/Images/age_filter.png)
![age image 2](https://raw.githubusercontent.com/kiseki1107/New-York-City-Crime-Analysis/master/Images/age_filter_2.png)

dropping unnecessary columns

renaming short-handed nomenclature into more proper column names

consolidating similar crime types

![same crime](https://raw.githubusercontent.com/kiseki1107/New-York-City-Crime-Analysis/master/Images/similar_crime.png)
reverse geocoding

<a name="DataVisualization"></a>
## Data Visualization

<a name="MachineLearning"></a>
## Machine Learning

<a name="PresentationSlides"></a>
## Further Notes
More descriptive and visual information can be found in the presentation slides provided [here](https://github.com/kiseki1107/New-York-City-Crime-Analysis/blob/master/CrimeProject.pdf).
