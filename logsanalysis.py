#import psycopg2 module
import psycopg2


#create database connection
db = psycopg2.connect('dbname=news')
cursor = db.cursor()


# the most popular three articles of all time
def top_three_popular_articles():
    cursor.execute()
    results = cursor.fetchall()
    print "* The most popular three articles of all time are"
    for result in results:
        print result[0], result[1],"--views"


#the most popular article authors of all time
def popular_authors():
    cursor.execute()
    results = cursor.fetchall()
    print ""
    print ""
    print "* The most popular three articles of all time are"
    for result in results:
        print result[0] ,result[1],"--views"     

#day that led to more than one percent of errors
def error_led_requests():
    cursor.execute()
    print ""
    print ""
    results = cursor.fetchall()
    for result in results:
        print result[0]


#call the functions
top_three_popular_articles()
popular_authors()
error_led_requests()
#close db connection
db.close()