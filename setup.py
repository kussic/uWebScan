#py2exe build file: python setup.py py2exe
#then copy 'uws' directory under the newly created 'dist' directory.

from distutils.core import setup
import py2exe

setup(console=['uWebScan.py'])
