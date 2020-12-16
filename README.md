This project uses the readability Python library to return readability scores for assorted texts. Readability is a
metric used to determine how easy something is to read. There are a few different scoring scales used to determine
readability. This project uses the Flesch-Kincaid scale, noted here: https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests

The requirements.txt file includes all the specifications for set up, but the only libraries you really need will be
the logging, sys, and readability libraries. If you are using Pycharm, after you clone the project, it should ask you if 
you want to install the requirements. Select "yes."
 
The documentation for the readability library states that each line or sentence of text must be separated by Python's 
newline character. ('\n') However you can also achieve solid results if your sentences are separated by punctuation. 
This script not only deals with end punctuation but should eliminate any confusion caused by punctuation that is associated 
with titles, e.g. Dr. or Mrs. 

e.g. "Dr. McCoy is Captain Kirk's best friend." will be converted to "Dr McCoy is Captain Kirk's best friend."
e.g. "Dr. Timnit Gebru is one of the leading AI researchers of our time. She really inspires me!" becomes
 "Dr Timnit Gebru is one of the leading AI researchers of our time. She really inspires me."
 From this point the script will split your text into sentence sized chuncks which will be processed by the readability 
 library's main function. It will then return a score based on how difficult it is to read your text.

In the test folder you'll find the unit tests, along with a draft script that I wrote so that I could loop through 
several different text examples and check the scores. I wanted this separate from the main script because the final
iteration of the main script will likely be used with single examples and will not need a loop to operate. There may
also be different functionality requirements for the final version of the main script, but I haven't determined those
as of yet. 
 
Author: T. Roberts (Prismacolor)
