## iris-embedded-python-template
This is a template to work with Embedded Python in InterSystems IRIS
It demonstrates how to call python libs from ObjectScript in dc.python.test class.
And it demonstrates how to deal with IRIS from python scripts - python/irisapp.py

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

## How to work with it

### Working with Python libs from ObjectScript
Open IRIS terminal:

```
$ docker-compose exec iris iris session iris
USER>
```

The first test demonstrates the call to a standard python library working with dates datetime
```
USER>d ##class(dc.python.test).Today()
2021-02-09
```

Another example shows the work of a custom lib sample.py which is installed with repo or ZPM. It has function hello which returns string "world":
```
USER>d ##class(dc.python.test).Hello()
World
```

Another example shows how to work with files and use pandas and numpy libs. 
It calculates the mean age of Titanic passengers:

```
USER>d ##class(dc.python.test).TitanicMeanAge()
mean age=29.69911764705882

```
### Working with IRIS from Embedded Python
Open VSCode in Devcontainer - this is the bell(notifications) button in the left bottom corner, where you will see the suggestion to open VSCOde in DevContainer mode. 
Follow it - it will let to execute Embedded Python scripts vs IRIS and develop it at the same time.

Once devcontainer is opened go to /python/irisapp.py and run it, either with Run button in the top right corner, or in terminal via:
```
irispython /python/irisapp.py
```
The script contains different samples of working with IRIS from python and goes through it.

Feel free to use the template for your own development just by adding new py files.


