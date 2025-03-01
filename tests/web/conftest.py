import pytest  #  Python: Importing pytest for test setup and fixtures
import os  #  Python: Importing OS module to handle file paths
import json  #  Python: Importing JSON module to read test data files
from playwright.sync_api import sync_playwright  #  Playwright: Importing sync version of Playwright

# 🔹 Pytest fixture for launching Playwright browser
@pytest.fixture()
def browser():  #  Python: Defining a fixture function named 'nkbrowser'
    """Launch Playwright browser and share the instance across tests."""

    with sync_playwright() as p:  #  Playwright: Starting Playwright context (internally runs `playwright install` if needed)
        browser = p.chromium.launch(headless=False, slow_mo=700)  #  Playwright: Launching a Chromium browser (headless=False means UI is visible)
        context = browser.new_context()  #  Playwright: Creating a new browser session (like a new Chrome profile)
        page = context.new_page()  #  Playwright: Opening a new tab in the browser
        page.goto("https://demoqa.com")  #  Playwright: Navigating to the website

        yield page  #  Python: This returns `page` to test functions that request `nkbrowser` fixture

        browser.close()  #  Playwright: This line is commented out (if uncommented, it will close the browser after tests finish)

# 🔹 Pytest fixture for loading JSON test data
@pytest.fixture(scope="session")
def jsondata():
    """Load test data from JSON file."""
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    json_file_path = os.path.join(project_root, "data", "input_data.json")

    if not os.path.exists(json_file_path):
        raise FileNotFoundError(f" JSON file not found: {json_file_path}")

    with open(json_file_path, "r") as file:
        data = json.load(file)  # Load JSON data

    return data  # Return data to test functions

def update_json_status(data, first_name, new_status):
    """Update the status of a user in the JSON file."""
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    json_file_path = os.path.join(project_root, "data", "input_data.json")

    for user in data["users"]:
        if user["first_name"] == first_name:
            user["status"] = new_status  # Update status

    with open(json_file_path, "w") as file:
        json.dump(data, file, indent=4)

    print(f"✅ Status updated: {first_name} → {new_status}")

"""
import pytest  
 This line imports the `pytest` module.  
    Pytest is a tool used for writing and running test cases.  
    We need `pytest` to create and use fixture functions. 

import os  
 This line imports the `os` module.  
    The `os` module helps us to work with file paths and directories.  
    We use it to find the location of files in our project. 

import json  
 This line imports the `json` module.  
    The `json` module allows us to read and write JSON files.  
    In our test, we store data in a JSON file and read it using this module. 

from playwright.sync_api import sync_playwright  
 This line imports `sync_playwright` from Playwright.  
    Playwright is a tool used for browser automation.  
    `sync_playwright` helps us to control the browser step by step in a simple way. 

---

### **🔹 Pytest Fixture for Launching Browser**  

```python
@pytest.fixture()  
 This line tells Python that `nkbrowser` is a fixture function.  
    A fixture function helps to set up something before a test starts.  
    It runs first and passes the required setup to the test function. 

def nkbrowser():  
     This function will start the Playwright browser and provide it to the test cases. 

    with sync_playwright() as p:  
     This line starts Playwright.  
        Playwright needs a tool called Node.js to run.  
        This `with` statement ensures that Playwright starts and runs correctly.  
        The `p` is just a short name for Playwright, so we can use it easily. 

        browser = p.chromium.launch(headless=False)  
         This line opens a Chromium browser using Playwright.  
            `headless=False` means the browser will be visible when the test runs.  
            If `headless=True`, the browser runs in the background and is not visible. 

        context = browser.new_context()  
         This line creates a new browser context.  
            A context is like a separate user session.  
            This ensures each test runs in a clean and isolated browser environment. 

        page = context.new_page()  
         This line opens a new tab in the browser.  
            The `page` variable stores this new tab,  
            so we can use it to navigate and interact with web pages. 

        page.goto("https://demoqa.com")  
         This line tells Playwright to go to the website `https://demoqa.com`.  
            This is the website where our test cases will run. 

        yield page  
         This line gives the `page` (browser tab) to the test function.  
            When a test function uses `nkbrowser`, it will receive this `page`.  
            This allows the test to interact with the website. 

        # browser.close()  
         This line is commented out, so it does nothing right now.  
            If we remove `#`, it will close the browser after the test is done. 

---

### **🔹 Pytest Fixture for Loading JSON Test Data**  

```python
@pytest.fixture(scope="session")  
 This line defines another fixture function named `jsondata`.  
    `scope="session"` means this function will run only once for all test cases.  
    It is used to load the JSON file, so we do not have to read it again and again. 

def jsondata():  
     This function will read the test data from the JSON file and provide it to the test cases. 

    # ✅ **Finding the Project Root Path**
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))  
     This line finds the main folder of our project.  
        `__file__` means the location of this Python file (`conftest.py`).  
        `os.path.dirname(__file__)` gets the folder where `conftest.py` is stored.  
        `"../../"` moves two folders up to reach the main project folder. 

    # ✅ **Creating the Path to the JSON File**
    json_file_path = os.path.join(project_root, "data", "input_data.json")  
     This line creates the full path to our JSON file.  
        The JSON file is inside the `data` folder, named `input_data.json`. 

    print(f"📌 Looking for JSON file at: {json_file_path}")  
     This line prints the location of the JSON file.  
        It helps us check if the file is in the correct place. 

    # ✅ **Checking if the JSON File Exists**
    if not os.path.exists(json_file_path):  
        raise FileNotFoundError(f"❌ JSON file not found: {json_file_path}")  
         This checks if the JSON file exists.  
            If the file is missing, it will stop the test and show an error. 

    # ✅ **Reading the JSON File**
    with open(json_file_path, "r") as file:  
         This line opens the JSON file in read (`"r"`) mode.  
            The `file` variable stores the content of the file. 

        data = json.load(file)  
         This line reads the JSON content and converts it into a Python dictionary.  
            The `data` variable stores this dictionary, so we can use the test data easily. 

    return data  
     This line returns the loaded JSON data.  
        When a test function uses `jsondata`, it will receive this test data. 

"""