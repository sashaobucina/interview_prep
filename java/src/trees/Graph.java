package trees;

import java.util.*;

public class Graph<T> {

    private Map<T, ArrayList<Edge<T>>> adjacencyList;

    private List<T> vertices;

    /* default is set to false */
    private boolean directed;

    public Graph(boolean isDirected) {
        this.directed = isDirected;
        this.adjacencyList = new HashMap<>();
        this.vertices = new ArrayList<>();
    }
    
    public void setDirected(boolean isDirected) {
        this.directed = isDirected;
    }

    public boolean isDirected() {
        return directed;
    }


    class Edge<T> {

        private T vertex;

        private int weight;

        public Edge(T vertex, int weight) {
            this.vertex = vertex;
            this.weight = weight;
        }

        public T getVertex() {
            return this.vertex;
        }

        public void setVertex(T vertex) {
            this.vertex = vertex;
        }

        public int getWeight() {
            return this.weight;
        }

        public void setWeight(int newWeight) {
            this.weight = newWeight;
        }
        
        @Override
        public String toString() {
            return "( " + vertex + ", " + weight + " )";
        }
    }
}