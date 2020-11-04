from setuptools import setup

setup(
   name='Intercom',
   version='1.0',
   description='To invite people as per geo location',
   author='Abhilash Roy',
   author_email='abhidx92@gmail.com',
   packages=['src'],
   install_requires=['tabulate', 'pytest'], #external packages as dependencies
)