from pages.buttons_page import ButtonPage
from pages.check_box import CheckBox
from pages.elements_page import ElementsPage
from pages.home_page import HomePage
from pages.links_page import LinksPage
from pages.radio_buttons import Radiobutton
from pages.text_box_page import TextBoxPage
from pages.web_table_page import WebTable


def test_text_box_form(browser, jsondata):
    # Create Page Object instances
    home_page = HomePage(browser)
    elements_page = ElementsPage(browser)
    text_box_page = TextBoxPage(browser)
    check_box = CheckBox(browser, jsondata)
    radio_button = Radiobutton(browser, jsondata)
    web_table = WebTable(browser)
    button_page = ButtonPage(browser)
    links_page = LinksPage(browser)

    home_page.click_on_elements()

    # Expand "Elements" section if collapsed
    elements_page.expand_elements_if_needed()

    # Click on "Text Box"
    elements_page.click_text_box()

    # Fill the form with JSON data
    text_box_page.fill_form(jsondata)

    # Submit the form
    text_box_page.submit_form()

    # Validate Output
    text_box_page.verify_submission(jsondata)

    # Validate check box
    check_box.check_box()
    check_box.expand_folders()

    check_box.navigate_and_select_checkbox()

    radio_button.navigate_radio_button_page()
    radio_button.select_radio_button()

    web_table.navigate_web_table()
    web_table.search(jsondata)

    button_page.buttons_check()

    links_page.navigate_to_links_page()
    links_page.handle_home_link_click()
    links_page.dynamic_link_click()




"""
# ✅ Importing required Page Object files
from pages.check_box import CheckBox  
from pages.elements_page import ElementsPage  
from pages.home_page import HomePage  
from pages.text_box_page import TextBoxPage  
 These four imports bring different page classes from separate files:
    - `CheckBox` → Used for interacting with checkboxes.
    - `ElementsPage` → Used for interacting with the "Elements" section.
    - `HomePage` → Used for interacting with the home page.
    - `TextBoxPage` → Used for interacting with the text box form.
    These classes contain locators and methods to interact with the webpage.


# ✅ Defining the test function
def test_text_box_form(nkbrowser, jsondata):  
     This is the main test function.
        - `nkbrowser` → Comes from `conftest.py`, it provides the Playwright browser.
        - `jsondata` → Comes from `conftest.py`, it provides test data from a JSON file.
        This test checks if we can fill and submit a text box form correctly.
    

    # ✅ Creating Page Object Instances
    home_page = HomePage(nkbrowser)  
    elements_page = ElementsPage(nkbrowser)  
    text_box_page = TextBoxPage(nkbrowser)  
    check_box = CheckBox(nkbrowser)  
     These lines create objects for different page classes:
        - `home_page` → Helps interact with the Home Page.
        - `elements_page` → Helps interact with the "Elements" section.
        - `text_box_page` → Helps interact with the Text Box form.
        - `check_box` → Helps interact with the Check Box section.
        All these objects receive `nkbrowser`, which is the Playwright browser instance.
    

    # ✅ Clicking on "Elements" Card to Open the Section
    home_page.click_on_elements()  
     This function clicks on the "Elements" card on the home page.
        It helps us go to the Elements section where we can select options.
    

    # ✅ Expanding the "Elements" Section if Needed
    elements_page.expand_elements_if_needed()  
     This function checks if the "Elements" menu is collapsed.
        If it is collapsed, this function will expand it.
    

    # ✅ Clicking on the "Text Box" Button
    elements_page.click_text_box()  
     This function clicks on the "Text Box" option.
        It takes us to the form where we need to enter details.
    

    # ✅ Filling the Text Box Form Using JSON Data
    text_box_page.fill_form(jsondata)  
     This function fills the form using test data from `jsondata`.
        - It enters Full Name, Email, Current Address, and Permanent Address.
        - The values come from the `input_data.json` file.
    

    # ✅ Submitting the Form
    text_box_page.submit_form()  
     This function clicks the "Submit" button on the form.
        After clicking, it will display the entered details below the form.
    

    # ✅ Verifying the Form Submission
    text_box_page.verify_submission(jsondata)  
     This function checks if the entered values appear correctly after submission.
        - It compares the input data with the displayed output.
        - If the values do not match, the test will fail.
    

    # ✅ Navigating to the "Check Box" Section
    check_box.check_box()  
     This function clicks on the "Check Box" option in the Elements section.
        It helps us navigate to the page where checkboxes are available.
    

    # ✅ Expanding Required Folders in Check Box Section
    check_box.expand_folders()  
     This function expands the necessary folders:
        - "Home" → "Documents" → "WorkSpace"
        - This ensures that the required checkboxes are visible.
    

    # ✅ Selecting the "React" Checkbox
    check_box.navigate_and_select_react()  
     This function selects the "React" checkbox.
        - It navigates inside the folders and clicks on "React".
"""