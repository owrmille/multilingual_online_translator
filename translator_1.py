import re
import requests

from bs4 import BeautifulSoup

languages = {'1': 'Arabic',
             '2': 'German',
             '3': 'English',
             '4': 'Spanish',
             '5': 'French',
             '6': 'Hebrew',
             '7': 'Japanese',
             '8': 'Dutch',
             '9': 'Polish',
             '10': 'Portuguese',
             '11': 'Romanian',
             '12': 'Russian',
             '13': 'Turkish'}

def input_data_function(languages):
    print("Hello, you're welcome to the translator. Translator supports:")
    
    for key in languages:
        print(f'{key}. {languages[key]}')
        
    language_from = input('Type the number of your language: ')
    language_to = input("Type the number of a language you want to translate to or '0' to translate to all languages: ")
    word = input('Type the word you want to translate: ').lower()
    
    return [language_from, language_to, word]

def response_function(input_data):
    user_agent = 'Mozilla/5.0'
    
    try:
        response = requests.get(f'https://context.reverso.net/translation/{languages[input_data[0]].lower()}-{languages[input_data[1]].lower()}/{input_data[2]}', headers={'User-Agent': user_agent})
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
        text = f'{languages[input_data[1]].capitalize()} Translation:\n{translations[1]}\n\n{languages[input_data[1]].capitalize()} Example:\n{clean_examples[0]}:\n{clean_examples[1]}\n'
        file.write(text)
        print(text)
        
    except:
        print(f'Sorry, unable to find "{input_data[2]}" in {languages[input_data[1]]}\n')

    file.close()

def null_case(input_data, languages):
    file = open(f'{input_data[2]}.txt', 'w', encoding='utf-8')

    for key in languages:
        if key not in ('0', input_data[0]):

            input_data[1] = key
            res = response_function(input_data)
            translations, examples = res[0], res[1]
            
            try:
                clean_examples = [el.strip() for el in re.split(r'\n\n\n\n\r\n|\n\n\n\n\n', examples[0])]
                text = f'{languages[input_data[1]].capitalize()} Translation:\n{translations[1]}\n\n{languages[input_data[1]].capitalize()} Example:\n{clean_examples[0]}:\n{clean_examples[1]}\n'
                file.write(text + '\n')
                print(text)
                
            except:
                print(f'Sorry, unable to find "{input_data[2]}" in {languages[input_data[1]]}\n')

    file.close()
    
input_data = input_data_function(languages)
    
if input_data[1].lower() == '0':
    null_case(input_data, languages)
else:
    res = response_function(input_data)
    translations, examples = res[0], res[1]
    print_translations(input_data, translations, examples)
