ally_horde = {
    'A': 'Í',
    'B': '□',
    'C': 'À',
    'E': 'b',
    'F': '',
    'G': '℮',
    'H': '╤',
    'I': 'ф',
    'K': 'À',
    'L': '♫',
    'M': 'ñ',
    'N': 'Ћ',
    'O': 'm',
    'R': 'Ç',
    'S': 'ƒ',
    'T': 'Ё',
    'U': 'p',
    'V': 'ê',
    'W': '№',
    'Y': 'd',
    ' ': ' ',
    '\'': '\''
}

def allie_to_horde(pt):
    ct = ''
    for letter in str(pt):
        if letter in ally_horde:
            ct += str(ally_horde[letter] + ' ')
    return ct


def __main__():
    pt = str(input('Alliance: '))
    ct = allie_to_horde(pt)
    print('Horde: ' + str(ct))


if __name__ == '__main__':
    __main__()
