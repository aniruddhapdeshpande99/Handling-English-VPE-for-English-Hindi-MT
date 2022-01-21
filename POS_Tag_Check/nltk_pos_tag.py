import nltk

file = open('../Data/test_monolingual_data.txt', 'r')
lines = file.readlines()
file.close()

output_file = open('./Tagged_Data/nltk_output.txt', 'w')

count = 0

for line in lines:

    if count == 10000:
        break
    
    tokens = nltk.word_tokenize(line.strip())
    
    output_file.write('======\n')
    output_file.write(line)
    output_file.write('\n')
    output_file.write('POS Tags:\n\n')
    
    tags = nltk.pos_tag(tokens)
    for index in range(0,len(tags)):
        tag = tags[index]
        curr_token = tag[0]
        curr_tag = tag[1]
        
        output_file.write('(' + curr_token + ', ' + curr_tag + ')')
        output_file.write('\n')
    
    output_file.write('\n')
    output_file.write('======')
    count += 1

output_file.close()