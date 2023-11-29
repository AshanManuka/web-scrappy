from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.topjobs.lk/applicant/vacancybyfunctionalarea.jsp;jsessionid=KS5djcqsnRSHv9yv-g9E8X9w?FA=SDQ').text

soup = BeautifulSoup(page, 'lxml')

desc_box = soup.find_all('table', class_='tbldata_2 vbfa-table')

for p in desc_box:
    job = p.find_all('td')

    for i in job:
        title = i.find('h2')
        company = i.find('h1')
        if title is not None and company is not None:
            print("Job Title : ",title.text)
            print("Company : ",company.text)
            print(" ")
            print("----------------------------------------------------------------")
            
