# Sites Monitoring Utility

Modul for cheking sites health.

# How to install
Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash

pip install -r requirements.txt # alternatively try pip3

```

# Quickstart

Example of script launch on Windows, Python 3.5:

``` bash


$ python check_sites_health.py url_file.txt


```

Example of program results:

``` bash

Domain: http://yandex.ru, Health status: healthy
Domain: http://mail.ru, Health status: healthy
Domain: http://vk.com, Health status: healthy

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
