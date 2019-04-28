#import psycopg2 module
import psycopg2


#create database connection
db = psycopg2.connect('dbname=news')
cursor = db.cursor()


# the most popular three articles of all time
def top_three_popular_articles():
    cursor.execute("""select articles.title, count(*) as views
    from log, articles
    where log.status = '200 OK'
    and articles.slug = substr(log.path, 10)
    group by articles.title
    order by views desc
    limit 3;""")
    results = cursor.fetchall()
    print "* The most popular three articles of all time are"
    for result in results:
        print result[0], result[1],"--views"


#the most popular article authors of all time
def popular_authors():
    cursor.execute("""select authors.name, count(*) as views
    from log, authors, articles
    where log.status = '200 OK'
    and articles.slug = substr(log.path, 10)
    and authors.id = articles.author
    group by authors.name
    order by views desc;""")
    results = cursor.fetchall()
    print ""
    print ""
    print "* The most popular three articles of all time are"
    for result in results:
        print result[0] ,result[1],"--views"     

#day that led to more than one percent of errors
def error_led_requests():
    cursor.execute("""select errors.date,
    errors.err/errors.total * 100 as percentage
    from (select cast(time as date) as date,
    count(*) as total,
    cast(sum(cast(status != '200 OK' as int)) as float) as err
    from log group by date) as errors
    where errors.err/errors.total > 0.01;""")
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