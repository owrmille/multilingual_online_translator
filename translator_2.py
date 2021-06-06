import re
import requests
import sys

from bs4 import BeautifulSoup

'''
Take command-line arguments like:
> python3 translator_2.py <source language> <target language or 'all'> <word>
* 'all' if you want to translate a word into all available languages
Example:
> pyhton3 translator_2.py english french hello
Example:
> python3 translator_2.py russian all пока
'''

languages = ['all', 'arabic', 'german', 'english', 'spanish', 'french', 'hebrew', 'japanese', 'dutch', 'polish', 'portuguese', 'romanian', 'russian', 'turkish']

def response_function(input_data):
    user_agent = 'Mozilla/5.0'

    try:
        response = requests.get(f'https://context.reverso.net/translation/{input_data[0].lower()}-{input_data[1].lower()}/{input_data[2]}', headers={'User-Agent': user_agent})
    except:
        print('Something wrong with your internet connection')

    soup = BeautifulSoup(response.content, 'html.parser')
    translations = [word.text.strip() for word in soup.find_all('a', class_='translation')]
    examples = [word.text.strip() for word in soup.find_all('div', class_='example')]

    return [translations, examples]

def print_translations(input_data, translations, examples):
    file = open(f'{input_data[2]}.txt', 'w', encoding='utf-8')

    try:
        clean_examples = [el.strip() for el in re.split(r'\n\n\n\n\r\n|\n\n\n\n\n', examples[0])]
        text = f'{input_data[1].capitalize()} Translation:\n{translations[1]}\n\n{input_data[1].capitalize()} Example:\n{clean_examples[0]}:\n{clean_examples[1]}\n'
        file.write(text)
        print(text)

    except:
        print(f'Sorry, unable to find "{input_data[2]}" in {input_data[1].capitalize()}\n')

    file.close()

def null_case(input_data, languages):

    file = open(f'{input_data[2]}.txt', 'w', encoding='utf-8')

    for el in languages:
        if el not in ('all', input_data[0]):

            input_data[1] = el
            res = response_function(input_data)
            translations, examples = res[0], res[1]

            try:
                clean_examples = [el.strip() for el in re.split(r'\n\n\n\n\r\n|\n\n\n\n\n', examples[0])]

                text = f'{input_data[1].capitalize()} Translation:\n{translations[1]}\n\n{input_data[1].capitalize()} Example:\n{clean_examples[0]}:\n{clean_examples[1]}\n'
                file.write(text)
                print(text)

            except:
                print(f'Sorry, unable to find "{input_data[2]}" in {input_data[1].capitalize()}\n')

    file.close()

args = sys.argv
input_data = args[1:]

if input_data[0] not in languages:
    print(f'Sorry, the program doesn\'t support {input_data[0].capitalize()}')
elif input_data[1] not in languages:
    print(f'Sorry, the program doesn\'t support {input_data[1].capitalize()}')

elif input_data[1].lower() == 'all':
    null_case(input_data, languages)

else:
    res = response_function(input_data)
    translations, examples = res[0], res[1]
    print_translations(input_data, translations, examples)
