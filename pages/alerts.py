from playwright.sync_api import Page, expect


class AlertsPage:
    def __init__(self, page:Page):
        self.page = page
        self.alerts_page = page.locator("#item-1").nth(1)
        self.click_me = page.locator("#alertButton")
        self.appear_after_5sec = page.locator("#timerAlertButton")
        self.confirm_alerts = page.locator("#confirmButton")
        self.prompt_alerts = page.locator("#promtButton")
        self.prompt_result = page.locator("#promptResult")

    def navigate_to_alert_page(self):
        # self.alerts_page.is_visible()
        self.alerts_page.click()

    def handle_alert(self, dialog):
        dialog.accept()

    def trigger_alert_handle(self):
        self.page.once("dialog", self.handle_alert)  # Alert listen
        self.click_me.click()

    def trigger_5sec_late_alert_and_handle(self):
        self.page.once("dialog", lambda dialog :dialog.accept())
        self.appear_after_5sec.click()

    def handle_alert_with_tab(self):
        self.page.once("dialog", lambda dialog: dialog.dismiss())
        self.confirm_alerts.click()
        # Wait for confirmation message update
        confirm_result = self.page.locator("#confirmResult")
        confirm_result.wait_for(state="attached")

        cancel_message = confirm_result.inner_text()
        expected_message = "You selected Cancel"

        assert cancel_message == expected_message, f"Expected '{expected_message}', but got '{cancel_message}'"

    def prompt_alert_box(self, prompt = "Testing"):
        self.page.once("dialog", lambda dialog: dialog.accept(prompt))
        self.prompt_alerts.click()
        # **Verify the entered text is updated in UI (if applicable)**
        prompt_result = self.page.locator("#promptResult")
        assert prompt_result.inner_text() == f"You entered {prompt}", "You entered Testing"

