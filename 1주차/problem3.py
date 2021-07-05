answer_list = list()
select_set = set()
UID, BID = [], []

def comp_name(a, b):
    if len(a) != len(b): return False
    for i in range(len(a)):
        if a[i] != b[i] and b[i] != '*': return False
    return True

def dfs(depth):
    global answer_list, select_set

    if depth == len(BID): # 모두 선택했다면 return
        select = select_set.copy()
        if select not in answer_list:
            answer_list.append(select)
        return

    for user in UID:
        if comp_name(user, BID[depth]):
            if user not in select_set:
                select_set.add(user)
                dfs(depth+1)
                select_set.discard(user) # if exist -> remove

def solution(user_id, banned_id):
    global UID, BID
    UID, BID = user_id, banned_id
    dfs(0)
    return len(answer_list)

test_input1 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
test_input2 = ["fr*d*", "*rodo", "******", "******"]

print(solution(test_input1, test_input2)) # 3
