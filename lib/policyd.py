import os
import requests
import time
from bs4 import BeautifulSoup
from colorama import Fore, Style

delim = ';'

def get_existing_list():
    url = 'http://127.0.0.1:7780/webui/policy-group-member-main.php?policy_group_id=6'
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')

        # Search for all tr elements that have class 'resultsitem'
        trs = soup.find_all('tr', class_='resultsitem')

        # Write a list of domains to the file listed-domains.tmp
        with open(os.path.join(os.getcwd(), 'data', 'listed-domains.tmp'), 'w') as f:
            for tr in trs:
                # Find td elements containing email and extract the text
                td_email = tr.find('td', class_='textcenter')
                email = td_email.get_text().strip()

                # Extract the domain using regular expression.
                if email.startswith('@'):
                    domain = email[1:]

                # Write the domain and member_id to the file
                f.write(f'{domain}\n')

        # Write a list of member_id to the file members-id.tmp
        with open(os.path.join(os.getcwd(), 'data', 'members-id.tmp'), 'w') as f:
            for tr in trs:
                # Find radio input elements and extract their values
                input_radio = tr.find('input')
                member_id = input_radio['value']
                f.write(f'{member_id}\n')

        time.sleep(1)

def check_members(line):
    # Read a list of domains from the file domains.txt
    with open(os.path.join(os.getcwd(), 'data', 'listed-domains.tmp'), 'r') as f:
        domain_list = set(f.read().splitlines())

    # List of domains to be ignored
    exclude_email_domain = [
        'gmail.com',
        'yahoo.com',
        'hotmail.com',
        'outlook.com',
        'live.com',
        'aol.com',
        'mail.com',
        'msn.com',
        'ymail.com',
        'icloud.com',
        'gmx.com',
        'zoho.com',
        'yandex.com',
        'protonmail.com',
        'mail.ru',
    ]

    # Find domains that match the domains in the file domains.txt
    description = line.split(delim)[0]
    email = line.split(delim)[1].replace('>', '')
    name, _, domain = email.rpartition('@')
    domain = domain.replace('\n', '').lower()

    if domain not in domain_list:
        if domain not in exclude_email_domain:
            print('[x] ' + Fore.LIGHTRED_EX + 'NOT EXIST ' + Style.RESET_ALL + f'{domain} ({description})')
            add_member(domain, description)
    else:
        print('[x] ' + Fore.LIGHTGREEN_EX + 'EXIST ' + Style.RESET_ALL + f'{domain} ({description})')

def add_member(domain, company):
    print(f'[+] Add member {domain} ({company})')

    url = 'http://127.0.0.1:7780/webui/policy-group-member-add.php'
    data = {
        "frmaction": "add2",
        "policy_group_id": "6",
        "policy_group_member_member": f'@{domain}',
        "policy_group_member_comment": company,
    }

    r = requests.post(url, data=data)
    if r.status_code == 200 and 'Policy group member created' in r.text:
        print('[+] ' + Fore.LIGHTGREEN_EX + 'Success ' + Style.RESET_ALL + 'add member')
        get_existing_list()

        # Read and write member_id and new domain to the file listed-domains.tmp
        with open(os.path.join(os.getcwd(), 'data', 'members-id.tmp'), 'r') as f:
            last_line = f.readlines()[-1]
            member_id =  int(last_line)

        # Write successfully added domains to the file listed-domains.tmp
        with open(os.path.join(os.getcwd(), 'data', 'members-id.tmp'), 'a') as f:
            f.write(f'{member_id}\n')

        enable_member(member_id)
    else:
        # Write failed domains to be added to the file error-policyd.txt
        with open(os.path.join(os.getcwd(), 'data', 'error-policyd.csv'), 'a') as f:
            f.write(f'{company};{domain}\n')
        print('[x] ' + Fore.LIGHTRED_EX + 'Failed ' + Style.RESET_ALL + 'add member')
        print('[+] Check it manually on ./data/error-policyd.txt')

def enable_member(member_id):
    print(f'[+] Enable member {member_id}')

    url = 'http://127.0.0.1:7780/webui/policy-group-member-change.php'
    data = {
        "frmaction": "change2",
        "policy_group_id": "6",
        "policy_group_member_id": f'{member_id}',
        "policy_group_member_disabled": "0",
    }

    r = requests.post(url, data=data)
    if r.status_code == 200 and 'Policy group member updated' in r.text:
        print('[+] ' + Fore.LIGHTGREEN_EX + 'Success ' + Style.RESET_ALL + 'enable member')
    else:
        print('[x] ' + Fore.LIGHTRED_EX + 'Failed ' + Style.RESET_ALL + 'enable member')