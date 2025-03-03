from playwright.sync_api import Page, expect
import os

class FileDownloadUpload:
    def __init__(self, page:Page):
        self.page = page
        self.file_upload_download_page = page.locator("#item-7").nth(0)
        self.download_button = page.locator("#downloadButton")
        self.choose_file = page.locator("//label[.='Select a file']/following-sibling::input")
        self.file_upload_path = page.locator("#uploadedFilePath")

    def goto_file_download_upload(self):
        self.file_upload_download_page.click()

    def file_download(self):
        self.download_button.click()
        #self.page.pause()
        with self.page.expect_download() as download_info:
            self.download_button.click()  # Click the download button

        download = download_info.value  # Capture the download event

        file_path = download.path()  # Get the temporary downloaded file path
        download.save_as("Downloads/sample.jpeg")  # Save file to a specific location

        print(f"File downloaded: {file_path}")
        self.page.pause()
    def file_upload(self):
        with self.page.expect_file_chooser() as upload_file:
            self.choose_file.click()  # Click to open file chooser

        uploadfile = upload_file.value  # Capture the file chooser

        file_path = "C:/Users/Narendra/Downloads/1.txt"  # Get absolute path
        uploadfile.set_files(file_path)  # Upload the file
        self.page.pause()


