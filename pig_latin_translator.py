print "Welcome to the Pig-Latin translator!"

#Like the title says, translate your text into Pig-Latin. Made 8/28/2016. Have fun!

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
   word = original.lower()
   first = word[0]
   new_word = word + first + pyg
   new_word = new_word [1:len(new_word)]
   print new_word

elif len(original) <= 0 or original.isalpha() is False:
    print "Please only use letters from A to Z when using the Pig-Latin translator. Thank you."

else:
    print "Derpy derp derrr"

word = original.lower()
first = word[0]
new_word = word + first + pyg
new_word = new_word[1:len(new_word)]
