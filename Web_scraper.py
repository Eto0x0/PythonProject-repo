from bs4 import BeautifulSoup
import requests 
import time

print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>') 
print(f"Filtering out {unfamiliar_skill}")


def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=&cboWorkExp1=0').text # .text so we see the text instead of the response code
    soup = BeautifulSoup(html_text, 'lxml') # scraping the url with lxml parser
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for job in jobs:   
        published_date = job.find('span', class_ = 'sim-posted').span.text 
        if 'few' in published_date: # to show post that were made a few days ago
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','') # replace white spaces with nothing
            Skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href'] # [], return's the value of the header element
            if unfamiliar_skill not in Skills: 
                print(f"Company name: {company_name.strip()}")
                print(f"Required Skills: {Skills.strip()}")
                print(f"more info: {more_info}")

                print('')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 1
        print(f'Waiting {time_wait} second...')
        time.sleep(time_wait * 10)





    


        
