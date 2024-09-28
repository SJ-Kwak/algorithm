function solution(s) {
    return [4, 6].includes(s.length) && /^-?\d+$/.test(s)
}