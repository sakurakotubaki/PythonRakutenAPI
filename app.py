# ホテルの検索
import requests

URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601'
APP_ID = 'アプリID’  # アプリケーションIDを正しいものに置き換えてください。

params = {
    'applicationId': APP_ID,
    'keyword': '東京'
}

res = requests.get(URL, params=params)
print(res.json())

# 楽天市場の検索
import requests

URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20220601?'
APP_ID = '*********'  # アプリケーションIDを正しいものに置き換えてください。

params = {
    'applicationId': APP_ID,
    'keyword': '東京'
}

res = requests.get(URL, params=params)
print(res.json())