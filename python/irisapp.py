# Script to test IRIS Embedded Python calls.
# Embedded python works in a shared memory with IRIS. 
# Thus direct calls to IRIS classmethods, globals and tables are available via iris lib.

print('Hello World')

# Run IRIS Class Method 
import iris

print("Method call:")
print(iris.cls('dc.python.ObjectScript').Test())

# function to return IRIS version
def iris_version():
    return iris.system.Version.GetVersion()

# testing the function
print("Iris Version:")
print(iris_version())

# function to create record in IRIS
def create_rec(var):
    obj=iris.cls('dc.python.PersistentClass')._New()
    obj.Test=var
    obj._Save()
    id=obj._Id()
    return id

# test record creation
from datetime import datetime
now=str(datetime.now())
print("Creating new record in dc.python.PersistentClass")
print(create_rec(now))

def print_rec(cls_name,id):
    obj=iris.cls(cls_name)._OpenId(id)
    print(iris.cls("%SYSTEM.OBJ").Dump(obj))

print("Printing one IRIS Object Dump:")
print_rec('dc.python.PersistentClass',1)

## run SQL and print data
def run_sql(query):
    rs=iris.sql.exec(query)
    for idx, row in enumerate(rs):
        print(f"[{idx}]: {row}")

query="Select * from dc_python.PersistentClass"
print("Running SQL query "+query)
run_sql(query)

def print_global(glname):
    gl=iris.gref(glname)
    for (key,value) in gl.query([]):
        print(f"key={key}: {value}")


glname=iris.cls("%Dictionary.CompiledStorage")._OpenId("dc.python.PersistentClass||Default").DataLocation
print("Printing the whole global of the persistence storage for the class dc.python.PersistentClass:"+glname)
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