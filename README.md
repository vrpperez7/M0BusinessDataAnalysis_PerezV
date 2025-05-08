### Business Understanding


As a business analyst, Shop Healthy has reached out to me to make an analysis on their "Retail Challenge" program and the stores participating in it. They'd like me to make an analysis that'd prove their company's initiative helps obesity rates in NYC to support promoting program funding in New York City. 
Shop Healthy asks:

### Is Shop Healthy’s Retail Challenge contributing to lower amounts of obese people in New York City's boroughs?

1. Collect CSV data and use Excel to read and filter. <br/>
2. Create pivot tables and graphs using Excel to find potential trends in databases. <br/>
3. Verify findings using Python to clean and confirm. <br/>



![datalifecycle](https://github.com/user-attachments/assets/0ec35c0a-d9d1-40d8-bcff-af3c7258ccd6)




## Data Collection:

I collected data from Shop Healthy’s Retail Challenge from NYC OpenData's Database created by the Department of Health and Mental Hygiene. This included participating stores’ location, boroughs, and year awarded for participating in the program. I was also able to see the requirements, which must be maintained at least a month to be recognized for the challenge. I also collected NYC.gov’s obesity data to find correlations between Shop Healthy's stores and obesity numbers.

## Data Processing:

I filtered Shop Healthy and NYC.gov's data by borough (Manhattan, Bronx, Brooklyn). I then filtered both datasets to display the years of 2013-2022 to have matching dates on both datasets. I also renamed the borough data labeled as New York on Shop Healthy's data to Manhattan after veryfing zip codes for formatting purposes. I compared NYC.gov's number of obese people vs Year and Shop Right's Year Awarded (received an award for participating and maintaining qualifiers for a month) vs Year. <br/>

Store names and boroughs are non-numeric data. <br/>
Number of obese people, years, and years awarded are discrete numeric data. <br/>


## Results & Recommendations:


On Excel, I created line and bar graphs and pivot tables to find trends between the obesity numbers and Shop Healthy data. I used Python to verify the correctness of the maximum, minimum, and totals within NYC.gov and Shop Right's data. I looked at the Obesity vs Year to find if obesity was trending upwards or downwards and I found that obesity numbers fluctuate throughout the years as shown on the maximum and minimum numbers being on a variety of years. I also looked at Year Awarded vs Year to compare years to see if obesity trending downwards related to an uptick in stores participating in Shop Right's Challenge. I was aware that some years, such as 2020, see higher amounts of stores awarded for Shop Healthy's Retail Challenge during the years of lower obesity numbers, but it is not consistent enough for me to claim a correlation. 

<img width="854" alt="Screenshot 2025-05-08 at 10 54 24 AM" src="https://github.com/user-attachments/assets/40bec78b-132a-4851-aa1e-e4b9fc438b60" />


<img width="811" alt="Screenshot 2025-05-08 at 10 54 37 AM" src="https://github.com/user-attachments/assets/9b6db7ce-dd9d-45f1-9389-deb5b3ab9790" />


To answer the business question, it is inconclusive if Shop Right's Retail Challenge lowers the amount of obese people due to a variety of factors that can contribute to obesity rates, and not enough data proving a correlation. <br/>

I recommend some additions to Shop Right's "Retail Challenge" if they would like to make a potential greater impact to obesity rates such as: <br/>
    1. Increase the longetivity of the requirements for recognition. <br/>
    2. Find data of frequently purchased healthy items to further promote and market in other stores in the challenge. <br/>
    3. Include check-ins with stores previously involved with Shop Right to continue a relationship of healthy foods. <br/>

# Conclusion
During this assignment I learned <br/>
- The importance of understanding the domain you're working with. <br/>
- The efficiency in visualizing trends in a chart/table. <br/>
- You can always go back in the data lifecycle and adjust.

# References:
https://data.cityofnewyork.us/Health/Recognized-Shop-Healthy-Stores/ud4g-9x9z/about_data <br/>
https://a816-dohbesp.nyc.gov/IndicatorPublic/data-explorer/overweight/?id=2063#display=summary <br/>

This is a fictitious scenario created by the github author for academic purposes only.
