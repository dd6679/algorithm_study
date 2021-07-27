def solution(n, s, a, b, fares):
    answer = 0
    d = [[999999]*n for i in range(n)]
    for i in range(n):
        d[i][i] = 0
    for i in range(len(fares)):
        d[fares[i][0]-1][fares[i][1]-1] = fares[i][2]
        d[fares[i][1]-1][fares[i][0]-1] = fares[i][2]
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k]+d[k][j]:
                    d[i][j] = d[i][k]+d[k][j]
                #d[i][j] = min(d[i][j], d[i][k]+d[k][j])
                
    answer = d[s-1][a-1] + d[s-1][b-1]
    for k in range(n):
        if answer > d[s-1][k] + d[k][a-1] + d[k][b-1]:
            answer = d[s-1][k] + d[k][a-1] + d[k][b-1]
        #answer = min(answer, d[s-1][k] + d[k][a-1] + d[k][b-1])
        
    return answer
