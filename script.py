import csv
import parameters
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def validate_field(field):
   
    if field:
        pass
    else:
        field = 'No results'
    return field

writer = csv.writer(open(parameters.file_name, 'wb'))

writer.writerow(['Name', 'Job Title', 'College', 'Experience', 'Location', 'URL'])

driver = webdriver.Chrome('C:\Webdrivers\chromedriver.exe')
driver.get('https://www.linkedin.com')

username = driver.find_element_by_class_name('login-email')
#enter your own LinkedIn email address
username.send_keys('')

password = driver.find_element_by_class_name('login-password')
#enter your own LinkedIn password
password.send_keys('')

log_in_button = driver.find_element_by_id('login-submit')
log_in_button.click()

driver.get('https:www.google.com')

search_query = driver.find_element_by_name('q')
search_query.send_keys(parameters.search_query)

search_query.send_keys(Keys.RETURN)

for i in range(1,3):
	linkedin_urls = driver.find_elements_by_class_name('iUh30')
	linkedin_urls = [url.text for url in linkedin_urls]
	
	sleep(0.5)

	for linkedin_url in linkedin_urls:
		driver.get(linkedin_url)
		sleep(5)
	
		sel = Selector(text=driver.page_source)
	
		name = sel.xpath('//*[starts-with(@class, "pv-top-card-section__name")]/text()').extract_first()
	
		if name:
			name = name.strip()
	
		job_title = sel.xpath('//*[starts-with(@class, "pv-top-card-section__headline")]/text()').extract_first()
	
		if job_title:
			job_title = job_title.strip()
		
		college = sel.xpath('//*[starts-with(@class, "pv-top-card-v2-section__entity-name pv-top-card-v2-section__school-name")]/text()').extract_first()
	
		if college:
			college = college.strip()
	
		experience = sel.xpath('//*[starts-with(@class, "pv-skill-category-entity__name-text")]/text()').extract_first()
	
		if experience:
			experience = experience.strip()
	
		location = sel.xpath('//*[starts-with(@class, "pv-top-card-section__location")]/text()').extract_first()
	
		if location:
			location = location.strip()
	
		linkedin_url = driver.current_url
	
		name = validate_field(name)
		job_title = validate_field(job_title)
		college = validate_field(college)
		experience = validate_field(experience)
		location = validate_field(location)
		linkedin_url = validate_field(linkedin_url)
	
		writer.writerow([name.encode('utf-8'),
			job_title.encode('utf-8'),                  
			college.encode('utf-8'),
			experience.encode('utf-8'),
			location.encode('utf-8'),
			linkedin_url.encode('utf-8')])
			
	driver.get('https:www.google.com')

	search_query = driver.find_element_by_name('q')
	search_query.send_keys(parameters.search_query)
	search_query.send_keys(Keys.RETURN)
	google_next = driver.find_element_by_class_name('pn')
	google_next.click()

	

driver.quit()