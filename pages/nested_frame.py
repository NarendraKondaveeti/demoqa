from playwright.sync_api import Page, expect

class NestedFramePage:
    def __init__(self, page:Page):
        self.page = page
        self.frame_page = page.locator("//li[.='Nested Frames']")

    def navigate_to_nested_frames_page(self):
        self.frame_page.click()

    def parent_frame(self):
        # Step 1: Switch to Parent Frame (#frame1) & Get Text
        parent_frame = self.page.frame("frame1")  # Locate parent frame
        if parent_frame:
            parent_text = parent_frame.locator("body").text_content()
            print("Parent Frame Text:", parent_text.strip())
            return parent_frame  # Return the parent frame
        else:
            return None

    def child_frame(self):
        # Step 2: Get Parent Frame First
        parent_frame = self.parent_frame()
        if parent_frame:
            # Step 3: Locate Child Frame inside Parent Frame
            child_iframe = parent_frame.frame_locator("iframe").first
            child_text = child_iframe.locator("p").text_content()
            print("Child Frame Text:", child_text.strip())
        else:
            print("Child Frame Not Found (Parent Frame Missing)!")