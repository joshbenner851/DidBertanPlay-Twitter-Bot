from crontab import CronTab
from datetime import datetime
cron = CronTab(user='joshbenner')
cron.remove_all()

#Spurs schedule
#date = month, day, hour, minute
games = [ [11, 6, 3, 0], [11, 12, 11, 59], [11, 14, 11, 59], [11, 16, 11, 59] ]

def createCronJobs(games):
    for x in range(0,len(games)):
        job = cron.new(command='/Library/Frameworks/Python.framework/Versions/3.4/bin/python3 /Users/joshbenner/DidBertansPlay/script.py',)
        job.month.on(games[x][0])
        job.day.on(games[x][1])
        job.hour.on(games[x][2])
        job.minute.on(games[x][3])
        job.enable()
    cron.write()

createCronJobs(games)