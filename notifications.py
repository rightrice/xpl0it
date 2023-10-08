import plyer
from plyer import notification

notification.notify(
    title="title",
    message="message",
    app_name="ASPECT Security",
    ticker="test",
##  app_icon="test.ico",
    timeout=7
)