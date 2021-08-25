import random

YunMuTable={
    'iu':'Q',
    'ia':'W',
    'ua':'E',
    'er':'R',
    'uan':'R',
    'ue':'T',
    'uai':'Y',
    'v':'Y',
    'uo':'O',
    'un':'P',
    'iong':'S',
    'ong':'S',
    'iang':'D',
    'uang':'D',
    'en':'F',
    'eng':'G',
    'ang':'H',
    'an':'J',
    'ao':'K',
    'ai':'L',
    'ing':';',
    'ei':'Z',
    'ie':'X',
    'iao':'C',
    'ui':'V',
    've':'V',
    'ou':'B',
    'in':'N',
    'ian':'M'
}

def main():
    ym_list = [key for key, value in YunMuTable.items()]
    while 1:
        ym = random.choice(ym_list)
        ans = YunMuTable[ym]
        user_ans = input(f'\033[0m{ym}: '.rjust(12))
        if user_ans == '':
            print(f'\033[31m{ym}: '.rjust(13) + f'\033[31m{ans}')
        elif user_ans == 'lookup':
            user_ym = input('\033[33mlookup: '.rjust(13))
            while user_ym not in ym_list:
                user_ym = input('\033[33mlookup: '.rjust(13))
            print(f'\033[33m{user_ym}: '.rjust(13) + f'\033[33m{YunMuTable[user_ym]}')
        else:
            while ans != user_ans and chr(ord(ans)+32) != user_ans:
                user_ans = input(f'\033[31m{ym}: '.rjust(13))
                if user_ans == '':
                    print(f'\033[31m{ym}: '.rjust(13) + f'\033[31m{ans}')
                    break

if __name__ == '__main__':
    main()