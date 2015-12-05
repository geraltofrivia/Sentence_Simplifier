from nltk import MaxentClassifier
from nltk import classify
from spacy.en import English
from pprint import pprint
import pickle

import features
import reader



class Classifier:
    def __init__(self):
        self.datasource = reader.Reader()
        self.nlp = English(entity = False)
        self.featuresets = []

        try:
            f= open('maxent.pickle')
            self.classifier = pickle.load(f)
            f.close()
        except IOError:
            self.classifier = None

        print "Initialized correctly"

    def train(self):
        for sentence,tags in self.datasource:
            sentence_processed = self.nlp(u' '.join(sentence))
            for token in range(len(sentence)):
                self.featuresets.append((features.feature_compiler(token,sentence_processed),tags[token]))

        train_set, test_set = self.featuresets[0:-1000], self.featuresets[-1000:]
        pprint(train_set[:10])
        self.classifier = MaxentClassifier.train(train_set)

        #Saving the classifier
        self.save()

    def classify(self,_string):
        #Expects one sentence as a string
        _string =  unicode(_string)
        _string_processed = self.nlp(_string)
        tags = []
        for index in range(len(_string_processed)):
            featureset = features.feature_compiler(index,_string_processed)
            tags.append(self.classifier.classify(featureset))
        return tags

    def save(self):
        file= open('maxent.pickle','wb')
        pickle.dump(self.classifier, file)
        file.close()


