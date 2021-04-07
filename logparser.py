import re

log_file_path = r"C:\Users\HP\Desktop\Solutions\LogData.log"
regex = '(<property name="(.*?)">(.*?)<\/property>)'
read_line = True

with open(log_file_path, "r") as file:
    match_list = []
    if read_line == True:
        for line in file:
            for match in re.finditer(regex, line, re.S):
                match_text = match.group()
                match_list.append(match_text)
                #print (match_text)
    else:
        data = f.read()
        for match in re.finditer(regex, data, re.S):
            match_text = match.group()
            match_list.append(match_text)


with open('Extracted_file.txt', 'w') as f:
    for item in match_list:
        f.write("%s\n" % item)
        
print("Extracted data from log file is saved in Extracted_file")