import plyer
from plyer import notification

notification.notify(
    title="title",
    message="message",
    app_name="company",
    ticker="test",
    app_icon="jellyfish.ico",
    timeout=7
)