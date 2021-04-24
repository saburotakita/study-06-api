from rakutenapi import base_api


class RakutenProductSeadrchApi(base_api.RakutenApi):
    """
    商品価格ナビ製品検索API
    詳細：https://webservice.rakuten.co.jp/api/productsearch/
    """
    def __init__(self, params):
        super().__init__(
            RakutenProductSeadrchApiResult,
            'https://app.rakuten.co.jp/services/api/Product/Search/20170426',
            params
        )


class RakutenProductSeadrchApiResult(base_api.RakutenApiResult):
    """
    結果解析用
    詳細：https://webservice.rakuten.co.jp/api/productsearch/
    """
    def __init__(self, response):
        super().__init__(response)

    def find_products(self, keys=None):
        """[Products]のタグでフィルター処理

        Args:
            keys (list, optional): Productsの中でさらにフィルターするキー

        Returns:
            list: 辞書型のリスト
        """
        return self.filter('Products', keys)
