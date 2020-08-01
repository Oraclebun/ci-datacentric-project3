## Testing
This project is partially tested using automated testing and fully tested manually.

## Automated testing
Automated testing is done using unittest in test_app.py. Unit test is being used as it conveniently comes packaged with python. 
The test and the results are tabulated as below:

| #  | Methods                                         | Methods summary                              | Test Results                 |  
|----|-------------------------------------------------|----------------------------------------------|------------------------------|
| 1  | Setup                                           | setup the test_client                        |                              |   
| 2  | test_routes                                     | get all accessible routes                    | status_code 200              |   
|    |                                                 | (that do not need authentication)            |                              |   
| 3  | test_valid_user_registration                    | post valid data to the create_profile route  | success_msg is in response   |   
| 4  | test invalid registration (duplicate username)  | post data with an existing username          | error_msg is in response     |   
| 5  | test invalid registration (invalid e-mail)      | post data with an invalid e-mail address     | error_msg is in response     |   
| 6  | test valid user login                           | post data with a valid username              | success_msg is in response   |   
| 7  | test user login with invalid username           | post data with a non-existent username       | error_msg is in response     |   
| 8  | test user login with invalid e-mail             | post data with a non-existent email address  | error_msg is in response     |   
| 9  | test authenticated user can access show_profile | get route '/profile'                         | status_code 200              |   
| 10 | test authenticated user is able to edit profile | get route '/profiles/edit/`<userid>`         | status_code 200              |
|    |                                                 | post editted data of test user               | success_msg is in response   |
| 11 | test user logout                                | get route '/logout                         ` | success_msg is in response   |
|    |                                                 |                                              | redirect back to login page  |
|    |                                                 |                                              |                              |
| 12 | test delete user                                | post route '/profiles/delete/`<userid>`      | success_msg is in response   |
|    |                                                 |                                              |                              |

To run autotest in the terminal or command prompt, type in the below command line after setting up this project.
```console
$ python3 test_main.py

```

### Manual Testing
The automated test fails for the testing of adding, editting and deleting comments due to the dynamic input of the forms.
As the automated testing did not cover 100% of this project's functionality, manual testing is also performed.

#### Home Page
* At homepage, user is greeted with a parallax/jumbotron of an image of a trail surrounded by trees.
* The Enter button links to the directory page
* The navbar links are functional. The navbar logo links back to the homepage. 
* The Directory, Top-Rated, Register and Login links to the correct route/pages.
* 3 cards are displayed below the parallax to show the 3 most recent comments.
* The materialize collapsible shows the trails sorted by countries and town are and the trail names inside links to the correct trail page.
* The footer has the project logo and also "Get the App" text in it.
* There are 2 badges that links to the Ios App Store and Google Play Store.

#### Directory Page
* The Directory page has a search bar and 2 drop down select bars in a row. Below those are rows of cards showing trail details.
* When a query is input into the search bar, user can retrieve what he/she searched for.
* The search input searches the fields of trail name, trail description, trail distance and trail location.
* There is combinative search to allow user to search for a text query string and route-type as well as route difficulty. 
The route-type and route difficulty are selected by ticking the checkboxes in the Materialize Multiple Select drop down.

#### Top Rated Page
The Top-Rated page displays the trail cards sorted by averaged rating in descending order(highest to lowest) .

#### CRUD Functionality testing
#### Register Page
* The register page displays a Create Profile form that allows user to create a profile for login purpose.
* If an invalid e-mail address is keyed in, the message "Please enter an e-mail address." is observed.
* If a user submits the form without uploading any profile picture, a toast message will appear to alert that the Profile Picture is empty.
* If the number of trails completed is not an integer number, a message will appear to alert the user that the number has to be an integer.
* If a user tries to register with a non-unique username, a flash message at the bottom of the form will appear with the message
'User already exists. Please choose another username.'
* When the profile picture has been succesfully uploaded, a toast message "Picture Upload Successful!" will appear.
* After picture has been uploaded, the upload button is hidden to disable user from multiple upload.
* After form has been submitted, the user will be redirected to home page and there he will see a flash message "Registration Successful".

#### Login Page
* The login page display the form that allows user to login. It only has 2 fields : username and e-mail address.
* If user enters a username that does not exists in the database, the user will see the message "Wrong username. Please try again." flashed on the top
part of the form.
* If user enters a username that is not linked to the correct e-mail address, they will see the message "Wrong e-mail address. Please try again."
flashed out at the top of the form.
* If user logins successfully, he/she will see the message "You logged in successfully as `<username>`" where username is the username of the user.
And the user will be directed to the home page.

#### Manage Profile Page
* If the user login is succesful, he/she will be able to see a man icon in place of the login link in the navbar
* When clicked, he/she will be able to see the Manage Profile in the drop down of the man icon.
* When clicked, the user will be directed to a /profiles route. 
* The user should be able to see a card containing his profile picture , and a table with his username, e-mail address, nationality and number of 
trails completed.
* The user should also see a blue edit button and a red delete button at the bottom of the table.
* Upon clicking the <span style="color:blue">blue edit</span> button, user will be directed to a '/profiles/edit/`<userid>` and see a form populated with the users' detail.
* The user also has the option to replace his uploaded photo with another image.
* Upon successful image upload, the upload button will be hidden to prevent users from uploading another image again.
* When the form is succesfully submitted, users will be redirected back to home page and he/she will be able to see the flash message "Profile Updated Successfully"
in the home page.

