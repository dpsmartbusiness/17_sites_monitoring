import requests
import argparse
from datetime import datetime
from whois import whois


def create_parser():
    parser = argparse.ArgumentParser(
        description='Modul for cheking sites health'
    )
    parser.add_argument(
        'urls_file',
        help='File includes domains urls.'
    )
    parser.add_argument(
        '--days_in_month',
        default=30,
        type=int,
        help='Days in month'
    )
    return parser


def load_urls_for_cheking(urls_file):
    with open(urls_file, 'r') as url:
        return url.read().splitlines()


def get_respond_200_url_list(url_list):
    respond_200_url_list = []
    for url in url_list:
        try:
            respond = requests.get(url)
        except requests.ConnectionError:
            continue
        if respond:
            respond_200_url_list.append(url)
    return respond_200_url_list


def get_paid_for_month_url_list(url_list, days_in_month):
    paid_url_list = []
    for url in url_list:
        url_expiration_date = whois(url).expiration_date
        delta = url_expiration_date - datetime.now()
        if delta.days > days_in_month:
            paid_url_list.append(url)
    return paid_url_list


def print_health_domains(url_list, health_status):
    for url in url_list:
        print('Domain: {0:30} Health status: {1:}'.format(
            url,
            health_status
        ))


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    urls_file = load_urls_for_cheking(args.urls_file)
    respond_200_url_list = get_respond_200_url_list(urls_file)
    paid_url_list = get_paid_for_month_url_list(
        respond_200_url_list,
        args.days_in_month
    )
    not_respond_200_list = list(set(urls_file) - set(respond_200_url_list))
    not_paid_list = list(set(urls_file) - set(paid_url_list))
    unhealthy_domain_list = list(set(not_respond_200_list) | set(not_paid_list))
    healthy_domain_list = list(set(respond_200_url_list) & set(paid_url_list))
    print_health_domains(healthy_domain_list, 'healthy')
    print_health_domains(unhealthy_domain_list, 'unhealthy')