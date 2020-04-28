def 깊이우선탐색(graph, start):
    방문 = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in 방문:
            방문.append(n)
            차집합 = graph[n] - set(방문)
            if len(차집합) == 0:
                방문 += stack
                break
            stack.append(max(차집합))
            print(f'visited : {방문}')
            print(f'stack : {stack}')

    return 방문

print(깊이우선탐색(graph, 100))
