# Zillow Regression Project: Estimating Home Values 
****

## About the Project

### Goals:

* Predict the values of single unit properties using the property data from those with a transaction during the "hot months" of May-August 2017 based on the tax assessed value

* Find where the properties are located 

* Calculate and visualize the distribution of tax rates for each county

**** 

### Deliverables:
* README.md file containing overall project information.
* A Jupyter Notebook Report detailing the pipeline process.
* Report/presentation slides that summarize findings about the drivers of the single unit property values and tax distribution for each county
* Python file `wrangle.py` 

**** 

### Data Dictionary

Feature      | Description   | Data Type
------------ | ------------- | ------------
bedrooms |  Number of bedrooms in home  | int 
bathrooms | Number of bathrooms in home including fractional bathrooms | float
square_feet |  Calculated total finished living area of the home  | int 
county_fips_code |  Federal Information Processing Standard code -  see https://en.wikipedia.org/wiki/FIPS_county_code for more details | int
age |  The difference between the predicting year and the year the principal residence was built  | int
tax_value | The total tax assessed value of the parcel | int
taxes | The total property tax assessed for that assessment year | float
tax_rate | Calculated column by using the property’s assessed value (tax_value) and the taxes paid each year | float

****

### Data Source:
CodeUp MySQL Database 

### Data Science Pipeline Process:

#### Plan
- State project description and goals
- Explore Zillow data using CodeUp's MySQL database 
- Form initial hypotheses and brainstorm ideas

#### 1. Acquire
- Define functions to:
    - Create a SQL url using personal credentials 
    - Acquire Zillow data from MySQL and return as a pandas dataframe
- All functions to acquire data are in [wrangle.py] file available here: (https://github.com/gabrielatijerina/regression-project/blob/main/wrangle.py)
- Summarize initial data to determine how data needs to be prepared and cleaned 

#### 2. Prepare
- Review data and address any missing or erroneous values 
- Define functions to:
    - Clean Zillow data and return as a cleaned pandas DataFrame
    - Split the dataframe into train, validate, test 
    - Scale the data
- All functions to prepare the data are included in [wrangle.py](https://github.com/gabrielatijerina/regression-project/blob/main/wrangle.py)

#### 3. Explore
- Address questions posed in planning and brainstorming and figure out drivers to predict home values
- Create visualizations of variables 
- Run statistical tests (correlation and t-test)
- Summarize key findings and takeaways

#### 4. Model/Evaluate
- Goal: develop a model that performs better than the baseline
- Establish and evaluate a baseline model
- Evaluate model using standard techniques: plotting the residuals, computing the evaluation metrics (SSE, RMSE, and/or MSE), comparing to baseline, plotting y by y-hat
- Choose the best model and test that final model on out-of-sample data
- Summarize performance, interpret, and document results

#### 5. Deliver
- Summarization of findings about the drivers of the single unit property values in a [report summary](link to google slides presentation). 


****

### Instructions for Reproducing Project: 
- To reproduce project, download [wrangle.py](https://github.com/gabrielatijerina/regression-project/blob/main/wrangle.py) and [zillow-report.ipynb](https://github.com/gabrielatijerina/regression-project/blob/main/zillow-report.ipynb) in your working directory and follow the steps from the data science pipeline process above
