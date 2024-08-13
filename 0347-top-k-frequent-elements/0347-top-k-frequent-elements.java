class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> numsFreq = new HashMap<>();

        for (int n: nums) {
            numsFreq.put(n, numsFreq.getOrDefault(n, 0) + 1);
        }

        Queue<Integer> heap = new PriorityQueue<>(Comparator.comparingInt(numsFreq::get));

        for (int n : numsFreq.keySet()) {
            heap.add(n);
            if (heap.size() > k) heap.poll();
        }

        int[] topK = new int[k];
        for (int i = 0; i < k; i++) {
            topK[i] = heap.poll();
        }
        return topK;
    }
}