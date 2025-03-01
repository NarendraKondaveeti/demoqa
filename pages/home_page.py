from playwright.sync_api import Page

class HomePage:
    def __init__(self, page:Page):
        self.page = page
        self.elements_card = page.locator(".card").nth(0)  # Click on "Elements"

    def click_on_elements(self):
        self.elements_card.click()
