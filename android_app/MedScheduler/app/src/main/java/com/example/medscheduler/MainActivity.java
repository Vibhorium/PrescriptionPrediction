package com.example.medscheduler;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class mainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home_page);

        final medicineSchedule[] Medicines = new medicineSchedule[3];

        //final medicineSchedule m1 = new medicineSchedule();
        Medicines[0] = new medicineSchedule();
        Medicines[0].name = "Crocin";
        Medicines[0].till_x_days = 3;
        Medicines[0].specifications = 2;
        Medicines[0].weekly_frequency = 0;
        Medicines[0].night = true;
        Medicines[0].Sos = true;

        Medicines[1] = new medicineSchedule();
        Medicines[1].name = "Ibuprofen";
        Medicines[1].till_x_days = 2;
        Medicines[1].specifications = 2;
        Medicines[1].weekly_frequency = 3;
        Medicines[1].morning = true;
        Medicines[1].night = true;

        Medicines[2] = new medicineSchedule();
        Medicines[2].name = "Lexapro";
        Medicines[2].till_x_days = 5;
        Medicines[2].specifications = 1;
        Medicines[2].weekly_frequency = 2;
        Medicines[2].morning = true;
        Medicines[2].evening = true;
        //random array of objects -

        Button submit_button = findViewById(R.id.uploadBtn);
        submit_button.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // Code here executes on main thread after user presses button
                Intent intent = new Intent(getBaseContext(), schedulerActivity.class);
                intent.putExtra("Medicines", Medicines);
                startActivity(intent);
            }
        });
    }
}
