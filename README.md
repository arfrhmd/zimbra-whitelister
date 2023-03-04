# Zimbra Whitelister
> An app to whitelist emails from a specific domain to CBPolicyd and Postfix

![Project language](https://img.shields.io/github/languages/top/arfrhmd/zimbra-whitelister)
[![GitHub release](https://img.shields.io/github/v/release/arfrhmd/zimbra-whitelister?include_prereleases)](https://github.com/arfrhmd/zimbra-whitelister/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](https://github.com/arfrhmd/zimbra-whitelister/blob/main/LICENSE)

## Installation

```sh
git clone https://github.com/arfrhmd/zimbra-whitelister.git
cd zimbra-whitelister
pip3 install -r requirements.txt
```

## Usage example

1. Add file list to `data` folder

```
.
└── zimbra-whitelister/
    └── data/
        └── example.csv
```

2. Run program

```sh
python3 main.py -f example.csv
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
