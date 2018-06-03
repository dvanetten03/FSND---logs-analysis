
# Logs Analysis Project
##### The Backend: Databases and Applications

##### Background
This application is an internal reporting tool that uses info from the newspaper's database to discover what kind of articles the site's readers like.

The database containes newspaper articles as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. It's this information that is used to answer the following questions:

  1. What are the most popular three articles of all time?
  2. Who are the most popular article authors of all time?
  3. On which days did more than 1% of requests lead to errors?

The newspaper company database contains three tables: 
* Articles - this table includes info about authors of the newspaper articles
* Authors - this table includes the articles
* Log - this table includes one entry for each time a user has accessed the site
  
### Requirements
    * Python
    * Vagrant
    * Virtualbox
    * PostgreSQL
    
### Accessing the information

You should have Virtualbox and Vagrant installed and be inside the vagrant box using the command vagrant ssh. Then you would need to navigate to the directory with the newsdata.sql file.

Run the following command inside the directory with newsdata.sql:

psql -d news -f newsdata.sql

Then run the following:

python newsdata.py

The output will be displayed on the terminal screen.


    
 
