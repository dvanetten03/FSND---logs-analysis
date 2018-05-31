# 'Database code' for the Logs Analysis Project
#!/usr/bin/env python3

import psycopg2

# Queries

q1 = """
SELECT title, count(*) AS views FROM articles 
INNER JOIN log ON path LIKE '%' || articles.slug || '%' 
WHERE log.status LIKE '%200%' GROUP BY title, path 
ORDER BY views DESC limit 3;"""

q2 = """
SELECT authors.name, count(*) AS views FROM articles 
INNER JOIN authors ON articles.author = authors.id 
INNER JOIN log ON concat('/article/', articles.slug) = log.path 
WHERE log.status LIKE '%200%' GROUP BY authors.name ORDER BY views;
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