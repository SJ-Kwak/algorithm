def solution(routes):
    routes.sort()
    answer = 1
    
    camera = routes[0]
    for route in routes[1:]:
        if camera[1] >= route[0]:
            camera = [route[0], min(route[1], camera[1])]
        else:
            camera = route
            answer += 1
        
    return answer