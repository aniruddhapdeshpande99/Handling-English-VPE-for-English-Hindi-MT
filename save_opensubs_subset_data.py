data_lines  = []
with open("/mnt/d/Work/New_Research/Ellipsis_Detection/Data/OpenSubtitles_Dataset/en.txt") as myfile:
    data_lines = [next(myfile) for x in range(30000)]

with open('./test_monolingual_data.txt', 'w') as f:
    for item in data_lines:
        f.write("%s" % item)