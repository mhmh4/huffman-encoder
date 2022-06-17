public class HuffmanNode implements Comparable<HuffmanNode> {

    // Denotes a HuffmanNode doesn't contain a character
    private static final char NULL_CHARACTER = '\u0000';

    // HuffmanNode's data
    private final char character;
    private final int frequency;

    // Subtree pointers
    private HuffmanNode left = null;
    private HuffmanNode right = null;

    public HuffmanNode(char character, int frequency) {
        this.character = character;
        this.frequency = frequency;
    }

    // Parent constructor
    public HuffmanNode(HuffmanNode left, HuffmanNode right) {
        this.character = NULL_CHARACTER;
        this.frequency = left.frequency + right.frequency;
        this.left = left;
        this.right = right;
    }

    public char getCharacter() { return this.character; }

    public boolean containsCharacter() {
        return this.character != NULL_CHARACTER;
    }

    public final HuffmanNode getLeft() { return this.left; }
    public final HuffmanNode getRight() { return this.right; }

    @Override
    public int compareTo(HuffmanNode other) {
        return Integer.compare(this.frequency, other.frequency);
    }

    @Override
    public String toString() {
        return "HuffmanNode{" +
                "character=" + character +
                ", frequency=" + frequency +
                ", left=" + left +
                ", right=" + right +
                '}';
    }
}
