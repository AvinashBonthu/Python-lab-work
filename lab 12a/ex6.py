import sqlite3
con=sqlite3.Connection('hrdb')
cur=con.cursor()
cur.execute("select ename,post,vehicle from emp cross join emp1,emp2 where emp.id=101")
cur.execute("select ename,post,vehicle,house from emp cross join emp1,emp2 where emp.id=101")
cur.execute("select emp.id,ename,post,vehicle,house from emp cross join emp1,emp2 where emp.id=101")
cur.execute("select emp2.id,ename,post,vehicle,house from emp cross join emp1,emp2 where emp.id=101")
print cur.fetchall()
