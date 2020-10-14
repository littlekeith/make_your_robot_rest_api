import os
import sys
import inspect
import shutil

__location__ = os.path.join(os.getcwd(), os.path.dirname(
    inspect.getfile(inspect.currentframe())))
print(__location__)

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.join(__location__, '../src'))


data = {
    "a": 1
}

try:
    print(data['d'])
except KeyError as ke:
    print(2222)
except Exception as e:
    raise e
