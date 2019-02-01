// ics226.lab5.ServerA 10101
// ics226.lab5.ClientA localhost 10101 + 1 2 3 4 5

package ics226.lab5;
import java.net.*;
import java.io.*;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;
import java.nio.charset.Charset;

class ClientA {
    public static void main(String[] args) {
        String host = "";
        String port = "";
        String operand = "";
        int operandNum = 0;
        List<Integer> numbers = new ArrayList<>();
        // System.out.println("Client running");

        for (int i = 0; i < args.length; i++) {
            if(i == 0){
                host = args[i];
            }
            if(i == 1){
                port = args[i];
            }
            if(i == 2){
                operand = args[i];
                switch(operand){
                    case "-": 
                    operandNum = 0;
                    break;
                    case "+": 
                    operandNum = 1;
                    break;
                    case "*": 
                    operandNum = 2;
                    break;
                    case "/": 
                    operandNum = 3;
                    break;
                }
            }
            else if(i > 2){
                numbers.add(Integer.parseInt(args[i]));
            }
        }
        // System.out.println(host + " " + port + " " + operand + " " + numbers);

        try{
            Socket socket = new Socket(host, Integer.parseInt(port));
            BufferedInputStream inputStream = new BufferedInputStream(socket.getInputStream());
            BufferedOutputStream outputStream = new BufferedOutputStream(socket.getOutputStream());
    
            byte[] buffer = new byte[1024];
            int count = inputStream.read(buffer); // Wait for READY from server
            String request = new String(buffer, Charset.forName("UTF-8")).trim(); //Convert to String and trim excess space
            // System.out.println(request);

            if(request.equals("READY")){
                // System.out.println("READY recieved from server");

                buffer[0] = (byte)operandNum; // make first index the operand
                buffer[1] = (byte)numbers.size(); // make second index the count

                for (int i = 0; i < numbers.size(); i++){ // assign buffer numbers 
                    buffer[i + 2] = (byte)numbers.get(i).intValue();
                    // System.out.println((byte)numbers.get(i).intValue());
                }

                // System.out.println("operandnum: " + operandNum);
    
                outputStream.write(buffer); // send it off
                outputStream.flush();

                // Get result
                int result = 0;
 
                inputStream.read(buffer);

                result = buffer[0] & 0xff;

                System.out.println(result);

        
                // When done:
                socket.close();

            }
            else{
                // System.out.println("Ready not recieved");
            }

        }
        catch(IOException error){
            error.printStackTrace();
        }

    }
}


