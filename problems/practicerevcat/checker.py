from dmoj.result import CheckerResult

def check(process_output, judge_output, judge_input, point_value, **kwargs):
    # convert from bytes to texts
    process_output = process_output.decode("ascii")
    judge_output = judge_output.decode("ascii")
    judge_input = judge_input.decode("ascii")

    source_code = kwargs["submission_source"]

    source_code = source_code.decode("utf-8")

    # read data as normal
    if process_output == judge_output:
        return CheckerResult(True, max(0, 100 - len(source_code)), "Ok answer is correct")
    else:
        return CheckerResult(False, 0, "Sorry answer is wrong")