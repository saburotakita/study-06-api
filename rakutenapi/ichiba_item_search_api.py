from rakutenapi import base_api


class RakutenIchibaItemSearchApi(base_api.RakutenApi):
    """
    楽天市場検索API
    詳細：https://webservice.rakuten.co.jp/api/ichibaitemsearch/
    """
    def __init__(self, params):
        super().__init__(
            RakutenIchibaItemSearchApiResult,
            'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706',
            params
        )
    
    def get_pages(self, end_page, ex_params=None):
        """
        複数のページに問い合わせ

        Args:
            end_page (int): 問い合わせするページ数
            ex_params (dict, optional): 追加のGET用クエリ

        Returns:
            list: 各ページの結果解析用クラスのリスト
        """
        if ex_params is None:
            ex_params = {}

        results = []
        for i in range(end_page):
            new_params = dict(ex_params, page=i+1)
            result = self.get(new_params)
            results.append(result)
        return results


class RakutenIchibaItemSearchApiResult(base_api.RakutenApiResult):
    """
    結果解析用
    詳細：https://webservice.rakuten.co.jp/api/ichibaitemsearch/
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
