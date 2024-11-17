from dmoj.result import CheckerResult

PAR_VERTICAL=100

def check(process_output, judge_output, judge_input, point_value, **kwargs):
    # convert from bytes to texts
    process_output = process_output.decode("ascii")
    judge_output = judge_output.decode("ascii")
    judge_input = judge_input.decode("ascii")

    source_code = kwargs["submission_source"]

    source_code = source_code.decode("utf-8")

    lines = source_code.splitlines()
    w=0
    for _ in lines:w=max(w,len(_))

    if w >= PAR_VERTICAL:
        return CheckerResult(False, 0, "Source code is too wide")

    # read data as normal
    if process_output==judge_output:
        return CheckerResult(True, 100 - w,"Ok answer is correct")
    
    return CheckerResult(False, 0, "Wrong Answer")