class Solution {
    topKFrequent(nums, k) {
        const count = {};
        // Note: use for...of for arrays; for...in gets indices as strings
        for (const num of nums) {
            count[num] = (count[num] || 0) + 1;
        }
        const arr = Object.entries(count).map(([num, freq]) => [
            freq,
            parseInt(num)
        ]);
        console.log(arr);
        arr.sort((a, b) => b[0] - a[0]);
        

        // Added 'return' and a semicolon
        return arr.slice(0, k).map((pair) => pair[1]);
    }
}
