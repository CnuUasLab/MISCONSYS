# IMG

# Introduction

The IMG portion of the code has a little more revamping to take care of since last year. The IMG portion of the system has a
lot of database management involved with the code that is written to validate data. Since there are special portions
of this we need to go over each section.

# MySQL Server

The use of a MySQL Server is cruicial to this task. One should be set up in the UAS Lab, but it would be good for you to set 
one up on your linux distributions in order to hold data about photos.
This is how we can categorize photos and then push them into the interoperability server using the mission interface. 

# Design

The following design is noted by the development of the different sections of the server. The MySQL Server is made up of two
seperate tables. 

## MySQL

The SQL structure of the IMG portion is split between two tables. The two are populated at different points. The IMG system is supposed to detect new photos being recieved.
Because of this, the IMG is set up into a system-level and an application-level interface. The camera code interacts with the system-level interface, and the application level code interacts with the front end, and vice versa.

### Table
<b> Photos Table </b>

Attribute | Description | Type
--- | --- | ---
Photo-ID | primary-key identification | primary-int
Photo Path | Folder path of the picture | String
Photo-longitude | Logitude location the photo was taken | double
Photo-latitude | Latitude location that the photo was taken | double
Photo-altitude | Altitidue at which the photo was taken. | double

<b> Promoted Contacts Table </b>

The contacts are promoted through a system on the front end. Since all of the photos are served through the MySQL Server, we can have 2-3 people looking through all available photos trying to see if there are promotable contacts.
The table for this will be developed as we look at the desing of the competition, and as the contact data is developed.
The interface is just as important for this to make sure that people promote contacts correctly, so there is a good setup with the correct number of contacts that are built up in a short period of time.

Design team will have to go over this design, as well as the display, and to make sure that we have a good form that allows us to promote contacts properly.
In time we may be able to artificially recognize photos that are captured, and to recognize if there are anomalies that show up using techniques such as linear regression, and artificial machine vision. This will come in time though.

## Interface

The interface will be made up of several different programs.

<b> Photo Class </b>
```python

class Photo():
      # Initializes the photo information.
      def __init__(self):
          pass

      # Stores photos to the MySQL Server.
      def store_photo(self):
          pass


      # Posts photo to the interoperability server.
      def post(self):
          pass

```

<b> IMG Operation </b>
```python


```

The camera code also needs to be able to interface with this system. We will investigate together, how we can test this.
However, we need to look into things we can change to potentially change the operations of the camera code.



