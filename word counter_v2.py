# I want to make a word counter. it needs to get the number of words, lines and characters in a file.
# First I want to define some parameters: I want the program to tell me the number of words and the number of lines.

#Function for word count
def count_words(poem):
    words = poem.split(' ')     # This splits the text by spaces, thereby counting the number of words in the next
    num_words= len(words)
    return num_words

#Function for line count
def count_lines(poem):
    lines = poem.split('\n')    # This splits the text by new lines, thereby counting the number of lines in the text
    for l in lines:             
        if not l:               # If the line is empty, we remove it from the list using the remove() command.
            lines.remove(l)
            
    return len(lines)


f = open('automate.txt', 'r')               # Opens the file 'automate.txt'
poem = f.read()
f.close()

num_words = count_words(poem)
num_lines = count_lines(poem)

print("The number of words: ", num_words)
print("The number of lines: ", num_lines)