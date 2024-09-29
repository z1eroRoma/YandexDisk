import requests
from typing import Dict, Any

class YandexDiskAPI:
    BASE_URL = 'https://cloud-api.yandex.net/v1/disk/public/resources'

    def __init__(self, public_key: str):
        self.public_key = public_key

    def get_files(self, path: str = '') -> Dict[str, Any]:
        params = {
            'public_key': self.public_key,
            'path': path
        }
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()

        return response.json()

    def get_download_link(self, file_path: str) -> str:
        params = {
            'public_key': self.public_key,
            'path': file_path
        }
        response = requests.get(f'{self.BASE_URL}/download', params=params)
        response.raise_for_status()
        return response.json().get('href')