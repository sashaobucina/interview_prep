package blockchain;

import java.util.*;
import java.lang.*;

/**
 * Singleton factory class that creates blocks in the blockchain.
 */
public class BlockFactory {

    private static BlockFactory sInstance = new BlockFactory();

    private BlockFactory() {}

    public BlockFactory getInstance() {
        return sInstance;
    }

    /**
     * Creates a blockchain of length <code>len</code>.
     * 
     * @param len the length of the block chain
     * @return the resulting blockchain
     */
    public ArrayList<Block> createChain(int len) {
        // TODO: implement
        return null;
    }

    public void append(ArrayList<Block> blockChain, Block block) {
        // TODO: implement
        return;
    }
}