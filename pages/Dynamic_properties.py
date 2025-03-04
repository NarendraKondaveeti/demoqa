from playwright.sync_api import Page, expect


class DynamicProperties:
    def __init__(self, page:Page):
        self.page = page
        self.dynamic_page = page.locator("#item-8").nth(0)
        self.random_id = page.locator("//p[.='This text has random Id']")
        self.button_enabled = page.locator("#enableAfter")
        self.colorChange = page.locator("#colorChange")
        self.visibleAfter = page.locator("#visibleAfter")

    def navigate_to_dynamic_page(self):
        self.dynamic_page.click()

    def text_check(self):
        expected_text = "This text has random Id"
        expect(self.random_id).to_be_visible()
        actual_text = self.random_id.inner_text().strip()

        # Validate the actual message against the expected message
        assert expected_text == actual_text, f" Expected '{expected_text}', but got '{actual_text}'"

    def check_button_enable(self):
        expect(self.button_enabled).to_be_visible()

    def text_color_check(self):
        # Get the initial class attribute before color change
        initial_class = self.colorChange.get_attribute("class")
        print(f"Initial class: {initial_class}")  # Debugging

        self.page.wait_for_function("document.querySelector('#colorChange').classList.contains('text-danger')")

        # Get the new class attribute after color change
        new_class = self.colorChange.get_attribute("class")
        print(f"New class: {new_class}")  # Debugging

        # Validate that the class has changed
        assert "text-danger" in new_class, f" Color did not change! Expected 'text-danger' but got: {new_class}"
        print("Color changed successfully!")

    def visible_after_5sec(self):
        expect(self.visibleAfter).to_be_visible()
        print("visible after 5 seconds")