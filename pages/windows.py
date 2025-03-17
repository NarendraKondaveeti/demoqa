from playwright.sync_api import Page, expect
import os

class Windows:
    def __init__(self, page:Page):
        self.page = page
        self.alert_frame_windows = page.get_by_text("Alerts, Frame & Windows")
        self.browser_windows = page.locator("//span[.='Browser Windows']")
        self.new_tab = page.locator("#tabButton")
        self.new_window = page.locator("#windowButton")
        self.new_window_message = page.locator("#messageWindowButton")

    def navigate_to(self):
        self.alert_frame_windows.click()
        self.browser_windows.click()

    def handle_new_page(self):
        with self.page.expect_popup() as new_paper:
            self.page.pause()
            self.new_tab.click()
        new_page = new_paper.value
        expect(new_page).to_have_url("https://demoqa.com/sample")
        new_page.close()

    def handle_new_window(self):
        with self.page.expect_popup() as new_window:
            self.new_window.click()
        new_page = new_window.value
        expect(new_page).to_have_url("https://demoqa.com/sample")
        new_page.close()

    def handle_new_window_message(self):
        with self.page.expect_popup() as new_window_popup:
            self.new_window_message.click()
        new_page = new_window_popup.value  # Opened new window reference
       # Use new_page instead of self.page
        expect(new_page.locator("body")).to_contain_text("Knowledge increases by sharing but not by saving.")
        new_page.close()