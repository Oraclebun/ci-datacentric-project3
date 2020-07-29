### Database Structure Design
The main database name is Project3DevDB
The database consists of 3 collections. These collections are setup using PyMODM in models.py file via MongoModels class.
From the models.py file the 3 collections and their details are as follows:

1. Hiker model.
* The hiker class is a MongoModel that defines the hiker or user object. It has field instances that represents the user/hiker entity 
attributes.
* In this project, the field instances are:
    + first name
    + last name
    + username 
    + country of origin
    + e-mail address
    + number of trails completed and 
    + a profile image link of the user.

2. Location model
* The location class defines the location object. Its field instance is as follows :
    + Country name
    + Embedded document list - Province(Region)

3. Province model (Embedded mongo model)
* The province class defines the region/province object. Its field instance is as follows:
    + Name of Province(region) of the trail location.
    + Embedded document field - town/city class.

4. Town/City model (Embedded mongo model)
    + Name of the town/city 

5. Trails model
* The Trails class is a Mongo Model that defines the trails object. Its field instances represents the trails entity attributes.
* The field instances of Trails class are:
     + trail name 
     + trail distance
     + trail elevation 
     + trail route type 
     + trail difficulty 
     + trail description 
     + trail image
     + trail embed route that holds the embedded google map route
     + the location field that reference the Location model and 
     + finally the comments field which is an embedded document list field.

6. Comments model
* The Comment class is an Embedded Mongo Model that holds the comments/reviews object. Its field instances hold the details of the reviews and comments given:
     + author (this field is a field that reference the hiker class). It stores the hiker id.
     + date of comment
     + body of comment/reviews
     + sightings (word tags to describe sightings on trail)
     + trail rating
     + date started hiking
     + hours taken to hike the trail
     + minutes taken to hike the trail (hours and minutes are mean to be the time period taken to hike the trail in total)