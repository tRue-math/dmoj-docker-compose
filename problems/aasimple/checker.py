from dmoj.result import CheckerResult

PAR_SIMPLE=100

def check(process_output, judge_output, judge_input, point_value, **kwargs):
    # convert from bytes to texts
    process_output = process_output.decode("ascii")
    judge_output = judge_output.decode("ascii")
    judge_input = judge_input.decode("ascii")

    source_code = kwargs["submission_source"]

    source_code = source_code.decode("utf-8")

    if len(set(source_code)) >= PAR_SIMPLE:
        return CheckerResult(False, 0, "Source code is too complex")

    # read data as normal
    if process_output==judge_output:
        return CheckerResult(True, 100 - len(set(source_code)),"Ok answer is correct")
    
    return CheckerResult(False, 0, "Wrong Answer")