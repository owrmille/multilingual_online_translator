# multilingual_online_translator
A project from JetBrains Academy that is a word translator with a choice of several languages. Python + html. The source of translations is the website: https://context.reverso.net/

The goal of my program is to find translations and example sentences for a given word. 

This program act as if it visits the website for you. The correct URL with the word you type is generated, determine the translation direction, and send the URL to the website. After getting to the needed page, the program should extract the required data: translations and sentences with usage examples. The program access this text via CSS classes and tags. 

There are two versions here:
* translator_1.py
* translator_2.py

In **version 1 (translator_1.py)** you need to enter the language from which the word is translated, the language into which the word is translated, and the word itself to be translated.

The list of supported languages contains 13 items:

* Arabic
* German
* English
* Spanish
* French
* Hebrew
* Japanese
* Dutch
* Polish
* Portuguese
* Romanian
* English
* Turkish

In addition to translating a word, the program displays an example of the use of a word in a sentence and the translation of the sentence into the original language. The program writes the resulting translations and examples to a file named <word> .txt.

If instead of the language into which you want to translate the word, you entered '0', then the word will be translated into all available languages, and the translation will be written to a file named <word> .txt.

In **version 2 (translator_2.py)** сommand line arguments are used instead of all input. The first argument is the name of the source language, the second argument is the name of the target language, the third argument is the word. If the word should be translated to all languages, the second argument will be 'all'.
