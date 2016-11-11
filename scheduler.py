from crontab import CronTab
from datetime import datetime
cron = CronTab(user='joshbenner')
cron.remove_all()

#Spurs schedule
#date = month, day, hour, minute
games = [[11, 10, 22, 13], [11, 10, 1, 15], [11, 11, 23, 59], [11, 12, 23, 59], [11, 14, 23, 59], [11, 17, 1, 59],
        [11, 19, 1, 59],  [11, 21, 23, 59], [11, 23, 23, 59], [11, 25, 23, 59],
        [11, 26, 23, 59], [11, 29, 23, 59], [11, 30, 23, 59], [12, 2, 23, 59],
        [12, 5, 23, 59], [12, 6, 23, 59], [12, 8, 23, 59], [12, 10, 23, 59],
        [12, 14, 23, 59], [12, 15, 23, 59], [12, 18, 23, 59], [12, 20, 23, 59],
        [12, 23, 1, 59], [12, 24, 1, 59], [12, 25, 21, 59], [12, 28, 23, 59],
        [12, 30, 23, 59], [1, 1, 21, 59], [1, 3, 23, 59], [1, 5, 1, 59],
        [1, 7, 23, 59], [1, 10, 23, 59], [1, 12, 23, 59], [1, 14, 23, 59],
        [1, 17, 23, 59], [1, 19, 23, 59], [1, 21, 23, 59], [1, 23, 23, 59],
        [1, 24, 23, 59], [1, 27, 23, 59], [1, 29, 23, 59], [1, 31, 23, 59],
        [2, 2, 23, 59], [2, 4, 23, 59], [2, 6, 23, 59], [2, 8, 23, 59],
        [2, 10, 23, 59], [2, 12, 23, 59], [2, 13, 23, 59], [2, 15, 23, 59],
        [2, 25, 1, 59], [2, 26, 19, 59], [3, 2, 1, 00], [3, 4, 1, 00],
        [3, 5, 1, 00], [3, 6, 23, 59], [3, 8, 23, 59], [3, 9, 23, 59],
        [3, 11, 23, 59], [3, 13, 23, 59], [3, 15, 23, 59], [3, 19, 0, 45],
        [3, 19, 23, 59], [3, 21, 23, 59], [3, 23, 23, 59], [3, 26, 1, 59],
        [3, 27, 23, 59], [3, 29, 1, 59], [3, 31, 1, 59],
        [4, 2, 19, 59], [2, 4, 23, 59], [2, 5, 23, 59], [2, 7, 23, 59],
        [2, 8, 23, 59], [2, 11, 1, 59], [2, 13, 23, 59]]

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