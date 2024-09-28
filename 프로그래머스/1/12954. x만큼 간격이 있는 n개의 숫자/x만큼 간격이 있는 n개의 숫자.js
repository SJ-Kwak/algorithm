function solution(x, n) {
    return Array(n).fill(x).map((i, j) => i * (j+1))
}