def distance(x,y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])

def partition_check(loc1,loc2,x_loc):
    if loc1[0] == loc2[0]:
        if [loc1[0], min(loc1[1], loc2[1])+1] in x_loc:
            return True
    elif loc1[1] == loc2[1]:
        if [min(loc1[0], loc2[0])+1, loc1[1]] in x_loc:
            return True
    else:
        if ([loc1[0], loc2[1]] in x_loc) and ([loc2[0], loc1[1]] in x_loc):
            return True
        else:
            return False
    
    return False

def room_check(p_loc, x_loc):
    for i in range(len(p_loc)-1):
        for j in range(i+1, len(p_loc)):
            if distance(p_loc[i],p_loc[j]) > 2:
                continue
                
            elif distance(p_loc[i],p_loc[j]) < 2:
                return 0
            
            elif distance(p_loc[i],p_loc[j]) == 2:
                if partition_check(p_loc[i], p_loc[j], x_loc) == True:
                    continue
                else:
                    return 0
    return 1
    
def solution(places):
    answer = []
    p_locs = []
    x_locs = []
    
    for room in places:
        p_loc = []
        x_loc = []
        for i in range(len(room)):
            for j in range(len(room[0])):
                if room[i][j] == "P":
                    p_loc.append([i,j])
                elif room[i][j] == "X":
                    x_loc.append([i,j])
                    
        p_locs.append(p_loc)
        x_locs.append(x_loc)
    
    for i in range(len(p_locs)):
        answer.append(room_check(p_locs[i], x_locs[i]))

    return answer