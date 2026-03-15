from playwright.sync_api import Page, expect

class APILinksPage:
    def __init__(self, page:Page):
        self.page = page
        self.created = page.locator("#moved")

    def api_call(self):
        with self.page.expect_response("https://demoqa.com/moved") as response_info:
            self.created.click()  # Click the button that triggers the network call

        response = response_info.value  # Capture the response
        print(f"Response URL: {response.url}")
        print(f"Status Code: {response.status}")
        assert response.status == 301, f"Expected 301, but got {response.status}"