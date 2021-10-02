
# Take an Input Phares from the User ---

a=input("Enter the Sentences")

# now here we can create a function for detecting words from Sentences and Serching words

def is_word_present(sentence,word):

    #Now We can put Every Letter from both in Lower Case to  Easily matche the word is Present or Not ..
    sentence = sentence.lower()
    word = word.lower()

    # Here I can Split the each word of sentences into word and ut it into a list
    list=sentence.split()

    # If Our List count is Greater than Zero(0)
    if(list.count(word) >0):
        return True
    else:
        return False

# Here is the Normal Function made using code
s= " 'Hello how are you doing' ,'My Name is joe',' I am going to home'"
word = "'how','what,'when','whome' "

if (is_word_present(s,word)):
    print("Yes")
else:
    print("No")