package tries;

import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.*;

public class PrefixTrie {

    private TrieNode root;

    /* Constructor */
    public PrefixTrie() {
        root = new TrieNode(' ');
    }

    public void insert(String str) {
        int strLen = str.length();
        if (strLen == 0) {
            root.isEndOfString = true;
        } else {
            int i = 0;
            TrieNode current = root, child = null;
            while (i < strLen) {
                child = current.subNode(str.toLowerCase().charAt(i));
                if (child == null) {
                    child = new TrieNode(str.toLowerCase().charAt(i));
                    current.children.add(child);
                }
                current = child;
                i++;
            }
            current.isEndOfString = true;
            current.leafNodeString = str.toLowerCase();
        }
    }

    public TrieNode getLocationOfString(String str) {
        TrieNode currentNode = root, child;
        int strLen = str.length();
        int i = 0;
        while (i < strLen) {
            child = currentNode.subNode(str.toLowerCase().charAt(i));
            if (child != null) {
                currentNode = child;
            } else {
                return null;
            }
            i++;
        }
        return currentNode;
    }

    /**
     * Prints a list of options that would autocomplete the given word terminating at {@code node}
     *
     * @param node The node to start trie traversal from.
     */
    public void autoComplete(TrieNode node) {
        // Base case
        if (node.isEndOfString) System.out.println("-" + node.leafNodeString);

        for (TrieNode child : node.children) {
            autoComplete(child);
        }
    }

    public boolean search(String str) {
        int strLen = str.length();
        if (strLen == 0) {
            return true;
        } else {
            int i = 0;
            TrieNode currentNode = root, child = null;
            while (i < strLen) {
                child = currentNode.subNode(str.toLowerCase().charAt(i));
                if (child != null) {
                    currentNode = child;
                } else {
                    return false;
                }
                i++;
            }
            return true;
        }
    }

    public class TrieNode {
        public char data;
        public boolean isEndOfString;
        public Collection<TrieNode> children;
        public String leafNodeString;

        public TrieNode(char data) {
            this.data = data;
            children = new ArrayList<>();
            this.isEndOfString = false;
        }

        public TrieNode subNode(char data) {
            if (children != null) {
                for (TrieNode child : children) {
                    if (child.data == data) {
                        return child;
                    }
                }
            }
            return null;
        }
    }

    // Driver
    public static void main(String[] args) throws IOException {
        PrefixTrie trie = new PrefixTrie();
        trie.insert("analyse");
        trie.insert("boondock");
        trie.insert("extend");
        trie.insert("append");
        trie.insert("insert");
        trie.insert("remove");
        trie.insert("free");
        trie.insert("Free weblog publishing tool from Google, for sharing text, photos and vide");
        trie.insert("clear");
        trie.insert("blog");
        trie.insert("what is autocomplete");
        trie.insert("blog is your best bet for a voice among the online crowd");
        trie.insert("start a WordPress blog or create a free website in seconds");
        trie.insert("start");
        trie.insert("While we hope these tips are informative, we are unable to answer individual questions");
        trie.insert("while");
        trie.insert("basement");

        InputStreamReader in = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(in);
        String line;
        TrieNode location = null;
        System.out.println("Enter your keywords (Type in 'Y' to exit): ");
        while (true) {
            line = br.readLine();
            if (line.equals("Y")) {
                break;
            }
            location = trie.getLocationOfString(line);
            if (location != null) {
                trie.autoComplete(location);
            } else {
                System.out.println("No match found for { " + line + " } in our database");
            }
        }
        System.out.println("Program terminating ...");
    }
}
