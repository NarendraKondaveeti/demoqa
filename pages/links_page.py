from playwright.sync_api import Page, expect

class LinksPage:
    def __init__(self, page:Page):
        self.page = page
        self.link_page = page.locator("//li[.='Links']")
        self.home_link = page.locator("#simpleLink")
        self.dynamic_link = page.locator("#dynamicLink")
        self.created = page.locator("#created")
        self.moved = page.locator("#moved")
        self.no_content = page.locator("#no-content")
        self.bad_request = page.locator("#bad-request")
        self.unauthorized = page.locator("#unauthorized")
        self.forbidden = page.locator("#forbidden")
        self.invalid_url = page.locator("#invalid-url")
        self.linkResponse = page.locator("#linkResponse")

    def navigate_to_links_page(self):
        expect(self.link_page).to_be_visible()
        self.link_page.click()



