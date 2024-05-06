# durrdental

To run allure report
1. Install with npm install --save-dev allure-commandline. Make sure Java version 8 or above installed, and its directory is specified in the JAVA_HOME environment variable.
2. Install with pip install allure-behave
3. Generate report with behave -f allure_behave.formatter:AllureFormatter -o <folder_name> .\features\
4. allure serve <folder_name>

# Result

**Overall result**

![image](https://github.com/MeeWai/durrdental/assets/38762366/2bd27432-e53a-448b-b162-2a04d019da6d)

**Scenario : Login with correct credential to VS Monitor Homepage**

![image](https://github.com/MeeWai/durrdental/assets/38762366/17bb9e5a-be9f-45d2-a038-4f4c80818449)

**Scenario: Login with incorrect credential to VS Monitor Homepage**

![image](https://github.com/MeeWai/durrdental/assets/38762366/89f1fe52-0a15-4c8d-95e1-1186e3d42135)

**Scenario: Verify the user detail in My user account**

![image](https://github.com/MeeWai/durrdental/assets/38762366/3319a346-e132-47cf-b12c-4508b0e48206)
