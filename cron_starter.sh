echo "PATH='/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin'
*/1 * * * * cd /Users/raullozano/Raul/GainerLoserTrader && /Users/raullozano/Raul/GainerLoserTrader/main.py 2&>cron_log
0 12 * * * cd /Users/raullozano/Raul/GainerLoserTrader && /Users/raullozano/Raul/GainerLoserTrader/main.py 0 2&>cron_log" >> mycron
crontab mycron
rm mycron