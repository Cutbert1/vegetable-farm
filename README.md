
# Vegetable Farm
## Introduction
#### Project Description
 Project is a vegetable sales system to enable farmers sell vegetable produce. Currently there are thirteen different vegetables types being cultivated on this farm (cabbage, carrot, mushroom, broccoli, cauliflower, avocado, asparagus, aubergine, tomato, cucumber, spinach, parsnip and onion), hence ready for sell in boxes. Users are expected to use this system to purchase any vegetables of their choice available for sale. 
Famer can also use the system to understand total daily sales at the end of each market day.


  [Live version of my project, Vegetable Farm is here](https://vegetable-farm-d2f6bd1576d7.herokuapp.com/)

  ![deployed app](./assets/readme-images/deployed%20app.jpg)
#### User Demographic
Vegetable farm data automation can be used by small to medium size vegetable farmers 
#### How to Use
Vegetable farm data automation is based on gathering statistical data used to improve farmers harvest forecast for longer vegetable shelf life.

Step 1. Run the program (python3 run.py)

Step 2. Enter trade data, collection of 13 numeric integers separated with commas

Step 3. Hit enter to run the program

Step 4. Trade worksheet auto Update

Step 5. Excess worksheet auto Update

Step 6. Harvest worksheet auto Update

Step 7. Print harvest forecast on terminal for next day


## Design
Lucid Chart to demonstrate development flow

![lucid chart](./assets/readme-images/lucidchart.jpg)
## Features
### Existing Features
#### Error handling:

      * Input must be numeric integers

      * Input must be collection of 13 numeric integers separated with commas

* Trade worksheet updated when valid record is entered

* Excess calculated and worksheet updated

* Harvest forecast calculated and worksheet updated

* Next day harvest forecast printed to terminal

### Future Features

* Forecast harvest numbers for a longer period and seasons, e.g. summer, 
  Christmas etc using average trade, harvest and excess data for several weeks.

* Convert vegetables to be weighed in tonnes  

## Data Model
Google sheet containing three worksheets (trade, excess and harvest)  was used with thirteen columns. The trade and excess worksheet contains nine rows of data while the harvest worksheet contains ten rows of data.
Excess worksheet represents the subtraction of trade data from harvest data which is achieved by using the function calculate_excess_data parsing trade_row. 
Harvest forecast is the average  trade for last week (7 days) and a markup of 20%.


## Validation Testing
Manually tested this project by passing the code through a [PEP8 Python Linter](https://pep8ci.herokuapp.com/) and confirmed there are no Warning or Error.

![PEP8 manual test](./assets/readme-images/manual-test.jpg)

### Features Testing
 Tested on my local terminal and code institute Heroku terminal after deployment
|Key Features|   User Value   |Functionality Test|Outcome|
|:------------|:----------------|:-------------|:------------|
|Input must be numeric integers|Ensure user enters integers with no alpha or alphanumeric entries|Enter 13 trade data with alphanumeric entries|Invalid data error message ![Integer](./assets/readme-images/Integer.jpg)|
|Input must be 13 digits separated with commas|Ensure user enters the correct number of data to match variety of vegetable on the farm|Enter integers that are not equal to 13 entries|Invalid data error message ![values](./assets/readme-images/numbeofvalues.jpg)|
|Trade worksheet updated when valid data is entered|Automatically update trade worksheet to with to match details entered for each vegetable|Enter valid data: 13 integers separated with commas|Valid data message printed on terminal and updates worksheet ![trade](./assets/readme-images/trade.jpg) ![trade worksheet](./assets/readme-images/tradews.jpg)|
|Calculated excess and updated worksheet|Automatically calculate excess by subtracting trade from harvest and update worksheet |Enter valid data: 13 collection of integers separated with commas|Excess progression tasks  printed on terminal and excess worksheet updated ![excess](./assets/readme-images/excess.jpg) ![excessws](./assets/readme-images/excessws.jpg)|
|Harvest with 20% forecast  calculated and worksheet updated|Automatically calculate average harvest with 20% markup |Enter valid data: 13 collection of integers separated with commas|Harvest progression tasks printed on terminal and harvest worksheet updated ![harvest](./assets/readme-images/harvest.jpg) ![harvestws](./assets/readme-images/excessws.jpg)|
|Print vegetable types and corresponding next day harvest forecast on terminal|Print next day vegetable harvest numbers on terminal|Enter valid data: 13 collection of integers separated with comma|Vegetable types and corresponding next day harvest forecast printed on terminal ![next day](./assets/readme-images/nextday.jpg)|

## Technologies Used

[Heroku](https://id.heroku.com/login)

[Google Sheet](https://docs.google.com/spreadsheets)

### Languages Used
[Python](https://en.wikipedia.org/wiki/Python_(programming_language))
## Bugs
#### Bugs Resolved
* For get_last_week_trade function column count, initially used range(0, 12) to pull last 7 days trade data for 13 vegetable columns thinking that function works just lists zero index. However this was not pulling trade data for all 13 columns. 
It was fixed by using range (1, 14)

#### Bugs Unresolved
There are no unresolved bug
## Deployment
### Deployment Steps

* To enable project to build, create dependency list on requirement.txt file in workspace using pip3 freeze > requirements.txt command

   ![requirements](./assets/readme-images/requirements.jpg)

* Fork or clone vegetable-farm repository

* Sign into Heroku and create a new app.

    ![create new app](./assets/readme-images/create%20app.png)

* Add App name (vegetable-farm) and choose region (Europe)
  
* Go to settings tab to add Config Var

   ![settings](./assets/readme-images/settings.png)
      
* Add credential json KEY and VALUE

   ![credential](./assets/readme-images/configvars.jpg)

* Add another config Var to set KEY as PORT and VALUE as 8000

   ![port](./assets/readme-images/port.jpg)

* Go to Deploy tab to continue deployment

   ![deploy](./assets/readme-images/deploy.png)

* Link Heroku App to GitHub repository

   ![link](./assets/readme-images/link.jpg)

* Search for GitHub repository (vegetable-farm)

* Click on deploy branch

  ![deploy branch](./assets/readme-images/deploy%20branch.jpg)

## Credits
### Codes
Code Institute [Love Sandwiches Tutorial](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/tree/master/02-accessing-user-data/05-updating-our-sales-worksheet)
### Tutorials
* Code Institute Python Essentials

* [stackoverflow](https://stackoverflow.com/questions/23739224/empty-heading-warning-on-html5-validation)

* Tutor Support 









