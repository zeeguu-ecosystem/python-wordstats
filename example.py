from wordstats import LanguageInfo
from wordstats.common_words import common_words

French = LanguageInfo.load("fr")

print("Top 10 most used words in French")
print(French.all_words()[:10])
print(" ")

print("Info about the word 'jamais'")
jamais_info = French.get("jamais")
print(jamais_info)
print(" ")

print("Word info via the Word class")
from wordstats import Word
print(Word.stats('bleu', 'fr'))

print("First four common words of more than 10 letters common between French and English")
English = LanguageInfo.load("en")
count = 0
for each in French.all_words():
    if len(each) > 10 and each in English.all_words():
        print(each)
        count += 1
    if count == 4:
        break
print("")

print("Words (>9chars) common in all the languages*")
for each in common_words():
    if len(each) > 9:
        print(each)
