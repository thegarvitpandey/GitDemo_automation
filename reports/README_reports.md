to run the python script for html report generation:
python -m pytest {file+name} --html reports/report.html

to capture the failed screenshots as well as the logs for the logs,
we use the common usage template and edit the changes for the function
the following function has to be kept inside the conftest as it will be used
multiple times at multiple pages

# conftest.py
import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # 1. Execute all other non-wrapped hooks to let pytest generate the report first
    outcome = yield
    
    2. Retrieve the actual TestReport object from the outcome
    report = outcome.get_result()
    
    3. Filter by phase ("setup", "call", "teardown") and status
    if report.when == "call" and report.failed:
        # Example: Log the failed test node ID
        print(f"Test failed: {report.nodeid}")
        
        # Access original test function details via 'item'
        # docstring = item.obj.__doc__



To start JENKINS via cmd:
cd E/d \Automation\Jenkins
java -jar jenkins.war --httpPort=9090