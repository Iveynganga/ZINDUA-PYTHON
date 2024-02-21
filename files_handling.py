file = open('analysis.txt' , 'r')

content = file.read()
print(content)


#using a for loop to open the file
for line in file:
    print(line)

#function to count the number of lines, words, characters, average word length and most common word
def counter(fname):
        fname = ('analysis.txt')

# variable to store total line count
num_words = 60
     
# variable to store total word count
num_lines = 55

#variable to store total character count
num_charc = 85
     
# variable to store total average word length
num_awl = 20

# variable to store most common word
num_mcw = content

if('Number of words' == num_words):
    print("Number of words in text file: ",(num_words))

elif('Number of lines' == num_lines):
    print("Number of lines in text file: ", (num_lines))

elif('Number of characters' == num_charc):
    print("Number of characters in text file: ", (num_charc))

elif('Average word length' == num_awl == 20):
    print("Number of average word length in text file: ", (num_awl))

elif('Most common word' == num_mcw):
    print("Number of most common word in text file: ", (num_mcw))


else:
    print('File does not exist')

