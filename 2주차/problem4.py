import math
dr, dc = [-1, 1, 0, 0], [0, 0, 1, -1]
g_board, cost_map = [],[]
answer = math.inf
R,C = 0,0

def dfs(node, before_dir):
    global cost_map, answer
    r, c, cost = node[0][0], node[0][1], node[1]
    if cost_map[r][c] > cost: cost_map[r][c] = cost

    if r==R-1 and c==C-1:
        answer = min(answer, cost); return

    for dir in range(4):
        nr, nc = r+dr[dir], c+dc[dir]
        if nr<0 or nc<0 or nr>R-1 or nc>C-1 or g_board[nr][nc]==1: continue # check map boundary

        n_cost = cost+100 if before_dir == dir else (cost+600)

        if n_cost > cost_map[R-1][C-1]: continue
        if n_cost - cost_map[nr][nc] >= 500: continue # 금액차이가 500이상이면 pass
        else:
            cost_map[nr][nc] = n_cost
            dfs([(nr, nc), n_cost], dir)

def solution(board):
    global g_board, cost_map, R, C
    R, C = len(board), len(board[0])
    g_board = board
    cost_map = [[math.inf]*C for _ in range(R)]
    for i in range(4):
        dfs([(0,0),0],i)

    return cost_map[R-1][C-1]