def solution(s):
    answer = []
    s = s.replace("{", "")
    tuple = [i for i in s.split("}")]
    tuple = sorted(tuple, key = lambda x : len(x))
    tuple = tuple[2:]
    for i in tuple:
        for j in i.split(","):
            if j =='':
                continue
            if int(j) in answer:
                continue
            answer.append(int(j))
    return answer
