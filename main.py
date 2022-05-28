# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 

    with open ("story.txt", "r") as f:
        lines = f.read().lower()
        print (lines)
        split_lines = lines.split()
        print(split_lines)
        
        count = {}
    for text in split_lines:
        if text in count:
            count[text] += 1
        else:
            count[text] = 1
    print (count)

read_file_content('story.txt')        
    # return "Hello World"


# def count_words():
#     word = read_file_content('story.txt')
#     # # [assignment] Add your code here
#     print(word)
#     split_lines = text.split()
#     print(split_lines)
#     count = {}
#     for text in split_lines:
#         if text in count:
#             count[text] += 1
#         else:
#             count[text] = 1
#     return count   

# count_words()

#     return {"as": 10, "would": 20}