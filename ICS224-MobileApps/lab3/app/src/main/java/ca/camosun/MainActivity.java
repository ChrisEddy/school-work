package ca.camosun;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity{
    final String tempLabel ="Temperature";
    final String c2fLabel = "C toF";
    final String f2cLabel = "F toC";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        TextView converterLabel = (TextView) findViewById(R.id.converterLabel);
        converterLabel.setText(tempLabel);
        Button leftButton = (Button) findViewById(R.id.leftButton);
        leftButton.setText(c2fLabel);
        Button rightButton = (Button) findViewById(R.id.rightButton);
        rightButton.setText(f2cLabel);
    }

    public void leftButton(View view) {
        EditText converterField = (EditText) findViewById(R.id.converterField);
        String temp = converterField.getText().toString();
        double convertedTemp = Double.parseDouble(temp) * 9.0 / 5.0 + 32.0;
        converterField.setText(Double.toString(convertedTemp));
    }

    public void rightButton(View view) {
        EditText converterField = (EditText) findViewById(R.id.converterField);
        String temp = converterField.getText().toString();
        double convertedTemp = (Double.parseDouble(temp) - 32.0) * 5.0 / 9.0;
        converterField.setText(Double.toString(convertedTemp));
    }
}
