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

## How to test it

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
### Working with IRIS from Embedded Python

As mentioned Embedded Python works in the **same process as IRIS**.

So you have 2 options to work with Embedded Python in IRIS:

1. Bind VsCode to the running IRIS container.
2. Develop in VSCode locally and then run the code in IRIS container with a shared folder.

#### Bind VSCode to the running IRIS container

Open VSCode in the project directory.

Go to the `docker-compose.yml` file, right-click on it and select `Compose Up`.

Once the container is up and running you can open the docker extension and right-click on the container name and select `Attach Visual Studio Code`.

#### Develop locally and run the code in IRIS container

By default, the template is configured to use the shared folder `./src` for python scripts to `/home/irisowner/dev/src` in IRIS container.

You can change the folder according to your preferences.

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

Run the python script:

```bash
# attach to the running IRIS container
docker-compose exec iris bash
# run the script
$ irispython ./python/irisapp.py
```


#### Working with IRIS from Embedded Python
Open VSCode in Devcontainer - this is the bell(notifications) button in the left bottom corner, where you will see the suggestion to open VSCOde in DevContainer mode.
Follow it - it will let to execute Embedded Python scripts vs IRIS and develop it at the same time.

Once devcontainer is opened go to /python/irisapp.py and run it, either with Run button in the top right corner, or in terminal via:
```bash
$ irispython /python/irisapp.py
```
The script contains different samples of working with IRIS from python and goes through it.


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


