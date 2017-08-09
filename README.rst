#######
Hangman
#######

Released: 08-August-2017

############
Introduction
############

This is a simple implemention of Hangman in Python. You can use this code as a guideline or just download it and play the game.
I've provided a set of German words that you can play with. If you're looking for a set of English words you might find some 
`here <https://github.com/dwyl/english-words>`__.
You can also check out this page for `other <https://github.com/wooorm/dictionaries/tree/master/dictionaries>`__ languages.
Note that this documention on the game probably fits best for beginners.

###########
Quick Setup
###########

Before running the game be sure to go into the code and replace the path with the one where you've saved the textfile with words.

::

    # Replace with the correct path
    self.filepath_words = ".../Hangman/GermanWords/Words.txt"

This could look like following after doing so:

::

  self.filepath_words = "C:/Users/Admin/Documents/Python/Games/Hangman/GermanWords/Words.txt"
  
#####################
When running the code
#####################

This version of Hangman works best when running it in the shell. This is due to the command 

::

  os.system("cls")
  
which clears the screen each time the user has confirmed his input. Should you be using a IDE dont be suprised if this command doesn't work.

To run the code go to the hangman directory and use the following command:

::

  $ python Hangman.py
  
You should now see something like this:

::

  - - - - - -

  Used letters:

  Lives: 10

  Take a guess:
  
Now you can start guessing :)
  
#############  
Closing words
#############

Coding is a hobby of mine and I don't do it reguarly - so please don't be too harsh on me:)

I've wanted to share this implementation of Hangman because when I was teaching a friend Python the other day I realised 
that there were only a few examples of it. I personally think this is a fantastic game to get started with
so I thought I'd make a (hopefully) well understandable documentation on it.
