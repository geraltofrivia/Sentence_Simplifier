import os

class Reader:
    '''
    The objective of this class is to read data from all the files.
    Thus in effect, this happens -
         iter yields
         [sentence1]

    '''
    def __init__(self):
        self.dataset_directory =  os.path.join(os.path.dirname(__file__), 'clauses/data')
        self.datafiles = os.listdir(self.dataset_directory)
        self.tagdata = {}

    def __iter__(self):
        #Returns one sentence per sentence
        for file_name in self.datafiles:
            file_obj = open(os.path.join(self.dataset_directory,file_name))
            file_data =  file_obj.read()
            for sentence in file_data.split("\n\n"):
                sentence_words = []
                sentence_tags = []
                for token in sentence.split("\n"):
                    sentence_words.append(token.split()[0])
                    sentence_tags.append(token.split()[-1])
                yield sentence_words, sentence_tags
