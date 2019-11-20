package com.example.medscheduler;

import android.app.Notification;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Intent;
import android.os.Build;
import android.os.Bundle;

import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.snackbar.Snackbar;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;

import android.os.IBinder;
import android.view.View;

public class notifyService extends AppCompatActivity {

//    @Override
    public IBinder onBind(Intent intent){
        return null;
    }
    @RequiresApi(api = Build.VERSION_CODES.JELLY_BEAN)
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_notify_service);
//        Toolbar toolbar = findViewById(R.id.toolbar);
//        setSupportActionBar(toolbar);
//
//        FloatingActionButton fab = findViewById(R.id.fab);
//        fab.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View view) {
//                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
//                        .setAction("Action", null).show();
//            }
//        });
        NotificationManager mNM = (NotificationManager)getSystemService(NOTIFICATION_SERVICE);
        Notification notification = new Notification(R.drawable.notification_icon, "Notify Alarm start", System.currentTimeMillis());
        Intent myIntent = new Intent(this , schedulerActivity.class);
        PendingIntent contentIntent = PendingIntent.getActivity(this, 0, myIntent, 0);
//        notification.setLatestEventInfo(this, "Notify label", "Notify text", contentIntent);
//        mNM.notify(NOTIFICATION, notification);
        Notification mNotify = new Notification.Builder(this)
                                .setContentTitle("Notification")
                                .setContentText("Take your medicines!")
                                .setSmallIcon(R.drawable.ic_launcher_foreground)
                                .setContentIntent(contentIntent)
//                                .setSound(sound)
                                .build();
        mNM.notify(1,mNotify);
    }

}
