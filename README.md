# Code Institute Data Centric Development with Python

# Global Community Hiking Trails Reviews

## Project Objectives
Hiking is a favourite past time of mine. Hiking time represents a respite from work, time with nature and it is an activity that heals the 
mind, body and soul. Travelling globally to hike is not going to be possible for awhile due to the global pandemic but it is still possible 
to hike locally and often, we may find some undiscovered gems along the way. This project is my dedication to the love of hiking. It is to be 
a platform for the global community to share their experience be it in joy or in frustrations of their time spent during their hikes. 

## Deployed Link
The deployed website can be found [here](https://oraclebun-project3.herokuapp.com/)

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
This project is partially tested using automated testing and fully tested manually. The testing process is detailed [here](https://github.com/Oraclebun/ci-datacentric-project3/blob/master/Tests.md)

## Deployment
### Running the project locally
This project is build using Gitpod.
The steps I went through to run the project locally are as follows:

1. Sign up for a MongoDB Atlas account [here](https://www.mongodb.com/cloud/atlas/register)
2. Follow the steps to creating an Atlas cluster [here](https://docs.atlas.mongodb.com/getting-started/)
3. Install the gitpod extensions for the local machine browser.
4. Sign up for a github account and login.
5. Sign up for a gitpod account and link it to github account.
6. Go to the personal github pages and start a new repository using the [Code Institute Gitpod Full Template](https://github.com/Code-Institute-Org/gitpod-full-template)
7. The project folder will be available on the personal github page repository.
8. At the top right of the personal repository, you will be able to see the green coloured Gitpod button like the picture below:
![Gitpod Button](https://github.com/Oraclebun/ci-datacentric-project3/blob/master/static/image/readme_image/Gitpod_link.png)
9. Click on the Gitpod link to open up the development environment for this project in Gitpod.
10. Once the project has fully loaded in the browser, a Visual Studio Code-like editor with a terminal will be seen.
11. In the terminal, type in the below command to install the dependencies.

```console

$ pip3 -r requirements.txt 

```
12. In the main directory of the gitpod project, an .env file have to be created. In the .env file the following environment variables have to be setup.  
a. MONGO_URI = mongodb+srv://[database_root_username]:[database_root_user_password]@[cluster_name].mongodb.net/[database_name]?retryWrites=true&w=majority  
   The above is just an example mongodb connection string. The string can be found in the mongodb atlas connection in each project folder created.  
b. SECRET_KEY = a random string generated from any random key generator sites  
c. CLOUD_NAME = cloudinary name provided when signed up for cloudinary account.  
d. UPLOAD_PRESET = cloudinary upload preset.   
e. API_SECRET = api secret provided by cloudinary.  
f. API_KEY = api key provided by cloudinary.

13. After setting up the environment variables and installing all dependencies, the database collection need to be setup to ensure 
consistencies in the data. This is done by running the models.py file as below:

```console
$ python3 models.py
```

14. After that, the database need to be populated with the data. This is done by automating the process as below:

```console
$ python3 insert.py
```

15. Finally, run the app on the terminal / command line interface by typing the below into the terminal like so:

```console
$ python3 app.py
```

### Deployment on Heroku
The steps taken to deploy this project on Heroku are as follows:
1. Sign up for Heroku account
2. Install Heroku CLI in the gitpod terminal if it hasn't been installed
3. If Heroku CLI has been installed, type in the below to login Heroku

```console
$ heroku login

```

4. Login Heroku via the opened browser. If browser window is not able to display, open the site in a new window and login heroku.
5. Type in the below to create a heroku app, where `<the_name_of_the_project>` is the name of the project to be deployed.  

```console
$ heroku create <name_of_the_project>

```

6. then create a remote repository by typing in 

```console
$ git remote -v
```

7. Install gunicorn with pip3

```console
$ pip3 install gunicorn
```

8. Create a Procfile with the content "web gunicorn `<name of the project>`:app"
9. Freeze all project dependencies by keying in to the terminal 

```console
$ pip3 freeze --local > requirements.txt 
```
10. commit the project to github again
11. Finally push the project to git as below:

```console
$ git push heroku master
```

12. Before opening the deployed project url, the same environment variables like the local deployment have to be set up.
To do that, in the terminal, type the following (the empty strings have to be filled in with the appropriate variable):

```console
$ heroku config:set MONGODB_URI='mongodb+srv://...'
$ heroku config:set SECRET_KEY=''
$ heroku config:set CLOUD_NAME=''
$ heroku config:set API_KEY=''
$ heroku config:set API_SECRET=''
$ heroku config:set UPLOAD_PRESET=''
```

13. Finally, the deployed url can be accessed from Heroku dashboard in their website (https://dashboard.heroku.com/apps/`<projectname>`)
where the `<project name>` is the name of the deployed project via an 'Open App" button on the dashboard, else the deployed link can 
also be found in the terminal message just right after executing step 11.

## Acknowledgements and Credits

### Trails Images 
1. Sugar Loaf Trail Image: [Shutterstock](https://www.shutterstock.com/)
2. Powerscourt Waterfall Trail Image: [Flickr](https://www.flickr.com/photos/76257358@N00/3472567195/)
3. Black Castle Wicklow Image: [Shutterstock](https://www.shutterstock.com/g/domenic+redl)
4. Mulaghcleevaun Image: [Flickr](https://www.flickr.com/photos/leondolman/4406997558/)
5. Torc Waterfall Image: [Flickr](https://www.flickr.com/photos/zoltanszabo/33698452810/in/photolist-TkPnZ5-ViHbrQ-VkrmLY-Ei8iRK-JDRKPv-YbdN6w-Wb6FSo-2c8XWeG-MaFLp2-8jMXb9-29uWtPL-mpmS5z-7K1Pxd-M2bqUP-JHWcKy-25fL5s9-PDQr5d-QuJmLQ-9bnSg8-JXoznQ-28d3uWm-28AGHP2-ZpPSJu-22wnqxK-yF87yg-2cweLR6-LQdscf-pcRZTM-LCAMM3-murxSe-LUft7B-eaKAib-otGjn9-qsc7pk-dJcTDY-NDDDVy-xMJDnW-24sGYyc-275LZcn-Ka1H6a-pjWHEv-uXxhm4-anCwVy-N5fk3C-AHkSwy-2bsXZkL-8ZSwmF-QmXVwy-24EKnEd-ASv3Sg)
6. City Centre to Shannon Fields Image: [Limerick](https://www.limerick.ie/discover/eat-see-do/sports-recreation/activities/walking-routes/limerick-city-routes/shannon-fields)
7. Minoo Park Trail Image: [Japan Visitor](https://www.japanvisitor.com/osaka/minoo-park)
8. Mount Ikoma Image: [Getty Images](https://media.gettyimages.com/photos/photo-taken-may-1-shows-poppies-in-full-bloom-on-ikoma-plateau-at-the-picture-id958285104?s=2048x2048)
9. Shijonowate Suihen-Shizen-en Trail Image[Muroike WaterPark](http://osaka-midori.jp/mori/muroike/waterPark.html)
10. Kanmangafuchi Abyss Trail Image[Image](https://www.atlasobscura.com/places/kanmangafuchi-abyss)
11. Hiji Falls Trail [Wikipedia](https://en.wikipedia.org/wiki/Hiji_Falls)
12. Hooker Valley Track [Flickr](https://www.flickr.com/photos/dangerousbiz/16139983682)
13. Kea Point from Mount Cook Village [Image](https://commons.wikimedia.org/wiki/File:Kea_Point_Track_in_Mount_Cook_National_Park_04.jpg)
14. Orakei Basin Walk [Flickr](https://www.flickr.com/photos/craigsyd/6827696545)
15. One Tree Hill Walk [Flickr](https://www.flickr.com/photos/125493053@N04/40327077615)
16. Queenstown Gardens Lakefront Walk [Flickr](https://www.flickr.com/photos/markdefleury/30649091336/in/photostream/)
17. Queenstown Hill [Flickr](https://www.flickr.com/photos/itravelnz/15935556068/)
18. Coney Island Park [NParks](https://www.nparks.gov.sg/-/media/nparks-real-content/gardens-parks-and-nature/parks-and-nature-reserve/coney-island-park/2.jpg)

### Non-Trail Images
1. Parallax Image on Landing Page: [Zotx](https://pixabay.com/users/Zotx-14174246/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4697056)
2. Hiker Henry Profile Photo: [Unsplash Credit](https://images.unsplash.com/photo-1489980557514-251d61e3eeb6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80)
3. Joe Jogger Profile Photo: [Man in Red Jacket](https://www.pexels.com/@creationhill)
4. Website Logo: [Flaticon](https://www.flaticon.com/free-icon/map_2082595?term=hiking&page=5&position=49)
5. 404 Error Image: [Freepik](https://www.freepik.com/free-vector/error-404-concept-landing-page_4730713.htm#query=pikisuperstar%20404%20&position=7)
6. 401 Error Image: [Freepik](https://www.freepik.com/free-vector/error-404-concept-landing-page_4660892.htm#page=2&query=pikisuperstar+404&position=12)
7. Appstore Badge in Footer [WorldVectorLogo](https://worldvectorlogo.com/logo/download-on-the-app-store-apple-4)
8. Playstore Badge in Footer [WorldVectorLogo](https://worldvectorlogo.com/logo/google-play-badge)

### Technical Related Acknowledgements and Attribution
1. My teachers in Trent Global College for teaching me the basics to do this project.
2. The college teaching assistants John and Arif, for giving me valuable feedback. 
3. MongoDB Manual [Manual](https://docs.mongodb.com/manual/crud/) 
4. StackOverflow community [StackOverflow](https://stackoverflow.com/) for various post I can refer to when I encounter mongoDB query 
related problems and flask, python and jinja related problems.
5. PyMODM example on pip3 page [Pypi](https://pypi.org/project/pymodm/)
6. PyMODM documentation [Pymodm read the docs](https://pymodm.readthedocs.io/en/stable/getting-started.html)
7. Rating Stars Display by [Tatu Ulmanen](https://stackoverflow.com/questions/1987524/turn-a-number-into-star-rating-display-using-jquery-and-css/1987545#1987545)
8. Rating Star Radio Button inspired partially by [Lea Verou](https://jsfiddle.net/leaverou/CGP87/).
9. Dynamic form for the comments is totally creditted to [Rafael Medina](https://www.rmedgar.com/blog/dynamic-fields-flask-wtf). 
Without this tutorial, I would never have been able to add fields dynamically in forms.
10. Jinja Documentation [Jinja Documentation](https://jinja.palletsprojects.com/en/2.11.x/) on how to manipulate variables in template.

## Disclaimer
Any content and images used on this website is purely for personal development and educational purpose. They are not meant for profit or for income purposes.