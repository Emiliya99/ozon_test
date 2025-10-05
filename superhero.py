import requests
import re

class SuperHero():
    def __init__(self, api_url):
        self.api_url = api_url

    def get_max_height_superhero(self, gender, occupation):
        ls_height = []
        ls_name = []
        ls_id = []
        ls_num_height = []
        for i in range(252, 290):
            response_appearance = requests.get(f"{self.api_url}{i}/appearance").json()
            response_work = requests.get(f"{self.api_url}{i}/work").json()
            response_biography = requests.get(f"{self.api_url}{i}/biography").json()
            # print(i, response_appearance['gender'], response_appearance['height'], response_name['name'], response_work['occupation'])

            if response_work['occupation'] != '-':
                response_work['occupation'] = True
            else:
                response_work['occupation'] = False

            if response_appearance['gender'] == gender and response_work['occupation'] == occupation:
                ls_height.append(response_appearance['height'])
                ls_name.append(response_biography['name'])
                ls_id.append(i)
        print(ls_height)

        pattern = re.compile(r'\d+\.?\d*')
        for i in range(len(ls_height)):
            ls_num_height.extend([float(num) for num in pattern.findall(ls_height[i][1])])
            # ls_num_height.append([int(num) for num in ls_height[i][1].split() if num.isdigit()])
        max_height = max(ls_num_height)
        name_max = ls_name[ls_num_height.index(max_height)]
        id_max = ls_id[ls_num_height.index(max_height)]
        print(f"Самый высокий герой {gender}: {name_max} (id={id_max}) высотой {max_height}")
