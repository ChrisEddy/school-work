// ics226.lab5.ServerA 10101
// ics226.lab5.ClientA localhost 10101 + 1 2 3 4 5

package ics226.lab5;
import java.net.*;
import java.io.*;
import java.nio.charset.Charset;
import java.util.ArrayList;
import java.util.List;

class ServerA {
    public static void main(String[] args) {
        String port = args[0];
        try{
            ServerSocket socket = new ServerSocket(Integer.parseInt(port));
            System.out.println("Server started on port:" + " " + port);

            while (true) {
                Socket client = socket.accept();
                System.out.println("New Client");
                BufferedInputStream inputStream = new BufferedInputStream(client.getInputStream());
                BufferedOutputStream outputStream = new BufferedOutputStream(client.getOutputStream());
    
                // To read:
                byte[] buffer = new byte[1024];
                System.out.println("Reading inputStream...");
                int count = inputStream.read(buffer);
                String request = new String(buffer, Charset.forName("UTF-8")).trim();
                System.out.println(request);

                if(request.equals("READY")){
                    System.out.println("Got READY from server");
                    // do the task

                    // To write:
                    // … add bytes to buffer as required.
                    System.out.println("Writing to buffer and flushing...");
                    outputStream.write(buffer);
                    outputStream.flush();
        
                    // When done:
                    System.out.println("Closing Client...");
                    client.close();
                    System.out.println("Closed Client");
                }
                else{
                    System.out.println("Ready not recieved");
                }
            }
        }
        catch(IOException error){
            error.printStackTrace();
        }
    }
}
