# FULL STACK FRAMEWORKS


## My Fourth Milestone Project

Throughout this project I will be using the Technologies that I have learnt so far from Code Institue.
This project will consist of HTML5 mostly in Jinja Templates format, CSS3, JQuery, JavaScript, Python/Django(Frameworks).
Databases used was stored and retrived in the backend via sqlite3. Also Deployment technologies like Heroku and PostgresSQL to store Heroku database were used. 
I will also be using for AWS3 Bucket for staticfiles storages(Images e.t.c.) and Amazon IAM service for security.

The site designed was an online ecommerce auction based only app that can earn money for the owner. 
The site has a great level of authorisation and authentication and will only take bid and payment from registered user.
User can learn more about artefacts before participating in any auctions.

User most wait until auction ends before payment can be made on a won bid. The winner is decided when bid has closed!
Payment is acheived via stripe payment JS.

I have decided to follow the project requirements and idea provided in brief.


## UX

The UX for this project is easy and understandable. It is mainly an ecommerce auction web based application that functions perfectly. 
Navigations are quite easy and smooth for users. The application is intuitive to use and has information on it presented well.
The search box that allows user to narrow/navigate thier search through the application. This search box is only visible for registered user
The web application allows user to create, read(view), edit(update), make payment and delete without any interference.



    - As a user I want to be able to buy or get an expensive artefacts at an affordable price.
    - As a user I want to have control over the app by having a user account.
    - I also want to be able to store and access my information in a profile page.
    - I want to bid from home and have my placed bid stored for me.
    - I also want bid that is saved from homepage to be updated into auctions.
    - I will then like to increase/raise my bid price/amount and let it differ from the last bid price/amount that was entered.
    - If I win a bid I want to be able to make payment with a simple button.
    - After payment is successful, I want to check my bids if product is still available, if not then I can place new bids.
    
    

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



### Possible feature to implement 

* Reviews - Try to allow user leave a review on purchased/ bided product
* Checkout - Allow the use of basket checkout should incase user intend to buy product and not participate in auction.
* Countdown Timer - Add a countdown timer for auctions still ongoing


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



* HTML - Was used with a Jinja Template to display data stored in backend. [HTML]https://djangobook.com/)

