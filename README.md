# FULL STACK FRAMEWORKS


## My Fourth Milestone Project

Throughout this project I will be using the Technologies that I have learnt so far from Code Institue.
This project will consist of HTML5 mostly in Jinja Templates format, CSS3, JQuery, JavaScript, Python/Django(Frameworks).
Databases used was stored and retrived in the backend via sqlite3. Also Deployment technologies like Heroku and PostgresSQL to store Heroku database were used. 
I will also be using for AWS3 Bucket for staticfiles storages(Images e.t.c.) and Amazon IAM service for security.

The site designed was an online ecommerce auction based only app that can earn money for the owner. 
The site has a great level of authorisation and authentication and will only take bid and payment from registered user.
User can learn more about artefacts before participating in any auctions.

User most wait until auction ends before payment can be made for the last bided price.
Payment is acheived via stripe payment JS.

I have decided to follow the project requirements and an idea provided in brief.


## UX

The UX for this project is easy and understandable. It is mainly an ecommerce auction web based application that functions perfectly. 
Navigations are quite easy and smooth for users. The application is intuitive to use and has information on it presented well.
The search box that allows user to narrow/navigate thier search through the application. This search box is only visible for registered user
The web application allows user to create, read(view), edit(update), make payment and delete without any interference.


    - As a user I want to be able to bid or get an expensive artifacts at an affordable price.
        - I will like to be able to know description and history about each piece of artifacts.
        - I will like to see the products, images, both auction price and real price before I proceed to use.
        
    - As a user I want to have control over my account.
        - I will like to see a button that will allow me sign in or register to use the application.
        - I will want a form to be displayed to me so I can imput my details at registration.
        - I will like the app to store and secure my details, where I can have access to it at anytime.
        - I will like to see a link to my Profile available to me.
        
    - As a registered user I want to have the ability to bid from home and have my placed bid saved.
        - I will like to see an input field and button that will allow me to place a bid.
        - If my bid is placed I will like to be redirected to rest of the auctions.
        - I will like to see the start and time of the bid I placed in auctions.
        
    - As a registered user I want the ability to raise my auction which has been saved from home.
        - While in auctions I want to be able to see an input field and a button that allows me to raise my bid from previous
        - I want a message to inform me if my bid has been updated, if not I should also see a message that it has ended.
        - If the auction is still live I want to see the product in my bids which must be private to me.
        
    - As a registered user I want to be able to monitor my bid and make payment when auction has ended.
        - I want to be able to see a countdown timer that let me know the time left for the auction to end.
        - I want a button that when I click displays a page that takes my payment from me when the auction is won or ends.
        
    - As a user I want to able to see an acknowledgement that I made payment.
    - I also want to confirm in my bids to check if my last bid has been removed from my list of bids.
    - When I'm through placing a bid, I like a link that once I click it will log me out of the application easily.


The data schema used throughout the form/submit implement all of the CRUD rule perfectly. 
The colour scheme was very simple and makes the site quite clear and readable enough for users. 
Fonts sizes are also considered for good readability. The site has a little interactivity functions.
This application is very easy for a user to manipulate and understand.
The Wireframes are done with balsamiq and images are avaialble in a project folder called **wireframes**



## Features 


* Navbar - Bootstrap Navbar allows user to for quickly move around the app with help of bootstrap predefined classes.

* Alert Messages - Allows message returned to user about a bid that has taken effect in the web app. 

* Images - Django ImageField attribute are used to store images in models. Images are hosted on AWS3 Bucket to allow hosting on cloud servers. Images were acquired via google.

* Button - Allows registered user to bid from home. When this button is clicked it will redirect user to auctions. Button in auctions allows user to raise/increase bid.

* Search Box - Search makes it possible to filter search base on product name or artefact category. Search can ony be seen when user is authenticated.

* Forms - Allows user to sign in and sign up. Also allows user to trigger a button actions

* PayButton - Allows user to make payment when auction is over. This button appears when auction is ended

* StripeJS - StripeJS payment used is to take payment from the web app from only an auction winner.

* Profile - Allows user to view thier details when signed into the app.

* CountDown Timer - Allow user to see the timer displayed in ongoing auction. 



### Possible feature to implement 

* Reviews - Try to allow user leave a review on purchased/ bided product
* Checkout - Allow the use of basket checkout should incase user intend to buy product and not participate in auction.


### Getting Started

The website is built using **HTML5**, **CSS3**, **JavaScript and JQuery** for interactivity, **Python**, **Bootstrap**, **Django** frameworks

### Prerequisites

