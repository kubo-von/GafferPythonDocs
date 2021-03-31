#export LD_LIBRARY_PATH="/media/colin/ssd/apps/gafferHQ/gaffer-0.59.6.0-linux-python3/lib"
#export PYTHONPATH="/media/colin/ssd/apps/gafferHQ/gaffer-0.59.6.0-linux-python3/python/"

import inspect
import markdown
import Gaffer

members = inspect.getmembers(Gaffer)

md = '''
# Gaffer
'''

md += '''

## Modules
'''
for m in members:
    print(type(m[1]))
    if inspect.ismodule(m[1]):
        md+=''' 
'''
        md+='''* '''
        md+=(m[0])

md += '''

## Classes
'''
for m in members:
    if inspect.isclass(m[1]):
        md+=''' 
'''
        md+='''* '''
        md+=(m[0])

md += '''

## Methods
'''
for m in members:
    if inspect.ismethod(m[1]):
        md+=''' 
'''
        md+='''* '''
        md+=(m[0])

md += '''

## Functions
'''
for m in members:
    if inspect.isfunction(m[1]) or (str(type(m[1])) =="<class 'Boost.Python.function'>"):
        md+=''' 
'''
        md+='''* '''
        md+=(m[0])




with open('README.md', 'w') as f:
    f.write(md)

html = markdown.markdown(md)
with open('README.html', 'w') as f:
    f.write(html)