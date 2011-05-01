#
# Regular cron jobs for the mylittlecrawler package
#
0 4	* * *	root	[ -x /usr/bin/mylittlecrawler_maintenance ] && /usr/bin/mylittlecrawler_maintenance
