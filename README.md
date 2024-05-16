# Project setup

**Version of Python in this project: 3.12**

- Install Python 3.12 at [here](https://www.python.org/downloads/release/python-3122/).
- Install PyCharm at [here](https://www.jetbrains.com/pycharm/download/?section=windows) and select for PyCharm Community Edition.

**Two methods to create virtual environment in Python.** <i>Choose either step 1 or step 2</i>

1. Download Pycharm to create virtual environment, refer to [this wiki](https://github.com/MeeWai/durrdental/wiki/Create-Virtual-Environment-with-PyCharm).
2. Install the virtual environment in the terminal, refer to [this wiki](https://github.com/MeeWai/durrdental/wiki/Create-Virtual-Environment-in-Terminal).

**Install Behave and Selenium**

1. After installing the virtual environment, activate it with the command below.

    ``<virtual_environment_folder_name>\Scripts\activate``

2. After activated the virtual environment, you will see the <i>(venv)</i> in front of the file location as example below.

    ``(venv) PS C:\Users\durrdental``
3. Then, install the selenium and behave by running the command below.
    
    ``pip install selenium``
    ``pip install behave``
4. Lastly, freeze the required libraries in **requirements.txt**.

**Install allure report**
1. Install with ```npm install --save-dev allure-commandline```. Make sure Java version 8 or above installed, and its directory is specified in the JAVA_HOME environment variable. 
2. Install with ```pip install allure-behave```

# Run allure report
1. Generate report with ``behave -f allure_behave.formatter:AllureFormatter -o <report_folder_name> <feature_folder_name>``
2. You can open the report on the browser by running ``allure serve <report_folder_name>``

# Result
Visit to this [test result wiki](https://github.com/MeeWai/durrdental/wiki/Test-Result) to view the test result.
