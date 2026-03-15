from playwright.sync_api import Page, expect
import os

class FormsPage:
    def __init__(self, page:Page, data):
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
        self.subject = page.locator("#subjectsInput")
        self.upload_file = page.locator("#uploadPicture")
        self.state = page.locator("#react-select-3-input")
        self.city = page.locator("#react-select-4-input")

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
                self.gender.nth(i).scroll_into_view_if_needed()  # Ensure the element is in view
                self.gender.nth(i).click(force=True)  # Click forcefully
                print(f" Selected Gender: {data["Gender"]}")
                break  # Stop loop after selecting
        else:
            print(f" Gender '{data["Gender"]}' not found!")

    def fill_subject(self, data):
        subjects_list = data["Subjects"]  # Get subjects from JSON (list)

        for subject in subjects_list:  # Loop through each subject
            partial_text = subject[:1]  # Get first 2 letters of the subject
            self.subject.press_sequentially(partial_text)  # Type first two letters
            self.page.wait_for_selector(".subjects-auto-complete__menu")  # Wait for dropdown

            dropdown_options = self.page.locator(".subjects-auto-complete__option")  # Get options
            count = dropdown_options.count()  # Get total options

            for i in range(count):
                option_text = dropdown_options.nth(i).inner_text()  # Get option text

                if option_text == subject:  # Compare with JSON subject
                    dropdown_options.nth(i).click()  # Select subject
                    print(f" Selected Subject: {option_text}")
                    break  # Stop searching for this subject
            self.page.wait_for_timeout(500)  # Small delay before next input

    def date_of_birth(self, page:Page, data):
        dob = data["DOB"]
        self.page = page
        page.locator("#dateOfBirthInput").click()
        page.select_option(".react-datepicker__year-select", dob[2])

        # Select Month (April = index 3, so subtract 1)
        page.select_option(".react-datepicker__month-select", str(int(dob[1]) - 1))

        # Select Day (300
        page.click(f".react-datepicker__day--{'0'+ dob[0]}")

        # Wait to see selection
        page.wait_for_timeout(2000)

    def select_hobbies(self, data):
        checkboxes = self.page.locator("#hobbiesWrapper .custom-control")
        for checkbox in range(checkboxes.count()):
            checkbox_option = checkboxes.nth(checkbox).inner_text()

            if checkbox_option in data["Hobbies"]:
                checkboxes.nth(checkbox).scroll_into_view_if_needed()
                checkboxes.nth(checkbox).click(force=True)

    def file_upload(self):
        with self.page.expect_file_chooser() as upload_file:
            self.upload_file.click()  # Click to open file chooser

        upload_file = upload_file.value  # Capture the file chooser

        file_path = "D:\demoqa\Downloads\sample.jpeg"  # Get absolute path

        upload_file.set_files(file_path)  # Upload the file

    def select_state_and_city(self, data):

        def state_selection():
            # Step 1: Click on the dropdown to activate it
            self.page.locator("#state").click()

            # Step 2: Type the state name
            self.page.locator("#state input[id^='react-select']").fill(data["State"])

            # Step 3: Wait for the dropdown options to appear
            self.page.wait_for_timeout(500)  # Small wait for dropdown to load

            # Step 4: Press Enter to select the first matching option
            self.page.locator("#state input[id^='react-select']").press("Enter")

        def city_selection():
            # Step 1: Click on the dropdown to activate it
            self.page.locator("#state").click()

            # Step 2: Type the City name
            self.page.locator("#city input[id^='react-select']").fill(data["City"])

            # Step 3: Wait for the dropdown options to appear
            self.page.wait_for_timeout(500)  # Small wait for dropdown to load

            # Step 4: Press Enter to select the first matching option
            self.page.locator("#city input[id^='react-select']").press("Enter")
        # ❗ Calling internal functions inside the outer function
        state_selection()
        city_selection()

    def submit(self):
        submit = self.page.locator("#submit")
        submit.click()

    def verify_submitted_data(self, data):
        """Verifies if the submitted form contains correct values and highlights mismatches"""

        # ANSI Color Codes for Console Output
        GREEN = "\033[92m"  # Green for matches
        RED = "\033[91m"  # Red for mismatches
        RESET = "\033[0m"  # Reset color

        # Expected data mapping
        expected_data = {
            "Student Name": f"{data['first_name']} {data['last_name']}",
            "Student Email": data["email"],
            "Gender": data["Gender"],
            "Mobile": data["Mobile_No"],
            "Date of Birth": f"{data['DOB'][0]} {self.get_month_name(data['DOB'][1])},{data['DOB'][2]}",
            "Subjects": ", ".join(data["Subjects"]),
            # Check if "Hobbies" is a list
            # If it is a list, join all items with ", " (comma and space) to make a single string
            # If it is already a string, keep it as it is
            "Hobbies": ", ".join(data["Hobbies"]) if isinstance(data["Hobbies"], list) else data["Hobbies"], #isinstance() checks what type of data it is!
            "Picture": "sampleFile.jpeg",  # Assuming fixed file name
            "Address": data["current_address"],
            "State and City": f"{data['State']} {data['City']}",
        }

        # Verify each label
        for label, expected_value in expected_data.items():
            row_locator = self.page.locator(f"//tr[td[text()='{label}']]")

            if row_locator.count() == 0:
                print(f"{RED}Label '{label}' not found in the table!{RESET}")
                continue

            actual_value = row_locator.locator("td:nth-child(2)").text_content().strip()

            if actual_value == expected_value:
                print(f"{GREEN}Match Found: {label} -> {actual_value}{RESET}")
            else:
                print(f" {RED}Mismatch: {label} -> Expected: '{expected_value}', Found: '{actual_value}'{RESET}")

    def get_month_name(self, month_number):
        """Helper function to convert month number to name"""
        months = {
            "01": "January", "02": "February", "03": "March", "04": "April",
            "05": "May", "06": "June", "07": "July", "08": "August",
            "09": "September", "10": "October", "11": "November", "12": "December"
        }
        return months.get(str(month_number), "Invalid")
