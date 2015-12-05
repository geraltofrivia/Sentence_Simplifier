import features
from spacy.en import English
nlp = English(entity=False)

a = u'We wish you a merry christmas'
ap = nlp(a)
x = features.feature_compiler(3,ap)
