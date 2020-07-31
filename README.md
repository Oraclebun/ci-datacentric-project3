# Code Institute Data Centric Development with Python

# Global Community Hiking Trails Reviews

## Project Objectives
Hiking is a favourite past time of mine. Hiking time represents a respite from work, time with nature and it is an activity that heals the mind, body and soul.  This project 
is a dedication to the love of hiking and to allow the global community to share their experience be it in joy or in frustrations of their time spent during 
their hikes.

## UX/UI
### Overview and Colour
The colour chosen for this website is base on nature theme. The navbar is chosen to have a dark green colour to match the image on the parallax.
The colour of the background (the html body) is chosen to be light yellow, to give some colour to the site as well as to make the cards stand out. Yellow is also chosen, to give the site a bright feel. 
The cards are chosen to be white to make the text and content stand out.

### User Stories
1. The user, as a hiking enthusiast, would like to browse trails by countries and location to enable him/her to plan his/her hiking trip on his/her visit to that country.
2. The user should be able to see a directory of all the trails available.
3. The user should be able to search for a specific term in the search bar in directory.
4. The user should be able to register to create a profile on the site.
5. The user should be able to manage his/her profile on the site.
6. The user should be able to post as well as rate the hiking trip, edit and delete his/her comments on the site.
7. The user presumably would want to see the trails sorted by ratings.

