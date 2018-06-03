# 'Database code' for the Logs Analysis Project
#!/usr/bin/env python3

import psycopg2

DBNAME = "news"

# Queries

q1 = """
SELECT title, count(*) AS views FROM articles 
JOIN log ON path LIKE '%' || articles.slug || '%' 
WHERE log.status LIKE '%200%' GROUP BY title, path 
ORDER BY views DESC limit 3;
"""

q2 = """
SELECT authors.name, count(*) AS views FROM articles  
JOIN authors ON articles.author = authors.id 
JOIN log ON concat('/article/', articles.slug) = log.path 
WHERE log.status LIKE '%200%' GROUP BY authors.name ORDER BY views DESC;
"""

q3 = """
SELECT total.day AS "Days with more than 1 percent errors", ROUND(cast(error.totalError AS decimal)/cast(total.total AS decimal)*100,2) 
FROM (SELECT date(log.time) AS day, count(*) AS total FROM log GROUP BY day) AS total 
LEFT JOIN (SELECT date(log.time) AS day, count(*) AS totalError FROM log WHERE status LIKE '%404%' 
GROUP BY day) AS error ON total.day = error.day WHERE (error.totalError*100)/total.total >= 1 ORDER BY total.day;
"""


db = psycopg2.connect(database=DBNAME)
c = db.cursor()
c.execute(q1)
top_arts = c.fetchall()
	
c.execute(q2)
pop_auth = c.fetchall()
	

c.execute(q3)
err_rate = c.fetchall()

db.close()

print("1. What are the three most popular articles?")
for row in top_arts:
	print('\t"{}" - {} views'.format(row[0], row[1]))

print("\n2. Who are the most popular article authors?")
for row in pop_auth:
	print('\t"{}" - {} views'.format(row[0], row[1]))

print("\n3. On which days did more than 1% of requests lead to errors?")
for row in err_rate:
	print('\t"{}"'.format(row[0]))


