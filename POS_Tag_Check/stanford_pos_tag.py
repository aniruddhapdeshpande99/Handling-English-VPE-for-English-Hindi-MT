"""
CC Coordinating conjunction
CD Cardinal number
DT Determiner
EX Existential there
FW Foreign word
IN Preposition or subordinating conjunction
JJ Adjective
JJR Adjective, comparative
JJS Adjective, superlative
LS List item marker
MD Modal
NN Noun, singular or mass
NNS Noun, plural
NNP Proper noun, singular
NNPS Proper noun, plural
PDT Predeterminer
POS Possessive ending
PRP Personal pronoun
PRP$ Possessive pronoun
RB Adverb
RBR Adverb, comparative
RBS Adverb, superlative
RP Particle
SYM Symbol
TO to
UH Interjection
VB Verb, base form
VBD Verb, past tense
VBG Verb, gerund or present participle
VBN Verb, past participle
VBP Verb, non­3rd person singular present
VBZ Verb, 3rd person singular present
WDT Wh­determiner
WP Wh­pronoun
WP$ Possessive wh­pronoun
WRB Wh­adverb
"""

from pycorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP('http://0.0.0.0:9000')

file = open('../Data/test_monolingual_data.txt', 'r')
lines = file.readlines()
file.close()

output_file = open('./Tagged_Data/stanford_output.txt', 'w')

count = 0

for line in lines:
    
    if count == 10000:
        break
    
    output_file.write('======\n')
    output_file.write(line)
    output_file.write('\n')
    output_file.write('POS Tags:\n\n')
    
    result = nlp.annotate(line.strip(),properties = {'annotaters': 'pos', 'outputFormat': 'conll', 'timeout': '50000',})
    curr_result = result.split("\r\n")
    
    for token in curr_result:
        if token != '':
            tag_content = token.split('\t')
            output_file.write('(' + tag_content[1] + ', ' + tag_content[3] + ', ' + tag_content[6] + ')')
            output_file.write('\n')
    
    output_file.write('\n')
    output_file.write('======')
    count += 1





