def lineSegmenter(input_line):
    first_words = ["Tab", "Cap", "Syp","Tab.","Tabs", "Cap.", "Syp.","Tablet","Tablets" "Capsule","Capsules" "Syrup" ]
    output=[]    
    curr_line = ""
    for word in input_line.split(' '):
        if word in first_words:
            output.append(curr_line)
            curr_line=""
        curr_line += word +" "
    output.append(curr_line)
    return output