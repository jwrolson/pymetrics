#!/usr/bin/env python
from selenium import webdriver
from datetime import date
import json
import os
import time

def get_browsers_timings(site):
	driver = webdriver.Chrome()
	driver.get(site)

	timings = []

	scripts = [ 'return window.performance.timing.toJSON()',
				'return window.performance.getEntries()']

	for script in scripts:
		output = driver.execute_script(script)
		timings.append(output)

	driver.quit()

	return timings

if __name__ == '__main__':
	test = get_browsers_timings('http://www.google.com')
	print(json.dumps(test))