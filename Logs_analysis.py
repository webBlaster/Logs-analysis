#import psycopg2 module
import psycopg2
#import datetime
from datetime import datetime
#Create database connection
db = psycopg2.connect('dbname=news')
cursor = db.cursor()

###Sql queries to answer questions

# sql to get the most popular three articles of all time
first_sql = """select replace(log.path,'/article/',''),count(*) as num from log,articles 
            where log.status='200 OK' and log.path=concat('/article/',articles.slug)
            group by log.path order by num desc limit 3"""

#sql to get the three most popular aritcle authors of all time
second_sql = """ select authors.name,count(*) as num from log,articles,authors 
            where log.status = '200 OK' and log.path=concat('/article/',articles.slug) and 
            authors.id=articles.author group by authors.name order by num desc limit 3;"""

#sql to get the day that led to more than one percent of errors
third_sql = """select err.date,(err.count*100.0/req.num) as perc from err join req on err.date=req.date 
            where (err.count*100.0/req.num) > 1.0 order by req.num desc;"""
### Define functions

# the most popular three articles of all time
def first_question():
    cursor.execute(first_sql)
    results = cursor.fetchall()
    print "The most popular three articles of all time are"
    for result in results:
        print result[0], result[1],"--views"

#the three most popular article authors of all time
def second_question():
    cursor.execute(second_sql)
    results = cursor.fetchall()
    print ""
    print ""
    print "The most popular three authors of all time are:"
    for result in results:
        print result[0] ,result[1],"--views"  

#day that led to more than one percent of errors
def third_question():
    cursor.execute(third_sql)
    print ""
    print ""
    results = cursor.fetchall()
    #get date
    date_str = results[0][0]
    #format date
    formated_date = date_str.strftime('%B %d %Y')
    #output result
    print formated_date,"--",results[0][1],"%","errors"


#call the functions
first_question()
second_question()
third_question()
#close db connection
db.close()      
