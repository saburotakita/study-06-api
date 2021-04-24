from rakutenapi import ichiba_item_ranking_api


def test_get():
    params = {
        'applicationId': '0',
        'genreId': 100283,
        'format': 'json',
        'formatVersion': 2,
    }
    api = ichiba_item_ranking_api.RakutenIchibaItemRankingApi(params)
    result = api.get()

    assert type(result) is ichiba_item_ranking_api.RakutenIchibaItemRankingApiResult

    items = result.filter_items()
    assert type(items) is list
