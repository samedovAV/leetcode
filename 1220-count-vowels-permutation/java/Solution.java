public class Solution {
    public int countVowelPermutation(int n) {
        final int MOD = 1000000007;
        
        long a = 1, e = 1, i = 1, o = 1, u = 1;
        
        for (int j = 1; j < n; j++) {
            long aNext = e;
            long eNext = (a + i) % MOD;
            long iNext = (a + e + o + u) % MOD;
            long oNext = (i + u) % MOD;
            long unext = a;
            
            a = aNext;
            e = eNext;
            i = iNext;
            o = oNext;
            u = unext;
        }
        
        return (int)((a + e + i + o + u) % MOD);
    }
}