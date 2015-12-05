# Sentence_Simplifier
This repository is our attempts at NLP to break clauses, detect subjects, objects, relations, prepositional phrases etc.

**Contributors:**
  - Priyansh Trivedi
  - Gaurav Maheshwari
  - Silpa Rao
  - Hemil Shah
  - Yash Patel

To set this repo up on a fresh computer:

    $ git clone https://github.com/geraltofrivia/Sentence_Simplifier.git
    $ cd Sentence_Simplifier
    $ sudo apt-get install build-essential
    $ sudo apt-get install python-dev
    $ sudo pip install spacy
    $ sudo python -m spacy.en.download --force all
    $ sudo pip install -U nltk
    $ sudo pip install -U numpy
    $ python
    >>> import nltk
    >>> nltk.download()
    
To use the Clause classifier, we need to first train it. To do so, (while in the root directory of the repo)

    $ python
    $ import classifier
    $ c = classifier.Classifier()
    $ c.train()
    
At this point of time, we have installed every required library and trained our classifier over the given data. 
Now we're ready to handle anything that's thrown to this.

