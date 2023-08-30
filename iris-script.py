import iris
import pandas as pd
from sqlalchemy import create_engine
from grongier.pex import Utils

# switch namespace to the %SYS namespace
iris.system.Process.SetNamespace("%SYS")

# set credentials to not expire
iris.cls('Security.Users').UnExpireUserPasswords("*")

# switch namespace to IRISAPP built by merge.cpf
iris.system.Process.SetNamespace("IRISAPP")

# load zpm packages
iris.cls('%ZPM.PackageManager').Shell("load /home/irisowner/dev -v")

# load demo data
engine = create_engine('iris+emb:///')
df = pd.read_csv('/home/irisowner/dev/data/titanic.csv')
df.to_sql('Titanic', engine, if_exists='replace', index=False, schema='Demo')

# load interop demo
Utils.migrate('/home/irisowner/dev/src/python/interop/reddit/settings.py')