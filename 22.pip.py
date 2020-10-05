'''
PIP Packages:

Commands for pip packages:

1. check version: pip --version
2. check list of existing librarys: pip list
3. install camelcase library: pip install camelcase
4. uninstall camelcase libray: pip uninstall camelcase
'''

import camelcase as c

name = 'hello anjali'
cobject = c.CamelCase()
print(cobject.hump(name))
