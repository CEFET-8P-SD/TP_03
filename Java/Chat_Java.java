import org.zeromq.ZMQ;
import org.zeromq.ZContext;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.format.DateTimeFormatter;
import java.util.Date;
import java.util.Scanner;


public class Chat_Java
{
    public static void main(String[] args) throws Exception
    {
        Scanner ler = new Scanner(System.in);

        System.out.printf("----------------------------------\n");
        System.out.printf("      Welcome to Java Chat…       \n");
        System.out.printf("----------------------------------\n");

        System.out.printf("What is your name? \n");
        String nome = ler.nextLine();

        try (ZContext context = new ZContext()) {
            // Socket to talk to clients
            ZMQ.Socket socket = context.createSocket(ZMQ.REP);
            socket.bind("tcp://*:5556");

            ZContext context2 = new ZContext();

            ZMQ.Socket socket2 = context2.createSocket(ZMQ.REQ);
            socket2.connect("tcp://localhost:5555");

            while (!Thread.currentThread().isInterrupted()) {

                // Block until a message is received
                byte[] reply = socket.recv(0);

                // Print the message
                System.out.println(
                        " " + new String(reply, ZMQ.CHARSET) + " "
                );

                String recebido = "Recebido";
                socket.send(recebido.getBytes(ZMQ.CHARSET), 0);

                System.out.printf("Say anything:\n");

                String menssage = ler.nextLine();

                String response = " " + nome + ": " + menssage + " ";

                socket2.send(response.getBytes(ZMQ.CHARSET), 0);
                socket2.recv(0);

            }
        }
    }

    public String get_hora() throws ParseException {

        SimpleDateFormat fmt = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
        Date data = fmt.parse("17/12/2007 19:30:20");
        String str = fmt.format(data);

        return(str);
    }

}
