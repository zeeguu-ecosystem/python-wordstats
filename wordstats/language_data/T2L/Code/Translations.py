from query import query_site
from pathlib import Path

"""

Class that calls a translation API to translate words and stores the
translations as an xml file

"""

# First word from which to start translating
BEGIN = 0
# How many words to translate before storing them (the last one is not included)
BATCH = 750

LANG = "Spanish"
FROM = "es"
DEST = "en"

# Path of the txt file with the words
PATH_INPUT_WORDS = str(Path(__file__).parent.parent) + '/Words/' + LANG + '.txt'

# Path of the txt file with the translations
PATH_OUTPUT_TRANSLATIONS = str(Path(__file__).parent.parent) + '/Translations/' + LANG + "-English.txt"


# Glosbe API parameters
BASE_GLOSBE_URL = "https://glosbe.com/gapi/translate"


def query_glosbe_by_word(url, word, from_lang, dest_lang, fmt="json"):
    """Queries the Glosbe API for the translations of a word

    :param url:         -- string with base Glosbe url
    :param word:        -- string with the word to translate
    :param from_lang:   -- string with the iso code of the language of the word
    :param dest_lang:   -- string with the iso code of the language to which to translate the word
    :param fmt:         -- string with the format in which to receive the query response (default JSON)
    :return:            -- a json object with the query response

    """
    params = dict()
    params["pretty"] = "true"
    params["from"] = from_lang
    params["dest"] = dest_lang
    params["phrase"] = word
    params["format"] = fmt
    return query_site(url, params)


def parse_glosbe_result(input):
    """Gets the word translations from a json object and stores them in a list

    :param input:       -- json object with the response of the Glosbe API
    :return:            -- list with all the word translations

    """
    list = []
    result = input["tuc"]

    for res in result:
        if "phrase" in res:
            res = res["phrase"]
            if res["language"] == DEST:
                list.append(res["text"])

    return list


def translate(word, from_lang, dest_lang):
    """Gets all words translations from an API and stores them in a list

    :param word:        -- string with the word
    :param from_lang:   -- string with the language of the word
    :param dest_lang:   -- string with the language to which translate the word
    :return:            -- list with all possible translations of the word

    """

    return parse_glosbe_result(query_glosbe_by_word(BASE_GLOSBE_URL, word, from_lang, dest_lang))



def main():
    global PATH_INPUT_WORDS, PATH_OUTPUT_TRANSLATIONS, BEGIN, BATCH

    words = []
    file = open(PATH_INPUT_WORDS)


    for line in file:
        words.append(line.rstrip('\n'))

    count = 1

    with open(PATH_OUTPUT_TRANSLATIONS, 'a') as file:

        for w in words:

            count += 1

            if count < BEGIN:
                continue

            if count < BEGIN + BATCH:


                meanings = translate(w, FROM, DEST)

                if len(meanings) == 0:
                    continue

                file.write(str(w))
                file.write("\n\t")


                temp = 0
                for ceva in meanings:
                    if temp == 3:
                        break
                    file.write(ceva)
                    file.write("\n\t")
                    temp += 1
                file.write("\n\n")
                print(count)



if __name__ == "__main__":
    main()
