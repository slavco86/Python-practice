#! /usr/bin/env python3
PASSWORDS = {'email': 'gmail',
             'blog': 'SlavCo',
             'luggage': '12345'}
import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()
account = sys.argv[1]
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print ('Password for the account '+ account +' has been copied to your clipboard')
else:
    print ('There is no password for '+ account +'. Would you like to set one up? (Y for yes, N for no)')
    answer = input().upper()
    while True:
        if(answer == 'N'):
            print('Ok, see you later...')
            break
        elif (answer == 'Y'):
            print('Great, please type in you password for '+ account +' ...')
            password = input()
            PASSWORDS.setdefault(account,password)
            pyperclip.copy(PASSWORDS[account])
            print('All set. You password for '+ account +' has been stored and copied to your clipboard')
            break
        else:
            print('I\'m not sure what you mean... please type in Y to set up a new password for '+ account +' or N to exit')
            answer = input().upper()