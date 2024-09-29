function solution(numbers, hand) {
    let answer = '';
    const keypad = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        '*': [3, 0], 0: [3, 1], '#': [3, 2]
    }
    let lpos = keypad['*']
    let rpos = keypad['#']
    
    numbers.forEach(n => {
        let cur = keypad[n]
        if ([1,4,7].includes(n)) {
            answer += 'L'
            lpos = cur
        } else if ([3,6,9].includes(n)) {
            answer += 'R'
            rpos = cur
        } else {
            let dist = getDistance(cur, lpos) - getDistance(cur, rpos)
            if (dist > 0) {
                answer += 'R'
                rpos = cur
            } else if (dist === 0) {
                answer += hand.split('')[0].toUpperCase()
                hand.split('')[0].toUpperCase() === 'R' ?
                    rpos = cur : lpos = cur
            } else {
                answer += 'L'
                lpos = cur
            }
        }
    })
    return answer;
}

function getDistance(cur, pos) {
    return Math.abs(cur[0] - pos[0]) + Math.abs(cur[1] - pos[1]);
}