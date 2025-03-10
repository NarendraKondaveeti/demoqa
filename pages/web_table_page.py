from playwright.sync_api import Page, expect

class WebTable:
    def __init__(self, page:Page, data):
        self.page = page
        self.webtable = page.locator("#item-3").nth(0)
        self.searchBox = page.locator("#searchBox")
        self.no_rows = page.locator("//div[.='No rows found']")
        self.add_button = page.locator("#addNewRecordButton")
        self.firs_name = page.get_by_placeholder("First Name")
        self.last_name = page.get_by_placeholder("Last Name")
        self.mail = page.get_by_placeholder("name@example.com")
        self.age = page.get_by_placeholder("Age")
        self.salary = page.get_by_placeholder("Salary")
        self.department = page.get_by_placeholder("Department")
        self.submit = page.locator("#submit")
        self.edit = page.locator(f"//div[normalize-space()='{data['first_name']}']/following-sibling::div[last()]//span[@title='Edit']")

    def navigate_web_table(self):
        expect(self.webtable).to_be_visible()
        self.webtable.click()

    def search_and_add_user(self, data):
        self.searchBox.fill(data["first_name"])  # Fill the search box

        if self.no_rows.is_visible():  # Check if "No rows found" exists
            self.add_button.click()
            self.firs_name.fill(data["first_name"])
            self.last_name.fill(data["last_name"])
            self.mail.fill(data["email"])
            self.age.fill(data["age"])  # Convert age to string
            self.salary.fill(data["salary"])  # Convert salary to string
            self.department.fill(data["department"])
            self.submit.click()
        else:
            if self.firs_name == data["first_name"]:
                self.edit.click()
                self.salary.fill("200000")
                self.submit.click()