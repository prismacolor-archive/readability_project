This project uses the readability Python library to return readability scores for assorted texts. 

The requirements file should include all the specifications for set up, but the only libraries you really need will be
the logging, sys, and readability libraries. 
 
The documentation for readability states that each line or sentence of text must be separated by Python's 
newline character. ('\n') However you can also achieve solid results if your sentences are separated by punctuation. 
This script not only deals with sentences that end with punctuation but should eliminate any confusion caused by 
punctuation that is associated with titles, e.g. Dr. or Mrs. 

In the test folder you'll find the unit tests, along with a draft script that I wrote so that I could loop through 
several different text examples and check the scores. I wanted this separate from the main script because the final
iteration of the main script will likely be used with single examples and will not need a loop to operate. There may
also be different functionality requirements for the final version of the main script, but I haven't determined those
as of yet. 
 
Author: T. Roberts (Prismacolor)