package com.example.medscheduler;

public class medicineSchedule {
    String name = "NA";
    int till_x_days = 1000;
    int specifications = 0; //2 = after meal, 1= before meal, 0= no specification
    int weekly_frequency = -1; //0=daily, 1= alternate days, 2= twice a week, 3 = once a week
    boolean Sos = false;
    boolean empty_stomach = false;
    boolean morning = false;
    boolean afternoon = false;
    boolean evening =false;
    boolean night = false;
}
