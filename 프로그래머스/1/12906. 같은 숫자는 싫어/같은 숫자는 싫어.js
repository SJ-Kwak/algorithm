function solution(arr)
{
    let tmp = null;
    let answer = [];
    
    arr.forEach((num) => {
        if (num !== tmp) {
            answer.push(num)
            tmp = num;
        }
    });
    
    return answer;
}