# CS50 Final Project - cs50-online-shop

The project is a webpage for online shopping for home decoration and accessories. I wanted to make a project like this to expand my knowledge in web development.

Technologies used:

- HTML
- CSS
- Javascript
- flask
- python
- sqlites3

Tools used:
- visual studio 
- MSQL

## How the webpage works?

This is eshopping website. Customer need to register if first time visit for the website or login using username / password to access the homepage. 
In Homepage, custmomers have the choice to select their disered category and then viewing the products.
While viewing the product, they can either go for prduct details ot checkout direclty.

During registration the user needs to enter these fields
- First name
- Last name
- Email
- Username
- Password
THe customer can't move foraward without filling out all the fields.

During checkout the user needs to enter these fields
- First name
- Last name
- Email
- Telephone
- Country
- City
- Address
- Postal code
THe customer can't move foraward without filling out all the fields and after successful checkout order confirmation page will be displayed to the user with the order ID to enable the user to track his/her order

### Routing

Each route checks if the user is authenticated. It means if the user provide correct username and password so he/she will be able to access any page from the website rather than this the user will have to register to the website.

### Sessions

The webpage uses sessions to confirm that user is logged in. Once the user logged in, his/her credentials are checked in if exist in the database and a session is created (and stored in the cookies.

### Database

Database is created to store users details, products, orders and checkout information. 

## Possible improvements
- Add shopping cart and support multi-purchases
- Have administrator account which will be used to add products details and track orders.
- Ability to change the user account details
- Sending Email confirmation upon placinhg a new order
- Support VISA/Mastercard payment.

## How to launch application

1. Make sure that Python 3 is installed.
2. Clone the code: `git clone https://github.com/Abdelhameed88/cs50-online-shop.git`
3. Run command prompt in the folder and run `python -m pip install flask` to install flask
4. Once installed run command `python flask run`
5. In your browser go to `http://localhost:5000/home`
6. You are ready to go!
