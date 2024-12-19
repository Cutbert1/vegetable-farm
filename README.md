
# Vegetable Farm
## Introduction
#### Project Description
 Project is a vegetable sales system to enable farmers sell vegetable produce. Currently there are thirteen different vegetables types being cultivated on this farm (cabbage, carrot, mushroom, broccoli, cauliflower, avocado, asparagus, aubergine, tomato, cucumber, spinach, parsnip and onion), hence ready for sell in boxes. Users are expected to use this system to purchase any vegetables of their choice available for sale. 
Famer can also use the system to understand total daily sales at the end of each market day.


  [Live version of my project, Vegetable Farm is here](https://vegetable-farm-d2f6bd1576d7.herokuapp.com/)

  ![deployed app](./assets/readme-images/deployed%20app.jpg)
#### User Demographic
Vegetable farm produce sales system can be used by small to medium size vegetable farmers 
#### How to Use
Vegetable farm produce sales system is used for easy self-serve vegetable purchase. It can also be used by back office (famer) to understand daily sales, hence facilitate daily farmers vegetable availability planning.

Step 1. Run the program (python3 run.py)

Step 2. From the dispplayed items, enter item number of your choice

Step 3. Hit enter to run the program

Step 4. Enter amount displayed for your selected item

Step 5. Hit enter to run the program

Step 6. If amount entered is not sufficient, program will display remaining amount and request user input

Step 7. If amount entered is greater than produce price program will return balance

Step 8. Hit enter once correct amount is entered

Step 9. Sales worksheet auto update with item and amount 

**Back-Office**
Step 10. Program total amount sold at end of each market day



## Design
Lucid Chart to demonstrate development flow

![lucid chart](./assets/readme-images/lucidchart.jpg)
## Features
### Existing Features
#### Error handling:

      * Input must be item number

      * Input amount must be >= price of vegetable
 
      * Sales worksheet values for total daily sum must be integers or float


### Future Features

* Convert vegetables to be weighed in tonnes for large vegetable farmers 

## Data Model
Google sheet containing one sales worksheet  was used were vegetables names are updated with corresponding purchased value and sum of total amount sold for back office use.


## Validation Testing
Manually tested this project by passing the code through a [PEP8 Python Linter](https://pep8ci.herokuapp.com/) and confirmed there are no Warning or Error.

![PEP8 manual test](./assets/readme-images/manual-test.jpg)

### Features Testing
 Tested on my local terminal and code institute Heroku terminal after deployment
|Key Features|   User Value   |Functionality Test|Outcome|
|:------------|:----------------|:-------------|:------------|
|Input must be item number|Ensure user enter item number matching any of the displayed available vegetables|Enter vegetable_box item number that isn’t displayed |Invalid selection error message ![Ivalid-selection](../vegetable-farm/assets/readme-images/invalidselection.jpg)|
|Input amount must be >= price of vegetable|Ensure amount entered must be greater than or equal to price of vegetable displayed|Enter amount not equal to a greater than price of vegetable displayed|Insufficient payment error message![Insufficient-payment](./assets/readme-images/insufficient.jpg)|
|Return balance when user input amount > price of vegetable displayed|Ensure amount balance is provided to the user when money inserted is > than the price of vegetable|Enter amount > than price of vegetable displayed|Amount balance returned to the user ![Balalnce](./assets/readme-images/balalnce.jpg)|
|Update sales worksheet with name of vegetable purchased and amount|Automatically update sales worksheet |Enter valid vegetable number and sufficient amount for the price of item selected|Sales worksheet progression task printed to terminal and worksheet updated ![sales](./assets/readme-images/sales.jpg) ![salesws](./assets/readme-images/salesws.jpg)|
|Total daily sales calculated and print to terminal for back office use|Automatically calculate total purchase value in real time and print to terminal |Enter valid vegetable number and sufficient amount for the price of item selected|Calculate total purchase value in real time and print to terminal ![total](./assets/readme-images/total.jpg)|

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









