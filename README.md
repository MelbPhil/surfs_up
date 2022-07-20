# Surfs_Up
Analyzing weather data with SQLite and SQLAlchemy in preparation for pitching investors on funding a new surf and shake shop in Oahu.

## Overview of Surfs_Up
In determining whether or not the surf and ice cream shop business is sustainable year-round, I reviewed the descriptive statistics for temperatures in Hawaii in the months of June and December. Below are the results of this analysis and suggestions for further research.

## Resources
- Data Sources: hawaii.sqlite
- Python: 3.7.13, Jupyter Notebook
- SQLite
- SQLAlchemy

## Analysis Results
Descriptive statistics for temperatures in Hawaii in the months of June and December:

(_June Statistics_)--(_December Statistics_)

![june_temp_stats](https://user-images.githubusercontent.com/106599446/180037882-496c3973-d067-4cdc-b50e-e245f08506f3.png)
![dec_temp_stats](https://user-images.githubusercontent.com/106599446/180037899-6869dc1f-24ab-434b-b024-bf9d0ee4c4c5.png)

The data in both (_above_) tables start in the year 2010, but ends in June 2017 and December 2016, respectively. The descriptive statistics for temperatures during these periods in Hawaii seem to show a general year-round consistancy. The mean and median temperatures in December (_71 and 71 Degrees F_) are each ~4 degrees lower than they are in June (_74.9 and 75 Degrees F_). The max temperature is 2 degrees lower in December (_83 as compared to 85 in June_). The biggest difference is in the min temperature, which is 8 degrees lower in December (_56_) as compared that of June (_64_).

## Analysis Summary
Although overall this temperature data bodes well for the year-round sustainability of a surf and shake shop in Oahu, it would be prudent to check whether or not the statistics are shifting. (_Are recent years getting hotter or colder in December?_) (_It is possible that the aggregate data that we viewed in this analysis is being skewed by an unusually hot/cold year?_) By viewing the data year by year, we will be better able to determine if this data is indeed reliably predictive of years to come. 

The same logic should be applied to the precipitation data. Should the further analysis that I just suggested uncover that the climate is becoming less predictable, then this would be considered a risky investment.
