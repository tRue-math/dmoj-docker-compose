from dmoj.result import CheckerResult
import re

def check(process_output, judge_output, judge_input, point_value, **kwargs):
    # convert from bytes to texts
    process_output = process_output.decode("ascii")
    judge_output = judge_output.decode("ascii")
    judge_input = judge_input.decode("ascii")

    source_code = kwargs["submission_source"]

    source_code = source_code.decode("utf-8")

    source_code = source_code.replace("\r\n","\n")

    source_code = source_code.encode("utf-8")

    n = int(judge_input)

    ACmessage = "Ok answer is correct, code length: "+str(len(source_code)) if n == 10 else "AC"
    WAmessage = "Sorry answer is wrong, code length: "+str(len(source_code)) if n == 10 else "WA"

    #check correctness

    splitted_output = re.split("[^0-9]",process_output)
    num_seq = []
    for elem in splitted_output:
        if len(elem) == 0:
            continue
        elem = re.sub(r"^0+", "", elem[:-1]) + elem[-1]
        num_seq.append(elem)
    
    flag = True

    for i in range(n):
        if str(i) not in num_seq:
            flag = False
            break
    
    if not flag:
        return CheckerResult(False, 0, WAmessage)

    Graph = {}
    for i in range(0, len(num_seq) - 1, 2):
        u, v = num_seq[i], num_seq[i+1]
        if u == v:
            continue
        if u in Graph:
            Graph[u].append(v)
        else:
            Graph[u] = [v]
        if u in Graph:
            Graph[v].append(u)
        else:
            Graph[v] = [u]
    
    Queue = ["0"]
    l, r = 0, 1
    visited = {"0"}
    while l < r:
        cur = Queue[l]
        l += 1
        for to in Graph[cur]:
            if to not in visited:
                visited.add(to)
                Queue.append(to)
                r += 1
    
    for i in range(n):
        if str(i) not in visited:
            flag = False
            break
    
    if flag:
        return CheckerResult(True, 100, ACmessage)
    else:
        return CheckerResult(False, 0, WAmessage)