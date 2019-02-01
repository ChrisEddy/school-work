// ics226.lab5.ServerB 10101
// ics226.lab5.ClientB localhost 10101 + 1 2 3 4 5

package ics226.lab5;
import java.net.*;
import java.io.*;
import java.nio.charset.Charset;
import java.util.ArrayList;
import java.util.List;

class ServerB {
    public static void main(String[] args) {
        String port = args[0];
        try{
            ServerSocket socket = new ServerSocket(Integer.parseInt(port));
            // System.out.println("Server started on port:" + " " + port);

            while (true) {
                Socket client = socket.accept();
                // System.out.println("New Client");

                BufferedInputStream in = new BufferedInputStream(client.getInputStream());
                BufferedOutputStream out = new BufferedOutputStream(client.getOutputStream());
                PrintWriter stringOut = new PrintWriter(out);
                DataOutputStream dataOut = new DataOutputStream(out);
     
                byte[] buffer = new byte[1024];

                // System.out.println("Sending READY to client...");
                stringOut.write("READY\n");
                stringOut.flush();

                // System.out.println("Waiting for client response...");
                int count = in.read(buffer);

                List<Integer> numbers = new ArrayList<>();

                for (int i = 0; i < buffer.length; i++){ // create int list for math later
                    numbers.add(buffer[i] & 0xff);
                }
                // System.out.println(numbers);

                // System.out.println("Operand: " + numbers.get(0));
                // System.out.println("Count: " + numbers.get(1));

                double result = numbers.get(2);

                for(int i = 3; i <= (int)buffer[1] + 1; i++){
                    switch(numbers.get(0)){
                        case 0:
                        result = result - (buffer[i] & 0xff);
                        break;
                        case 1:
                        result = result + (buffer[i] & 0xff);
                        break;
                        case 2:
                        result = result * (buffer[i] & 0xff);
                        break;
                        case 3:
                        result = (double)result / (double)(buffer[i] & 0xff);
                        break;
                    }
                }

                // System.out.println("Result: " + result);


                // Send to Client

                if(result < 255){
                    buffer[0] = (byte)result;
                    dataOut.write(buffer);
                    dataOut.flush();
                }
                else{
                    int i = 0;
                    while(result > 255){
                        buffer[i] = (byte)255;
                        result = result - 255;
                        i++;
                    }
                    buffer[i] = (byte)result;
                    dataOut.write(buffer);
                    dataOut.flush();
                }
                
                // When done:
                // System.out.println("Closing Client...");
                client.close();
                // System.out.println("Closed Client");
            }
        }
        catch(IOException error){
            error.printStackTrace();
        }
    }
}