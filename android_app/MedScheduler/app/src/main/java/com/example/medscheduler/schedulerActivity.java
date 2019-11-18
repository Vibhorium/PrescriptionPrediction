package com.example.medscheduler;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.text.InputType;
import android.util.Log;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.LinearLayout.LayoutParams;
import android.widget.Spinner;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.List;

public class schedulerActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        final LinearLayout outerBox = (LinearLayout) findViewById(R.id.outerBox);
        Log.i("Err", "found ob");


        medicineSchedule[] Medicines = (medicineSchedule[]) getIntent().getSerializableExtra("Medicines");
        // for loop = object call outerBox.addView(getMedicine(  "   obj ", this));

        for (int i=0; i<Medicines.length; i++){
            outerBox.addView(getMedicine(Medicines[i], this));
        }

//        medicineSchedule Med1 = new medicineSchedule();
//        Med1.name = "Betadine";
//
//        Log.i("Err", "made medicine object" + Med1);
//
//        outerBox.addView(getMedicine(Med1, this));

        Button addBtn = (Button) findViewById(R.id.addBtn);
        addBtn.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // Code here executes on main thread after user presses button
                medicineSchedule Med = new medicineSchedule();
                outerBox.addView(getMedicine(Med, getApplicationContext()));
            }
        });

        Button submitBtn = (Button) findViewById(R.id.submitBtn);
        submitBtn.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // Code here executes on main thread after user presses button

                medicineSchedule[] Meds = saveSchedule();

                for(int i=0; i<Meds.length; i++) {
                    Log.i("Medicines", Meds[i].toString());
                }

                Intent intent = new Intent(getBaseContext(), profilePage.class);
                intent.putExtra("Medicines", Meds);
                startActivity(intent);
            }
        });
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
        arr1.add("No specification");
        arr1.add("Before meal");
        arr1.add("After meal");
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

    public medicineSchedule[] saveSchedule(){
        LinearLayout outerBox = findViewById(R.id.outerBox);
        int count = outerBox.getChildCount();
        medicineSchedule[] Medicines = new medicineSchedule[count];
        for(int i=0; i<count; i++) {
            Medicines[i] = new medicineSchedule();
            LinearLayout med = (LinearLayout) outerBox.getChildAt(i);
            LinearLayout one = (LinearLayout) med.getChildAt(0);
            LinearLayout two = (LinearLayout) med.getChildAt(1);
            LinearLayout three = (LinearLayout) med.getChildAt(2);

            EditText namee = (EditText) one.getChildAt(0);
            Medicines[i].name = namee.getText().toString();
            EditText till_days = (EditText) one.getChildAt(2);
//            if(one.getChildAt(2).toString().length() > 0)
            Medicines[i].till_x_days = Integer.parseInt(till_days.getText().toString());

            CheckBox check0 = (CheckBox)two.getChildAt(0);
            if(check0.isChecked())
                Medicines[i].empty_stomach = true;

            CheckBox check1 = (CheckBox)two.getChildAt(1);
            if(check1.isChecked())
                Medicines[i].morning = true;

            CheckBox check2 = (CheckBox)two.getChildAt(2);
            if(check2.isChecked())
                Medicines[i].afternoon = true;

            CheckBox check3 = (CheckBox)two.getChildAt(3);
            if(check3.isChecked())
                Medicines[i].evening = true;

            CheckBox check4 = (CheckBox)two.getChildAt(4);
            if(check4.isChecked())
                Medicines[i].night = true;

            Spinner specifications = (Spinner) three.getChildAt(0);
            int selectedItem = specifications.getSelectedItemPosition();
            Medicines[i].specifications = selectedItem;

            Spinner weekly_freq = (Spinner) three.getChildAt(1);
            int index = weekly_freq.getSelectedItemPosition();
            Medicines[i].weekly_frequency = index;

            CheckBox check_sos = (CheckBox)three.getChildAt(2);
            if(check_sos.isChecked())
                Medicines[i].Sos = true;
        }
        return Medicines;
    }
}
