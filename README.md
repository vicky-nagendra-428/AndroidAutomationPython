# AndroidAutomationPython
Android mobile app automation using Appium and Python with simple unit test framework. 
Which implements page object model for making it more modular and maintainable


The Project contains 3 python packages

commons:
Which contains common stuff like utils, config files

pages:

This project followed POM, so this package contains all the page specific functions and attributes, 
and a page setup which does some initialization stuff

tests:

tests package contains all the test case files and test runner.

How to Run the tests:

Add all the test cases that are required to run to the suite_runner.py

Then, Right click on suite_runner and click on `Run`

or else

You can use the command 

python -m unittest test_module1 test_module2

python -m unittest test_module.TestClass

python -m unittest test_module.TestClass.test_method
