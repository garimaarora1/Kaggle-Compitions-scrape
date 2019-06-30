# -*- coding: utf-8 -*-
import scrapy
import json

class KaggleSpider(scrapy.Spider):
    name = 'kaggle'

    start_urls = [
    'https://www.kaggle.com/competitions.json?sortBy=grouped&group=general&page=1&pageSize=20'
    ]

    def parse(self, response):
        data=json.loads(response.text)
        
        for i in data['fullCompetitionGroups'][1]['competitions']:
            yield{
            'Competition Title': i['competitionTitle'],
            'Competition Description':i['competitionDescription'],
            'Total Teams':i['totalTeams'],
            'Reward Quantity':i['rewardQuantity'],
            'Reward Type Name':i['rewardTypeName'],
            'Reward Display':i['rewardDisplay'],
            'Organization Name':i['organizationName'],
            'Host Segment Title':i['hostSegmentTitle'],
            'Deadline':i['deadline'],
            }
