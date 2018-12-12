from setuptools import setup, find_packages
from codecs import open
from os import path 

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
   name='arxivtorm',
   version='0.1.3',
   description='Gets papers from ArXiv and puts them on your remarkable',
   author='Naren Dasan',
   author_email='naren@narendasan.com',
   url='https://github.com/narendasan/ArXivToRm',
   license="NCSA",
   long_description=long_description,
   long_description_content_type='text/markdown',
   packages=['arxivtorm'],
   install_requires=['arxiv'],
   entry_points = {
              'console_scripts': [
                  'arxivtorm = arxivtorm.main:main',                  
              ],              
          },
)