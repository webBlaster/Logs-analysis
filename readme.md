#LOGS ANALYSIS

##ABOUT
a Udacity project where you answer three questions with sql on a large database
the questions include:
1-what are the top three most popular post of all time
2-who are the top three authors that got the most views
3-on which day did more than one percent of request led to errors

##VIEWS
this project contains two views err and req
which are used in question three

###VIEW SETUP
first view:

create view err as select cast(time as date) as date,count(*) from log where status !='200 OK' group by date order by count(*) desc;

second view:

create view req as select cast(time as date) as date,count(*) as num from log
group by date order by num desc;
