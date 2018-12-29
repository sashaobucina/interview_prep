package data_structures;

import java.util.*;
import java.lang.*;

public class ChainMap<K,V> extends AbstractMap<K,V> {

    private LinkedList<Map<K,V>> internalMap = new LinkedList<>();

    transient Collection<K> keys;
    transient Collection<V> values;
    transient Collection<Entry<K, V>> entryCollection;

    public ChainMap(Map<K, V>... maps) {
        internalMap.addAll(Arrays.asList(maps));
    }

    @Override
    public V get(Object key) {
        V result;
        for (Map<K, V> mapping : internalMap) {
            if ((result = mapping.get(key)) != null) {
                return result;
            }
        }
        return null;
    }

    @Override
    public int size() {
        return internalMap.size();
    }

    private int entryCount() {
        int count = 0;
        for (Map<K, V> mapping : internalMap) {
            count += mapping.size();
        }
        return count;
    }

    @Override
    public boolean containsKey(Object key) {
        for (Map<K, V> mapping : internalMap) {
            if (mapping.containsKey(key)) {
                return true;
            }
        }
        return false;
    }

    @Override
    public boolean isEmpty() {
        if (internalMap.isEmpty()) return true;

        for (Map<K, V> mapping : internalMap) {
            if (!mapping.isEmpty()) return false;
        }
        return true;
    }

    @Override
    public V remove(Object key) {
        for (Map<K, V> mapping : internalMap) {
            if (mapping.containsKey(key)) {
                return mapping.remove(key);
            }
        }
        return null;
    }

    private boolean removeEntry(K key) {
        for (Map<K, V> mapping : internalMap) {
            if (mapping.containsKey(key)) {
                mapping.remove(key);
                return true;
            }
        }
        return false;
    }

    @Override
    public boolean containsValue(Object value) {
        for (Map<K, V> mapping : internalMap) {
            if (mapping.containsValue(value)) {
                return true;
            }
        }
        return false;
    }

    @Override
    public V put(K key, V value) {
        return super.put(key, value);
    }

    @Override
    public void putAll(Map<? extends K, ? extends V> m) {
        throw new UnsupportedOperationException("ChainMap does not support the putAll method, use addMap instead");
    }

    @Override
    public void clear() {
        for (Map<K, V> mapping : internalMap) {
            mapping.clear();
        }
        internalMap.clear();
    }

    @Override
    public Set<K> keySet() {
        throw new UnsupportedOperationException("ChainMap doesn't support keySet," +
                "use keys() instead to get collection of keys");
    }

    public Collection<K> keys() {
        Collection<K> ks = keys;
        if (ks == null) {
            ks = new KeyCollection();
            keys = ks;
        }
        return ks;
    }

    @Override
    public Collection<V> values() {
        Collection<V> vals = values;
        if (vals == null) {
            vals = new Values();
            values = vals;
        }
        return vals;
    }

    @Override
    public boolean equals(Object o) {
        if (o == this)
            return true;

        if (!(o instanceof ChainMap))
            return false;
        Map<?,?> m = (ChainMap<?,?>) o;
        if (m.size() != size())
            return false;
        // TODO: Implement entry set to add a custom iterator to compare against

        return super.equals(o);
    }

    // TODO: Implement iterator to make this function cleaner with hasNext() functionality instead of using count mechanism
    @Override
    public String toString() {
        int count = 0;
        int size = size();
        StringBuilder sb = new StringBuilder();
        sb.append('[').append(' ');
        for (Map<K, V> mapping : internalMap) {
            sb.append(mapping.toString());
            if (count != size - 1) {
                sb.append(',').append(' ');
            }
            count++;
        }
        sb.append(' ').append(']');
        return sb.toString();
    }

    // TODO: Implement EntrySet and Iterator object
    @Override
    public Set<Entry<K, V>> entrySet() {
        throw new UnsupportedOperationException("ChainMap does not have unique key values, use entryCollection instead!");
    }

    public Collection<Entry<K, V>> entryCollection() {
        Collection<Entry<K, V>> ec;
        return (ec = entryCollection) == null ? (entryCollection = new EntryCollection()) : ec;
    }

    @Override
    protected Object clone() throws CloneNotSupportedException {
        ChainMap<?,?> result = (ChainMap<?,?>) super.clone();
        result.keys = null;
        result.values = null;
        result.entryCollection = null;
        return result;
    }

    public void addMap(Map<K, V> newMap) {
        internalMap.add(newMap);
    }

    public Map<K, V> flatten() {
        Map<K, V> target = new HashMap<>();
        for (Map<K, V> mapping : internalMap) {
            Map<K, V> temp = new HashMap<>(mapping);
            temp.keySet().removeAll(target.keySet());
            target.putAll(temp);
        }
        return target;
    }

    public List<Map<K, V>> maps() {
        return internalMap;
    }

    public ChainMap<K, V> newChild() {
        ChainMap<K, V> newMap = new ChainMap<>(new HashMap<>());

        for (Map<K, V> mapping : internalMap) {
            newMap.internalMap.addLast(mapping);
        }
        return newMap;
    }


    public ChainMap<K, V> parents() {
        ChainMap<K, V> parentMap = new ChainMap<>();
        int count = 0;
        if (internalMap.size() > 0) {
            for (Map<K, V> mapping: internalMap) {
                if (count == 0) {
                    count++;
                    continue;
                }
                parentMap.internalMap.addLast(mapping);
            }
        }
        return parentMap;
    }

    /** ---------------------------------------------------- */
    private class EntryCollection extends AbstractCollection<Entry<K, V>> {

