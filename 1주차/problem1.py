def solution(board, moves):
    answer = 0
    a = []
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                pass
            else:
                a.append(board[j][i-1])
                board[j][i-1] = 0
                break
            
        if len(a) >= 2 and a[-1] == a[-2]:
            a.pop(-1)
            a.pop(-1)
            answer+=2

    return answer