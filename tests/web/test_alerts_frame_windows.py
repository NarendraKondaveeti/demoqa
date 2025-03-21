from pages.alerts_accept import AlertsPage
from pages.alerts_dismiss import AlertsDismissPage
from pages.windows import Windows
from pages.frames_page import FramePage
from pages.nested_frame import NestedFramePage
from pages.modal_dialogs import ModalDialogs

def test_alerts_frame_windows(browser):
    window = Windows(browser)
    alerts = AlertsPage(browser)
    alert_dismiss = AlertsDismissPage(browser)
    frame_page = FramePage(browser)
    nested_frame_page = NestedFramePage(browser)
    modal_dialogs = ModalDialogs(browser)

    window.navigate_to()
    window.handle_new_page()
    window.handle_new_window()
    window.handle_new_window_message()

    alerts.navigate_to_alert_page()
    alerts.only_accept()
    alerts.dialog_appear_after_5sec()
    alerts.prompt_dialog()
    alert_dismiss.dismiss_alert_dialog()

    frame_page.navigate_to_frames_page()
    frame_page.switch_frames()
    frame_page.scroll_frame()

    nested_frame_page.navigate_to_nested_frames_page()
    nested_frame_page.parent_frame()
    nested_frame_page.child_frame()

    modal_dialogs.navigate_to_modal_dialogs_page()
    modal_dialogs.check_small_modal()
    modal_dialogs.check_large_modal()



