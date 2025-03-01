from playwright.sync_api import Page, expect

class Radiobutton:
    def __init__(self, page:Page, data):
        self.page = page
        self.Radio_button = data["Radio_button"]
        self.radio_button_page = page.locator("//span[.='Radio Button']")
        self.radio_selection = page.locator(f"//label[.='{self.Radio_button}']")
        self.result_message = page.locator(".mt-3")

    def navigate_radio_button_page(self):
        expect(self.radio_button_page).to_be_visible()
        self.radio_button_page.click()

    def select_radio_button(self):
        self.radio_selection.click()

        expected_text = f"You have selected {self.Radio_button}"

        # Get the actual displayed message
        actual_text = self.result_message.inner_text().replace("\n", " ").strip()

        # Validate the actual message against the expected message
        assert expected_text == actual_text, f" Expected '{expected_text}', but got '{actual_text}'"




