package blockchain;

import java.util.*;

/**
 * Class representing a single Block and it's necessary components in a blockchain.
 */
public class Block {

    /* SHA of the current block in the chain */
    private String hash;
    
    /* SHA of the previous block in the chain */
    private String previousHash;
    
    /* data of the Block */
    private String data;
    
    /* number of milliseconds as of 1/1/1970 */
    private long timeStamp;
    
    /* 32 bit arbitrary number adjusted for mining so that hash is less than or equal to target */
    private int nonce;

    /* Constructor */
    public Block(String data, String previousHash) {
        this.data = data;
        this.previousHash = previousHash;
        this.timeStamp = new Date().getTime();
        this.hash = calculateHash();
    }

    /**
     * Calculate the hash of the current block based off the previous
     * hash, timestamp, and data of the block.
     *
     * The hashing algorithm applied is SHA256.
     * 
     * @return the calculated hash of the current block.
     */
    private String calculateHash() {
        String calculatedHash = StringUtil.applySha256(
                        previousHash +
                        Integer.toString(nonce) +
                        Long.toString(timeStamp) +
                        data);

        return calculatedHash;
    }

    /**
     * 
     */
    public void mineBlock(int difficulty) {
        // create a string of "0" * difficulty 
        String target = new String(new char[difficulty]).replace('\0', '0');
        while (!hash.substring(0, difficulty).equals(target)) {
            nonce ++;
            hash = calculateHash();
        }
    }

    /**
     * A getter for the current block's hash.
     * 
     * @return the hash of this block.
     */
    public String getHash() {
        return this.hash;
    }

}