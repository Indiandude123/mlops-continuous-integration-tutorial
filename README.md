# mlops-continuous-integration-tutorial

- you may want to change any existing method say in the ML app which has been added to a repo. You may want to make your code more efficient. You may want to add or remove say a method. 
- while implementing the changes there may be certain risks which you may want to mitigate. For example say your coding standard is poor. You might have added some buggy code. You might have integration issues. 
- to handle these issues there should be a server which is providing you some sort of service to check all the tests. So then the server would have to be loaded with a OS which was used during dev, the python and its dependencies, it will pull the code, it will perform the tests and generate a report. All these things that is setting up the server and all the tasks in itself is a full time job for an individual. So there is an automated service to handle all of this. This is known as continuous integration(CI).
- This automated service on GitHub is GitHub Actions 
    - you will have to write down the tasks and the checks by creating a YAML file.
    - There are other services like Jenkins and Travis CI too. There are other GitHub sort of services like GitLab and Bitbucket which have their own CI services too. 



CI YAML FILE:

on: 
  push: 
    branches:
      - main
  pull_request:
    branches:
      - main

The above code means that execute the flow only when the code is pushing or pulling on the branch main. 

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with: 
        python-version: "3.9"
      
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest streamlit
    
    - name: Run tests
      run: |
        pytest _test.py
        

This above code means there is only one job named test. Then defining a few rules like you're running it on ubuntu. Then some steps are mentioned which need to be executed. The "uses" syntax can't change. The "name" can be different. 


