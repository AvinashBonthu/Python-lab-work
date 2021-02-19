import sqlite3
con=sqlite3.Connection('hrdb')
cur=con.cursor()
cur.execute("update emp set ename='Kunj' where esal<70000")
cur.execute("select * from emp")
cur.execute("select * from emp where id in (select id from emp where esal>70000)")

print cur.fetchall()
