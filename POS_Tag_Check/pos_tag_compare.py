import nltk
import spacy
from pycorenlp import StanfordCoreNLP
import json

nlp_spacy = spacy.load("en_core_web_sm") # Loading Spacy
nlp_stanford = StanfordCoreNLP('http://0.0.0.0:9000') # Loading Stanford

# Reading Sentences
file = open('../Data/test_monolingual_data.txt', 'r')
lines = file.readlines()
file.close()

all_comparisons = []

count = 0

for line in lines:

    if count == 10000:
        break
    
    # Dict to Store conflict data
    tag_conflicts = {}
    tag_conflicts['Sentence'] = line.strip()

    # Retrieving Tokens and Tags for Stanford parser
    stanford_result = nlp_stanford.annotate(line.strip(),properties = {'annotaters': 'pos', 'outputFormat': 'conll', 'timeout': '50000',})
    stanford_result = stanford_result.split("\r\n")
    stanford_tokens = []
    stanford_tags = []
    for token in stanford_result:
        if token != '':
            tag_content = token.split('\t')
            stanford_tokens.append(tag_content[1])
            stanford_tags.append(tag_content[3])
    

    # Retrieving Tokens and Tags for Spacy parser
    spacy_result = nlp_spacy(line.strip())
    spacy_tokens = []
    spacy_tags = []
    for token in spacy_result:
        spacy_tokens.append(token.text) 
        spacy_tags.append(token.tag_)
    
    # Retrieving Tokens and Tags for NLTK parser
    nltk_tokens = nltk.word_tokenize(line.strip())
    nltk_result = nltk.pos_tag(nltk_tokens)
    nltk_tokens_copy = []
    nltk_tags = []
    for tag in nltk_result:
        nltk_tokens_copy.append(tag[0])
        nltk_tags.append(tag[1])   
    nltk_tokens = nltk_tokens_copy
    # print(str(len(nltk_tokens)) + ', ' + str(len(spacy_tokens)) + ', ' + str(len(stanford_tokens)))

    # If there are Different number of Tokens then there is both Tag and Token Conflict
    if len(nltk_tokens) != len(spacy_tokens) or len(nltk_tokens) != len(stanford_tokens) or len(spacy_tokens) != len(stanford_tokens):
        tag_conflicts['Token_count_conflict'] = True
        tag_conflicts['Tag_conflict'] = True
    else:
        tag_conflicts['Token_count_conflict'] = False
        tag_conflicts['Tag_conflict'] = False

    # print(tag_conflicts['Token_count_conflict'])
    
    # Checking for Individual Tag conflicts when there is no Token Count Conflict
    if not tag_conflicts['Token_count_conflict']:
        tag_conflicts['Token_wise_conflicts'] = []
        for index in range(0, len(nltk_tags)):
            curr_token_tags = {}
            curr_token_tags['token'] = spacy_tokens[index]
            curr_token_tags['nltk_tag'] = nltk_tags[index]
            curr_token_tags['stanford_tag'] = stanford_tags[index]
            curr_token_tags['spacy_tag'] = spacy_tags[index]
            
            # All Tags are same
            if curr_token_tags['nltk_tag'] == curr_token_tags['stanford_tag'] and curr_token_tags['stanford_tag'] == curr_token_tags['spacy_tag']:
                curr_token_tags['Different'] = 'ALL_SAME'
            
            # NLTK Tag is different
            elif curr_token_tags['nltk_tag'] != curr_token_tags['stanford_tag'] and curr_token_tags['nltk_tag'] != curr_token_tags['spacy_tag'] and curr_token_tags['stanford_tag'] == curr_token_tags['spacy_tag']:
                curr_token_tags['Different'] = 'nltk'
                tag_conflicts['Tag_conflict'] = True
            
            # Spacy Tag is different
            elif curr_token_tags['spacy_tag'] != curr_token_tags['stanford_tag'] and curr_token_tags['spacy_tag'] != curr_token_tags['nltk_tag'] and curr_token_tags['stanford_tag'] == curr_token_tags['nltk_tag']:
                curr_token_tags['Different'] = 'spacy'
                tag_conflicts['Tag_conflict'] = True
            
            # Stanford Tag is different
            elif curr_token_tags['stanford_tag'] != curr_token_tags['nltk_tag'] and curr_token_tags['stanford_tag'] != curr_token_tags['spacy_tag'] and curr_token_tags['nltk_tag'] == curr_token_tags['spacy_tag']:
                curr_token_tags['Different'] = 'stanford'
                tag_conflicts['Tag_conflict'] = True
            
            # All Tags different
            else:
                curr_token_tags['Different'] = 'ALL_DIFFERENT'
                tag_conflicts['Tag_conflict'] = True
            
            tag_conflicts['Token_wise_conflicts'].append(curr_token_tags)
    
    # Appending content to all comparisons
    all_comparisons.append(tag_conflicts)
    print('Conflict comparison for the line is completed: ' + line.strip())
    count += 1

# Only selecting sentences with conflict
only_with_conflicts = []
for i in range(0,len(all_comparisons)):
    if all_comparisons[i]['Token_count_conflict'] == True or all_comparisons[i]['Tag_conflict'] == True:
        only_with_conflicts.append(all_comparisons[i])

# Storing them as JSON file
with open("./Tagged_Data/pos_tag_conflicts.json", "w") as outfile:
    json.dump(only_with_conflicts, outfile)






            



