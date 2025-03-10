import pytest
from pages.forms_page import FormsPage

#@pytest.mark.dependency(depends=["test_elements_page"])  # Wait for first test
def test_forms(browser, jsondata):
        for user_data in jsondata:
                forms_page = FormsPage(browser, user_data)

                forms_page.fill_form(user_data)
                forms_page.select_gender(user_data)
                forms_page.fill_subject(user_data)
                forms_page.date_of_birth(browser, user_data)
                forms_page.select_hobbies(user_data)
                forms_page.file_upload()
                forms_page.select_state_and_city(user_data)
                forms_page.submit()
                forms_page.verify_submitted_data(user_data)
                break