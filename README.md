## iris-embedded-python-template
This is a template to work with Embedded Python in InterSystems IRIS
It demonstrates how to call python libs from ObjectScript in `dc.Demo.Python` class.
And it demonstrates how to deal with IRIS from python scripts - `python/irisapp.py`

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

```
USER>zpm "install iris-python-template"
```

## Installation docker

Clone/git pull the repo into any local directory

```
$ git clone https://github.com/intersystems-community/iris-embedded-python-template.git
```

Open the terminal in this directory and run:

```
$ docker-compose build
```

3. Run the IRIS container with your project:

```
$ docker-compose up -d
```

### How to Test it

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

Create a virtual environment in the project directory:

```
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
$ python3 ./src/python/irisapp.py
```

### Working with IRIS from Embedded Python

Open VSCode in Devcontainer - this is the bell(notifications) button in the left bottom corner, where you will see the suggestion to open VSCOde in DevContainer mode. 
Follow it - it will let to execute Embedded Python scripts vs IRIS and develop it at the same time.

Once devcontainer is opened go to /python/irisapp.py and run it, either with Run button in the top right corner, or in terminal via:

```bash
$ python3 src/python/irisapp.py
```

The script contains different samples of working with IRIS from python and goes through it.

Feel free to use the template for your own development just by adding new py files.

### Working with IOP (Interoperability On Python)

The template also contains samples of working with IOP.

Connect to the running with a bash terminal:
```
docker-compose exec iris bash
```

Run the following commands to start the IOP:
```
iop -s dc.Python.Production
```

That will start the IOP server and you will see the following output:
```
2023-08-30 14:41:18.066 Info None 1356 63 None Ens.Director StartProduction Production 'dc.Python.Production' starting...
2023-08-30 14:41:18.076 Info Ens.Actor 1357 63 None Ens.Job Start ConfigItem 'Ens.Actor' started in job 1357
2023-08-30 14:41:18.082 Info Ens.Actor 1358 63 None Ens.Job Start ConfigItem 'Ens.Actor' started in job 1358
2023-08-30 14:41:18.088 Info Ens.Alarm 1359 63 None Ens.Job Start ConfigItem 'Ens.Alarm' started in job 1359
2023-08-30 14:41:18.098 Info Ens.MonitorService 1360 63 None Ens.Job Start ConfigItem 'Ens.MonitorService' started in job 1360
2023-08-30 14:41:18.100 Info Ens.ScheduleHandler 1361 63 None Ens.Job Start ConfigItem 'Ens.ScheduleHandler' (Ens.Actor) started in job 1361
2023-08-30 14:41:18.108 Info EnsLib.Testing.Process 1362 63 None Ens.Job Start ConfigItem 'EnsLib.Testing.Process' (Ens.Actor) started in job 1362
2023-08-30 14:41:18.121 Info Python.FilterPostRoutingRule 1364 63 None Ens.Job Start ConfigItem 'Python.FilterPostRoutingRule' (Ens.Actor) started in job 1364
2023-08-30 14:41:18.129 Info None 1356 64 None Ens.Director StartProduction Production 'dc.Python.Production' started.
2023-08-30 14:41:18.129 Info Ens.ScheduleHandler 1361 64 64 Ens.Director UpdateProduction Production 'dc.Python.Production' updating...
2023-08-30 14:41:18.478 Info Python.FileOperation 1363 64 None Ens.Job Start ConfigItem 'Python.FileOperation' started in job 1363
2023-08-30 14:41:18.562 Info Python.RedditService 1365 64 None Ens.Job Start ConfigItem 'Python.RedditService' started in job 1365
2023-08-30 14:41:18.566 Info Python.RedditService 1365 64 None RedditService on_process_input Sending post VENDER LIVROS É UM DOS TRABALHO MAIS SIGNIFICANTES EM UMA ÉPOCA DE OBSCURANTISMO.
```

`52773` is mapped to `55038` in docker-compose.yml

You can see the Production in the Management Portal: `http://localhost:55038/csp/irisapp/EnsPortal.ProductionConfig.zen?PRODUCTION=dc.Python.Production&IRISUsername=_SYSTEM&IRISPassword=SYS`

To stop the IOP press `Ctrl+C` in the terminal.

To exit the logs press `Ctrl+C` again.

### Working with flask

The template also contains samples of working with flask.

Connect to the running with a bash terminal:
```
docker-compose exec iris bash
```

Run the following commands to start the flask server:
```
python3 src/python/rest/app.py
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

### Working with Python libs from ObjectScript
Open IRIS terminal:

```
$ docker-compose exec iris iris session iris -U IRISAPP
USER>
```

The first test demonstrates the call to a standard python library
```
USER>d ##class(Demo.Python).HelloWorld()
Hello world
```

Another example shows the work of a custom lib sample.py which is installed with repo or ZPM. It has function hello which returns string "world":
```
USER>d ##class(Demo.Python).Hello()
World
```