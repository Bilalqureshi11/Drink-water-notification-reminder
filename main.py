import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title='Please Drink Water Now!!',
            message="""carrying nutrients and oxygen to your cells, flushing bacteria from your bladder, aiding digestion, preventing constipation, normalizing blood pressure.""",
            app_icon="C:\\Users\\Mohd. Bilal\\OneDrive\\python projects\\Water Notification Reminder\\icon.ico",
            timeout=2
        )

        time.sleep(15)
