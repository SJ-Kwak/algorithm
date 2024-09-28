function solution(n) {
    const arr = n.toString().split("").reverse()
    return arr.map((a) => parseInt(a))
}