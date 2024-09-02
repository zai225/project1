import time
from plyer import notification

title = "Drink water Notification"
message = "Its been a will since you have drink water, Zaid drink water."

# Display the notification
notification.notify(
    title=title,
    message=message,
    app_name="My App",
    app_icon=None,
    timeout=10
)

while True:
    show_notification()
    time.sleep(3600)

