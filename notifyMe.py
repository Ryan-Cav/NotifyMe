import psutil as ps
import time
from datetime import datetime as t, date as d, timedelta
import plyer.platforms.win.notification
from plyer import notification

def checkIfRunning(processName):
    for proc in ps.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (ps.NoSuchProcess, ps.AccessDenied, ps.ZombieProcess):
            pass
    return False;

totalDuration = timedelta(0,0,0,0,0,0,0)
done = False
while not done:
    duration = timedelta(0,0,0,0,0,0,0)
    if checkIfRunning('rocketleague'):
        start = t.now().time()
        while checkIfRunning('rocketleague'):
            now = t.now().time()
            duration = t.combine(d.min,now) - t.combine(d.min,start)
            if totalDuration+duration > timedelta(0,0,0,0,0,1,0):
                break
    totalDuration += duration
    if totalDuration > timedelta(0,0,0,0,0,1,0):
        notification.notify("TIMES UP!", "You have played for 1 hour")
        done = True
        break
        
    time.sleep(5)

