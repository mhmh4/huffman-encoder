import java.io.*;

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
        var sb = new StringBuilder();
        try {
            var br = new BufferedReader(new FileReader(f));
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
        var input = new File("input/message.txt");

        if (!input.exists()) {
            System.err.printf("Error: no such file '%s'\n", input);
            System.exit(1);
        }

        String message = getFileContents(input);
        String messageBinary = toBinary(message);
        int numBitsMessageBinary = messageBinary.length();

        var huf = new HuffmanTree();
        String compressedMessageBinary = huf.compress(message);

        int numBitsMessageBinaryCompressed = compressedMessageBinary.length();
        int encodingTableBitSize = huf.getEncodingTableBitSize();
        int totalBitSizeCompressedBinary = numBitsMessageBinaryCompressed + encodingTableBitSize;

        double compressionRatio = (double)totalBitSizeCompressedBinary / numBitsMessageBinary;
        int compressionRatioPercentage = (int)Math.round(compressionRatio * 100);
        int smallerPercentage = 100 - compressionRatioPercentage;

        var output = new File("output/results.txt");

        if (!output.exists()) {
            System.err.printf("Error: no such file '%s'\n", input);
            System.exit(1);
        }

        BufferedWriter bw;
        try {
            bw = new BufferedWriter(new FileWriter(output));
            bw.write("Message: " + message + '\n');
            bw.write("Binary message: " + messageBinary + '\n');
            bw.write("Number of bits in binary message: " + numBitsMessageBinary + '\n');
            bw.write('\n');
            bw.write("Compressed binary message: " + compressedMessageBinary + '\n');
            bw.write("Number of bits in compressed binary message: " + numBitsMessageBinaryCompressed + '\n');
            bw.write("Bit size of Huffman encoding table: " + encodingTableBitSize + '\n');
            bw.write('\n');
            bw.write("Total number of bits after compression: " + totalBitSizeCompressedBinary + '\n');
            bw.write('\n');
            bw.write("Compressed message is " + smallerPercentage + "% smaller\n");
            bw.close();
        } catch (IOException e) {
            System.err.printf("Error: %s", e.getMessage());
            System.exit(1);
        }
    }

}
