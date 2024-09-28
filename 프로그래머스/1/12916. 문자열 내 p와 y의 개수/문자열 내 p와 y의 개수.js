function solution(s){
    const str = s.toLowerCase();
    let p = str.split('p').length;
    let y = str.split('y').length;
    
    return p === y;
}