#### Logout Page
* User is logged out when he/she clicks this link.

#### Trails Page
* In the individual trails page, user will see a responsive image of the trail. He/she should be able to click this image and enlarge it.
* Next to this image is an embedded google map to view the route of the trail.
* Below the image is a rectangle box detailing the trails information.
* Below this is a circular floating button, when hovered, will show the tooltip "Add Comments". On clicking this button, the page will be directed to
an add comments page with a form to allow user to fill in their comments.
* Below these buttons, users will be able to see the comments in rows of framework cards.
* If user is logged in and did post a comment, he/she will see 2 buttons next to his /her comments. 
There will be 1 <span style="color:blue">edit</span> button and 1 <span style="color:red">delete</span> button on the left side of each comment to allow editting and deletion 
by the authenticated user, if he/she is the author of the comment.

#### Add Comments Page
* When the add comments button is clicked, user will be directed to an Add Comments page that displays a form.
* The form has a:
    * text area field for user to fill in the comments & reviews, 
    * date hiked field is a date picker that allows user to pick the date of the hike,
    * time spent hiking field - this field consists of 2 number type input that allows user to key in the time spent hiking (collectively) in hours and minutes.
    * sightings field. This field has dynamic text input. User has to key in at least 1 word or phrase that the user sees or encounter during the hike. The maximum number
    of text input the user can add is 6.
    * ratings field. This field is a set of radio buttons shown as stars. When user click a star that is in a position x, user will see that the star clicked and the 
    the stars before that will be coloured to show a total of x rating.
* If the any of the fields are blank, the form will not be validated and user will still see the form page.
* The number of hours taken to hike the trail field only accept a maximum number of 23, else form will not submit.
* The number of minutes taken to hike the trail field only accept a maximum number of 59, else form will not submit.
* Upon the successful validation of the form, user will be redirected to the trails page and there above the add comments floating button,
user will see a flash message to say "New Comments by `{name}` on `{comment date}` have been added." 

#### Edit Comments Page
* When the user clicks the edit comments button in the trails page, user will be directed to an Edit Comments page that displays a form.
* The form will not be validated if any of the fields are blank or invalid (the number of hours exceed 23 and the number of minutes exceed 59).
* Upon successful validation of the form, user will be redirected to the trails page and a flash message will show
"Comments have been editted by `{comment_to_edit.author}`, on `{comment_date}`."

#### Deleting Comments
* When the user clicks the red delete comments buttons in the trails page, a modal will pop up to ask the user to confirm if they want to
delete the comment. If the user clicks the Confirm button, the particular comment is removed and user will redirected to the trails page.
* The deleted comment is no longer visible in the page.

#### Deleting User Profile
* When the user is logged in and goes to the Manage Profile Page, if he/she were to click the Delete button in his/her profile card,
he/she will see a modal to confirm the deletion.
* If the deletion is confirmed, all the user's comments are pulled out of the database (the comments are in embedded list).
* Then the user will be logged out of the session.
* Finally the user's profile will be deleted in the database.

### Bugs
1. One of the major bugs encountered is during the writing of the automated test for post,edit and delete comment. The form will not validated
when posting the data back to the route. This is due to the way the dynamic field for the form is being created. This needs more time to debug.
2. Another major bug happens if a comment is posted by a user. Then if the admin for some reason deletes the user profile in the database,
Some of the trail pages that has his/her comments will not show up. This is because the comments are embedded in the trails models. And this
causes inconsistencies in the data that will mess up the programming logic serving the webpages. The only way to handle this is to delete
the profile via the application and not directly at the database.
3. While testing the website, I also discover a bug that on my locally run webpages and my website does not seem to match. While the deployed 
website shows the layout to be just fine, the local website shows layout inconsistencies. Please see the images attached below. 
As I have tried the deployed website on Google Chrome as well, I did not manage to find the bug or problem that cause the locally run webpages
to have the bad layout.

![Deployed Screen Shot](https://github.com/Oraclebun/ci-datacentric-project3/blob/master/static/image/readme_image/DeployedSS.jpg)

![Local Screen Shot](https://github.com/Oraclebun/ci-datacentric-project3/blob/master/static/image/readme_image/LocalSS.jpg)

## Mobile Responsiveness
1. The website is tested on [Amiresponsive](http://ami.responsivedesign.is/#) and the screenshot is show as below:
![Responsive Screen Shot](https://github.com/Oraclebun/ci-datacentric-project3/blob/master/static/image/readme_image/Amiresponsive.jpg)
2. It is also tested on [search.google/test/mobile-friendly](https://search.google.com/test/mobile-friendly) and the screenshot results:
![Responsive Screen Shot](https://github.com/Oraclebun/ci-datacentric-project3/blob/master/static/image/readme_image/Mobile_responsivess.jpg)
3. Next the website is tested on my personal phone which is an Iphone 6. The website fits into the mobile screen and the layout if fine.