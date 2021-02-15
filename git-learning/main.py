from greets import greetings
from translate import Translator

translate = Translator(to_lang='pt')
for g in greetings:
    print(translate.translate(g).title())

