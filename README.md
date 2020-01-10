# FULL STACK FRAMEWORKS


## My Fourth Milestone Project

Throughout this project I will be using the Technologies that I have learnt so far from Code Institue.
This project will consist of HTML5 in Jinja format, CSS3, JQuery, JavaScript, Python/Django(Frameworks) and Sqlite.
I will be using Travis for Test and also Deployment Technologies like Heroku and AWS3(Images)

The site designed was an online ecommerce auction based app that can earn money for the owner.
User can learn and know about the artefact before biding or purchasing.
You have to be registered to place a bid.

Registered user are allowed to either wait until auction ends or buy product directly.
Winnner is decided when bid has closed!

All databases used was stored and retrived in the backend via sqlite3.
I have decided to follow the project requirements provided in brief.

## UX

The UX for this project is easy and understandable. It is mainly an ecommerce web based application that functions perfectly. 
Navigations are quite easy and smooth for users. The application is intuitive to use and has information on it presented well.
There is a search input box that allows user to narrow/navigate thier search through the application. 
The web application allows user to create, read(view), edit(update) and make payment without any interference.

As a user I want to be able to buy or get an expensive artefacts at an affordable price.

The data schema used throughout the form/submit implement some of the CRUD rule perfectly. 
The images used are are stored in a S3 Bucket to display correctly across every web platform.

The colour scheme was very simple and makes the site quite clear and readable enough for users.
Fonts sizes are also considered for good readability.
The site also has some interactivity functions but minimal.
This application is very easy for a user to manipulate and understand.


## Features 

* Navbar - Materialize was used for quick production of modern CSS and use of their predefinded classes.

* Alert Messages - Used to inform user of interaction on the app. 

* Images - Flask werkzeug was used to allow user attach image files. Images used are acquired via google.

* Button - Was used to allow users actions on application.

* Font Awesome -  Icons was used to improve the UX for each logo when viewed by a user/visitor.

* Forms/Search Bar - Bootstrap and Django Forms was helpful and usable in Jinja templates to allow app functions.

* Wireframing- I just did some mock ups on balsamiq of how the site generally should look and feel. and I attach this to each html as a png file.


### Possible feature to implement 

* User Profile - Try to add ability for a user to view profile section
* Reviews - Try to allow user leave a review on purchased/ bided product
* Checkout - Allow the use of basket checkout should incase user bid more than one item.


### Getting Started

The website is built using **HTML5**, **CSS3**, **JavaScript and JQuery** for interactivity, **Python**, **Bootstrap** frameworks, **Django** frameworks

### Prerequisites

The site is fully functional without any local files needed to be downloaded all frameworks and scripts
used are loaded via an approved CDN. Before deployment the site was tested on several browsers and devices.
This site is supported on all browsers. Check below for tested devices and browsers.

# [Live Demo Here](https://denny-auctionsite.herokuapp.com/home/)

### External sites used 

* [Bootstrap](https://getbootstrap.com/) - The web framework used 
* [W3 Schools](https://www.w3schools.com/html/default.asp) - Help & tips 
* [Stackoverflow](https://stackoverflow.com/) - Help & tips
* [Django](https://www.djangoproject.com/) -Help & tips
* [Fontawesome](https://favicon.io/) - Fontawesome
* [Colors](https://coolors.co/) - Colours
* [Stripe JS](hhttps://stripe.com/ie) - Stripe JS

### Frameworks/API used 

* [Materialize 0.100.2](https://materializecss.com/)
* [JQuery 3.2.1](https://jquery.com/download/)
* [Stripe](https://stripe.com/ie)
* [Django](https://www.djangoproject.com/)


## Custom Fonts 

I used fonts from **@googleapis CSS 'Cormorant+Upright, Muli, Nunito'** to create difference in headers, paragraph, span and written styles.

## Technologies used


* JQuery & JavaScript - Was used to allow interactivity, file attachment and buttons to function smoothly. [Jquery](https://jquery.com/)

* Sqlite3 - SQLite3 was used to create database and pulled via the backend. [SQLite3](https://www.sqlite.org/)

* Python - Was used to route and call backend database schema from MongoDB.[Python](Lecture Notes)

* Django - Produces very useful packages like Auth, Admin Jinja, Bootstrap Forms,  that allows application to be more functional.[Django](https://www.djangoproject.com/)

* AWS3 BUCKET - Using amazon cloud based server to store images and static files.[Amazon](https://aws.amazon.com/s3/)

* AWS3 IAM - Used to manage access to our S3.[Amazon](https://aws.amazon.com/iam/)

* Heroku - Was used to deploy application to run on any every technological devices. [Heroku](https://heroku.com/)

* Stripe JS - For easy payment when user select paynow option on all screen sizes [Stripe](https://stripe.com/ie)

* Fontawesome - Used to improve UX when viewing the top of the webpage. [Fontawesome](https://fontawesome.com/)

* Bootstrap Classes - To trigger more styles and reduce CSS over-styling [Bootstrap](https://getbootstrap.com/)

* Travis - To test build of website and check if all test are passing [Travis](https://travis-ci.org/)




## Testing

### Travis Testing

Was done through github repositories

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

This then allows us to into our terminal window and install some settings
**Boto3**
**Django Storages**

The **Django Storages** is passed into the installed apps in settings. And once everything looks fine we can **collectstatic**
And your folder and files should display in your ***AWS3 BUCKETS**

Then we have our added images displaying on any webserve.



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