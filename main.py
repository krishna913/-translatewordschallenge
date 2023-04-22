import time
import psutil
import csv
import re

#to calculate the time at the start of the program
Time_calculation_output = time.time()

#total english words list
english_words=[]
#french_words_list
french_words = []
#frequency_of words_saving
frequencylist={}


#to read the input file
inputfile = open("C:\\find_words.txt", "r")
findingwords = inputfile.read()
inputfile.close()
findlist = findingwords.split()

#regular expression....
shakespeare_input = open("c:\\t8.shakespeare.txt", 'r')
input_text = shakespeare_input.read().lower()
regular_expression_match = re.findall(r'\b[a-z]\b', input_text)
with open('c:\\french_dictionary.csv', mode='r') as csv_input:
    csv_storage = csv.reader(csv_input)
    dictionary_input = {rows[0]: rows[1] for rows in csv_storage}
for text in regular_expression_match:
    if text in findlist:
        english_words.append(text)
english = set(english_words)
english = list(english)


for i in english:
    for key, value in dictionary_input.items():
        if i in key:
            french_words.append(value)

# frequency list calculation
for j in english_words:
    num_count = frequencylist.get(j, 0)
    frequencylist[j] = num_count + 1
frequency_list_store = frequencylist.keys()
freq = []
for a in frequency_list_store:
    freq.append(frequencylist[a])
output_f= list(zip(english, french_words, freq))

#frequency file creation
appear_at_top= ['English Word', 'French Word', 'Frequency']
with open('frequency.csv', 'w', encoding='UTF8') as fileedit:
    writer = csv.writer(fileedit)
    writer.writerow(appear_at_top)
    for row in output_f:
        for x in row:
            fileedit.write(str(x) + ',')
        fileedit .write('\n')

# t8.shakespeare.translated.txt output file creation
trans = input_text
print("The original string is : " + str(trans))
dictinput = dictionary_input
store_input= trans.split()
result_output= []
for inp in store_input:
    result_output.append(dictinput.get(inp, inp))
result_output = ' '.join(result_output)
translated = open("t8.shakespeare.translated.txt", "w")
translated.write(str(result_output))
translated.close()
total_time_cal = time.time() - Time_calculation_output
used_memory = psutil.cpu_percent(total_time_cal)



#performance and the time taken to complete
perf = open("performance.txt", "w")
perf.write(f'Time to process: 0 minutes {total_time_cal} seconds\nMemory used: {used_memory} MB')
perf.close()
