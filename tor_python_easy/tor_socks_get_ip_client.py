from typing import Dict, Optional

import requests


class TorSocksGetIpClient:
    requests_proxies: Dict[str, str]

    def __init__(self, requests_proxies: Dict[str, str]):
        self.requests_proxies = requests_proxies

    def get_ip(self) -> Optional[str]:
        return requests.get('https://www.ifconfig.me/ip', proxies=self.requests_proxies).text
