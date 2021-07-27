import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)


def dfs(l, idx, num, dp1, dp2, child):
    if idx == -1:
        return

    left = child[idx][0]
    right = child[idx][1]

    dfs(l, left, num, dp1, dp2, child)
    dfs(l, right, num, dp1, dp2, child)

    dp1[idx] = dp1[left] + dp1[right]
    if num[idx] + dp2[left] + dp2[right] <= l:
        dp2[idx] = num[idx] + dp2[left] + dp2[right]
    elif num[idx] + dp2[left] <= l or num[idx] + dp2[right] <= l:
        dp1[idx] += 1
        dp2[idx] = num[idx] + min(dp2[left], dp2[right])
    else:
        dp1[idx] += 2
        dp2[idx] = num[idx]
        if num[idx] > l:
            dp1[idx] = 10000

    return dp1[idx]
def solution(k, num, links):
    answer = 0

    par = [-1 for _ in range(len(num))]
    for n, (left, right) in enumerate(links):
#자식노드가 있는 경우
        if left != -1: 
	par[left] = n
        if right != -1: 
	par[right] = n
#par [6, 7, 5, 6, 9, 4, 7, 9, 4, -1, 5, 8]

    root_idx = 0
    while par[root_idx] != -1:
        root_idx = par[root_idx]

    start = sum(num) // k
    end = sum(num)
    answer = end

    num += [0]
    while start <= end:
        mid = (start + end) // 2
#트리를 자를 때, 필요한 그룹의 수가 k개 이하인지 판별하기 위해  정의
        dp1 = [0 for _ in range(len(num))]
        dp2 = [0 for _ in range(len(num))]
        if dfs(mid, root_idx, num, dp1, dp2, links) < k:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer
