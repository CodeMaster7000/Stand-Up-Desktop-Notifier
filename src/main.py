import time
from datetime import datetime
from plyer import notification

def remind_to_stand(interval_minutes=60):
    try:
        while True:
            notification.notify(
                title='Stand Up Reminder',
                message='Time to stand up and stretch!',
                timeout=10
            )
            log_reminder()
            time.sleep(interval_minutes * 60)
    except KeyboardInterrupt:
        print("\nReminder stopped.")

def log_reminder():
    with open("reminder_log.txt", "a") as log_file:
        log_file.write(f"Reminder at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

if __name__ == "__main__":
    try:
        interval = input("Enter the reminder interval in minutes (default is 60): ")
        if interval.strip() == "":
            interval = 60
        else:
            interval = int(interval)
            if interval <= 0:
                raise ValueError("Interval must be a positive integer.")
    except ValueError as e:
        print(f"Invalid input: {e}. Using default interval of 60 minutes.")
        interval = 60

    remind_to_stand(interval)
