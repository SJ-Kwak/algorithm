function solution(s) {
    const dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    
    Object.entries(dict).forEach(([k, v]) => {
        s = s.replaceAll(k, v.toString())
    })
    return Number(s);
}