#!/usr/bin/env python
import os, json
from selenium import webdriver

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