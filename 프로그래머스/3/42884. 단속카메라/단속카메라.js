function solution(routes) {
    let answer = 1;
    
    routes.sort((a, b) => a[1] - b[1])
    
    camera = routes[0][1]
    
    for (const route of routes.slice(1)) {
        if (camera < route[0]) {
            answer += 1;
            camera = route[1];
        }
    }
    return answer;
}