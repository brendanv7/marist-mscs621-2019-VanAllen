Marist Dictionary - A simple Python Flask app utililizing Redis
-----------------------------------------------------------------------------------------------
This application serves as a community dictionary for Marist students. This dictionary is meant to hold the lingo that is unique to the Marist student population. It is based slightly off of [sample_microserivce](https://github.com/jinho10/marist-mscs621-2019/tree/master/unit-4/sample-microservice).

The code uses the Flask microframework for web requests and Redis as a database for storing hashes.

When a user loads the site, they are given a form in which they can add words to the dictionary. The program uses the Flask framework to handle the form request, creates a hash of the word and its definition, and adds it to the hashed set in the Redis database. The program also retrieves the entire hashed set from the database and displays it to the user.

The application can be deployed on any host as long as it has a docker engine and docker-compose installed.

The application can also be deployed to IBM Cloud using the IBM Cloud cli tool.

## Click [here](http://maristdictionary.mybluemix.net/) to access the application.
