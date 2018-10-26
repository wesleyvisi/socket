package com.example.wesley.idoso;

import android.os.Vibrator;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

public class Alerta extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_alerta);

        Vibrator vibrator = (Vibrator) getSystemService(VIBRATOR_SERVICE);
        long milliseconds = 2000;
        vibrator.vibrate(milliseconds);
//        for(int i = 0;i < 50;i++){
//            Vibrator vibrator = (Vibrator) getSystemService(VIBRATOR_SERVICE);
//            long milliseconds = 2000;
//            vibrator.vibrate(milliseconds);
//        }
    }
}
