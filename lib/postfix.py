import dns.resolver as resolver
import time
from colorama import Fore, Style

delim = ';'

def get_smtp_domain(domain):
    smtp_domains = []
    try:
        mx_records = resolver.resolve(domain, 'MX')
        for mx_hostname in mx_records:
            mx_hostname = str(mx_hostname.exchange)[:-1]
            smtp_hostname.append(mx_hostname)
    except dns.resolver.NoAnswer:
        print(Fore.RED + f'No MX record for {domain}' + Style.RESET_ALL)
    return smtp_domains

def add_smtp(smtp_domains):
    if os.path.isfile(filename):
        print("File exists.")
    else:
        print("File does not exist.")
    with open('/opt/zimbra/conf/postfix_rbl_override', 'r') as f:
        smtp_exist = set(f.read().splitlines())

    for smtp_domain in smtp_domains:
        print('Adding ' + Fore.CYAN + smtp_hostname + Style.RESET_ALL + ' to postfix_rbl_override', end='')
        for i in range(1, 3):
            print('.', end='')
            time.sleep(0.5)
        if smtp_hostname + ' OK' not in smtp_exist:
            with open('/opt/zimbra/conf/postfix_rbl_override', 'a') as f:
                f.write(smtp_hostname + ' OK\n')
            print(Fore.GREEN + ' OK' + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + ' already exist' + Style.RESET_ALL)

def send(line):
    company = line.split(delim)[0]
    email = line.split(delim)[1].replace('>', '')
    name, _, domain = email.rpartition('@')
    smtp_hostnames = get_smtp_domain(domain)
    print(smtp_hostnames)
    add_smtp(smtp_hostnames)