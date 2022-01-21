import spacy
nlp = spacy.load("en_core_web_sm")

file = open('../Data/test_monolingual_data.txt', 'r')
lines = file.readlines()
file.close()

output_file = open('./Tagged_Data/spacy_output.txt', 'w')

count = 0

for line in lines:
    if count  == 10000:
        break
    doc = nlp(line.strip())
    
    output_file.write('======\n')
    output_file.write(line)
    output_file.write('\n')
    output_file.write('POS Tags:\n\n')
    
    for token in doc:
        output_file.write('(' + token.text + ', ' + token.pos_ + ', ' + token.tag_ + ', ' + token.dep_ + ')')
        output_file.write('\n')
    
    output_file.write('\n')
    output_file.write('======')
    count += 1

output_file.close()