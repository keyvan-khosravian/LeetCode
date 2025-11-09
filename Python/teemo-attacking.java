class Solution {
    public int findPoisonedDuration(int[] timeSeries, int duration) {
        int result = 0;

        for (int i = 0; i < timeSeries.length - 1; i++) {
            result = result + Math.min(timeSeries[i+1] - timeSeries[i], duration);
        }

        return result + duration;        
    }
}