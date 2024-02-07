from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(title="Reminder",message="Please drink some water and stretch",timeout=10)
        time.sleep(60*60)
