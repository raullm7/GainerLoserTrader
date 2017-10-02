from crontab import CronTab

cron = CronTab(user='raullozano')

job_1h = cron.new(command='python3 main.py')
job_24h = cron.new(command='python3 main.py 0')

job_1h.hour.every(1)
job_24h.day.every(1)

cron.write()
