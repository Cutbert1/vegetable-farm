
# Vegetable Farm
## Introduction
#### Project Description
  Vegetable Farm is a statistical collection project to enable vegetable farmers collect details of daily sales of 13 different vegetables being cultivated on a farm (cabbage, carrot, mushroom, broccoli, cauliflower, avocado, asparagus, aubergine, tomato, cucumber, spinach, pasnip and onion) types. To understand and forecast daily vegetable harvest with reference to daily trade and excess. Excess references amount of each vegetable type sold out with more required to be harvested or more vegetable harvested than what was sold. This will enable the farmer provide fresh vegetable to customers and improved vegetable shelf life. 

  [Here is a live version of my project, Vegetable Farm](https://vegetable-farm-d2f6bd1576d7.herokuapp.com/)

  ![deployed app](./assets/readme-images/deployed%20app.jpg)
#### User Demographic
Vegetable farm data automation can be used by small to medium size vegetable farmers 
#### How to Use
Vegetable farm data automation is based on gathering statistical data used to improve farmers harvest forecast for longer vegetable shelf life.
Step 1. Run the program

Step 2. Enter trade data, 13 values(integers) separated with commas

Step 3. Hit enter to run the program

Step 4. Trade worksheet auto Update

Step 5. Excess worksheet auto Update

Step 6. Harvest worksheet auto Update


## Design
Lucid Chart to demonstrate development flow

![lucid chart](./assets/readme-images/lucidchart.jpg)
## Features
### Existing Features
* #### Error handling:

Input must be integers

Input must be 13 values separated with commas

* Trade worksheet is updated when valid record is entered

* Excess is calculated and worksheet updated

* Harvest and forecast is calculated and worksheet updated

### Future Features
## Validation Testing
Manually tested this project by passing the code through a [PEP8 linter](https://pep8ci.herokuapp.com/) and confirmed there are no Warning or Error.

![PEP8 manual test](./assets/readme-images/Manual-test.jpg)

### Features Testing
 Tested on my local terminal and code institute Heroku terminal after deployment
|Key Features|   User Value   |Functionality Test|Outcome|
|:------------|:----------------|:-------------|:------------|
|Input must be integers|Ensure user enters integers with no alpha or alpahnumeric entries|Enter 13 trade data with alphanumberic emtries|Invalid data error message ![Integer](./assets/readme-images/Integer.jpg)|
|Input must be 13 digits separated with commas|Ensure user enters the correct number of data to match variety of vegetable on the farm|Enter integers that are not equal to 13 entries|Invalid data error message ![values](./assets/readme-images/numbeofvalues.jpg)|
|Trade worksheet updated when valid data is entered|Automatically update trade worksheet to with to match details entered for each vegetable|Enter valid data: 13 integers separated with commas|Valid data message printed on terminal and updates worksheet ![trade](./assets/readme-images/trade.jpg) ![trade worksheet](./assets/readme-images/tradews.jpg)|
|Calculated excess and updated worksheet|Automatically calculate excess by subtracting trade from harvest and update worksheet |Enter valid data: 13 integers separated with commas|Excess progression tasks  printed on terminal and excess worksheet updated ![excess](./assets/readme-images/excess.jpg) ![excessws](./assets/readme-images/excessws.jpg)|
|Harvest with 20% forecast  calculated and worksheet updated|Automatically calculate average harvest with 20% markup |Enter valid data: 13 integers separated with commas|Harvest progression tasks printed on terminal and harvest worksheet updated ![harvest](./assets/readme-images/harvest.jpg) ![harvestws](./assets/readme-images/excessws.jpg)|

## Technologies Used

[Heroku](https://id.heroku.com/login)

[Lucid Chart](https://www.lucidchart.com/)
### Languages Used
[Python](https://en.wikipedia.org/wiki/Python_(programming_language))
## Bugs
#### Bugs Resolved
* For get_last_week_trade function column count, initially used range(0, 12) to pull last 7 days trade data for 13 vegetable columns thinking that function works just lists zero index. However this was not pulling trade data for all 13 columns. 
It was fixed by using range (1, 14)

#### Bugs Unresolved
There are no unresolved bug
## Deployment
## Credits
### Codes
Code Institute [Love Sandwiches project](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/tree/master/02-accessing-user-data/05-updating-our-sales-worksheet)
### Tutorials
* Code Institute Python Essentails

* [stackoverflow](https://stackoverflow.com/questions/23739224/empty-heading-warning-on-html5-validation)

* Tutor Support 









