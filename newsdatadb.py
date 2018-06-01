# 'Database code' for the Logs Analysis Project
#!/usr/bin/env python3

import psycopg2

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


DBNAME = "newsdata"

def get_posts():
	db = psycopg2.connect(database=DBNAME)
	c = db.cursor()
	c.execute("select count(*) from log group by DATE(time)")
	posts = c.fetchall()
	db.close()
	return posts

	print( "There are " + posts + " different days in this database ");