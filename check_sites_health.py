import requests
import argparse
from datetime import datetime
from whois import whois


def create_parser():
    parser = argparse.ArgumentParser(
        description='Modul for cheking sites health'
    )
    parser.add_argument(
        'url_file',
        help='File includes domains urls.'
    )
    return parser


def load_urls_for_cheking(url_file):
    with open(url_file, 'r') as urls:
        return urls.read().splitlines()


def is_respond_200(url_list):
    respond_200_url_list = []
    for url in url_list:
        respond = requests.get(url)
        if respond:
            respond_200_url_list.append(url)
    return respond_200_url_list


def is_paid_for_month(url_list):
    paid_url_list = []
    days_in_month = 30
    for url in url_list:
        delta = whois(url).expiration_date - datetime.today()
        if delta.days > days_in_month:
            paid_url_list.append(url)
    return paid_url_list


def print_health_domains(url_list, health_status):
    for number, url in list(enumerate(url_list, start=1)):
        print('{}# Domain: {} \tHealth status: {}'.format(
            number,
            url,
            health_status
        ))


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    url_file = load_urls_for_cheking(args.url_file)
    respond_200_url_list = is_respond_200(url_file)
    paid_url_list = is_paid_for_month(url_file)
    not_respond_200_list = list(set(url_file) - set(respond_200_url_list))
    not_paid_list = list(set(url_file) - set(paid_url_list))
    unhealthy_domain_list = list(set(not_respond_200_list) | set(not_paid_list))
    healthy_domain_list = list(set(respond_200_url_list) & set(paid_url_list))
    print_health_domains(healthy_domain_list, 'healthy')
    print_health_domains(unhealthy_domain_list, 'unhealthy')