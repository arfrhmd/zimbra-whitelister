#!/usr/bin/env python3

import argparse
import os
import pwd
from lib import postfix, policyd

if __name__ == '__main__':
    if pwd.getpwuid(os.getuid())[0] != 'root':
        print('[x] Please run this script as root')
        exit()
    parser = argparse.ArgumentParser(description='Format list: description;email')
    parser.add_argument('-d', '--delim', help='set delimiter (Default: ;)', default=';')
    parser.add_argument('-f', '--file', help='list file', required=True)
    parser.add_argument('-po', '--policyd', help='add list to Policyd only', action='store_true')
    parser.add_argument('-ps', '--postfix', help='add list to Postfix only', action='store_true')
    parser.add_argument('-v', '--version', action='version', version='1.0.0-alpha')
    args = parser.parse_args()

    if args.policyd:
        print(f'[+] Add list to Policyd only\n')
        if args.delim != ';':
            policyd.delim = args.delim
        policyd.get_existing_list()
        with open(args.file, 'r') as f:
            for line in f:
                policyd.check_members(line)
    elif args.postfix:
        print('[+] Add list to Postfix only')
        if args.delim != ';':
            postfix.delim = args.delim
        with open(args.file, 'r') as f:
            for line in f:
                postfix.send(line)
                print('[+] Postmap postfix_rbl_override')
                os.system('su - zimbra -c "postmap /opt/zimbra/conf/postfix_rbl_override"')
                print('[+] Apply the changes to the Zimbra Collaboration Server')
                os.system('su - zimbra -c "zmprov mcf +zimbraMtaRestriction ' +
                          '\'check_client_access lmdb:/opt/zimbra/conf/postfix_rbl_override\'"')
    else:
        print('[+] Add list to Policyd and Postfix')
        if args.delim != ';':
            policyd.delim = args.delim
            postfix.delim = args.delim
        policyd.get_existing_list()
        with open(args.file, 'r') as f:
            for line in f:
                policyd.check_members(line)
                postfix.send(line)
                print('[+] Postmap postfix_rbl_override')
                os.system('su - zimbra -c "postmap /opt/zimbra/conf/postfix_rbl_override"')
                print('[+] Apply the changes to the Zimbra Collaboration Server')
                os.system('su - zimbra -c "zmprov mcf +zimbraMtaRestriction ' +
                          '\'check_client_access lmdb:/opt/zimbra/conf/postfix_rbl_override\'"')

    # Remove temporary files
    print('[+] Remove temporary files')
    os.remove(os.path.join(os.getcwd(), 'data', 'listed-domains.tmp'))
    os.remove(os.path.join(os.getcwd(), 'data', 'members-id.tmp'))
    print('[+] Done')