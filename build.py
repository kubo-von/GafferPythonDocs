#export LD_LIBRARY_PATH="/media/colin/ssd/apps/gafferHQ/gaffer-0.59.6.0-linux-python3/lib"
#export PYTHONPATH="/media/colin/ssd/apps/gafferHQ/gaffer-0.59.6.0-linux-python3/python/"

import inspect
import markdown
import Gaffer
from md_utils import *

members = inspect.getmembers(Gaffer.Node)

md = '''# Gaffer'''
md = md_newline(md)

md += '''## Modules'''
for m in members:
    #print(type(m[1]))
    if inspect.ismodule(m[1]):
        md = md_newline(md)
        md+='''* '''
        md+=(m[0])

md = md_newline(md)
md += '''## Classes'''

for m in members:
    if inspect.isclass(m[1]):
        md = md_newline(md)
        md+='''* '''
        md+=(m[0])
        #print( str((m[1]).__doc__) )

md = md_newline(md)
md += '''## Methods'''
for m in members:
    if inspect.ismethod(m[1]):
        md = md_newline(md)
        md+='''### '''
        md+=(m[0])
        #print( inspect.getsource((m[1]).__func__ ) )
        #print( inspect.signature((m[1]).__func__ ) )
        md = md_newline(md)
        md+=('''	'''+str(inspect.getsource((m[1]).__func__ )))


md = md_newline(md)
md += '''## Functions'''

for m in members:
    if inspect.isfunction(m[1]) or (str(type(m[1])) =="<class 'Boost.Python.function'>"):
        md = md_newline(md)
        md+='''### '''
        md+=(m[0])
        md = md_newline(md)
    if (str(type(m[1])) =="<class 'Boost.Python.function'>"):
        md = md_newline(md)
        md+=(str((m[1]).__doc__))
        #md+=str( inspect.getsource((m[1]) ) )

with open('README.md', 'w') as f:
    f.write(md)

html = markdown.markdown(md)
with open('README.html', 'w') as f:
    f.write(html)

