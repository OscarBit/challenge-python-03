# Resolve the problem!!
import re

def run():
    with open('encoded.txt', 'r', encoding='utf-8') as f:
        raw_secret = f.read()
    print('The secrect key is: ', "".join(re.findall(r'[a-z]',raw_secret)))

if __name__ == '__main__':
    run()
