import ScheduleModel
import re

#Sample Input
scanned_lines=[
    ["Syp. Paracetamol x3d OD", "Paracetamol"],
    ["Tab. Combiflam twice a day for 5 days", "Combiflam"],
    ["Cap. Paracetamol bid", "Paracetamol"],
    ["Cap. Paracetamol td", "Paracetamol"],
    ["Tab. Paracetamol qd", "Paracetamol"],
    ["Tab. Paracetamol empty stomach", "Paracetamol"],
    ["Tab. Paracetamol x3 wks after meals thrice a day", "Paracetamol"],
    ["Tab. Paracetamol MWF OD", "Paracetamol"],
    ["Cap. Paracetamol before bed", "Paracetamol"],
    ["Syp. Paracetamol once a week for 8 wks", "Paracetamol"],
    ["Tab. Paracetamol every night for 7 d", "Paracetamol"]
]

def makeSchedule(line):
    Med = ScheduleModel.MedSchedule()
    Med.medicine_name = line[1]
    text = line[0]
    text = text.lower()
    
    #daily frequency
    if re.search("thrice(\W+)(a|o)(\W+)day", text) or re.search("t(i)?d", text) or re.search("three(\W+)times(\W+)(a|o)(\W+)day", text) or re.search("3(\W+)times(\W+)(a|o)(\W+)day", text) or re.search("(1|l|\\|\/|\|)(\W*)-(\W*)(1|l|\\|\/|\|)(\W*)-(\W*)(1|l|\\|\/|\|)", text):   #last one is 1-1-1
        Med.daily_frequency.night = True
        Med.daily_frequency.morning = True
        Med.daily_frequency.afternoon = True
    
    if re.search("twice(\W+)(a|o)(\W+)day", text) or re.search("b(i)?d", text) or re.search("two(\W+)times(\W+)(a|o)(\W+)day", text) or re.search("2(\W+)times(\W+)(a|o)(\W+)day", text) or re.search("(1|l|\\|\/|\|)(\W*)-(\W*)(0|o)(\W*)-(\W*)(1|l|\\|\/|\|)", text):
        Med.daily_frequency.night = True
        Med.daily_frequency.morning = True
    
    if re.search("once(\W+)(a|o)(\W+)day", text) or re.search("(\W+)od((\W)|$)", text) or re.search("one(\W+)time(\W+)(a|o)(\W+)day", text) or re.search("1(\W+)time(\W+)(a|o)(\W+)day", text) or re.search("(1|l|\\|\/|\|)(\W*)-(\W*)(o|0)(\W*)-(\W*)(o|0)", text):
        Med.daily_frequency.night = True  #can take user's preference when to take medicines which are to be taken once a day
    
    if re.search("qid", text) or re.search("four(\W+)times(\W+)(a|o)(\W+)day", text) or re.search("4(\W+)times(\W+)(a|o)(\W+)day", text):
        Med.daily_frequency.night = True        
        Med.daily_frequency.evening = True
        Med.daily_frequency.morning = True
        Med.daily_frequency.afternoon = True
    
    if re.search("empty(\W+)stomach", text) or re.search("early(\W+)morning", text):
        Med.daily_frequency.empty_stomach = True
    
    if re.search("every(\W+)night", text) or re.search("night(s?)", text) or re.search("each(\W+)night", text) or re.search("qpm", text):
        Med.daily_frequency.night = True
    if re.search("bedtime", text) or re.search("before(\W+)bed", text):
        Med.daily_frequency.night = True
        Med.specifications = 2  #after meal

    #til x days or weeks
    if re.search("(for)?(\W+)(\d+)(\W+)(day(s?)|d)", text) :
        numerics = [int(s) for s in re.findall(r'\d+', text)]
        days = numerics[0]
        Med.till_x_days = days
    if re.search("(for)?(\W+)(\d+)(\W+)(week(s?)|wk(s?))", text) :
        numerics = [int(s) for s in re.findall(r'\d+', text)]
        days = numerics[0]*7
        Med.till_x_days = days
    if re.search("x?(\W*)(\d+)(\W*)(day(s?)|d)", text) :
        numerics = [int(s) for s in re.findall(r'\d+', text)]
        days = numerics[0]
        Med.till_x_days = days
    if re.search("x?(\W*)(\d+)(\W*)(week(s?)|wk(s?))", text) :
        numerics = [int(s) for s in re.findall(r'\d+', text)]
        days = numerics[0]*7
        Med.till_x_days = days
    
    #emergency
    if re.search("prn", text) or re.search("sos", text):
        Med.Sos = True
        
    #specifications
    if re.search("before(\W+)meal(s?)", text) or re.search("before(\W+)lunch", text) or re.search("before(\W+)dinner", text) or re.search("(\W+)ac(\s)", text):
        Med.specifications = 1
    if re.search("after(\W+)meal(s?)", text) or re.search("after(\W+)lunch", text) or re.search("after(\W+)dinner", text) or re.search("after(\W+)breakfast", text) or re.search("(\W+)pc(\s)", text):
        Med.specifications = 2
        
    #weekly frequency
    if re.search("daily", text) or re.search("qd", text) or re.search("everyday", text):
        Med.weekly_frequency = 0
    if re.search("alternate(\W+)day(s?)", text) or re.search("qod", text) or re.search("mwf", text) or re.search("tts", text) or re.search("every other day", text):
        Med.weekly_frequency = 1
    if re.search("once(\W+)a(\W+)week", text) or re.search("weekly", text):
        Med.weekly_frequency = 2
    if re.search("twice(\W+)a(\W+)week", text) or re.search("bi(-?)weekly", text) or re.search("two(\W+)times(\W+)(in)?(\W+)(a)?(\W+)week", text):
        Med.weekly_frequency = 3
    
    return Med

def schedulePredicter(scanned_lines):
    output = []
    for line in scanned_lines:
        Med = makeSchedule(line)
        output.append(Med)
    return output