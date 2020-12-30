import readability
import logging
import sys

logger = logging.getLogger('reader_logger')
logger.setLevel(logging.INFO)
stdout_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stdout_handler)

text_sample = [
    "Please do not use this fax machine. It is broken. A call is out to maintenance, and they should be by later this afternoon.",
    "We'd like to congratulate Joe Smith on his recent promotion to project manager. Joe has worked tirelessly to deliver"
    " high quality products to our clients, and he has been instrumental in working across teams to deliver real results."
    "We know Joe is excited to get started in his new role and we can't wait to see what he does. Congratulations, Joe!",
    "We are currently seeking a full time data engineer to join our product team. The ideal candidate will have 5 - 7 years of "
    "experience building data pipelines and deploying production level code. In addition, they will have experience with DevOps, "
    "and data tools like Apache Spark and Hadoop. They should also be proficient in scripting languages like Python and Bash.",
    "Dr. Beverly Crusher is an amazing physician. She makes it very clear from the moment you walk into her office that you are "
    "her number one priority. She took the time to explain everything and helped me set up next steps. I'd recommend her to anyone!",
    "We have received several complaints from customers about employees using their cell phones on the sales floor. Please "
    "remember the customers are our number one priority and they should not have to wait for help because our staff are distracted."
    "In the future, we ask that you leave your cell phones in the back room and only use them during lunch or breaks.",
    "Open enrollment begins on Jan. 15. HR will be holding informal info sessions over the next two weeks to answer any questions "
    "you have about benefits or the enrollment process. Please be on the lookout for calendar invites coming within the next few days. "
    "We will have multiple sessions, so don't worry if you can't make the initial session.",
    "We're having an ice cream party! Who wants chocolate? Who wants vanilla? What about cookies and cream? How about all three?"
    " See you at the department social!",
    "Acme Labs is seeking a product tester for a full time position in our tools department. The ideal candidate will have "
    "extensive experience working with a variety of tools such as large hammers, drills, catapults, and springs. They should "
    "have a positive, can-do attitude and a sense of humor. We offer competitive pay and great health benefits! This job will "
    "be based in our Colorado office. We are not offering relocation at this time. Also, should note, the job is pretty dangerous.",
    "Look, Jim. I'm a doctor, not a magician!"
]


def main():
    for text in text_sample:
        readability_score = get_readability_score(text)
        print(readability_score)


def clean_text(text):
    ''' Later code separates sentences by periods. This function will address suffixes and prefixes that include
        periods, as well as periods present in other forms of text, i.e. websites. It will also convert other
        ending punctuation like ! and ?. It will also remove any empty strings within the sentence.

        param: list of text samples

        returns: cleaned text sample with appropriate punctuation for readability library '''
    abbrev_list = ['Mr.', 'Mrs.', 'Ms.', 'Dr.', 'Ph.d', 'Ph.D', 'Esq.', 'Sr.', 'Jr.']
    otherUsesOfPeriods = ['.com', 'www.', '.org', '.gov', '.edu', '.io', '.net']
    punctuation = ['.', '!', '?', '...']

    text_words_list = text.split(' ')

    for index, word in enumerate(text_words_list):
        website_present = False
        for item in otherUsesOfPeriods:
            if item in word:
                website_present = True
                new_word = ""
                text_words_list[index] = new_word
                break
        if word in abbrev_list:
            new_word = word.replace('.', '')
            text_words_list[index] = new_word
        else:
            for symbol in punctuation:
                if symbol in word and not website_present:
                    new_word = word.replace(symbol, '.')
                    text_words_list[index] = new_word

    for word in text_words_list:
        if word == "":
            text_words_list.remove(word)

    cleaned_sample = ' '.join(text_words_list)

    return cleaned_sample


def get_readability_score(text):
    final_text = clean_text(text)
    sentences = final_text.split(".")

    for sentence in sentences:
        if sentence == '':
            sentences.remove(sentence)

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
