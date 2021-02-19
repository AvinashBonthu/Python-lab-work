import sqlite3
con=sqlite3.Connection('hrdb')
cur=con.cursor()
cur.execute("create table if not exists emp(id number primary key,ename varchar(30),esal number)")
#cur.execute("insert into emp values(101,'KB Meena',50000)")
#a=[(102,'Ratnesh',70000),(103,'Ajay kr',75000),(104,'Prateek',72000)]
#cur.executemany("insert into emp values(?,?,?)",a)
#cur.execute('select * from emp')
cur.execute("select ename from emp where esal>72000")
cur.execute("select ename from emp where esal>=72000")
cur.execute("select ename from emp where esal between 70000 and 74000")
cur.execute("delete from emp where esal==70000")
cur.execute("select * from emp")

con.commit()
print cur.fetchall()
