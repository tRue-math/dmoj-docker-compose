from dmoj.result import CheckerResult

def check(process_output, judge_output, judge_input, point_value, **kwargs):
    # convert from bytes to texts
    process_output = process_output.decode("ascii", "replace")
    judge_output = judge_output.decode("ascii")
    judge_input = judge_input.decode("ascii")

    source_code = kwargs["submission_source"]

    source_code = source_code.decode("utf-8")

    source_code = source_code.replace("\r\n","\n")

    source_code = source_code.encode("utf-8")

    # read data as normal
    if len(process_output) == 100:
        return CheckerResult(True, 100, "Ok answer is correct, code length: "+str(len(source_code)))
    else:
        return CheckerResult(False, 0, "Sorry answer is wrong, code length: "+str(len(source_code)))