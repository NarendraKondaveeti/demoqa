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

    def handle_home_link_click(self):
        with self.page.expect_popup() as popup_info:
            self.home_link.click()
        new_page = popup_info.value
        expect(new_page).to_have_url("https://demoqa.com/")  # Replace with the actual URL or condition
        # Add more actions or assertions on the new_page as needed
        new_page.close()

    def dynamic_link_click(self):
        with self.page.expect_popup() as popup_info:
            self.dynamic_link.click()
        new_page = popup_info.value
        expect(new_page).to_have_url("https://demoqa.com/")  # Replace with the actual URL or condition
        # Add more actions or assertions on the new_page as needed
        new_page.close()

        self.created.click()
        expected_text = "Link has responded with staus 201 and status text Created"
        expect(self.linkResponse).to_be_visible()
        assert expected_text == self.linkResponse.inner_text().strip()






