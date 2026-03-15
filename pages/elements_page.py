from playwright.sync_api import Page

class ElementsPage:
    def __init__(self, page:Page):
        self.page = page
        self.expand_button = "//div[contains(@class, 'header-wrapper')]//div[@class='icon']"
        self.text_box_button = "//li[.='Text Box']"

    def expand_elements_if_needed(self):
        """Expand 'Elements' section if collapsed."""
        if self.page.locator(self.text_box_button).nth(0).is_disabled():
            self.page.locator(self.expand_button).click()

    def click_text_box(self):
        """Click on 'Text Box' button."""
        self.page.locator(self.text_box_button).click()