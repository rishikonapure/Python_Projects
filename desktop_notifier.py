# Set windows notifications
#Usage --
	# pip install win10toast
	# pip install schedule
	# python desktop_notifier.py 

import win10toast
toaster = win10toast.ToastNotifier()
import schedule
import time
def job():
    toaster.show_toast('Reminder', "Drink some water!", duration = 15)
#scheduling for every hour; 
#you can even change the scheduled time with schedule library
schedule.every().hour.do(job)  
while True:
    schedule.run_pending()
    time.sleep(1)