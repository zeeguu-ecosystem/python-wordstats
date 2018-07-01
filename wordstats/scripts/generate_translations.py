
"""
    script used for automatically generating translations.
    takes an existing translation dictionary or creates a new translation dictionary and proceeds
    to query Glosbe for translations which will be stored in the translations file/database
    each word in the wordlist specified by languageFrom is stored with all its possible translations in the
    translation dictionary

"""


from wordstats.translate import Translate

from python_translators.translators.glosbe_pending_translator import GlosbePendingTranslator

languageFrom = "lang1"
languageTo = "lang2"

translations = Translate.load_cached(languageFrom, languageTo)

print(len(translations.translations))

translations.generate_translations(GlosbePendingTranslator,"Tochter", save=True)
translations.generate_translations_from_hermit(GlosbePendingTranslator, save=True)
translations.save_translations()