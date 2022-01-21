from flair.data import Sentence
from flair.models import SequenceTagger

# load the NER tagger
tagger = SequenceTagger.load('pos-fast')

file = open('../Data/test_monolingual_data.txt', 'r')
lines = file.readlines()
file.close()

output_file = open('./Tagged_Data/flair_output.txt', 'w')

count = 0

for line in lines:
    
    if count == 10000:
        break
    
    sentence = Sentence(line.strip())
    tagger.predict(sentence)

    output_file.write('======\n')
    output_file.write(line)
    output_file.write('\n')
    output_file.write('POS Tags:\n\n')

    for entity in sentence.get_labels('pos'):
        output_file.write('(' + entity.identifier.split()[0] + ', ' + entity.value + ')')
        output_file.write('\n')
    
    output_file.write('\n')
    output_file.write('======')
    count += 1

output_file.close()