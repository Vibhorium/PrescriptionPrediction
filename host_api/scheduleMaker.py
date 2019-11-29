import re

class MedSchedule:
#     medicine_name = "NA",
#     till_x_days = 100000, #default is infinite days
#     specifications = 0,  # 0 = no specifications, 1 = before meal, 2 = after meal
#     weekly_frequency = -1, #0=daily, 1= alternate days, 2= twice a week, 3 = once a week
#     Sos = False #true when the medicine is to be taken only on emergency
#     daily_frequency = DailyFrequency()
    
    def __init__(self):
        self.medicine_name = "NA"
        self.till_x_days = 100000
        self.specifications = 0
        self.weekly_frequency = -1
        self.Sos = False
        self.empty_stomach= False
        self.morning = False
        self.afternoon = False
        self.evening = False
        self.night = False
#         self.daily_frequency = DailyFrequency()
    
    def printSchedule(self):
        print("Medicine Name: ", self.medicine_name)
        
        if(self.Sos == True):
            print("SOS only")
        
        if (self.till_x_days != 100000):
            print("Till ", self.till_x_days, "Days")
        
        if (self.weekly_frequency == 0):
            print("To be taken : Daily" )
        elif (self.weekly_frequency == 1):
            print("To be taken : On alternate days" )
        elif (self.weekly_frequency == 2):
            print("To be taken : Once a week" )
        elif (self.weekly_frequency == 3):
            print("To be taken : Twice a week" )
            
        print("Daily Schedule: -> ")
        if self.empty_stomach:
            print("Empty Stomach: ", self.empty_stomach)
        if self.morning:
            print("Morning: ", self.morning)
        if self.afternoon:
            print("Afternoon: ", self.afternoon)
        if self.evening:
            print("Evening: ", self.evening)
        if self.night:
            print("Night: ", self.night)
        
        if (self.specifications == 2):
            print("Specifcations : After Meal" )
        elif (self.specifications == 1):
            print("Specifcations : Before Meal" )
        print("--------------------------------------")

        
def makeSchedule(line):
    Med = MedSchedule()
    Med.medicine_name = line[1]
    text = line[0]
    text = text.lower()
    
    #daily frequency
    if re.search("thrice(\W+)(a|o)(\W+)day", text) or re.search("t(i)?d", text) or re.search("three(\W+)times(\W+)(a|o)(\W+)day", text) or re.search("3(\W+)times(\W+)(a|o)(\W+)day", text) or re.search("(1|l|\\|\/|\|)(\W*)-(\W*)(1|l|\\|\/|\|)(\W*)-(\W*)(1|l|\\|\/|\|)", text):   #last one is 1-1-1
        Med.night = True
        Med.morning = True
        Med.afternoon = True
    
    if re.search("twice(\W+)(a|o)(\W+)day", text) or re.search("b(i)?d", text) or re.search("two(\W+)times(\W+)(a|o)(\W+)day", text) or re.search("2(\W+)times(\W+)(a|o)(\W+)day", text) or re.search("(1|l|\\|\/|\|)(\W*)-(\W*)(0|o)(\W*)-(\W*)(1|l|\\|\/|\|)", text):
        Med.night = True
        Med.morning = True
    
    if re.search("once(\W+)(a|o)(\W+)day", text) or re.search("(\W+)od((\W)|$)", text) or re.search("one(\W+)time(\W+)(a|o)(\W+)day", text) or re.search("1(\W+)time(\W+)(a|o)(\W+)day", text) or re.search("(1|l|\\|\/|\|)(\W*)-(\W*)(o|0)(\W*)-(\W*)(o|0)", text):
        Med.night = True  #can take user's preference when to take medicines which are to be taken once a day
    
    if re.search("qid", text) or re.search("four(\W+)times(\W+)(a|o)(\W+)day", text) or re.search("4(\W+)times(\W+)(a|o)(\W+)day", text):
        Med.night = True        
        Med.evening = True
        Med.morning = True
        Med.afternoon = True
    
    if re.search("empty(\W+)stomach", text) or re.search("early(\W+)morning", text):
        Med.empty_stomach = True
    
    if re.search("every(\W+)night", text) or re.search("night(s?)", text) or re.search("each(\W+)night", text) or re.search("qpm", text):
        Med.night = True
    if re.search("bedtime", text) or re.search("before(\W+)bed", text):
        Med.night = True
        Med.specifications = 2  #after meal
        
    #for numeric schedule
    if re.search("(1|l|\\|\/|\|)(\W*)-(\W*)(1|l|\\|\/|\|)(\W*)-(\W*)(1|l|\\|\/|\|)", text):
        Med.morning=True
        Med.afternoon=True
        Med.night=True
        
    if re.search("(1|l|\\|\/|\|)(\W*)-(\W*)(0|o)(\W*)-(\W*)(1|l|\\|\/|\|)", text):
        Med.morning=True
        Med.night=True
        
    if re.search("(1|l|\\|\/|\|)(\W*)-(\W*)(o|0)(\W*)-(\W*)(o|0)", text):
        Med.night=True
        
    #for circles shcedule
    if re.search("(0|o)(\W+)(0|o)(\W+)(0|o)", text):
        Med.morning=True
        Med.afternoon=True
        Med.night=True
        
    if re.search("(0|o)(\W+)(0|o)", text):
        Med.morning=True
        Med.night=True
        
    if re.search("(\W)(0|o)(\W)", text):
        Med.night=True


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
        print(vars(Med))
        output.append(Med)
    return output
