# Marist Dictionary - A simple Python Flask app utilizing Redis
-----------------------------------------------------------------------------------------------
This application serves as a community dictionary for Marist students. This dictionary is meant to hold the lingo that is unique to the Marist student population. It is based slightly off of [sample_microserivce](https://github.com/jinho10/marist-mscs621-2019/tree/master/unit-4/sample-microservice).

The code uses the Flask microframework for web requests and Redis as a database for storing hashes.

When a user loads the site, they are given a form in which they can add words to the dictionary. The program uses the Flask framework to handle the form request, creates a hash of the word and its definition, and adds it to the hashed set in the Redis database. The program also retrieves the entire hashed set from the database and displays it to the user.

The application can be deployed on any host as long as it has a docker engine and docker-compose installed.

The application can also be deployed to IBM Cloud using the IBM Cloud CLI tool.

### Click [here](http://maristdictionary.mybluemix.net/) to access the application.
IMPORTANT: Please let me know when you have finished grading right away. The Redis service in IBM Cloud is a paid service so I am paying out of pocket for it. It is a very cheap service so as long as you aren't creating a ton of data for the database, it'll only cost a dollar or so, but I still would like to stop this service as soon as possible. Thank you :)

## Manual Deployment
Download the code:
```bash
    $ git clone https://github.com/brendanv7/marist-mscs621-2019-VanAllen.git
    $ cd marist-mscs621-2019-VanAllen
```
Use docker-compose to run the code as containers:
```bash
    $ docker-compose build
    $ docker-compose up -d
```
The application should now be able to be accessed at http://localhost:5000/ 

When you are done, you can use the following command to remove the containers:
```bash
    $ docker-compose kill
    $ docker-compose rm
```
    
## IBM Cloud Deployment
This requires a provisioned [IBM Cloud Databases for Redis service](https://www.ibm.com/cloud/databases-for-redis)

[Download and install the IBM Cloud CLI](https://cloud.ibm.com/docs/cli/reference/bluemix_cli?topic=cloud-cli-install-ibmcloud-cli)

Use the CLI to login to IBM Cloud:
```bash
    $ ibmcloud login
```

