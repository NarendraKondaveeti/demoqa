from playwright.sync_api import Page, expect

class ModalDialogs:
    def __init__(self, page:Page):
        self.page = page
        self.modal_dialogs_page = page.locator("//span[.='Modal Dialogs']")
        self.small_modal = page.locator("#showSmallModal")
        self.small_model_text = page.locator(".modal-body")
        self.close_small_modal = page.locator("#closeSmallModal")
        self.small_modal_expected_text = "This is a small modal. It has very less content"
        self.large_modal = page.locator("#showLargeModal")
        self.large_modal_expected_text = "It has survived not only five centuries"
        self.large_modal_text = page.locator(".modal-body")
        self.large_modal_close = page.locator("#closeLargeModal")

    def navigate_to_modal_dialogs_page(self):
        self.modal_dialogs_page.click()

    def check_small_modal(self):
        self.small_modal.click()
        actual_text = self.small_model_text.inner_text()
        assert actual_text == self.small_modal_expected_text, f"Expected '{self.small_modal_expected_text}', but got '{actual_text}'"
        self.close_small_modal.is_visible()
        self.close_small_modal.click()

    def check_large_modal(self):
        self.large_modal.click()
        actual_text = self.large_modal_text.inner_text()
        assert self.large_modal_expected_text in actual_text
        self.large_modal_close.is_visible()
        self.large_modal_close.click()