from nltk import MaxentClassifier
from nltk import classify
from spacy.en import English
import features
import reader



class Classifier:
    def __init__(self):
        self.datasource = reader.Reader()
        self.nlp = English(entity = False)
        self.featuresets = []

        print "Initialized correctly"

    def train(self):
        for sentence,tags in datasource:
            sentence_processed = nlp(u' '.join(sentence))
            for token in range(len(sentence)):
                self.featuresets.append((features.feature_compiler(token,sentence_processed),tags[token]))

        train_set, test_set = self.featuresets[0:-1000], self.featuresets[-1000,]
        me3_megam_classifier = MaxentClassifier.train(train_set, "megam")



# for document in datasource:
#     document_id, processed_document = nlp(document)                         #Process the entire file as a single document.
#     annotated_data = Reader.juxtapose(document_id,processed_document)       #Use the tags detected for the document.

#     '''Annotated data is of this format:
#     [ document begins
#         [   sentence begins
#             (token,tag),(token,tag)
#         ],
#         [   sentence begins
#             (token,tag),(token,tag)
#         ]
#     ]
#     '''

#     for sentence in annotated_data:
#         sentence_ = [x[0] for x in sentence]
#         for token in range(len(sentence)):
#             featuresets.append((features.feature_compiler(token,sentence_),sentence[token][1]))
