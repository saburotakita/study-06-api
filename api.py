from pprint import pprint

import pandas as pd

from rakutenapi import ichiba_item_search_api
from rakutenapi import product_search_api
from rakutenapi import ichiba_item_ranking_api


def main():
    params1 = {
        'applicationId': '0',
        'keyword': 'あああああああ',
        'format': 'json',
        'formatVersion': 2,
    }
    api1 = ichiba_item_search_api.RakutenIchibaItemSearchApi(params1)
    results1 = api1.get_pages(10)
    for result1 in results1:
        pprint(result1.filter_items(['itemName', 'itemPrice']))

    params2 = {
        'applicationId': '0',
        'keyword': 'あああああああ',
        'format': 'json',
        'formatVersion': 2,
    }
    api2 = product_search_api.RakutenProductSeadrchApi(params2)
    result2 = api2.get()
    pprint(result2.find_products(['productName', 'maxPrice', 'minPrice']))
    
    
    params3 = {
        'applicationId': '0',
        'genreId': 100283,
        'format': 'json',
        'formatVersion': 2,
    }
    api3 = ichiba_item_ranking_api.RakutenIchibaItemRankingApi(params3)
    result3 = api3.get()
    df = pd.DataFrame(result3.filter_items(['rank', 'itemName']))
    df.to_csv('ranking.csv')

main()
