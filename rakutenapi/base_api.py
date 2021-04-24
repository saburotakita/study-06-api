import time

import requests


class RakutenApi:
    """
    楽天API接続用のベースクラス
    """
    def __init__(self, result_cls, base_url, params):
        """
        Args:
            result_cls (Class): 解析用のRakutenApiResultベースのクラス
            base_url ([type]): クエリを除いたURL
            params ([type]): クエリ
        """
        self._result_cls = result_cls
        self._base_url = base_url
        self._params = params

    def get(self, ex_params=None):
        """
        GETでの問い合わせ

        Args:
            ex_params (dict, optional): 追加のGET用クエリ

        Returns:
            RakutenApiResultベースのクラス: 解析用クラス
        """
        if ex_params is None:
            ex_params = {}

        # 元の辞書を破壊しないように、クエリを新規で作成して問い合わせ
        new_params = dict(self._params, **ex_params)
        response = requests.get(self._base_url, new_params)

        # 規約に則り1秒につき1回の問い合わせ
        time.sleep(1)

        return self._result_cls(response)


class RakutenApiResult:
    """
    APIのレスポンス解析用のベースクラス
    """
    def __init__(self, response):
        self._json_data = response.json()

    def filter(self, parent_key, child_keys=None):
        """
        [Items]のタグでフィルター処理

        Args:
            parent_key (list): 最初にフィルターするキー
            child_keys (list, optional): parent_keyの中でさらにフィルターするキー

        Returns:
            list: 辞書型のリスト
        """
        # すべてのキーを出力する場合
        if child_keys is None:
            return self._json_data[parent_key]

        # 子要素をさらにフィルターする場合
        children = []
        for child in self._json_data[parent_key]:
            child_dict = {key: child.get(key) for key in child_keys}
            children.append(child_dict)
        return children
