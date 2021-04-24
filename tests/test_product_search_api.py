from rakutenapi import product_search_api


def test_get():
    params = {
        'applicationId': '0',
        'keyword': 'あああああああ',
        'format': 'json',
        'formatVersion': 2,
    }
    api = product_search_api.RakutenProductSeadrchApi(params)
    result = api.get()

    assert type(result) is product_search_api.RakutenProductSeadrchApiResult

    products = result.find_products()
    assert type(products) is list
