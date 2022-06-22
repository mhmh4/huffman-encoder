import java.util.ArrayList;
import java.util.HashMap;
import java.util.PriorityQueue;

public class HuffmanTree
{
    private HuffmanNode root = null;

    private String message;

    // New binary codes each of `message`'s character will be mapped to.
    private final HashMap<Character, String> encodingTable = new HashMap<>();

    public HuffmanTree() {}

    public String compress(String message)
    {
        this.message = message;

        HashMap<Character, Integer> frequencyTable = createFrequencyTable(message);
        ArrayList<HuffmanNode> huffmanNodes = createNodes(frequencyTable);

        buildTree(huffmanNodes);
        buildEncodingTable(root, null);

        return generateCompressedBinaryMessage();
    }

    private String generateCompressedBinaryMessage()
    {
        var output = new StringBuilder();

        for (char c : message.toCharArray()) {
            String code = encodingTable.get(c);
            output.append(code);
        }

        return output.toString();
    }

    private HashMap<Character, Integer> createFrequencyTable(String str)
    {
        var frequencyTable = new HashMap<Character, Integer>();

        for (char c : str.toCharArray()) {
            frequencyTable.put(c, frequencyTable.getOrDefault(c, 0) + 1);
        }

        return frequencyTable;
    }

    private ArrayList<HuffmanNode> createNodes(HashMap<Character, Integer> frequencyTable)
    {
        var nodes = new ArrayList<HuffmanNode>();

        for (var entry : frequencyTable.entrySet()) {
            char character = entry.getKey();
            int frequency = entry.getValue();

            var huffmanNode = new HuffmanNode(character, frequency);
            nodes.add(huffmanNode);
        }

        return nodes;
    }

    private void buildTree(ArrayList<HuffmanNode> nodes)
    {
        var pq = new PriorityQueue<>(nodes);

        while (pq.size() > 1) {
            HuffmanNode smallest1 = pq.poll();
            HuffmanNode smallest2 = pq.poll();

            HuffmanNode parent = new HuffmanNode(smallest1, smallest2);
            pq.add(parent);
        }

        this.root = pq.poll();
    }

    private void buildEncodingTable(HuffmanNode node, String path)
    {
        if (node == null) return;
        if (path == null) path = "";

        buildEncodingTable(node.getLeft(), path + '0');

        if (node.containsCharacter()) {
            encodingTable.put(node.getCharacter(), path);
        }

        buildEncodingTable(node.getRight(), path + '1');
    }

    public HashMap<Character, String> getEncodingTable() { return this.encodingTable; }

    public int getEncodingTableBitSize()
    {
        final int totalBinaryStringsBitSize = encodingTable.values()
                .stream()
                .mapToInt(String::length)
                .sum();

        final int NUM_BITS_IN_CHAR = 8;
        final int numChars = encodingTable.keySet().size();
        final int totalCharsBitSize = NUM_BITS_IN_CHAR * numChars;

        return totalBinaryStringsBitSize + totalCharsBitSize;
    }

    @Override
    public String toString() { return root.toString(); }

}
