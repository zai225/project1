from plyer import notification

# Title and message for the notification
title = "Drink water Notification"
message = "Its been a will since you have drink water, Zaid drink water."

# Display the notification
notification.notify(
    title=title,
    message=message,
    app_name="My App",        # Optional: The name of the application
    app_icon=None,            # Optional: Path to an icon file (e.g., ".ico" file)
    timeout=10                # Optional: Duration in seconds for which the notification stays on screen
)


