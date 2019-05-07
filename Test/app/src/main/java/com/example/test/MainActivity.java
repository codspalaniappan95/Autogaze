package com.example.test;

import android.app.Activity;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothServerSocket;
import android.bluetooth.BluetoothSocket;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.util.Log;
import android.view.View;
import android.widget.Button;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.UUID;

public class MainActivity extends Activity {
    BluetoothConnectionService mBluetoothConnection;
    private static final String TAG = "MY_APP_DEBUG_TAG";
    private Handler handler; // handler that gets info from Bluetooth service
    private UUID MY_UUID=UUID.randomUUID();
    BluetoothAdapter bluetoothAdapter = BluetoothAdapter.getDefaultAdapter();
    private BluetoothSocket socket;

    @Override
    protected void onCreate( Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Button button=findViewById(R.id.blue);
        Button button1=findViewById(R.id.start);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
            mBluetoothConnection.write("1");
            }
        });
        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
            mBluetoothConnection.connected(socket);
            }
        });
    }


}