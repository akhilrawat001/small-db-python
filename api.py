import requests
import os
import json
def check_cache(url,file_name):
    value = os.path.exists('cache/' + file_name)
    if value == True:
        json_data = open('cache/' + file_name).read()
        json_data = json.loads(json_data)
    else:
        raw =  requests.get(url)
        json_data = json.loads(raw.text)
        with open('cache/' + file_name,'w') as file:
            json.dump(json_data,file)
        json_data = open('cache/' + file_name).read()
        json_data = json.loads(json_data)
    return json_data
# content = json.loads(requests.get('http://saral.navgurukul.org/api/courses').text)['availableCourses']
# ids = [course['id'] for course in content]
def get_data(url):
    # url = 'http://saral.navgurukul.org/api/courses/{}/exercises'.format(str(i_d))
    i_d = url[-12:-10] 
    value = check_cache(url, str(i_d) + '.json')
    return value




