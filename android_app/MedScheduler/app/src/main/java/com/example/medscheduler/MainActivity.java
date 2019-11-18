package com.example.medscheduler;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.os.Bundle;
import android.text.InputType;
import android.util.Log;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.LinearLayout.LayoutParams;
import android.widget.Spinner;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        LinearLayout outerBox = (LinearLayout) findViewById(R.id.outerBox);
        Log.i("Err", "found ob");

        medicineSchedule Med1 = new medicineSchedule();
        Med1.name = "Betadine";

        Log.i("Err", "made medicine object" + Med1);

        outerBox.addView(getMedicine(Med1, this));

    }

    public LinearLayout getMedicine(medicineSchedule M, Context context){
        LinearLayout ll = new LinearLayout(context);
        ll.setLayoutParams(new LayoutParams(LayoutParams.MATCH_PARENT,LayoutParams.WRAP_CONTENT));
        ll.setOrientation(LinearLayout.VERTICAL);
        ll.setPadding(0,15,10,0);

        LinearLayout ll1 = new LinearLayout(context);
        ll1.setLayoutParams(new LayoutParams(LayoutParams.MATCH_PARENT,LayoutParams.WRAP_CONTENT));
        ll1.setOrientation(LinearLayout.HORIZONTAL);
        ll1.setPadding(0,10,0,0);

        EditText name = new EditText(context);
        name.setLayoutParams(new LayoutParams(0,LayoutParams.MATCH_PARENT, 3));
        name.setText(M.name);

        TextView tv = new TextView(context);
        tv.setLayoutParams(new LayoutParams(0,LayoutParams.MATCH_PARENT, 1));
        tv.setText("Till no of days:");

        EditText days = new EditText(context);
        days.setLayoutParams(new LayoutParams(0,LayoutParams.MATCH_PARENT, 3));
        days.setInputType(InputType.TYPE_CLASS_NUMBER);
        days.setText(String.valueOf(M.till_x_days));

        ll1.addView(name);
        ll1.addView(tv);
        ll1.addView(days);

        LinearLayout ll2 = new LinearLayout(context);
        ll2.setLayoutParams(new LayoutParams(LayoutParams.MATCH_PARENT,LayoutParams.WRAP_CONTENT));
        ll2.setOrientation(LinearLayout.VERTICAL);
        ll2.setPadding(0,10,0,0);

        CheckBox c1 = new CheckBox(context);
        c1.setLayoutParams(new LayoutParams(ViewGroup.LayoutParams.WRAP_CONTENT,LayoutParams.MATCH_PARENT,1));
        c1.setText("Empty Stomach");
        if(M.empty_stomach==true)
            c1.setChecked(true);

        CheckBox c2 = new CheckBox(context);
        c2.setLayoutParams(new LayoutParams(ViewGroup.LayoutParams.WRAP_CONTENT,LayoutParams.MATCH_PARENT,1));
        c2.setText("Morning");
        if(M.morning==true)
            c2.setChecked(true);

        CheckBox c3 = new CheckBox(context);
        c3.setLayoutParams(new LayoutParams(ViewGroup.LayoutParams.WRAP_CONTENT,LayoutParams.MATCH_PARENT,1));
        c3.setText("Afternoon");
        if(M.afternoon==true)
            c3.setChecked(true);

        CheckBox c4 = new CheckBox(context);
        c4.setLayoutParams(new LayoutParams(ViewGroup.LayoutParams.WRAP_CONTENT,LayoutParams.MATCH_PARENT,1));
        c4.setText("Evening");
        if(M.evening==true)
            c4.setChecked(true);

        CheckBox c5 = new CheckBox(context);
        c5.setLayoutParams(new LayoutParams(ViewGroup.LayoutParams.WRAP_CONTENT,LayoutParams.MATCH_PARENT,1));
        c5.setText("Night");
        if(M.night==true)
            c5.setChecked(true);

        ll2.addView(c1);
        ll2.addView(c2);
        ll2.addView(c3);
        ll2.addView(c4);
        ll2.addView(c5);


        LinearLayout ll3 = new LinearLayout(context);
        ll3.setLayoutParams(new LayoutParams(LayoutParams.MATCH_PARENT,LayoutParams.WRAP_CONTENT));
        ll3.setOrientation(LinearLayout.HORIZONTAL);
        ll3.setPadding(0,10,0,0);

        Spinner s1 = new Spinner(context);
        s1.setLayoutParams(new LayoutParams(0,LayoutParams.MATCH_PARENT,1));
        List<String> arr1 = new ArrayList<String>();
        arr1.add("After meal");
        arr1.add("Before meal");
        arr1.add("No specification");
        ArrayAdapter<String> adap1 = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, arr1);
        adap1.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        s1.setAdapter(adap1);
        if(M.specifications==0)
            s1.setSelection(0);
        else if(M.specifications==1)
            s1.setSelection(1);
        else
            s1.setSelection(2);


        Spinner s2 = new Spinner(context);
        s2.setLayoutParams(new LayoutParams(0,LayoutParams.MATCH_PARENT,1));
        List<String> arr2 = new ArrayList<String>();
        arr2.add("Daily");
        arr2.add("Alternate days");
        arr2.add("Twice a week");
        arr2.add("Once a week");
        ArrayAdapter<String> adap2 = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, arr2);
        adap2.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        s2.setAdapter(adap2);
        if(M.weekly_frequency==0)
            s2.setSelection(0);
        else if(M.weekly_frequency==1)
            s2.setSelection(1);
        else if(M.weekly_frequency==2)
            s2.setSelection(2);
        else
            s2.setSelection(3);


        CheckBox cb = new CheckBox(context);
        cb.setLayoutParams(new LayoutParams(0,LayoutParams.MATCH_PARENT,1));
        cb.setText("S.O.S");
        if(M.Sos==true)
            cb.setChecked(true);

        ll3.addView(s1);
        ll3.addView(s2);
        ll3.addView(cb);

        ll.addView(ll1);
        ll.addView(ll2);
        ll.addView(ll3);

        Log.i("Err", "fn complete");


        return ll;
    }
}
