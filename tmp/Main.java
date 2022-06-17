import java.io.*;
import java.net.URL;

public class Main {

    // Converts a string to a binary string (e.g. "Hi" -> 0100100001101001)
    public static String convertToBinary(final String str) {

        final byte[] bytes = str.getBytes();
        final StringBuilder binaryString = new StringBuilder();

        for (final byte b : bytes) {
            int value = b;
            for (int i = 0; i < 8; i++) {
                binaryString.append((value & 128) == 0 ? 0 : 1);
                value <<= 1;
            }
            // binaryString.append(' ');
        }

        return binaryString.toString();
    }

    public static void main(String[] args) {
//        if (args.length < 2) {
//            System.err.println("Error: ...");
//            System.exit(1);
//        }
//        args[1] = "input/message.txt";
        URL url = null;
        try {
            url = Main.class.getResource("input/message.txt");
        } catch (NullPointerException npe) {
            System.err.printf("Error: cannot locate path '%s'", args[1]);
        }
        File f = new File(url.getPath());

        if (!f.exists()) {
            //
        }

        StringBuilder sb = new StringBuilder();

        try {
            BufferedReader br = new BufferedReader(new FileReader(f.getPath()));
            String line;
            while ((line = br.readLine()) != null) {
                sb.append(line);
            }
            br.close();
        } catch (IOException e) {
            System.err.printf("Error: %s", e.getMessage());
            return;
        }

        final String message = String.valueOf(sb);
        final String messageBinary = convertToBinary(message);
        final int numBitsMessageBinary = messageBinary.length();

        HuffmanTree huf = new HuffmanTree();
        String compressedMessageBinary = huf.compress(message);

        var a = compressedMessageBinary.length();
        var b = huf.getEncodingTableBitSize();
        System.out.println((a + b));

        System.out.println(compressedMessageBinary);
//        huf

        System.out.println("Message: " + message);
        System.out.println("Message in binary: " + messageBinary);
//        System.out.println("Message: " + message);

//        System.out.println(characterFrequency(message));
    }

}
