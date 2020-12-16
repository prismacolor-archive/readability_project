import readability
import logging
import sys

logger = logging.getLogger('reader_logger')
logger.setLevel(logging.INFO)
stdout_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stdout_handler)

sample8 = "Dr. Beverly Crusher is the greatest! She is so caring and compassionate. Do you think she'll be back in the " \
          "next season?"


def main():
    user_text = sample8

    final_text = clean_text(user_text)
    readability_score = get_readability_score(final_text)
    print(readability_score)


def clean_text(text):
    # address any suffixes or prefixes that include periods, and convert all ending punctuation to .
    abbrev_list = ['Mr.', 'Mrs.', 'Ms.', 'Dr.', 'Ph.d', 'Ph.D', 'Esq.', 'Sr.', 'Jr.']
    punctuation = ['.', '!', '?', '...']

    text_words_list = text.split(' ')

    for index, word in enumerate(text_words_list):
        if word in abbrev_list:
            new_word = word.replace('.', '')
            text_words_list[index] = new_word
        else:
            for symbol in punctuation:
                if symbol in word:
                    new_word = word.replace(symbol, '.')
                    text_words_list[index] = new_word

    cleaned_sample = ' '.join(text_words_list)

    return cleaned_sample


def get_readability_score(text):
    sentences = text.split(".")

    print(sentences)

    try:
        results = readability.getmeasures(sentences, lang='en')
        score_results = results['readability grades']['FleschReadingEase']
    except Exception as e:
        score_results = "Unable to return readability score. Please review user text."
        logger.debug(e)

    return score_results


if __name__ == '__main__':
    main()

