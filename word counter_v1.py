#!/usr/bin/python

#I want to make a word counter. it needs to get the number of words, lines and characters in a file.

# First, it must be able to read and print the file.
f = open('automate.txt', 'r')               # Opens the file 'automate.txt'
data = f.read()
f.close()
print(data)                                 # Prints the data within the file.

#Second, I want it to be able to count words and lines

words = data.split(' ') # This splits the text by spaces, thereby counting the number of words in the next
print('The words in the text are: ')
print(words)
num_words = 0
for word in words: # For the number of words in the text, the program adds a +1 to the total until the program is complete
    num_words +=1
print('The number of words is ', num_words)

lines = data.split('\n') # This splits the text by new lines, thereby counting the number of lines in the text
print('The lines in the text are: ')
print(lines)
num_lines = 0
for line in lines: # For the number of lines in the text, the program adds a +1 to the total until the program is complete
    num_lines +=1
print('The wrong number of lines is ', num_lines)

#Empty lines are also counted. I do not want that. This needs to be fixed
for l in lines:
    if not l:
        lines.remove(l)
print('The correct number of lines is ' + str(len(lines)))