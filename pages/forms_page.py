from playwright.sync_api import Page, expect
import os

class FormsPage:
    def __init__(self, page:Page):
        self.page = page
        self.forms_page = page.locator("//div[.='Forms']")
        self.practice_form = page.locator("//div[.='Practice Form']")
        self.firstName = page.locator("#firstName")
        self.lastName = page.locator("#lastName")
        self.full_name = page.get_by_placeholder("Full Name")
        self.email = page.locator("#userEmail")
        self.current_address = page.get_by_placeholder('Current Address')
        self.submit_button = page.locator("#submit")
        self.gender = page.locator("input[name='gender']")
        self.mobile_number = page.get_by_placeholder("Mobile Number")
        self.DOB = page.locator("#dateOfBirthInput")
        self.subject = page.locator("#subjectsInput")
        self.upload_file = page.locator("#uploadPicture")
        self.state = page.locator("#react-select-3-input")
        self.city = page.locator("#react-select-4-input")
        self.Hobbies = page.locator("#hobbiesWrapper")

    def fill_form(self, data):
        self.page.pause()
        self.forms_page.click()
        self.practice_form.click()
        self.email.fill(data["email"])
        self.current_address.fill(data["current_address"])
        self.firstName.fill(data["first_name"])
        self.lastName.fill(data["last_name"])
        self.mobile_number.fill(data["Mobile_No"])

    def select_gender(self, data):
        count = self.gender.count()  # Get total gender options
        for i in range(count):
            option_value = self.gender.nth(i).get_attribute("value")  # Get value of each option
            if option_value == data["Gender"]:  # Check if it matches the JSON data
                self.gender.nth(i).check()  # Select the matching gender
                print(f" Selected Gender: {data["Gender"]}")
                break  # Stop loop after selecting
        else:
            print(f" Gender '{data["Gender"]}' not found!")

        self.page.pause()