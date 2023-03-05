# Zimbra Whitelister
> An app to whitelist emails from a specific domain to CBPolicyd and Postfix

![Project language](https://img.shields.io/github/languages/top/arfrhmd/zimbra-whitelister)
[![GitHub release](https://img.shields.io/github/v/release/arfrhmd/zimbra-whitelister?include_prereleases)](https://github.com/arfrhmd/zimbra-whitelister/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](https://github.com/arfrhmd/zimbra-whitelister/blob/main/LICENSE)

## Compatibility

| Features | Other OS | Linux |
|---|---|---|
| CBPolicyD | <p align="center">:white_check_mark:</p> | <p align="center">:white_check_mark:</p> |
| Postfix | <p align="center">:x:</p> | <p align="center">:white_check_mark:</p> |

You can run the CBPolicyD feature even if you don't run it from a Linux operating system because it uses the Web UI.

To run the CBPolicyD feature outside the Linux system, you need to change the URL address in the [policyd.py](./lib/policyd.py) file with your own. Let's see the code:

```py
...

def get_existing_list():
    url = 'http://127.0.0.1:7780/webui/policy-group-member-main.php?policy_group_id=6'

...

def add_member(domain, description):
    print(f'[+] Add member {domain} ({description})')

    url = 'http://127.0.0.1:7780/webui/policy-group-member-add.php'

...

def enable_member(member_id):
    print(f'[+] Enable member {member_id}')

    url = 'http://127.0.0.1:7780/webui/policy-group-member-change.php'

...
```

## Installation

```sh
git clone https://github.com/arfrhmd/zimbra-whitelister.git
cd zimbra-whitelister
pip3 install -r requirements.txt
```

## Usage

```sh
python3 /path/to/zimbra-whitelister/main.py -f /path/to/example.csv
```

## Options

```
usage: main.py [-h] [-d DELIM] -f FILE [-po] [-ps] [-v]

Format list: description;email

options:
  -h, --help            show this help message and exit
  -d DELIM, --delim DELIM
                        set delimiter (Default: ;)
  -f FILE, --file FILE  list file
  -po, --policyd        add list to Policyd only
  -ps, --postfix        add list to Postfix only
  -v, --version         show program's version number and exit
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