        @Override
        public Iterator<Entry<K, V>> iterator() {
            return new EntryIterator();
        }

        @Override
        public int size() {
            return ChainMap.this.entryCount();
        }

        @Override
        public boolean isEmpty() {
            return ChainMap.this.isEmpty();
        }

        @Override
        public void clear() {
            ChainMap.this.clear();
        }

        @Override
        public boolean contains(Object o) {
            if (!(o instanceof Entry))
                return false;
            Entry<?,?> entry = (Entry<?,?>) o;
            Object key = entry.getKey();
            Object value = entry.getValue();
            Object candidate = ChainMap.this.get(key);
            return (candidate != null && ChainMap.this.containsKey(key) && candidate.equals(value));
        }

        @Override
        public boolean remove(Object o) {
            try {
                if ((o instanceof Entry)) {
                    Entry<?,?> entry = (Entry<?,?>) o;
                    return ChainMap.this.removeEntry((K) entry.getKey());
                }
                return false;
            } catch (ClassCastException e) {
                return false;
            }
        }
    }

    private class EntryIterator implements Iterator<Entry<K, V>> {

        private Queue<Iterator<Entry<K, V>>> queue = new LinkedList<>();

        EntryIterator() {
            for (Map<K, V> mapping : internalMap) {
                Iterator<Entry<K, V>> iter = mapping.entrySet().iterator();
                queue.add(iter);
            }
        }

        @Override
        public boolean hasNext() {
            while (!queue.isEmpty()) {
                if (queue.peek().hasNext()) {
                    return true;
                }
                queue.poll();
            }
            return false;
        }

        @Override
        public Entry<K, V> next() {
            if (!hasNext())
                throw new NoSuchElementException();
            Iterator<Entry<K, V>> iter = queue.poll();
            Entry<K, V> result = iter.next();
            queue.offer(iter);
            return result;
        }

        @Override public void remove() { throw new UnsupportedOperationException(); }
    }

    /** ---------------------------------------------------- */
    private class Values extends AbstractCollection<V> {

        @Override
        public Iterator<V> iterator() {
            return new ValueIterator();
        }

        @Override
        public int size() {
            return ChainMap.this.entryCount();
        }

        @Override
        public boolean isEmpty() {
            return ChainMap.this.isEmpty();
        }

        @Override
        public void clear() {
            ChainMap.this.clear();
        }

        @Override
        public boolean contains(Object v) {
            return ChainMap.this.containsValue(v);
        }
    }

    private class ValueIterator implements Iterator<V> {

        private Queue<Iterator<Entry<K, V>>> queue = new LinkedList<>();

        public ValueIterator() {
            for (Map<K, V> mapping : internalMap) {
                Iterator<Entry<K, V>> iter = mapping.entrySet().iterator();
                queue.add(iter);
            }
        }

        @Override
        public boolean hasNext() {
            while (!queue.isEmpty()) {
                if (queue.peek().hasNext()) {
                    return true;
                }
                queue.poll();
            }
            return false;
        }

        @Override
        public V next() {
            if (!hasNext())
                throw new NoSuchElementException();
            Iterator<Entry<K, V>> iter = queue.poll();
            Entry<K, V> entry = iter.next();
            V result = null;
            if (entry != null) {
                result = entry.getValue();
            }
            queue.offer(iter);
            return result;
        }

        @Override public void remove() { throw new UnsupportedOperationException(); }
    }

    /** --------------------------------- */
    class KeyCollection extends AbstractCollection<K> {

        @Override
        public Iterator<K> iterator() {
            return new KeyIterator();
        }

        @Override
        public int size() {
            return ChainMap.this.entryCount();
        }

        @Override
        public boolean isEmpty() {
            return ChainMap.this.isEmpty();
        }

        @Override
        public void clear() {
            ChainMap.this.clear();
        }

        @Override
        public boolean contains(Object key) {
            return ChainMap.this.containsKey(key);
        }

        @Override
        public boolean remove(Object o) {
            try {
                return ChainMap.this.removeEntry((K) o);
            } catch (ClassCastException e) {
                return false;
            }
        }
    }


    private class KeyIterator implements Iterator<K> {

        private Queue<Iterator<Entry<K, V>>> queue = new LinkedList<>();

        public KeyIterator() {
            for (Map<K, V> mapping : internalMap) {
                Iterator<Entry<K, V>> iter = mapping.entrySet().iterator();
                queue.add(iter);
            }
        }

        @Override
        public boolean hasNext() {
            while (!queue.isEmpty()) {
                if (queue.peek().hasNext()) {
                    return true;
                }
                queue.poll();
            }
            return false;
        }

        @Override
        public K next() {
            if (!hasNext())
                throw new NoSuchElementException();
            Iterator<Entry<K, V>> iter = queue.poll();
            Entry<K, V> entry = iter.next();
            K result = null;
            if (entry != null) {
                result = entry.getKey();
            }
            queue.offer(iter);
            return result;
        }

        @Override public void remove() { throw new UnsupportedOperationException(); }
    }

    // Driver class for testing
    public static void main(String[] args) {
        HashMap<String, String> map = new HashMap<>();
        HashMap<String, String> map2 = new HashMap<>();
        HashMap<String, String> map3 = new HashMap<>();

        map.put("Sasha", "Obucina");
        map.put("Subject", "Test");

        map2.put("Anything", "Value");
        map2.put("Really", "Anything");

        ChainMap<String, String> chainMap = new ChainMap<>(map, map2, map3);
        System.out.println("ChainMap: " + chainMap);
    }

}