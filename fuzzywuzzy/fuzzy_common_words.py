from fuzzywuzzy import fuzz
import re
file1 = open("common_words.txt","r") 

parameter_common_word = 55

common_words = file1.readlines()
common_words =[word[:-1] for word in common_words]

def fuzzy_common_word(input_word):
    max_score=0
    output="NA"
    for curr_word in common_words:
        curr_score=fuzz.token_set_ratio(input_word, curr_word)
        if(curr_score > max_score):
            max_score=curr_score
            output=curr_word

    return output, max_score

def replace_with_fuzzy_match(scanned_line):
    line = scanned_line[0]
    medicine_name = scanned_line[1]
    words = line.split(' ')
    output =""
    for word in words:
        #if word has a number skip it
        numerics = [int(s) for s in re.findall(r'\d+', word)]
        if(len(numerics) >0):
            output+= word
            output += " "
            continue
            
        if (word == medicine_name):  #skip if it is same as medicine name detected
            output += word
            output += " "
            continue
        fuzzy_match, score = fuzzy_common_word(word)
        print("For word: \"", word, "\" fuzzy match is \"", fuzzy_match, "\" with score--", score)
        if score >= parameter_common_word:
            word = fuzzy_match
        output += word
        output += " "
    return output

scanned_lines=[
    ["Sgp. Paracetamol x3d OD", "Paracetamol"],
    ["Taq. Combiflam fwise a day fon 5 days", "Combiflam"],
    ["Cap. Paracetamol bid", "Paracetamol"],
    ["Cap. Paracetamol td", "Paracetamol"],
    ["Tab. Paracetamol qd", "Paracetamol"],
    ["Tab. Paracetamol enptg stanach", "Paracetamol"],
    ["Tab. Paracetamol x3 wks abter neats thwico a dag", "Paracetamol"],
    ["Tab. Paracetamol MWT OD", "Paracetamol"],
    ["Cap. Paracetamol qefare beb", "Paracetamol"],
    ["Syp. Paracetamol omce a ueek for 8 wks", "Paracetamol"],
    ["Tab. Paracetamol euerg niyjt fur 7 d", "Paracetamol"]
]