### Wireframes
A basic wireframe was drawn with AdobeXD to act as a the scaffold for laying out the website. The wireframe can be found [here](https://github.com/Oraclebun/ci-datacentric-project3/tree/master/documents).

### Features
#### Index/ Home Page
a. Feature that draws the user attention and persuades user to browse the site information.
* The landing page/ index page is a parallax/jumbotron image of a hiking trail that welcomes the user. It has a Call-to-Action heading and a button that links the user to the directory of the trails.  

b. Feature that allow user to easily navigate to other pages in the website.
* At the top of the homepage, there is a nav bar to allow user to click the links to other pages. Each link serving its own function.
* At the bottom of the Home Page, there is a footer that encourages users to download the app in IOS Appstore or Android play store.
* There are also links to the company information and also to social media sites.  

c. Features that inform user of the latest review/comments and also to allow user to quickly access the directory.
* Below it, there is a row of cards to show the latest 3 comments, by the global hiking community. The 3 comments are the most recent comments in all the trails combined.
* Below the row of comments, user is able to browse the hiking trail by countries, sorted by region and then by towns.


#### Directory Page
a. Search feature  
* There is a link in navbar to a directory page. 
* On this page, the users are able to see a search form input and 2 select drop down with checkboxes. The 2 select drop-down checkboxes allow users to filter the trails by route-type or route difficulty.
* If the user keys in an empty string, the search result will return all trails in the database.

#### Top Rated Page
a. Sorting feature  
* After the directory link in the navbar, there is also a "Top Rated" link in the navbar.
* Users are able to see all trails sorted by average community ratings (in descending order). (From 5 stars rated to unrated(0 star)).

#### Register Page
a. User Registration Feature  
* If user clicks on the "Register" link in the navbar, they will be directed to the Register Page.
* Over here, user will see a form to let them register their name, country of origin, e-mail, username, number of tracks completed and upload a profile photo.
* Upon form submit, user will be directed back to the home page and they should see an alert message "Registration Successful" just below the parallax.
* If user use a non-unique username or an invalid e-mail address, user should not be able to register successfully.
* With a non unique username, user will see the error message "User already exists. Please choose another username." flashed out in the form.
* With an invalid e-mail address, user will see the error message "Not a valid e-mail address" flashed out in the form.

#### Login Page
a. User Login Feature  
* The login page is a simple page consisting of a form with just 2 inputs and a submit button.
* The first input required is username.
* The second input required is the user's e-mail address, submitted during the registration process.
* The forms are validatted to reject login if user keys in the wrong username or the wrong e-mail address.

#### Individual Trail Detail pages
a. Feature that allows user to read trail information:
* Every trail document in the collection has its own page.
* The trail page has an image of the trail or an image of the main feature in the trail on the top right of the page.
* Next to the image, there is also an embedded google map showing the trail route.
* At the bottom, there is a bordered rectangle containing the trail description, trail distance, trail route-type, trail elevation, trail difficulty level and finally the average star rating of the trail (rated by the comment owners).  

b. Feature that links user to a comments/reviews form for writing comments/ reviews.  
* Below the bordered rectangle containing the trail details, there is a floating button that allow users to add comments/reviews.  

c. Feature that allows user to read community comments.
* The comments are displayed in rows of cards below the "add comments" button.
* Every comment card has a profile photo, the name of the comment owner, the date posted, the stars rating by the comment owners, the body of the comments, the word tag that describe the trail sightings, the date hiked and the time period taken to hike in hours and minutes.

#### Post and Editting Comments page
a. Feature that facilitates user to write in their reviews/ comments 
* When the add comments floating button is clicked, user will be directed to a forms page that allows them to input their trail reviews and comments and give a rating to the trails.
* This feature is only available if user registers and log in.
* If user does not log in, he/she should not be able to post or edit or delete any comment. But he/she should be able to view all the information and comments/reviews.
b. Post and Edit Comments form features  
* The ratings of the trail are a row of stars. Clicking the stars by order will give the rating of the trail. The stars are arranged from left to right, with the left-most star representing a rating of 1 while the right-most star represents a rating of 5.
For example, when the 3rd star is clicked, users should see 3 stars coloured with orange while the rest is gray. This represents a rating value of 3.
* The form also has a dynamic input for sightings. The user can input a phrase or a short word tag to describe the sightings seen during hiking. For example, if the user wants to key in "Cars" and "Trees", the user needs to key in "Cars" in the first sighting input,
after which he/she has to click the '+' button to add an input to the form. Then he/she will be able to key in the word "Trees" in the second sightings input. To remove the dynamically added input, the user needs to click the '-' button. However the user need to submit 
at least 1 sighting word/phrase to succesfully post his/her comment.

## Technologies Used.
The technologies used for this project are:
1. [Flask (Release 1.1.2)](https://flask.palletsprojects.com/en/1.1.x/)  
Flask is the microweb framework that supports and serves the web applications (services). It provides the logic and controls the database access,
view templates and session management to the client. Flask is written in python and it is the main project requirement.
2. [Python (Release 3.8.3)](https://www.python.org/downloads/release/python-383/)  
Python is the programming language used in Flask.
3. [HTML5](https://html.spec.whatwg.org/)  
HTML is the markup language that structures the webpage documents.
4. [CSS3](https://www.w3.org/TR/2001/WD-css3-roadmap-20010523/)  
CSS is the style sheet language that supports the presentation of document written in HTML.
5. [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)  
Jinja is leveraged by Flask as its template engine. Although HTML is still needed to structure the web documents, Jinja dynamizes the web documents.
6. [Javascript and JQuery](https://developer.oracle.com/sg/javascript/)  
Javascript and Jquery is used primarily to do DOM manipulation and it is the main engine to serve interactivity and event handling to the webpages. 
7. [Materialize](https://materializecss.com/about.html)  
Materialize is a responsive CSS framework library based on Material Design by Google. The template writting process to build this site is eased and hasten with the usage of this library.
8. [Gitpod](https://www.gitpod.io/)  
Gitpod is an online IDE that can be launched in Github. It is used to develope and write the code for this project.
9. [Git and Github](https://github.com/)  
Github is an online hosting service for software development that utilizes Git for version control.
10. [PYMongo Release 3.10.1](https://pymongo.readthedocs.io/en/stable/)  
Pymongo is a Python driver for MongoDB. It is the engine that allows Flask to interface to MongoDB.
11. [PyMODM Release 0.4.3](https://pymodm.readthedocs.io/en/stable/)  
PyMODM is the generic ODM (Object Document Mapper) that works on top of Pymongo and is used to ease data structuring for this project.
12. [WTForms Release 2.3.1](https://wtforms.readthedocs.io/en/2.3.x/)  
WTForms is a form validation and rendering library for Python development. It is used in this project to simplify forms building.
13. [Flask-WTF Release 0.14.3](https://flask-wtf.readthedocs.io/en/stable/)  
Flask-WTF is an integration of Flask and WTF that provides CSRF, file upload, and reCAPTCHA.
14. [Cloudinary](https://cloudinary.com/)
Cloudinary is used for its cloud-based image and video management platform to enhance user experience in this project's profile registration process.
15. [Google Fonts](https://fonts.google.com/)
Google Font Ruluko (sans-serif) is used primarily to style the headings in the HTML documents in this projects.
Google Font Crimson Text (serif font) is used as the content font in the HTML documents in this projects. 
16. [Font Awesome 5](https://fontawesome.com/start)
Font Awesome Icon is used in the footer for Instagram, Pinterest and Github links 

### Database
The database used in the project is MongoDB. MongoDB is a cross platform document oriented database program. It is classified as a NoSQL
(non relational)database that provides a means of storing data in JSON-like format. MongoDB has a fully managed cloud database service called
MongoDB Atlas and this database service is being used in this project.

### Database Structure
A rough ERD diagram to illustrate the data structure is shown in the [here](https://github.com/Oraclebun/ci-datacentric-project3/blob/master/documents/ERD.pdf).
For a detail explaination of the database structure, please refer to database_structure.md in [here](https://github.com/Oraclebun/ci-datacentric-project3/tree/master/documents/Database_structure.md)

## Testing
This project is partially tested using automated testing and fully tested manually. The testing process is detailed [here](https://github.com/Oraclebun/ci-datacentric-project3/Tests.md)

## Deployment
### Running the project locally
This project is build using Gitpod.
The steps to run the project locally are as follows:
1. Install the gitpod extensions for your browser.
2. Sign up for a github account and login.
3. Go to the github repository in this [link](https://github.com/Oraclebun/ci-datacentric-project3)
4. Click on the fork button on the upper right of the 
website just below your navbar profile image. ![Fork Button](/static/image/readme_image/blob/master/Bootcamp-Fork.png?raw=true)
5. You will now be able to see the project in your own repository in your github page.
6. On your own repository, look for this project and click to go into the site.
7. At the top right of your repository