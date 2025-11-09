class Solution {
    public String betterCompression(String compressed) {
        int[] mem = new int[26];
        int i = 0;

        while (i < compressed.length()) {
            char c = compressed.charAt(i++);
            int num = 0;
            while (i < compressed.length() && Character.isDigit(compressed.charAt(i))) {
                num = (num * 10) + compressed.charAt(i++) - '0';
            }
            mem[c - 'a'] += num;
        }

        StringBuilder sb = new StringBuilder();
        for (int j = 0; j < 26; ++j) {
            if (mem[j] == 0) continue;
            sb.append((char)('a' + j)).append(mem[j]);
        }

        return sb.toString();
    }
}