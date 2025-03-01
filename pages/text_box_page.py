from playwright.sync_api import Page

class TextBoxPage:
    def __init__(self, page:Page):
        self.page = page
        self.full_name = page.get_by_placeholder("Full Name")
        self.email = page.locator("#userEmail")
        self.current_address = page.get_by_placeholder('Current Address')
        self.permanent_address = page.locator("#permanentAddress")
        self.submit_button = page.locator("#submit")
        self.output_section = page.locator(".mt-4.row")

    def fill_form(self, data):
        """Fill the text box form with provided data."""
        self.full_name.fill(data["full_name"])
        self.email.fill(data["email"])
        self.current_address.fill(data["current_address"])
        self.permanent_address.fill(data["permanent_address"])

    def submit_form(self):
        """Click the submit button if visible."""
        self.submit_button.click()
        if self.output_section.is_visible():
            self.output_section.click()

    def verify_submission(self, data):
        """Verify the output contains entered data."""
        output_text = self.output_section.inner_text()
        assert data["full_name"] in output_text, "Full Name mismatch!"
        assert data["email"] in output_text, "Email mismatch!"
        assert data["current_address"] in output_text, "Current Address mismatch!"
        assert data["permanent_address"] in output_text, "Permanent Address mismatch!"

"""
# ✅ Importing Playwright's Page class
from playwright.sync_api import Page  
 This line imports `Page` from Playwright.
    - `Page` is a Playwright class that represents a browser tab.
    - It allows us to interact with web pages (click, type, check elements, etc.).
    - This import is needed because we are using `Page` inside this class.


# ✅ Defining the Page Object Class for the Text Box Page
class TextBoxPage:  
 This is a class for the Text Box Page.
    - It contains locators (to find elements on the page).
    - It contains methods (to interact with the page, like filling forms, submitting data, etc.).
    - This class follows the Page Object Model (POM), which makes automation testing **structured and reusable**.

    # ✅ Constructor Method (Runs When the Class is Created)
    def __init__(self, page: Page):  
     This method runs automatically when we create an object of `TextBoxPage`.
        - `page: Page` → It takes a Playwright `Page` instance as input.
        - This `page` instance allows us to interact with the web page.
        - We store this `page` instance in `self.page` so it can be used in other methods.
    
        self.page = page  
         This line stores the Playwright `Page` instance in `self.page`.
            - `self.page` → Now this stores the browser tab.
            - This allows us to use `self.page.locator()` to find elements on the page.
        
        # ✅ Defining Locators for Input Fields and Buttons
        self.full_name = page.get_by_placeholder("Full Name")  
         This locator finds the Full Name input field using its placeholder text.
            - `get_by_placeholder("Full Name")` → Finds an input field with `placeholder="Full Name"`.
            - This makes it easy to find elements without using long XPath.
        
        self.email = page.locator("#userEmail")  
         This locator finds the Email input field.
            - `page.locator("#userEmail")` → Finds the element using CSS ID `userEmail`.
            - `#userEmail` means it's an element with `id="userEmail"`.
        
        self.current_address = page.get_by_placeholder('Current Address')  
         This locator finds the Current Address input field using its placeholder text.
            - `get_by_placeholder("Current Address")` → Finds the field with `placeholder="Current Address"`.
        
        self.permanent_address = page.locator("#permanentAddress")  
         This locator finds the Permanent Address input field.
            - `page.locator("#permanentAddress")` → Finds the field using `id="permanentAddress"`.
        
        self.submit_button = page.locator("#submit")  
         This locator finds the Submit button.
            - `page.locator("#submit")` → Finds the button using `id="submit"`.
        
        self.output_section = page.locator(".mt-4.row")  
         This locator finds the output section (where submitted data appears).
            - `page.locator(".mt-4.row")` → Finds the section using class `mt-4 row`.
        
    # ✅ Method to Fill the Form with JSON Data
    def fill_form(self, data):  
     This method fills the text box form with data from a JSON file.
        - `data` is a Python dictionary containing values (Full Name, Email, etc.).
        - This method types the data into the correct input fields.
    
        self.full_name.fill(data["full_name"])  
         This line types the Full Name from `data` into the Full Name input field.
            - `data["full_name"]` gets the Full Name from the JSON file.
            - `.fill()` method clears existing text and enters new text.
        
        self.email.fill(data["email"])  
         This line types the Email from `data` into the Email input field.
            - `data["email"]` gets the Email from the JSON file.
        
        self.current_address.fill(data["current_address"])  
         This line types the Current Address from `data` into the Current Address input field.
        
        self.permanent_address.fill(data["permanent_address"])  
         This line types the Permanent Address from `data` into the Permanent Address input field.
        
    # ✅ Method to Submit the Form
    def submit_form(self):  
     This method clicks the Submit button.
        - It also checks if the output section appears after submission.
    
        self.submit_button.click()  
         This line clicks the Submit button using the `.click()` method.
        
        if self.output_section.is_visible():  
            self.output_section.click()  
         This block checks if the output section is visible after clicking Submit.
            - `is_visible()` → Checks if the output section appears.
            - `click()` → Clicks on the output section to ensure it is displayed.
        
    # ✅ Method to Verify the Form Submission
    def verify_submission(self, data):  
     This method verifies if the submitted data is displayed correctly.
        - It checks if the values displayed match the values entered in the form.
    
        output_text = self.output_section.inner_text()  
         This line gets the text inside the output section.
            - `inner_text()` gets the visible text inside the element.
            - The text contains the submitted form details.
        
        assert data["full_name"] in output_text, "Full Name mismatch!"  
         This assertion checks if the Full Name in `data` is inside `output_text`.
            - If not, it raises an error: "Full Name mismatch!"
        
        assert data["email"] in output_text, "Email mismatch!"  
         This assertion checks if the Email in `data` is inside `output_text`.
        
        assert data["current_address"] in output_text, "Current Address mismatch!"  
         This assertion checks if the Current Address in `data` is inside `output_text`.
        
        assert data["permanent_address"] in output_text, "Permanent Address mismatch!"  
         This assertion checks if the Permanent Address in `data` is inside `output_text`.
        

"""