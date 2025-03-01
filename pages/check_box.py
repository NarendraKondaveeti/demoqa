from playwright.sync_api import Page, expect
from pages.expected_messages import expected_messages

class CheckBox:
    def __init__(self, page:Page, data):
        self.page = page
        self.checkbox_name = data['checkbox_name']
        self.checkbox = page.locator("//span[.='Check Box']")
        self.expand_home = page.locator("//span[text()='Home']/parent::label/preceding-sibling::button")
        self.expand_documents = page.locator("//span[text()='Documents']/parent::label/preceding-sibling::button")
        self.expand_workspace = page.locator("//span[text()='WorkSpace']/parent::label/preceding-sibling::button")
        self.select_checkbox = page.locator(f"//span[text()='{self.checkbox_name}']")
        self.result_message = page.locator("#result")

    def check_box(self):
        """Click the Check Box section if visible."""
        expect(self.checkbox).to_be_visible()
        self.checkbox.click()

    def expand_folder(self, locator):
        """Expands a folder only if it's collapsed."""
        if locator.get_attribute("class") and "rct-collapse" in locator.get_attribute("class"):
            locator.click()

    def expand_folders(self):
        """Expands Home → Documents → WorkSpace if not already expanded."""
        expect(self.expand_home).to_be_visible()
        self.expand_home.click()

        expect(self.expand_documents).to_be_visible()
        self.expand_documents.click()

        expect(self.expand_workspace).to_be_visible()
        self.expand_workspace.click()

    def navigate_and_select_checkbox(self):
        """Selects a checkbox dynamically and verifies the correct message appears."""
        self.select_checkbox.click()

        # Get the correct expected text from the imported dictionary
        expected_text = expected_messages.get(self.checkbox_name, f"You have selected : {self.checkbox_name}")

        # Get the actual displayed message
        actual_text = self.result_message.inner_text().replace("\n", " ").strip()

        # Validate the actual message against the expected message
        assert expected_text.replace("\n", " ") in actual_text, f" Expected '{expected_text}', but got '{actual_text}'"