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

1# Url: https://yandex.ru
HTTP status 200: OK
Domain paid more than 30 days: TRUE


2# Url: https://mail.ru
HTTP status 200: OK
Domain paid more than 30 days: TRUE

3# string is empty. Check in your file

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
