#!/usr/bin/env python
from selenium import webdriver
from datetime import date
import json
import os
import time

def get_browsers_timings(site):
	driver = webdriver.Chrome()
	driver.get(site)
	metrics = ( 'navigationStart', 'redirectStart', 'redirectEnd', 
				'fetchStart', 'domainLookupStart', 'domainLookupEnd', 
				'connectStart', 'connectEnd', 'requestStart', 'responseStart', 
				'responseEnd', 'domLoading', 'domInteractive', 'domContentLoaded', 
				'domComplete', 'loadEventStart', 'loadEventEnd' )
	metric_timings = {}
	metric_timings['url'] = str(site)
	metric_timings['timestamp'] = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
	for metric in metrics:
		script = 'return window.performance.timing.{}'.format(metric)
		metric_timings[metric] = driver.execute_script(script)
	driver.quit()
	return metric_timings

if __name__ == '__main__':
	test = get_browsers_timings('http://www.google.com')
	print(json.dumps(test))