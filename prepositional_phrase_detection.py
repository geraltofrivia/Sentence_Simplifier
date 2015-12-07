#Not including compound for now 
#Need to refactor code 
from spacy.en import English
nlp = English()

a = raw_input("enter a single sentece ")
doc = nlp(unicode(a))
from collections import defaultdict
def everything_detectorv3(doc):
	prepositional_phrase = {}
	clausal_phrase = defaultdict(list)
	subject_phrase = {}
	object_phrase = {}
	relation_phrase = {}
	modifier_phrase = defaultdict(list)
	quantifier_phrase = {}
	for tokens in doc:
		print tokens, tokens.dep_, tokens.head
		if tokens.dep_ == "ROOT":
			relation_phrase[tokens] = ""
			# print tokens,
			for a in tokens.children:
				#print a , a.dep_
				if a.dep_ == "conj":
					# print "in conj"
					relation_phrase[a] = ""
				if a.dep_ == "apos":
					# print "in pos"
					relation_phrase[a] = ""
		##Now you have got all the main root tokens .. relations = {"root1":"","root2":""}
	print relation_phrase		
	for root in relation_phrase:
		_root_token = []	#a temproary list for storing the subtree 
		for a in root.lefts:	#in order to maintain the sequences .. look into left , then root and finally right 
			if a.dep_ == "aux" or a.dep_ == "prt" or a.dep_ == "auxpass":
				for b in a.subtree:
					_root_token.append(b)
		_root_token.append(root)
		for a in root.rights:
			if a.dep_ == "aux" or a.dep_ == "prt":
				for b in a.subtree:
					_root_token.append(b)
		relation_phrase[root] = _root_token
	print "the relationship phrase"		
	print relation_phrase
	#detecting prepositonal phrase
	for tokens in doc:
		if tokens.dep_ == "prep":
			_prep_token = []
			for a in tokens.subtree:
				_prep_token.append(a)
			prepositional_phrase[tokens.head] = _prep_token
	print "the prepositional phrase"			
	print prepositional_phrase
# subject and object phrase
	for root in relation_phrase:
		for tokens in root.children:
			if tokens.dep_ =="nsubj" or tokens.dep_ == "nsubjpass" or tokens.dep_=="agent" or tokens.dep_ == "csubj" or tokens.dep_ == "csubjpass":
				#Now we have a list subject 
				subject_phrase[tokens] = ""
				for a in tokens.subtree:
					if a.dep_ == "conj" or a.dep_ == "apos":
						subject_phrase[a] = ""
			if tokens.dep_  == "attr" or tokens.dep_  == "dobj" or tokens.dep_  == "dative" or tokens.dep_ == "iobj" or tokens.dep_ == "oprd":
				object_phrase[tokens] = ""
				for a in tokens.subtree:
					if a.dep_ == "conj" or a.dep_ == "apos":
						object_phrase[a]="" 			
	print "subject phrase is "					
	print subject_phrase
	print "object phrase is "
	print object_phrase
# prepositional phrase
	for tokens in doc:
		if tokens.dep_ == "prep":
			_prep_token = []
			for a in tokens.subtree:
				_prep_token.append(a)
			prepositional_phrase[tokens.head] = _prep_token
	print "prepositional phrase is "		
	print prepositional_phrase
	for root in relation_phrase:
		for a in root.children:
			#write a function here
			if "comp" in a.dep_  or a.dep_ == "advcl" or a.dep_ == "mark" or a.dep_ == "rcmod": 
				_root_token = []
				for b in a.subtree:
					print b,
					_root_token.append(b)
				print _root_token	
				print a.head
				clausal_phrase[a.head].append(_root_token)
	for root in subject_phrase:
		for a in root.children:
			#write a function here
			if "comp" in a.dep_  or a.dep_ == "advcl" or a.dep_ == "mark" or a.dep_ == "rcmod": 
				_root_token = []
				for b in a.subtree:
					_root_token.append(b)
				clausal_phrase[a.head].append(_root_token)
	for root in object_phrase:
		for a in root.children:
			#write a function here
			if "comp" in a.dep_  or a.dep_ == "advcl" or a.dep_ == "mark" or a.dep_ == "rcmod": 
				_root_token = []
				for b in a.subtree:
					_root_token.append(b)
				clausal_phrase[a.head].append(_root_token)								
	print "clausal phrase are "
	print clausal_phrase
	for tokens in doc:
		if "mod" in tokens.dep_ or tokens.dep_ == "appos" or tokens.dep_ == "nn" or tokens.dep_ == "num" or tokens.dep_ == "meta" or tokens.dep_ == "poss":
			modifier_phrase[tokens.head].append(tokens)
	print "modifiers are "		
	print modifier_phrase

print everything_detectorv3(doc)