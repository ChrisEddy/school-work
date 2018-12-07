// ics226.lab5.ServerA 10101
// ics226.lab5.ClientA localhost 10101 + 1 2 3 4 5

package ics226.lab5;
import java.net.*;
import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.nio.charset.Charset;

class ClientA {
    public static void main(String[] args) {
        String host = "";
        String port = "";
        String operand = "";
        List<String> numbers = new ArrayList<>();
        System.out.println("Client running");

        for (int i = 0; i < args.length; i++) {
            if(i == 0){
                host = args[i];
            }
            if(i == 1){
                port = args[i];
            }
            if(i == 2){
                operand = args[i];
            }
            else if(i > 2){
                numbers.add(args[i]);
            }
        }
        System.out.println(host + " " + port + " " + operand + " " + numbers);

        try{
            Socket socket = new Socket(host, Integer.parseInt(port));
            BufferedInputStream inputStream = new BufferedInputStream(socket.getInputStream());
            BufferedOutputStream outputStream = new BufferedOutputStream(socket.getOutputStream());
    
            // To read:
            byte[] buffer = new byte[1024];

            String ready = "READY\n";
            byte[] data = ready.getBytes(Charset.forName("UTF-8"));

            for(int i = 0; i < data.length; i++){
                buffer[i] = data[i];
            }

            // To write:
            // … add bytes to buffer as required.
            outputStream.write(buffer);
            outputStream.flush();
    
            // When done:
            socket.close();
        }
        catch(IOException error){
            error.printStackTrace();
        }

    }
}


