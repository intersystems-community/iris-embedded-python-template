# Script to test IRIS Embedded Python calls.
# Embedded python works in a shared memory with IRIS. 
# Thus direct calls to IRIS classmethods, globals and tables are available via iris lib.
# You an invoke this script from shell in the container by calling:
# python3 src/python/irisapp.py
import iris
from sqlalchemy import create_engine,text

print('Hello World')

# print current namespace
print("Current namespace:")
print(iris.system.Process.NameSpace())

# Run IRIS Class Method 
print("Method call:")
print(iris.cls('Demo.ObjectScript').Test())

# function to return IRIS version
def iris_version():
    return iris.system.Version.GetVersion()

# testing the function
print("Iris Version:")
print(iris_version())

# function to create record in IRIS
def create_rec(var):
    obj=iris.cls('Demo.PersistentClass')._New()
    obj.Test=var
    obj._Save()
    id=obj._Id()
    return id

# test record creation
from datetime import datetime
now=str(datetime.now())
print("Creating new record in Demo.PersistentClass")
print(create_rec(now))

def print_rec(cls_name,id):
    obj=iris.cls(cls_name)._OpenId(id)
    print(obj.Test)

print("Printing one IRIS Object :")
print_rec('Demo.PersistentClass',1)

## run SQL and print data
def run_sql(query):
    # create sqlalchemy engine
    engine = create_engine('iris+emb:///')
    # run query
    with engine.connect() as conn:
        rs = conn.execute(text(query))
        for row in rs:
            print(row)

query="Select * from Demo.PersistentClass"
print("Running SQL query "+query)
run_sql(query)

def print_global(glname):
    gl=iris.gref(glname)
    for (key,value) in gl.query([]):
        print(f"key={key}: {value}")


glname=iris.cls("%Dictionary.CompiledStorage")._OpenId("Demo.PersistentClass||Default").DataLocation
print("Printing the whole global of the persistence storage for the class Demo.PersistentClass:"+glname)
print_global(glname)

def global_order_demo():
    gl=iris.gref("^EPython.Order")
    # set three indexes in unsorted order
    list=["John","Jim","James"]
    for key in list:
        gl.set([key],"")
    # print global indexes traversing via order function. Notice that indexes are sorted automatically
    key=""
    while True:
        key=gl.order([key])
        if key==None:
            break
        print(key)

# demoing persistent key-value global setting and traversing
global_order_demo()