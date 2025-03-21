from playwright.sync_api import Page, expect

class FramePage:
    def __init__(self, page:Page):
        self.page = page
        self.frame_page = page.locator("//li[.='Frames']")


    def navigate_to_frames_page(self):
        self.frame_page.click()

    def switch_frames(self):
        iframe = self.page.frame_locator("#frame1")
        text_content = iframe.locator("#sampleHeading").text_content()
        assert text_content == "This is a sample page", f"Expected text not found! Got: {text_content}"
        self.page.pause()
    def scroll_frame(self):
        # Wait for iframe to be available
        self.page.wait_for_selector("#frame2")
        # Locate the iframe
        iframe = self.page.frame("frame2")

        if iframe:
            iframe.evaluate("() => window.scrollBy(0, 100)")  # Vertical
            iframe.evaluate("() => window.scrollBy(100, 0)")  # Horizontal
            print("Scrolling completed!")
        else:
            print("Error: Frame not found!")