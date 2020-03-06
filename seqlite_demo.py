import sqlite3

conn = sqlite3.connect('info.db')
c  = conn.cursor()

#c.execute("""CREATE TABLE sec (
#          first text    
#           )""")

#c.execute("""CREATE TABLE seats (
#           first text    
#            )""")

#c.execute("""CREATE TABLE apply (
#           first text    
#            )""")

#c.execute("""CREATE TABLE locate (
#           first text    
#            )""")

#c.execute("""CREATE TABLE campus (
#           first text    
#            )""")

#c.execute("""CREATE TABLE dorm (
#           first text    
#            )""")

#c.execute("""CREATE TABLE scholarship (
#           first text    
#            )""")

#c.execute("""CREATE TABLE study_abroad (
#           first text    
#            )""")

#c.execute("""CREATE TABLE alumnai (
#           first text    
#            )""")

#c.execute("""CREATE TABLE labs (
#           first text    
#            )""")

#c.execute("""CREATE TABLE cse_dept (
#           first text    
#            )""")

#c.execute("""CREATE TABLE eee_dept (
#           first text    
#            )""")

#c.execute("""CREATE TABLE ce_dept (
#           first text    
#            )""")

#c.execute("""CREATE TABLE library (
#           first text    
#            )""")

#c.execute("""CREATE TABLE interent (
#           first text    
#            )""")

#c.execute("""CREATE TABLE clubs (
#           first text    
#            )""")

#c.execute("""CREATE TABLE academic (
#           first text    
#            )""")

#c.execute("""CREATE TABLE tution_fee (
#           first text    
#            )""")

#c.execute("""CREATE TABLE second_timer (
#          first text    
#           )""")

#c.execute("""CREATE TABLE ap_qualification (
#           first text    
#            )""")

#c.execute("""CREATE TABLE ad_date (
#           first text    
#            )""")

#c.execute("""CREATE TABLE eligiable (
#           first text    
#            )""")

#c.execute("""CREATE TABLE admission_fee (
#           first text    
#            )""")

#c.execute("""CREATE TABLE quota (
#           first text    
#            )""")

#c.execute("""CREATE TABLE admission_test (
#           first text    
#            )""")

#c.execute("""CREATE TABLE gpa (
#           first text    
#            )""")

#c.execute("""CREATE TABLE marking (
#           first text    
#            )""")

#c.execute("""CREATE TABLE contact_email (
#           first text    
#            )""")

#c.execute("""CREATE TABLE phone (
#           first text    
#            )""")

#c.execute("""CREATE TABLE path (
#           first text    
#            )""")

#c.execute("""CREATE TABLE session (
#           first text    
#            )""")

#c.execute("""CREATE TABLE website (
#          first text    
#            )""")

#c.execute("""CREATE TABLE dept (
#          first text    
#            )""")





#c.execute("INSERT INTO locate(first) VALUES ('SEC is located at Tilagarh, Alurtol Road, Sylhet 3100 near beside Sylhet Agricultural University.')")

#c.execute("SELECT * FROM path ORDER BY RANDOM() LIMIT 1")
#c.execute("SELECT * FROM dept")
#c.execute("DELETE from locate WHERE first = ''")

c.execute("SELECT * FROM dorm")


z=c.fetchall()

conn.commit()

conn.close()

