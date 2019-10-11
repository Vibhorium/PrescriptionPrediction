import fuzzy_matching

parameter_of_selection = 50

#Sample Input
scanned_lines=[
    "Syp. Paracetamol x3d OD",
    "Tab. Combiflam twice a day for 5 days",
]

def detect_lines_with_medicine(scanned_lines):
    output=[]
    for line in scanned_lines:
        words = line.split(' ')
#         print(words)
        curr_best_score=0
        curr_best_match="NA"
        curr_word_to_be_replaced =""
        for word in words:
            out = fuzzy_matching.find_Drug_Name(word)
#             print(out[0], "...", out[1])
            if (out[1] >= curr_best_score):
                curr_best_score=out[1]
                curr_best_match = out[0]
                curr_word_to_be_replaced = word
        if(curr_best_score > parameter_of_selection):
            line = line.replace(curr_word_to_be_replaced, curr_best_match)
            output.append([line, curr_best_match, curr_best_score])            
    return output