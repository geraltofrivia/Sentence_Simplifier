'''This script is a set of features which we would run, on our dataset.
The return type of every function would be of this form :

{
	'feature 1': value 1,
	'feature 2': value 2
}

This is our featureset -

1. wordform: word form of this word
2. wordpos: POS tag of the word
3...


We then use NLTK's classifier to use maxent model to train over the data using this feature set
'''

def feature_compiler(_word_index, _sentence):
    '''This function compiles the entire feature set per word.

                    **args**


    _word_token: the index of the processed form of this word in the sentence`
    type: Integer

    _cluster: +- 3 words around the current word, bounded by the sentence
    type: list of spacy.Token

    _sentence: The sentence to which this word belongs
    type: list of spacy.Token
    '''

    _sentence = [x for x in _sentence]
    _word_token = _sentence[_word_index]

    _cluster = _sentence[max(0,_word_index - 3) : (min(len(_sentence)-1,_word_index + 3))]

    for token in _sentence:
        print [str(token),token.pos_,token.dep_]

    features = {}
    features["wordform"] = str(_word_token)                                        #Just the word. String
    features["wordpos"] = _word_token.pos_                                         #Pos tag of the word
    features["clusterpos"] = [x.pos_ for x in _cluster]                            #Pos tag of the cluster
    features["clusterlemma"] = [x.lemma_ for x in _cluster]                        #Lemma form of the cluster
    features["clusterpunct"] = 'PUNCT' in [ x.pos_ for x in _cluster]              #Boolean value True if punctuation in cluster. Else False
    features["distancefromroot"] = min([abs(_sentence.index(x) - _sentence.index(_word_token)) for x in _sentence if x.dep_ == u'ROOT'])         #Shortest Distance from a root to this word
    features["samewordneighbours"] = _word_index > 0 and _word_index < len(_sentence)-1 and str(_sentence[max(0,_word_index - 1)]) == str(_sentence[min(len(_sentence),_word_index + 1)])       #If the previous and the next word are the same
    features["sameposneighbours"] = _word_index > 0 and _word_index < len(_sentence)-1 and _sentence[max(0,_word_index - 1)].pos_ == _sentence[min(len(_sentence),_word_index + 1)].pos_       #If the previous and the next word are the same
    features["clusterverb"] = u'VERB' in [x.dep_ for x in _cluster]                 #Whether you encounter a verb in the cluster
    features["punctuationfreq"] = len([x for x in cluster if x.pos_ == u'PUNCT'])   #Number of punctuation in cluster
    features["verbfreq"] = len([x for x in cluster if x.pos_ == u'VERB'])           #Number of verb in cluster
    features["verbfreq"] = len([x for x in cluster if x.pos_ == u'VERB'])           #Number of verb in cluster




    #Return the dictionary.
    return features

