package recursion;

import java.io.File;
import java.util.LinkedList;
import java.util.Queue;

public class FileUtil {

    public static int countFiles(String dirPath) {
        File rootDir = new File(dirPath);
        if (!rootDir.exists() || !rootDir.isDirectory()) {
            throw new IllegalArgumentException("Directory path does not exist or is not a directory");
        }
        return countFilesHelper(rootDir);
    }

    private static int countFilesHelper(File rootDir) {
        int count = 0;

        File[] contents = rootDir.listFiles();
        if (contents != null) {
            for (File content : contents) {
                if (content.isDirectory()) {
                    count += countFilesHelper(content);
                } else {
                    count += 1;
                }
            }
        }
        return count;
    }

    public static int breadthFileCount(String dirPath) {
        File rootDir = new File(dirPath);
        if (!rootDir.exists() || !rootDir.isDirectory()) {
            throw new IllegalArgumentException("Directory path does not exist or is not a directory");
        }
        return breadthFileCountHelper(rootDir);
    }

    public static int breadthFileCountHelper(File rootDir) {
        int count = 0;

        Queue<File> q = new LinkedList<>();
        ((LinkedList<File>) q).push(rootDir);

        while (!q.isEmpty()) {
            File currFile = ((LinkedList<File>) q).pop();

            // next element is a file
            if (currFile.isFile()) {
                count += 1;
            }

            // next element is a directory
            File[] files = currFile.listFiles();
            if (files != null) {
                for (File file : files) {
                    ((LinkedList<File>) q).push(file);
                }
            }

            System.out.println(String.format("File: %s, Count: %d", currFile.getName(), count));
        }

        return count;
    }

    public static void main(String[] args) {
        String dirPath = "/home/saobucina/";
        int numFiles = countFiles(dirPath);
        System.out.println(String.format("Number files in directory %s is %d", dirPath, numFiles));

        System.out.println();
        System.out.println();

        breadthFileCount(dirPath);
    }
}
