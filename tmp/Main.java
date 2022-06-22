import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class Main
{

    public static String toBinary(String s)
    {
        var binary = new StringBuilder();
        for (byte b : s.getBytes()) {
            int value = b;
            for (int i = 0; i < 8; i++) {
                binary.append((value & 128) == 0 ? 0 : 1);
                value <<= 1;
            }
        }
        return binary.toString();
    }

    public static String getFileContents(File f)
    {
        final StringBuilder sb = new StringBuilder();
        try {
            BufferedReader br = new BufferedReader(new FileReader(f));
            String line;
            while ((line = br.readLine()) != null) {
                sb.append(line);
            }
            br.close();
        } catch (IOException e) {
            System.err.printf("Error: %s", e.getMessage());
            System.exit(1);
        }
        return sb.toString();
    }

    public static void main(String[] args)
    {
        final File inputFile = new File("input.txt");
        String content = getFileContents(inputFile);

        final String message = String.valueOf(content);
        final String messageBinary = toBinary(message);
        final int numBitsMessageBinary = messageBinary.length();

        final HuffmanTree huf = new HuffmanTree();
        final String compressedMessageBinary = huf.compress(message);

        final int numBitsMessageBinaryCompressed = compressedMessageBinary.length();

        var a = compressedMessageBinary.length();
        var b = huf.getEncodingTableBitSize();
        System.out.println(a + b);

        System.out.println(compressedMessageBinary);

        System.out.println("Message: " + message);

        System.out.println();

        System.out.println("Message in binary: " + messageBinary);
        System.out.printf("Size of message in binary: %d bits\n", numBitsMessageBinary);

        System.out.println("Message in binary compressed: " + compressedMessageBinary);
        System.out.printf("Size of message in compressed binary: %d bits\n", numBitsMessageBinaryCompressed);

        // System.out.println("Message: " + message);
        // System.out.println(characterFrequency(message));
    }

}
