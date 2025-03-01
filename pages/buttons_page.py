from playwright.sync_api import Page, expect

class ButtonPage:
    def __init__(self, page:Page):
        self.page = page
        self.button = page.locator("//span[.='Buttons']")
        self.double_button = page.locator("#doubleClickBtn")
        self.right_button = page.locator("#rightClickBtn")
        self.click = page.locator("//button[.='Click Me']")
        self.dynamic_click_message = page.locator("#dynamicClickMessage")
        self.right_click_message = page.locator("#rightClickMessage")
        self.double_click_message = page.locator("#doubleClickMessage")

    def buttons_check(self):
        expect(self.button).to_be_visible()
        self.button.click()
        self.double_button.dblclick()
        self.right_button.click(button="right")
        self.click.click()

        double_click_message = "You have done a double click"
        right_click_message = "You have done a right click"
        dynamic_click_message = "You have done a dynamic click"

        expect(self.right_click_message).to_be_visible()
        assert right_click_message == self.right_click_message.inner_text().strip()

        expect(self.double_click_message).to_be_visible()
        assert double_click_message == self.double_click_message.inner_text().strip()

        expect(self.dynamic_click_message).to_be_visible()
        assert dynamic_click_message == self.dynamic_click_message.inner_text().strip()




