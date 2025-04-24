# MLOps: Continuous Integration (CI) Tutorial

This tutorial demonstrates how to set up Continuous Integration (CI) for a Machine Learning application using **GitHub Actions**.

---

## Why Continuous Integration?

As your ML application grows, you may:

- Modify existing methods to improve efficiency  
- Add or remove functions as part of development  
- Refactor code for better readability or structure  

However, these changes bring **risks** such as:

- Poor coding standards  
- Introducing bugs  
- Breaking integration with other parts of the system  

To **mitigate these risks**, it's important to **automate testing and integration** every time a change is made. This is where **Continuous Integration (CI)** comes in.

---

## What Does CI Do?

A CI system handles tasks like:

- Pulling the latest version of your code  
- Setting up a virtual server environment (OS, Python version, dependencies)  
- Running tests (e.g., with `pytest`)  
- Generating a test report  

Setting this up manually is a time-consuming and error-prone process. Luckily, we have automated CI services to do this for us.

---

## CI with GitHub Actions

**GitHub Actions** is GitHub’s native CI/CD platform. Other popular CI tools include:

- **Jenkins**
- **Travis CI**
- **GitLab CI/CD**
- **Bitbucket Pipelines**

With GitHub Actions, you define your CI pipeline using a `.yaml` file.

---

## Sample GitHub Actions YAML File

Here’s an example CI configuration in a file called `.github/workflows/ci.yaml`:

```yaml
on: 
  push: 
    branches:
      - main
  pull_request:
    branches:
      - main

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
```

---

### Explanation:

- `on`: Specifies the trigger for the workflow. Here, the CI pipeline runs on push or pull requests to the `main` branch.
- `jobs`: Defines the sequence of tasks. This example has a single job named `test`.
- `runs-on`: Specifies the OS used in the virtual environment (e.g., `ubuntu-latest`).
- `steps`: A list of actions:
  - **Checkout code**: Clones your repo into the runner
  - **Set up Python**: Defines the Python version
  - **Install dependencies**: Installs required packages
  - **Run tests**: Executes test files using `pytest`

Note:  
- The `uses:` keyword references GitHub-provided actions.  
- You can customize the `name:` field to describe each step.

