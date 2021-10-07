from tor_python_easy.tor_control_port_client import TorControlPortClient
from tor_python_easy.tor_socks_get_ip_client import TorSocksGetIpClient

if __name__ == '__main__':
    proxy_config = {
        'http': 'socks5://localhost:9050',
        'https': 'socks5://localhost:9050',
    }
    ip_client = TorSocksGetIpClient(proxy_config)
    tor_control_port_client = TorControlPortClient('localhost', 9051, 'test1234')

    for it in range(10):
        old_ip = ip_client.get_ip()
        tor_control_port_client.change_connection_ip(seconds_wait=10)
        new_ip = ip_client.get_ip()
        print(f'iteration {it + 1} ::  {old_ip} -> {new_ip}')
