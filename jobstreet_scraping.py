import requests
from bs4 import BeautifulSoup
import pandas as pd


key = 'data-analyst'
loc = 'jakarta-raya'
url = 'https://www.jobstreet.co.id/id/job-search/{}-jobs-in-{}/'.format(key, loc)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

data_all = []
for page in range (1,23):
    res = requests.get(url+str(page), headers=headers)
    # print(res.status_code)
    soup = BeautifulSoup(res.text, 'html.parser')
    items = soup.findAll('div', 'sx2jih0 zcydq876 zcydq866 zcydq896 zcydq886 zcydq8n zcydq856 zcydq8f6 zcydq8eu')
    for item in items:
        try : logo = item.find('div', 'sx2jih0 zcydq8bm').find('img', 'sx2jih0 rqoqz6')['src']
        except : logo = 'no image'
        job_name = item.find('span', 'sx2jih0').text
        company = item.find('span', 'sx2jih0 iwjz4h1 zcydq84u zcydq80 zcydq8r').text
        location = item.find('a', {'data-automation': 'jobCardLocationLink'}).text
        time_upload = item.find('span', 'sx2jih0 zcydq84u es8sxo0 es8sxo1 es8sxo22 es8sxoh').text
        data_dict = {
            'Company Logo':logo,
            'Job Name':job_name,
            'Company':company,
            'Location':location,
            'Time Upload':time_upload
        }
        data_all.append(data_dict)
df = pd.DataFrame(data_all)
df.to_excel('jobstreet_data.xlsx', index=False)