The site is fully functional without any local files needed to be downloaded all frameworks and scripts
used are loaded via an approved CDN. Before deployment the site was tested on several browsers and devices.
This site is supported on all browsers. Check below for tested devices and browsers.

# [Live Demo Here](https://denny-auctionsite.herokuapp.com/home/)

### External sites used 

* [Bootstrap](https://getbootstrap.com/) - A web framework used 
* [W3 Schools](https://www.w3schools.com/html/default.asp) - Help & tips 
* [Stackoverflow](https://stackoverflow.com/) - Help & tips
* [Django](https://www.djangoproject.com/) - The web framework used
* [Fontawesome](https://favicon.io/) - Fontawesome
* [Colors](https://coolors.co/) - Colours
* [Stripe JS](https://stripe.com/ie) - Stripe API used

### Frameworks/API used 

* [Bootstrap 3.3.7](https://getbootstrap.com/docs/3.3/getting-started/)
* [JQuery 3.2.1](https://jquery.com/download/)
* [Stripe](https://stripe.com/ie)
* [Django](https://www.djangoproject.com/)


## Custom Fonts 

I used fonts from **@googleapis CSS 'Cormorant+Upright, Muli, Nunito'** to create difference in headers, paragraph, span and written styles.

## Technologies used


* HTML - Was used with a Jinja Template to display data stored in backend. [HTML](https://djangobook.com/)

* CSS3 - Was used for styling the web app. [CSS3](http://www.css3.info/)

* JQuery & JavaScript - Was used to allow payment, showing countdown and payment button to function smoothly. [Jquery](https://jquery.com/)

* Sqlite3 - SQLite3 was used to store database and retrieve data via the backend. [SQLite3](https://www.sqlite.org/)

* Python - Was used to route and retrieve backend database schema from SQLite3. [Python](Lecture Notes)

* Django - Produces very useful packages like Auth, Admin Jinja, Bootstrap Forms, Classes and Attributes that can be used to make the application more functional. [Django](https://www.djangoproject.com/)

* AWS3 BUCKET - Using amazon cloud based server to store images and static files. [Amazon](https://aws.amazon.com/s3/)

* AWS3 IAM - Used to manage access to our S3 storages. By providing us with ID and KEY to use. [Amazon](https://aws.amazon.com/iam/)

* Heroku - Was used to deploy application to run on any every technological devices. [Heroku](https://heroku.com/)

* Stripe JS - For easy payment when user select paynow option on all screen sizes [Stripe](https://stripe.com/ie)

* Fontawesome - Used to improve UX when viewing the top of the webpage. [Fontawesome](https://fontawesome.com/)

* Bootstrap Classes - To trigger more styles and reduce CSS over-styling. [Bootstrap](https://getbootstrap.com/)

* Travis - To test build of website and check if all test are passing. [Travis](https://travis-ci.org/)

* PostgresSQL - To allow the storage of database in sqlite before it can be used in Heroku as a database. [PostgresSQL](https://www.postgresql.org/) 



## Testing

### Travis Testing

Open the Travis at **travis-ci.org** then click to **sign in with GitHub**. Once you are signed in, locate **settings** at the top right dropdown arrown.
Once you are inside **settings**, you'll see list of all **GitHub repositories**, you then need to find **GitHub repositories** for the specific app and switch it on.
If the repositories has been switched on, then go to top of our page, copy **markdown text** and paste at the bottom of our README.md file. 
After this, create a **.travis.yml** file to configure our travis settings **language, python version, installer, script** into.. 

Then we can **add, commit and push** all our changes to GitHub then we can now check if tests are passing or failing. 
By default Travis is updated along when we push our commits into GitHub  

+ Tested on **Chrome** (Tested in DevOps on all mobile and tablet devices possible for testing.)
+ Tested on **IE**
+ Tested on  **Android**
+ Tested on  **Samsung S6 - S9**
+ Tested on **Iphone**
+ Tested on **Firefox** (Tested in DevOps on all mobile and tablet devices possible for testing.)
+ Tested on **Opera** (Tested in DevOps on all mobile and tablet devices possible for testing.)
+ Tested on **Safari** (Tested in DevOps on all mobile and tablet devices possible for testing.)



|    Tested      |   Chrome      | Functions  |
| -------------  |:-------------:|  ---------:|
|Navbar          |    Yes        |     Yes    |
|Search          |    Yes        |     Yes    |
|Forms           |    Yes        |     Yes    |
|Images          |    Yes        |     Yes    |
|Pay BTN         |    Yes        |     Yes    |
|Place Bid       |    Yes        |     Yes    |
|Update Bid      |    Yes        |     Yes    |
|Search Product  |    Yes        |     Yes    |
|Search Category |    Yes        |     Yes    |
|Carousel        |    Yes        |  Partially |
|CountDown Timer |    Yes        |     Yes    |




|    Tested      |   IE          | Functions  |
| -------------  |:-------------:|  ---------:|
|Navbar          |    Yes        |     Yes    |
|Search          |    Yes        |     Yes    |
|Forms           |    Yes        |     Yes    |
|Images          |    Yes        |     Yes    |
|Pay BTN         |    Yes        |     Yes    |
|Place Bid       |    Yes        |     Yes    |
|Update Bid      |    Yes        |     Yes    |
|Search Product  |    Yes        |     Yes    |
|Search Category |    Yes        |     Yes    |
|Carousel        |    Yes        |  Partially |
|CountDown Timer |    Yes        |     Yes    |




|    Tested      |   Android     | Functions  |
| -------------  |:-------------:|  ---------:|
|Navbar          |    Yes        |     Yes    |
|Search          |    Yes        |     Yes    |
|Forms           |    Yes        |     Yes    |
|Images          |    Yes        |     Yes    |
|Pay BTN         |    Yes        |     Yes    |
|Place Bid       |    Yes        |     Yes    |
|Update Bid      |    Yes        |     Yes    |
|Search Product  |    Yes        |     Yes    |
|Search Category |    Yes        |     Yes    |
|Carousel        |    Yes        |  Partially |
|CountDown Timer |    Yes        |     Yes    |





|    Tested      |Samsung S7-S10 | Functions  |
| -------------  |:-------------:|  ---------:|
|Navbar          |    Yes        |     Yes    |
|Search          |    Yes        |     Yes    |
|Forms           |    Yes        |     Yes    |
|Images          |    Yes        |     Yes    |
|Pay BTN         |    Yes        |     Yes    |
|Place Bid       |    Yes        |     Yes    |
|Update Bid      |    Yes        |     Yes    |
|Search Product  |    Yes        |     Yes    |
|Search Category |    Yes        |     Yes    |
|Carousel        |    Yes        |  Partially |
|CountDown Timer |    Yes        |     Yes    |





|    Tested      |   IPhone      | Functions  |
| -------------  |:-------------:|  ---------:|
|Navbar          |    Yes        |     Yes    |
|Search          |    Yes        |     Yes    |
|Forms           |    Yes        |     Yes    |
|Images          |    Yes        |     Yes    |
|Pay BTN         |    Yes        |     Yes    |
|Place Bid       |    Yes        |     Yes    |
|Update Bid      |    Yes        |     Yes    |
|Search Product  |    Yes        |     Yes    |
|Search Category |    Yes        |     Yes    |
|Carousel        |    Yes        |  Partially |
|CountDown Timer |    Yes        |     Yes    |





|    Tested      |   Firefox      | Functions |
| -------------  |:-------------:|  ---------:|
|Navbar          |    Yes        |     Yes    |
|Search          |    Yes        |     Yes    |
|Forms           |    Yes        |     Yes    |
|Images          |    Yes        |     Yes    |
|Pay BTN         |    Yes        |     Yes    |
|Place Bid       |    Yes        |     Yes    |
|Update Bid      |    Yes        |     Yes    |
|Search Product  |    Yes        |     Yes    |
|Search Category |    Yes        |     Yes    |
|Carousel        |    Yes        |  Partially |
|CountDown Timer |    Yes        |     Yes    |





|    Tested      |   Opera       | Functions  |
| -------------  |:-------------:|  ---------:|
|Navbar          |    Yes        |     Yes    |
|Search          |    Yes        |     Yes    |
|Forms           |    Yes        |     Yes    |
|Images          |    Yes        |     Yes    |
|Pay BTN         |    Yes        |     Yes    |
|Place Bid       |    Yes        |     Yes    |
|Update Bid      |    Yes        |     Yes    |
|Search Product  |    Yes        |     Yes    |
|Search Category |    Yes        |     Yes    |
|Carousel        |    Yes        |  Partially |
|CountDown Timer |    Yes        |     Yes    |





|    Tested      |   Safari      | Functions  |
| -------------  |:-------------:|  ---------:|
|Navbar          |    Yes        |     Yes    |
|Search          |    Yes        |     Yes    |
|Forms           |    Yes        |     Yes    |
|Images          |    Yes        |     Yes    |
|Pay BTN         |    Yes        |     Yes    |
|Place Bid       |    Yes        |     Yes    |
|Update Bid      |    Yes        |     Yes    |
|Search Product  |    Yes        |     Yes    |
|Search Category |    Yes        |     Yes    |
|Carousel        |    Yes        |  Partially |
|CountDown Timer |    Yes        |     Yes    |





## Deployment

### AWS3 Deployment Process

Created a new Amazon account and connect to amazon service **AWS3** account are cloud based serve where 
the project media and staicfiles will be stored unto.
At first, we locate **S3** on amazon service then we create a bucket. While creating the bucket on **S3**,
the note that public access must be all switched off to allow access for users.

Once we've created the bucket, we now can now click on it's properties and enable the **Static Website Hosting** option, 
so it can serve the purpose of hosting our static files, you will need to imput an **index.html** and **error.html** before saving.
Then we go into the created bucket **Permissions** and click into **CORS configuration**, this part already have a prefilled default config,
All that is needed is just to write the default code and save the config.

Then we go into the **bucket policy** to allows access to the contents across all web 
and inside this we will put in here some code including  arn address displayed at the top of the heading.
Then we go into amazon **IAM** to allow identity and access management of our stored files and folder.
In the **IAM** service, we add a new group for our application and then we set the policies to **ALL**
Then it generates a downlaodable zip file containing **ID and KEY** for us to use for the newly added group. 
This **ID and KEY** as to be stored in an environment variable.

This then allows us to into our terminal window and install some settings
**Boto3**
**Django Storages**

The **Django Storages** is passed into the installed apps in settings and also a **custom_storage** file is created to store credentials in environment variable.
And once everything looks fine we can **collectstatic**
And your folder and files should display in your ***AWS3 BUCKETS**



### GitHub Deployment

Created a new repositories on **Github** where the project will be deployed unto at each commit.
At first, use a **git remote** command to link project with new repo.
Then use the **git push -u origin master** command to push codes and every change into new repo

Using the CLI in terminal to call **git init** to start git initialization on the project.
This allows a file/files to be added to the Github repo by calling a **git add** command.
Then any added file/files is being commited with a **git commit -m "commit message"** command.
Afterwards, the file is been pushed with **git push** where Github username + password is required.
Once successful, code will be deployed into your repo and **git status** command should indicate branch tree clean.




### Heroku Deployment

Created a new app on **Heroku** where the app is hosted live.
At first, to allow **Heroku** locate application we login into the CLI using ** heroku login -i** command.
You will be requested to imput username and password for **Heroku** account. 
After which you can request **Heroku Apps** via CLI. 

Knowing the apps you need to pass deployment into then we can use **heroku git:remote -a <app>** 
to allow Git automatically update deployment in Heroku. 
Once this has been remotely passed . 
To host the app unto heroku pass the IP and PORT config to match the route **__main__** config.

To **allow PostgresSQL**, we have to go into our newly created app and click into **resources** inside here you can type **PostgresSQL** 
and add as an add on, it should prompt up on your screen choose the **hobby dev free** and click on **provision**.
Once you allow **PostgresSQL** it will generate a **DATABASE_URL** in the heroku settings.

Now we need to install in production terminal **dj-database-url** and **psycopg2**
Then we run a **migrate** to to update our new **PostgresSQL** database and since this is new in Heroku, all data imputed will be erased.
Which means we need to **createsuperuser** from terminal and add our contents again,
Our new production database is ready. So we can rebuild all our projects again.

To allow git to push to heroku the command **git push heroku master** must be called for a final **push**.
For a succefull and healthy push it is best adviced to have the **requirement.txt** and **Procfile** 
files installed or updated. Most especially for **requirement.txt** file which gave me a lot of challenges,
it requires to be updated along with any installed packages so it can depoly successfully, i.e Flask packages.



### HTML, CSS, JQuery, JavaScript, Python(Django Framework)

All my mark up is **HTML valid**
All my styling is **CSS valid**
All my syntax is **JavaScript syntactically valid**
All my routing, views and urls is **Django valid**

#### Version Used

I use [GitHub](github.com) for version control. Which backup my code incase I encounter a bug or an error that needs urgent fix or restoration. 
I can easily traceback my code on GitHub to changes applied and versions updates.


### Authors

**Dehinde - Shogbanmu** - *Project 4* 



## Credits

### Content 
The images and history used was retrieved from Google
The logos was generated via icon8
The data was retrived from my sqlite3


### Acknowledgements
I received a great inspiration for this project via my mentor, tutors, and slack he was a great help.
* Ali Ashik(Mentor)
* Samantha(Tutor)
* Michael(Tutor)
* Stephen(Tutor)
* Chris(Mentor)
* Friends



[![Build Status](https://travis-ci.org/dennyshow/milestone-project4.svg?branch=master)](https://travis-ci.org/dennyshow/milestone-project4)