# Zimbra Whitelister
> An app to whitelist emails from a specific domain to CBPolicyd and Postfix

## Installation

```sh
git clone https://github.com/arfrhmd/zimbra-whitelister.git
```

## Usage example

```sh
cd zimbra-whitelister
python3 main.py -f list.txt
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