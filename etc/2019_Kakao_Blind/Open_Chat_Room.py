from collections import defaultdict

def solution(record):
    ENTER, LEAVE = 0, 1
    answer, names, a = [], defaultdict(str), []
    for r in record:
        if r[0] == 'L':
            e, uid = r.split()
        else:
            e, uid, name = r.split()
        if e != "Change":
            a.append((ENTER, uid) if e == "Enter" else (LEAVE, uid))
        if e != "Leave":
            names[uid] = name
    for e, uid in a:
        s = "님이 들어왔습니다." if e == ENTER else "님이 나갔습니다."
        answer.append(str(names[uid]) + s) 
    return answer
