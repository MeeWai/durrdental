# durrdental

To run allure report
1. Install with npm install --save-dev allure-commandline. Make sure Java version 8 or above installed, and its directory is specified in the JAVA_HOME environment variable.
2. Install with pip install allure-behave
3. Generate report with behave -f allure_behave.formatter:AllureFormatter -o <folder_name> .\features\
4. allure serve <folder_name>

Result

Overall result



Scenario : Login with correct credential to VS Monitor Homepage



Scenario: Login with incorrect credential to VS Monitor Homepage



Scenario: Verify the user detail in My user account

