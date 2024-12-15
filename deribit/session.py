from typing import Union, Dict, Optional
import requests


class Session:

    def __init__(self, base_url: str, debug: bool) -> None:
        self.base_url = base_url
        self.debug = debug

    def get_url(self, end_point) -> str:
        return f'{self.base_url}/{end_point}'

    def execute_get_request(self, end_point: str, params: Optional[Dict[str, Union[str, float, int]]] = None) -> requests.Response:
        url = self.get_url(end_point=end_point)
        if self.debug:
            print(f'executing get request on {url}')
        response = requests.get(url=url, params=params)
        if self.debug:
            print(f'executed get request on {url}')
        return response
