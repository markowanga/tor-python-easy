# tor-python-easy

-------

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

1. First one is using docker and docker-compose from this repo. You can manipulate with mapping ports and password.
   ```bash
   docker-compose up
   ```
2. Second one uses tor installed in OS
   ```bash
   tor --configport 9051 
   ```


## Use lib with python