ARG IMAGE=intersystemsdc/irishealth-community
ARG IMAGE=intersystemsdc/iris-community
ARG IMAGE=intersystemsdc/iris-community:preview
FROM $IMAGE

WORKDIR /home/irisowner/irisbuild

ARG TESTS=0
ARG MODULE="iris-python-template"
ARG NAMESPACE="USER"

# create Python env
ENV PYTHON_PATH=/usr/irissys/bin/irispython
ENV SRC_PATH=/irisdev/app
ENV IRISUSERNAME "SuperUser"
ENV IRISPASSWORD "SYS"
ENV IRISNAMESPACE "USER"

RUN pip3 install -r requirements.txt

## Start IRIS

RUN --mount=type=bind,src=.,dst=. \
    iris start IRIS && \
	iris session IRIS < iris.script && \
    ([ $TESTS -eq 0 ] || iris session iris -U $NAMESPACE "##class(%ZPM.PackageManager).Shell(\"test $MODULE -v -only\",1,1)") && \
    iris stop IRIS quietly
