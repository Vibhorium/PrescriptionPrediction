class DailyFrequency:
    empty_stomach = False
    morning = False
    afternoon = False
    evening =False
    night = False
    def __init(self):
        self.empty_stomach= False
        self.morning = False
        self.afternoon = False
        self.evening = False
        self.night = False

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
        self.daily_frequency = DailyFrequency()
    
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
#         if self.daily_frequency.empty_stomach:
        print("Empty Stomach: ", self.daily_frequency.empty_stomach)
#         if self.daily_frequency.morning:
        print("Morning: ", self.daily_frequency.morning)
#         if self.daily_frequency.afternoon:
        print("Afternoon: ", self.daily_frequency.afternoon)
#         if self.daily_frequency.evening:
        print("Evening: ", self.daily_frequency.evening)
#         if self.daily_frequency.night:
        print("Night: ", self.daily_frequency.night)
        
        if (self.specifications == 2):
            print("Specifcations : After Meal" )
        elif (self.specifications == 1):
            print("Specifcations : Before Meal" )
        print("--------------------------------------")
