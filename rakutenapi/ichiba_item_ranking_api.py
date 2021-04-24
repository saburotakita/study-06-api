from rakutenapi import base_api


class RakutenIchibaItemRankingApi(base_api.RakutenApi):
    """
    楽天市場ランキングAPI
    詳細：https://webservice.rakuten.co.jp/api/ichibaitemranking/
    """
    def __init__(self, params):
        super().__init__(
            RakutenIchibaItemRankingApiResult,
            'https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628',
            params
        )


class RakutenIchibaItemRankingApiResult(base_api.RakutenApiResult):
    """
    結果解析用
    詳細：https://webservice.rakuten.co.jp/api/ichibaitemranking/
    """
    def __init__(self, response):
        super().__init__(response)

    def filter_items(self, keys=None):
        """[Items]のタグでフィルター処理

        Args:
            keys (list, optional): Itemsの中でさらにフィルターするキー

        Returns:
            list: 辞書型のリスト
        """
        return self.filter('Items', keys)
