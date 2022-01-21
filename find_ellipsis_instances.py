import regex as re

output_lines  = []
with open("./Data/output_testdata.txt", 'r') as myfile:
    for line in myfile:
        output_lines.append(line)

print("Data Reading Complete")

line_index = 1
ellipsis_count = 0
curr_content = []
for line in output_lines:
    curr_content.append(line)
    if not (line[0].isdigit()):
        ellipsis_found_arr = re.search(r'Found verb:\s\s\[(.*?)\]', line)
        if ellipsis_found_arr is not None:
            bracket_content = re.search(r'\[(.*?)\]',line).group(1)
            if bracket_content != "":
                ellipsis_count+=1
                print("\n=====")
                for content in curr_content:
                    print(content)
                print("=====\n\n")
            curr_content = []
            line_index += 1            

print("Total %d instances of Ellipsis found amongst %d sentences" % (ellipsis_count, line_index))
