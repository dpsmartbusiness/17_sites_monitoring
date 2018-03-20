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


def load_urls_for_cheking(urls_filepath):
    with open(urls_filepath, 'r') as urls_file:
        return urls_file.read().splitlines()


def get_respond_200_url_list(url_list):
    respond_200_url_list = []
    for url in url_list:
        try:
            respond = requests.get(url)
        except requests.ConnectionError:
            continue
        except requests.exceptions.MissingSchema:
            continue
        if respond:
            respond_200_url_list.append(url)
    return respond_200_url_list


def get_paid_for_month_url_list(url_list, days_in_month):
    paid_url_list = []
    for url in url_list:
        url_expiration_date = whois(url).expiration_date
        if type(url_expiration_date) is list:
            url_expiration_date = url_expiration_date[0]
        elif url_expiration_date is None:
            continue
        delta = url_expiration_date - datetime.today()
        if delta.days > days_in_month:
            paid_url_list.append(url)
    return paid_url_list


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    urls_file = load_urls_for_cheking(args.urls_file)
    respond_200_url_list = get_respond_200_url_list(urls_file)
    paid_url_list = get_paid_for_month_url_list(
        urls_file,
        args.days_in_month
    )
    not_respond_200_list = list(set(urls_file) - set(respond_200_url_list))
    not_paid_list = list(set(urls_file) - set(paid_url_list))
    for url in respond_200_url_list:
        print('\nUrl: {} \nRespond 200'.format(url))
        if url in paid_url_list:
            print('Domain paid more than {} days'.format(args.days_in_month))
        else:
            print('Domain paid less than {} days'.format(args.days_in_month))
    for url in not_respond_200_list:
        print('\nUrl: {} \nNot Respond 200'.format(url))
        if url in not_paid_list:
            print('Domain paid less than {} days'.format(args.days_in_month))
        else:
            print('Domain paid more than {} days'.format(args.days_in_month))