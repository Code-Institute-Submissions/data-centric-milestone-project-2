[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/ricardorams/data-centric-milestone-project) 

# data-centric-milestone-project
data-centric-milestone-project


Project: ComDic (Community Dictionary)

This project is of the Full Stack Development course that I am taking, provided by Code Institute. This specific one, is the milestone project of the Data Centric Development Chapter.
The objective of this project is to test and put in practice the techologies and langueges I have learned during the chapter, which are: Python, Flask, PyMongo, MongoDb, Bootstrap, Materialize, Javascript, JQuery, etc.

The website itself it is a Community Dictionary with the goal of collecting and storing the meaning of specific terms inside specific domains.
I called it "Community.." because it is supposed to be edited  and updated by the community itself. The community can add and consult the terms that are used nowadays but that are not present in the traditional dictionaries.
The ultimate goal of the project is to create a book a publish it with all the terms collected from the users.

UX:

The user is supposed to find an easy and intuitive interface.

As a user I want to be able to:
- View current terms and respective definitions inserted in the website being displayed alphabetically;
- Be able to add terms and respective definitions, inserted in one of the available domains;
- Be able to edit terms and / or definitions;
- View current domains inserted in the website being displayed alphabetically;
- Be able to edit available domains;
- Be able to edit domains;

Mock-Up of the website scheme: 

FEATURES:

All the previous features mentioned in the UX part, are fully implemented and fully functional.
( chech the techologies part to see how they were implemented )

TECHNOLOGIES USED:

HTML and CSS
- Used to display the front-end;

Javascript
- Used to implement collapsable menus and form submitions;

JQuery
- JS framework used to implement JS mentioned above;

Materialize
- Front end template. All the front is based on Materialize;

Python
- Used to manipulate back end with the "app.py" file. This is the "central point" of the project;

Flask
- Python framework use to interact and implement HTML and CSS files. This is the framework the allows connections between front end files using python;

PyMongo
- Allows interactions between Python and MongoDB;

MongoDB
- NoSQL databse service used to store all the website's info (terms and domains).

TESTING:

- Front-End:
I have tested the website using multiple browsers, in this case Chrome, Opera and Safari. 
I have also tested it in mobile devices of multible size, using Chrome develpor options. (Iphone, Ipad, Samsung Galaxy, etc)

- Back-End:
I have tested all the links and buttons present in the website, as well as all the connections with the MongoDB.
After finishing all this tests I can guarantee that all the CRUD operations are available to the users, without broken links or options.

The main problem that I found during the testing was:
- when adding or editing a term to the terms database, was possible to write a domain that did not exist in the domains database, which is not possible.
Solution: when openning the ADD TERM or EDIT TERM options, the website loads all the available domains to a drop down menu, and the user has to choose from there.
To facilitate the UX I also added a note above the drop-down menu saying "If you cannot find desired Domain, please go to Domains page first".

DEPLOYMENT:

This project was deployed to Heroku to the following url: https://data-centric-milestone-project.herokuapp.com/

In order to implement this project in a safe and correct way, some environment variables were needed:
- MONGO_DBNAME variable
- MONGO_URI variable
- IP variable
- PORT variable
All the variables mentioned above are used in the code but no defined. They are defined in heroku as "Config Vars".

To run the code locally, you should run the "app.py" file. In order for it to run successful, you will need to define all the variables above. 
All of them should be defined in the "app.py" file.

CREDITS

- Materialize: All the front end is based on Materialize as CSS template. I found their template very complete, intuitive, and easely accessible on the web.
- Code Institute: I gained inspiration to this project in some tutorials made available to its students by Code Institute.

Ricardo Santos, 2019