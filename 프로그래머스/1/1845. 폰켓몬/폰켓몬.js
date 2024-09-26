function solution(nums) {
    return Math.min(Math.floor(nums.length / 2), new Set(nums).size);
}