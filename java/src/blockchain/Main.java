package blockchain;

import java.util.*;
import java.lang.*;

/**
 * The driver class to utilize and test blockchain components
 */
public class Main {


    public static void main(String[] args) {
        Block genesisBlock = new Block("I am the genesis block", "0");
        System.out.println("Hash of block 1: " + genesisBlock.getHash());

        Block secondBlock = new Block("I am the second block", genesisBlock.getHash());
        System.out.println("Hash of block 2: " + secondBlock.getHash());

        Block thirdBlock = new Block("I am the third block in the chain", secondBlock.getHash());
        System.out.println("Hash of block 3: " + thirdBlock.getHash());
        long start = System.currentTimeMillis();
        thirdBlock.mineBlock(5);
        long end = System.currentTimeMillis();
        System.out.println(end - start + "ms"); 

    }
}