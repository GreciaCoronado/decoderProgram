# decoderProgram
This program can read in an encoded message from coding_qual_input.txt and return the decoded version as a string
Here's an example of what the coding_qual_input.txt file will look like:

3 love

6 chocolate

2 dogs

4 cats

1 I

5 you

The program order the numbers from smallest to biggest and arranged them into a pyramid. Each line of the pyramid includes one more number than the line before it:

1

2 3

4 5 6

The numbers at the end of each line (1, 3 and 6) correspond to the words that are part of the message. So for the example the message words are:

1: I

3: love

6: chocolate

And the program return the string "I love chocolate"
