from playwright.sync_api import Page, expect

class AlertsDismissPage:
    def __init__(self, page:Page):
        self.page = page
        self.confirm_alerts = page.locator("#confirmButton")
        self.confirm_result = page.locator("#confirmResult")

    def alert_dismiss(self, dialog):
        dialog.dismiss()

    def dismiss_alert_dialog(self):
        self.page.once("dialog", self.alert_dismiss)
        self.confirm_alerts.click()

        # Verify if the text appears in the UI
        self.confirm_result.wait_for(state="visible")  # Ensure element is visible
        actual_text = self.confirm_result.inner_text()
        expected_text = f"You selected Cancel"
        assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"