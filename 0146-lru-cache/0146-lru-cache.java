class Node {
    public int key;
    public int value;
    public Node next;
    public Node prev;

    Node(int key, int val, Node prev, Node next) {
        this.key = key;
        this.value = val;
        this.next = next;
        this.prev = prev;
    }
}

class LRUCache {
    Map<Integer, Node> cache;
    Node head;
    Node tail;
    int capacity;

    public LRUCache(int capacity) {
        cache = new HashMap<>();
        head = new Node(0, 0, null, null);
        tail = new Node(0, 0, null, null);
        this.capacity = capacity;
        head.next = tail;
        tail.prev = head;    
    }

    public void deleteNode(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    public void addToHead(Node node){
        node.next = head.next;
        node.prev = head;
        head.next.prev = node;
        head.next = node; 
    }

    public void removeFromTail(){
        tail.prev.next = null;
        tail.prev.prev.next = tail;
        tail.prev = tail.prev.prev;
    }

    
    public int get(int key) {
        if(cache.containsKey(key)){
            Node node = cache.get(key);
            deleteNode(node);
            addToHead(node);
            return node.value;
        }
        return -1;
    }
    
    public void put(int key, int value) {
        if(cache.containsKey(key)){
            Node node = cache.get(key);
            node.value = value;
            deleteNode(node);
            addToHead(node);
            // cache.replace(key, node);
        } else {
            Node node = new Node(key, value, null, null);
            if(cache.size() < capacity){
                cache.put(key, node);
                addToHead(node);
            } else {
                cache.remove(tail.prev.key);
                deleteNode(tail.prev);
                cache.put(key, node);
                addToHead(node);        
            }
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */