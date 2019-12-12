package com.example.cameraint;


import java.io.Serializable;

public class medicine_schedule implements Serializable {
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

    public String toString(){
        String x="\n";
        x+="name" + name +"\n";
        x+="till_x_days" + till_x_days+"\n";
        x+="specifications" + specifications+"\n";
        x+="weekly_frequency" + weekly_frequency+"\n";
        x+="Sos" + Sos+"\n";
        x+="empty_stomach"+ empty_stomach+"\n";
        x+="morning"+ morning + "\n";
        x+="afternoon"+afternoon+"\n";
        x+="evening"+evening+ "\n";
        x+="night"+night+"\n";
        return x;
    }
}
