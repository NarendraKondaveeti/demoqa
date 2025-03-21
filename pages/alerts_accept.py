from playwright.sync_api import Page, expect

class AlertsPage:
    def __init__(self, page:Page):
        self.page = page
        self.alerts_page = page.locator("#item-1").nth(1)
        self.click_me = page.locator("#alertButton")
        self.appear_after_5sec = page.locator("#timerAlertButton")
        self.prompt_alerts = page.locator("#promtButton")
        self.prompt_result = page.locator("#promptResult")

    def navigate_to_alert_page(self):
        self.alerts_page.is_visible()
        self.alerts_page.click()

    def dialog_accept(self, dialog, text=""):
        """Handles alerts and passes input text for prompt dialogs."""
        print(f"Dialog Message: {dialog.message}")  # Debugging Purpose
        dialog.accept(text)  # Accept with text if available

    def only_accept(self):
        self.page.once("dialog", self.dialog_accept)  # Use `once()` to avoid conflicts
        self.click_me.click()

    def dialog_appear_after_5sec(self):
        with self.page.expect_event("dialog") as dialog_info:  # **Waits for dialog**
            self.appear_after_5sec.click()  # **Click and wait**
        dialog_info.value.accept()  # **Accept after waiting**
        print("Dialog Accepted Successfully!")

    def prompt_dialog(self, input_text="Testing"):
        """Handles a prompt alert and passes input text."""
        self.page.once("dialog", lambda dialog: self.dialog_accept(dialog, input_text))  # Pass text
        self.prompt_alerts.click()

        # Verify if the text appears in the UI
        self.prompt_result.wait_for(state="visible")  # Ensure element is visible
        actual_text = self.prompt_result.inner_text()
        expected_text = f"You entered {input_text}"
        assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"


        """
                Handle different types of dialogs with specified action

                Args:
                    dialog: The dialog object from Playwright
                    action: 'accept' or 'dismiss'
                    prompt_text: Text to input for prompt dialogs

        try:
            dialog_type = dialog.type
            print(f"Handling {dialog_type} dialog: {dialog.message}")

            if action.lower() == "accept":
                if dialog_type == "prompt" and prompt_text:
                    dialog.accept(prompt_text)
                else:
                    dialog.accept()
            elif action.lower() == "dismiss":
                dialog.dismiss()
            else:
                raise ValueError("Invalid action. Use 'accept' or 'dismiss'.")
        except Exception as e:
            print(f"Error handling dialog: {str(e)}")
            raise

    def trigger_alert_handle(self, action):
        Trigger and handle a simple alert
        self.page.once("dialog", lambda dialog: self.handle_alert(dialog, action))
        self.click_me.click()
        self.page.wait_for_timeout(500)

    def trigger_5sec_late_alert_and_handle(self, action="accept"):
        Trigger and handle a delayed alert
        self.page.once("dialog", lambda dialog: self.handle_alert(dialog, action))
        with self.page.expect_event("dialog", timeout=10000) as dialog_info:  # Alert listen
            self.appear_after_5sec.click()
        return dialog_info.value

    def prompt_alert_box(self, prompt_text="Testing", action="accept"):
        Handle prompt alert and verify result
        self.page.once("dialog", lambda dialog: self.handle_alert(dialog, action, prompt_text))
        self.prompt_alerts.click()
        if action == "accept":
            # Verify prompt result
            expect(self.prompt_result).to_be_visible(timeout=5000)
            actual_text = self.prompt_result.inner_text()
            expected_text = f"You entered {prompt_text}"
            assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"
            return actual_text
        return None
        """