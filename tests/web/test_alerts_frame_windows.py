from pages.alerts import AlertsPage
from pages.windows import Windows

def test_alerts_frame_windows(browser):
    window = Windows(browser)
    alerts = AlertsPage(browser)



    window.navigate_to()
    window.handle_new_page()
    window.handle_new_window()
    window.handle_new_window_message()

    alerts.navigate_to_alert_page()
    alerts.trigger_alert_handle()
    alerts.trigger_5sec_late_alert_and_handle()
    alerts.handle_alert_with_tab()
    alerts.prompt_alert_box()


