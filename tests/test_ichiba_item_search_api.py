from rakutenapi import ichiba_item_search_api


def test_get():
    params = {
        'applicationId': '0',
        'keyword': 'あああああああ',
        'format': 'json',
        'formatVersion': 2,
    }
    api = ichiba_item_search_api.RakutenIchibaItemSearchApi(params)
    results = api.get_pages(2)

    assert type(results) is list
    assert len(results) == 2

    result = results[0]
    assert type(result) is ichiba_item_search_api.RakutenIchibaItemSearchApiResult

    items = result.filter_items()
    assert type(items) is list
