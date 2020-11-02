# API Challenge 🚀:

This Project was made to complete the requirements to enter the Golang Bootcamp of Wizeline

## Requirements:
- Python 3.8.2
- Flask 1.1.2

To check the API response I recommend to use Postman https://www.postman.com/downloads/

## Installation:
No instalation required 

## How To Use:
  1.- Execute the python file Test_Api.py in your terminal

  2.- Use the url that the script tell you in a tool like Postman the url looks like this "http://127.0.0.1:5000" and put one of the two available options

      a) <url>/hello: this will give you the hello world message | Ex: http://127.0.0.1:5000/hello

      b) <url>/covid_data/<country>: this option will give you the uptated information of Covid-19 cases in a country. 
         In the contry part of the url put the initials of the contry to check | Ex: http://127.0.0.1:5000/covid_data/MX 
         or you can use the all option to see all te contry available to check | Ex: http://127.0.0.1:5000/covid_data/all 
         in both cases the contry part of the url is not case sensitive.
    
To run a test of the API you can used Test_modules.py that executes a testing to prove that the API return the expected information 
Last Executed result:
```
.....
----------------------------------------------------------------------
Ran 5 tests in 2.627s

OK

```
# Acknowledgments
Thanks to https://covid19api.com/ for the information on Covid-19

