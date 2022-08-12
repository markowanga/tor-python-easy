# tor-python-easy

**tor-python-easy** was developed for use tor proxy in python with easy interface, which allow for
changing ip address whenever you want.

Repo is very simple but if you want you can **add new feature request**.

## Donate

If you want to sponsor me, in thanks for the project, please send me some crypto 😁:

|Coin|Wallet address|
|---|---|
|Bitcoin|`3EajE9DbLvEmBHLRzjDfG86LyZB4jzsZyg`|
|Etherum|`0xE43d8C2c7a9af286bc2fc0568e2812151AF9b1FD`|

## Installation

Library is only one file, so you can copy it to project.

However, if you want you can install it with pip:

```bash
pip3 install tor-python-easy
```

## Run tor proxy

There are two simple ways to run tor proxy.

1. First one is using docker and docker-compose from this repo. You can manipulate with mapping
   ports and password.
   ```shell
   docker-compose up
   ```
2. Second one uses tor installed in OS
   ```shell
   tor --controlport 9051 
   ```

## Use lib with python

1. In terminal
   ```shell
   docker-compose up
   ```
2. In Python
   ```python
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
   ```
   
   Output will give 10 IP migrations.
