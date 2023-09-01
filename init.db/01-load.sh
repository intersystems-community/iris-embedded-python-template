#!/usr/irissys/bin/irispython
from iris import ipm

assert ipm('load /home/irisowner/dev -v')
print('')
assert ipm('list')
print('')

print('done')
