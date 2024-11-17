from dmoj.result import CheckerResult

PAR_SYMBOLLESS=100
SYMBOLS=["+","-","*","/","%","&","|","^","[","]"]

def check(process_output, judge_output, judge_input, point_value, **kwargs):
    # convert from bytes to texts
    process_output = process_output.decode("ascii")
    judge_output = judge_output.decode("ascii")
    judge_input = judge_input.decode("ascii")

    source_code = kwargs["submission_source"]

    source_code = source_code.decode("utf-8")

    cnt_symbols=0
    for i in source_code:
        cnt_symbols+=1 if i in SYMBOLS else 0

    if cnt_symbols >= PAR_SYMBOLLESS:
        return CheckerResult(False, 0, "Source code contains too much symbols")

    # read data as normal
    if process_output==judge_output:
        return CheckerResult(True, 100 - w,"Ok answer is correct")
    
    return CheckerResult(False, 0, "Wrong Answer")