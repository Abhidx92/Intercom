1. Technical problem

We have some customer records in a text file (customers.txt) -- one customer per line, JSON
lines formatted. We want to invite any customer within 100km of our Dublin office for some food
and drinks on us. Write a program that will read the full list of customers and output the names
and user ids of matching customers (within 100km), sorted by User ID (ascending).
● You must use the first formula from this Wikipedia article to calculate distance. Don't
forget, you'll need to convert degrees to radians.
● The GPS coordinates for our Dublin office are 53.339428, -6.257664.


2. Solution
The entire solution is divided into different modules as per functionality.
Core code, data models, utils and constants are segregated and implemented in the solutions.
Exception handling is added wherever required.
Unit and integration tests are added.

3. Requirements
Python 3.6.x

4. Steps to Run the code:
1) Install Python 3.6.x
2) Install pip (can be done via curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py)
2) pip install .
3) python3 -m src.main

5. Steps to run the tests:
1)python3 -m pytest
