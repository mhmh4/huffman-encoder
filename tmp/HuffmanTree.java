import java.util.ArrayList;
import java.util.HashMap;
import java.util.PriorityQueue;

public class HuffmanTree
{
    private HuffmanNode root = null;
    private HashMap<Character, String> encodingTable = new HashMap<>();
    private String message = "";
    private String compressedBinaryString = "";

    public HashMap<Character, String> getEncodingTable() {
        return encodingTable;
    }

//    public int getEncodingTableSize() {}

    public HuffmanTree(String message)
    {
        this.message = message;
        HashMap<Character, Integer> frequencyMap = buildFrequencyTable(message);
        ArrayList<HuffmanNode> huffmanNodes = createNodes(frequencyMap);

        buildTree(huffmanNodes);
        buildEncodingTree(this.root, "");

        System.out.println(encodingTable);
        System.out.println(root);

//        System.out.println();

        var s = compressString();
        System.out.println(s);
    }

    private String compressString()
    {
        var output = new StringBuilder();
        for (char c : message.toCharArray()) {
            String newCode = encodingTable.get(c);
            output.append(newCode);
        }
        return output.toString();
    }

    private HashMap<Character, Integer> buildFrequencyTable(String str)
    {
        var frequency = new HashMap<Character, Integer>();
        for (char c : str.toCharArray()) {
            frequency.put(c, frequency.getOrDefault(c, 0) + 1);
        }
        return frequency;
    }

    private ArrayList<HuffmanNode> createNodes(HashMap<Character, Integer> frequency)
    {
        var nodes = new ArrayList<HuffmanNode>();

        for (var entry : frequency.entrySet()) {
            var huffmanNode = new HuffmanNode(entry.getKey(), entry.getValue());
            nodes.add(huffmanNode);
        }

        return nodes;
    }

    private void buildTree(ArrayList<HuffmanNode> nodes)
    {
        var pq = new PriorityQueue<HuffmanNode>(nodes);

        while (pq.size() > 1) {
            HuffmanNode smallest1 = pq.poll();
            HuffmanNode smallest2 = pq.poll();
            HuffmanNode parent = new HuffmanNode(smallest1, smallest2);
            pq.add(parent);
        }

        this.root = pq.poll();
    }

    /**
     * Performs a DFS on the HuffmanTree while keeping track of the path.
     *
     * The path is determined by whether the left or right child is visited.
     * If it goes left, then the bit 0 is added to the path, if right, then 1.
     * Once a HuffmanNode that contains a character is visited, that character
     * is stored as a key in the "encodingTable" with the path as the value.
     */
    private void buildEncodingTree(HuffmanNode node, String path)
    {
        if (node == null) return;

        buildEncodingTree(node.visitLeft(), path + "0");

        if (node.isCharacterNode()) {
            this.encodingTable.put(node.getCharacter(), path);
        }

        buildEncodingTree(node.visitRight(), path + "1");
    }
}