* CSS3 - Was used for styling the web app. [CSS3](http://www.css3.info/)

* JQuery & JavaScript - Was used to allow payment, limit time and payment button to function smoothly. [Jquery](https://jquery.com/)

* Sqlite3 - SQLite3 was used to store database and retrieve data via the backend. [SQLite3](https://www.sqlite.org/)

* Python - Was used to route and call backend database schema from MongoDB. [Python](Lecture Notes)

* Django - Produces very useful packages like Auth, Admin Jinja, Bootstrap Forms, Classes and Attributes that can be used to make the application more functional. [Django](https://www.djangoproject.com/)

* AWS3 BUCKET - Using amazon cloud based server to store images and static files.[Amazon](https://aws.amazon.com/s3/)

* AWS3 IAM - Used to manage access to our S3 storages. By providing us with ID and KEY to use.[Amazon](https://aws.amazon.com/iam/)

* Heroku - Was used to deploy application to run on any every technological devices. [Heroku](https://heroku.com/)

* Stripe JS - For easy payment when user select paynow option on all screen sizes [Stripe](https://stripe.com/ie)

* Fontawesome - Used to improve UX when viewing the top of the webpage. [Fontawesome](https://fontawesome.com/)

* Bootstrap Classes - To trigger more styles and reduce CSS over-styling [Bootstrap](https://getbootstrap.com/)

* Travis - To test build of website and check if all test are passing [Travis](https://travis-ci.org/)

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
| Navbar         |    Yes        |     Yes    |
| Search         |    Yes        |     Yes    |
| Forms          |    Yes        |     Yes    |
| Images         |    Yes        |     Yes    |
| BTN            |    Yes        |     Yes    |
| Place Bid      |    Yes        |     Yes    |
| Update Bid     |    Yes        |     Yes    |
| Search Product |    Yes        |     Yes    |
| Search Category|    Yes        |     Yes    |
| Carousel       |    Yes        |  Partially |





|    Tested      |   IE          | Functions  |
| -------------  |:-------------:|  ---------:|
| Navbar         |    Yes        |     Yes    |
| Search         |    Yes        |     Yes    |
| Forms          |    Yes        |     Yes    |
| Images         |    Yes        |     Yes    |
| BTN            |    Yes        |     Yes    |
| Place Bid      |    Yes        |     Yes    |
| Update Bid     |    Yes        |     Yes    |
| Search Product |    Yes        |     Yes    |
| Search Category|    Yes        |     Yes    |
| Carousel       |    Yes        |  Partially |



|    Tested      |   Android     | Functions  |
| -------------  |:-------------:|  ---------:|
| Navbar         |    Yes        |     Yes    |
| Search         |    Yes        |     Yes    |
| Forms          |    Yes        |     Yes    |
| Images         |    Yes        |     Yes    |
| BTN            |    Yes        |     Yes    |
| Place Bid      |    Yes        |     Yes    |
| Update Bid     |    Yes        |     Yes    |
| Search Product |    Yes        |     Yes    |
| Search Category|    Yes        |     Yes    |
| Carousel       |    Yes        |  Partially |





|    Tested      |Samsung S7-S10 | Functions  |
| -------------  |:-------------:|  ---------:|
| Navbar         |    Yes        |     Yes    |
| Search         |    Yes        |     Yes    |
| Forms          |    Yes        |     Yes    |
| Images         |    Yes        |     Yes    |
| BTN            |    Yes        |     Yes    |
| Place Bid      |    Yes        |     Yes    |
| Update Bid     |    Yes        |     Yes    |
| Search Product |    Yes        |     Yes    |
| Search Category|    Yes        |     Yes    |
| Carousel       |    Yes        |  Partially |



|    Tested      |   IPhone      | Functions  |
| -------------  |:-------------:|  ---------:|
| Navbar         |    Yes        |     Yes    |
| Search         |    Yes        |     Yes    |
| Forms          |    Yes        |     Yes    |
| Images         |    Yes        |     Yes    |
| BTN            |    Yes        |     Yes    |
| Place Bid      |    Yes        |     Yes    |
| Update Bid     |    Yes        |     Yes    |
| Search Product |    Yes        |     Yes    |
| Search Category|    Yes        |     Yes    |
| Carousel       |    Yes        |  Partially |




|    Tested      |   Firefox      | Functions |
| -------------  |:-------------:|  ---------:|
| Navbar         |    Yes        |     Yes    |
| Search         |    Yes        |     Yes    |
| Forms          |    Yes        |     Yes    |
| Images         |    Yes        |     Yes    |
| BTN            |    Yes        |     Yes    |
| Place Bid      |    Yes        |     Yes    |
| Update Bid     |    Yes        |     Yes    |
| Search Product |    Yes        |     Yes    |
| Search Category|    Yes        |     Yes    |
| Carousel       |    Yes        |  Partially |





|    Tested      |   Opera       | Functions  |
| -------------  |:-------------:|  ---------:|
| Navbar         |    Yes        |     Yes    |
| Search         |    Yes        |     Yes    |
| Forms          |    Yes        |     Yes    |
| Images         |    Yes        |     Yes    |
| BTN            |    Yes        |     Yes    |
| Place Bid      |    Yes        |     Yes    |
| Update Bid     |    Yes        |     Yes    |
| Search Product |    Yes        |     Yes    |
| Search Category|    Yes        |     Yes    |
| Carousel       |    Yes        |  Partially |




|    Tested      |   Safari      | Functions  |
| -------------  |:-------------:|  ---------:|
| Navbar         |    Yes        |     Yes    |
| Search         |    Yes        |     Yes    |
| Forms          |    Yes        |     Yes    |
| Images         |    Yes        |     Yes    |
| BTN            |    Yes        |     Yes    |
| Place Bid      |    Yes        |     Yes    |
| Update Bid     |    Yes        |     Yes    |
| Search Product |    Yes        |     Yes    |
| Search Category|    Yes        |     Yes    |
| Carousel       |    Yes        |  Partially |





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
Then we run a **migrate** to to update our new **PostgresSQL** database and since this is new in Heroku, alll data imput will be deleted.
Which means we need to **createsuperuser** again and add our new production database is ready. So we can rebuild all our projects again.

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