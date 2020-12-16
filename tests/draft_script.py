import readability
import logging
import sys

# incidentally you actually don't seem to need \n characters for this to work. Should note that scores are lower when
# you push a block of text vs an iterable. Probably because the block may be read as a convoluted sentence, which would
# be more complicated to read.

logger = logging.getLogger('reader_logger')
logger.setLevel(logging.INFO)
stdout_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stdout_handler)

sample = "Here is some text I wrote. It's not very complicated, as you can see. My friend Dr. Eeyore and I are having " \
         "a grand ole time. Hope you are too."  # 114.36875
sample2 = "When I was in the 5th grade, a mischievous classmate asked me the question, 'Which weighs more, a ton of feathers" \
          "or a ton of lead?' No, I was not fooled, but little did I know how useful a critical understanding of density" \
          "would be to life and the universe. A common way to compute density is, of course, to take the ratio of an " \
          "object's mass to its volume."  # 79.27260
sample3 = "We are currently hiring for a full time data engineer. The ideal candidate will have five to seven years of " \
          "experience building complicated data pipelines, as well as deploying production level code. Experience with " \
          "Microsoft Azure is preferred. Master's or Ph.D in computer science preferred."  # 55.38858
sample4 = " . Now we are going to try to complicate things a little bit. . I am going to add some empty strings and weird " \
          "things. ... ."  # 106.8842391
sample5 = " . "  # error!
sample6 = "Next week marks the start of our open enrollment period. Our HR representatives will be having an informational " \
          "session next Monday for anyone who has questions about our new benefits packages. If you are unable to attend, " \
          "additional information is available on the COR. You may also contact Karen Crone."  # 53.71150
sample7 = "We would like to congratulate Dr. Temnit Gebru for being selected to Forbe's Greatest AI Contributors " \
          "of the Year. This is a huge accomplishment. Dr. Gebru has worked tirelessly for racial equity within the AI " \
          "space, and it's wonderful to see her efforts be recognized."  # 72.1333333
sample8 = "Dr. Beverly Crusher is the greatest! She is so caring and compassionate. Do you think she'll be back in the " \
          "next season?"  # 107.096811


def main():
    sample_list = [sample, sample2, sample3, sample4, sample5, sample6, sample7, sample8]

    for text in sample_list:
        final_text = clean_text(text)
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
    final_score = 0
    sentences = text.split(".")

    try:
        results = readability.getmeasures(sentences, lang='en')
        final_score = results['readability grades']['FleschReadingEase']
    except Exception as e:
        error_msg = "Unable to return readability score. Please review user text."
        logger.debug(e)
        return error_msg

    return final_score


if __name__ == '__main__':
    main()
