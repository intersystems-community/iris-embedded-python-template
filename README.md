## iris-embedded-python-template
This is a template to work with Embedded Python in InterSystems IRIS
It demonstrates how to call python libs from ObjectScript in dc.python.test class.
And it demonstrates how to deal with IRIS from python scripts - python/irisapp.py

## What is Embedded Python ?

Embedded Python is a feature of InterSystems IRIS that allows you to **run python code in the same process** as the IRIS database engine.

The benefits of Embedded Python are:

- **Performance**
  - no need to serialize data between IRIS and Python
  - speed of data processing in Python is comparable to ObjectScript
- **Simplicity**
  - no need to install and configure Python separately
  - easy to deploy IRIS and Python together
  - easy access to ObjectScript code and functionality from Python
- **Security**
  - no need to open any additional ports for communication between IRIS and Python

And the main benefit is that you can use all the power of Python libraries and frameworks in your InterSystems IRIS solutions.

## Prerequisites
Make sure you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Docker desktop](https://www.docker.com/products/docker-desktop) installed.


## Installation ZPM
Open IRIS terminal in your IRIS with installed IPM. Run the command:

```objectscript
USER>zpm "install iris-python-template"
```

## Installation docker

Clone/git pull the repo into any local directory

```bash
$ git clone https://github.com/intersystems-community/iris-embedded-python-template.git
```

Open the terminal in this directory and run:

```bash
$ docker-compose build
```

3. Run the IRIS container with your project:

```bash
$ docker-compose up -d
```

### IRIS Initialization
In this template two approaches are provided to initialize iris: merge and python.
merge.cpf is a convenient way to setup different IRIS configuration settings. [Learn more about merge.cpf](https://docs.intersystems.com/irislatest/csp/docbook/DocBook.UI.Page.cls?KEY=RACS_cpf#:~:text=Use%20the%20iris%20merge%20command,is%20the%20instance's%20current%20iris.).

1. Using merge to initialize IRIS and create IRIS Database and Namespace
Notice [merge.cpf](https://github.com/intersystems-community/iris-embedded-python-template/blob/4c12d4b02770c7422c7553ee818a18c1871c3759/merge.cpf) file that is being implemented during docker image build in Dockerfile
```
iris merge IRIS merge.cpf && \
```
 that contains:
```
[Actions]
CreateResource:Name=%DB_IRISAPP_DATA,Description="IRISAPP_DATA database"
CreateDatabase:Name=IRISAPP_DATA,Directory=/usr/irissys/mgr/IRISAPP_DATA
CreateResource:Name=%DB_IRISAPP_CODE,Description="IRISAPP_CODE database"
CreateDatabase:Name=IRISAPP_CODE,Directory=/usr/irissys/mgr/IRISAPP_CODE
CreateNamespace:Name=IRISAPP,Globals=IRISAPP_DATA,Routines=IRISAPP_CODE,Interop=1
ModifyService:Name=%Service_CallIn,Enabled=1,AutheEnabled=48
ModifyUser:Name=SuperUser,PasswordHash=a31d24aecc0bfe560a7e45bd913ad27c667dc25a75cbfd358c451bb595b6bd52bd25c82cafaa23ca1dd30b3b4947d12d3bb0ffb2a717df29912b743a281f97c1,0a4c463a2fa1e7542b61aa48800091ab688eb0a14bebf536638f411f5454c9343b9aa6402b4694f0a89b624407a5f43f0a38fc35216bb18aab7dc41ef9f056b1,10000,SHA512
```
As you can see it creates dabasases IRISAPP_DATA and IRISAPP_CODE for data and code, the related IRISAPP namespace to access it and the related resources %IRISAPP_DATA and %IRISAPP_CODE" to manage the access.

Also it enables Callin service to make Embedded python work via ModifyService clause.
and it updates the password for the built-in user SuperUser to "SYS". The hash for this password is obtained via the following command:
```bash
docker run --rm -it containers.intersystems.com/intersystems/passwordhash:1.1 -algorithm SHA512 -workfactor 10000
```

2. Using python to initialize IRIS.
Often we used a special [iris.script](https://github.com/intersystems-community/iris-embedded-python-template/blob/d7c817865b48681e3454997906e1374b3baeef74/iris.script) file to run ObjectScript commands during the initialization - it is here just for the information.
This template shows you how to use python for the same purpose with [iris_script.py](https://github.com/intersystems-community/iris-embedded-python-template/blob/4c12d4b02770c7422c7553ee818a18c1871c3759/iris_script.py)file.
It is being executed via the line in Dockerfile:
```
irispython iris_script.py && \
```
the iris_script.py file contains examples how developer can initialize different services of iris via Python code.


## How to test it

### Working with IRIS from Embedded Python

As mentioned Embedded Python works in the **same process as IRIS**.

So you have 2 options to work with Embedded Python in IRIS:

1. Run the code in IRIS container with a shared folder.
2. Bind VsCode to the running IRIS container.

#### Run the python script in iris container:

```bash
# attach to the running IRIS container
docker-compose exec iris bash
# run the script
$ irispython ./python/irisapp.py
```
The script contains different samples of working with IRIS from python and goes through it.
it should return something like this:
```
Hello World
Method call:
It works!
42
Iris Version:
IRIS for UNIX (Ubuntu Server LTS for ARM64 Containers) 2023.2 (Build 227U) Mon Jul 31 2023 17:43:25 EDT
Creating new record in dc.python.PersistentClass
1
Printing one IRIS Object Dump:
+----------------- general information ---------------
|      oref value: 1
|      class name: dc.python.PersistentClass
|           %%OID: $lb("1","dc.python.PersistentClass")
| reference count: 1
+----------------- attribute values ------------------
|       %Concurrency = 1  <Set>
|               Test = "2023-09-03 10:56:45.227577"
+-----------------------------------------------------
1
Running SQL query Select * from dc_python.PersistentClass
[0]: ['1', '2023-09-03 10:56:45.227577']
Printing the whole global of the persistence storage for the class dc.python.PersistentClass:^dc.Package4C8F.PersistentC1A93D
key=['1']: 2023-09-03 10:56:45.227577
James
Jim
John
```

#### Bind VSCode to the running IRIS container

Open VSCode in the project directory.

Go to the `docker-compose.yml` file, right-click on it and select `Compose Up`.

Once the container is up and running you can open the docker extension and right-click on the container name and select `Attach Visual Studio Code`.

#### Working with IRIS from Embedded Python
Open VSCode in Devcontainer - this is the bell(notifications) button in the left bottom corner, where you will see the suggestion to open VSCOde in DevContainer mode.
Follow it - it will let to execute Embedded Python scripts vs IRIS and develop it at the same time.

Once devcontainer is opened go to /python/irisapp.py and run it, either with Run button in the top right corner, or in terminal via:
```bash
$ irispython /python/irisapp.py
```


### Working with Python libs from ObjectScript
Open IRIS terminal:

```objectscript
$ docker-compose exec iris iris session iris
USER>zn "IRISAPP"
```

The first test demonstrates the call to a standard python library working with dates datetime
```objectscript
IRISAPP>d ##class(dc.python.test).Today()
2021-02-09
```

Another example shows the work of a custom lib sample.py which is installed with repo or ZPM. It has function hello which returns string "world":
```objectscript
IRISAPP>d ##class(dc.python.test).Hello()
World
```

Another example shows how to work with files and use pandas and numpy libs.
It calculates the mean age of Titanic passengers:

```objectscript
IRISAPP>d ##class(dc.python.test).TitanicMeanAge()
mean age=29.69911764705882

```

### Develop python scripts locally

By default, the template is configured to use the shared folder `./python` for python scripts to `/home/irisowner/dev/python` in IRIS container.

You can change the folder according to your preferences. Usually python developers name project at the root folder.

It's recommended to work with a virtual environment.

Create a virtual environment in the project directory. Click New Terminal in the VS Code menu:
```bash
$ python3 -m venv .venv
```
Activate the virtual environment:
```
$ source .venv/bin/activate
```

Install the requirements:
```
$ pip install -r requirements.txt
```



### Working with flask

The template also contains samples of working with flask.

Connect to the running with a bash terminal:
```bash
$ docker-compose exec iris bash
```

Run the following commands to start the flask server:
```
irispython /python/flask/app.py
```

That will start the flask server and you will see the following output:
```
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
```

`5000` is mapped to `55030` in docker-compose.yml


#### Test it

Hello world :
```http
GET http://localhost:55030/
Accept: application/json
```

Result:
```json
{
    "message": "Hello world"
}
```

Post a new persistent class

```http
POST http://localhost:55030/persistentclass
Content-Type: application/json
Accept: application/json
{
    "test": "toto"
}
```

Result:
```json
{
    "id": 1,
    "test": "toto"
}
```

Get the persistent class

```http
GET http://localhost:55030/persistentclass/1
Accept: application/json
```

Result:
```json
{
    "id": 1,
    "test": "toto"
}
```


Feel free to use the template for your own development just by adding new py files.


