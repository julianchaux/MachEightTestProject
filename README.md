# MachEight Test Project

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#About-this-Repository">About This Repository</a></li>
    <li><a href="#Using-this-Repository">Using this Repository</a></li>
    <li><a href="#Using-the-Main-Application">Using the Main Application</a></li>
    <li><a href="#Using-the-Tests">Using the Tests</a></li>
    <li><a href="#Requirements">Requirements</a></li>
    <li><a href="#Author">Author</a></li>
  </ol>
</details>

## About this Repository
This repository is the code solution proposed for MachEight challenge.  The requirements are described in the file [README_entry_level.md](README_entry_level.md)

----
## Using this Repository

* Move into a folder and clone the repository:
```
git clone https://github.com/julianchaux/MachEightTestProject.git
```

----
## Using the Main Application

The task is to write a function that finds pairs of integers from a list that sum to a given value. The function will take as input the list of numbers as well as the target sum.  The requirements described in [README_entry_level.md](README_entry_level.md) assume that all input values are integers and that there are no repeated values in the list.  Following the structure of the given example, we execute the application from a terminal, applying as input parameters the list of numbers separated by commas and followed by a space the target sum:
```
python app.py [list] [target-sum]
```
For a specific example, as parameters we enter the list of values 1,15,14,25,-25,-1,6,4,-15,35 and the target sum 10.
```
python app.py 1,15,14,25,-25,-1,6,4,-15,35 10
```
The following image shows the form execution of the application and the corresponding output:

![Output App](ImageResource/Output1.jpg)

It is verified that all pairs of numbers found add up to the target value.

----
## Using the Tests

To test the execution of the application and as good programming practices, two unit tests were created using the [unittest](https://docs.python.org/3/library/unittest.html) library. The structure for executing the tests is:
```
python test_app.py
```

The first unit test was done by entering target sum values that were as a pair of numbers in the list. The following image shows the result:

![Output Test 1](ImageResource/OutputTest1.jpg)

The second unit test was done by entering target sum values that were not as a pair of numbers in the list. The following image shows the result:

![Output Test 2](ImageResource/OutputTest2.jpg)

To modify the test values, you have to modify the [test_app.py](test_app.py) script, changing the values in the variables ***self.total_sum*** and ***self.numbers***.

----
## Requirements

**Program tested with:**
* Python 3.9.12

----
## Author

Julián René Cháux Cedeño - [Profile Link](https://www.linkedin.com/in/julianrenechaux-robotics-ai/)  
