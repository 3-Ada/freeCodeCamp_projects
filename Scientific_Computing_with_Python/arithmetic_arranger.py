def arithmetic_arranger(problems, result_displayed=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    arranged_problems_list = list()
    num_lines = 3
    if result_displayed:
        num_lines += 1
    for _ in range(num_lines):
        arranged_problems_list.append('')

    for problem in problems:
        if '+' not in problem and '-' not in problem:
            return "Error: Operator must be '+' or '-'."
        problem = problem.split()
        if not (problem[0].isdigit() and problem[2].isdigit()):
            return 'Error: Numbers must only contain digits.'
        if len(problem[0]) > 4 or len(problem[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        len_line = max(len(problem[0]), len(problem[2])) + 2
        arranged_problems_list[0] += problem[0].rjust(len_line) + ' '*4
        arranged_problems_list[1] += problem[1] + (
            len_line - 1 - len(problem[2])) * ' ' + problem[2] + ' '*4
        arranged_problems_list[2] += '-' * len_line + ' '*4
        if result_displayed:
            if '+' in problem[1]:
                result = int(problem[0]) + int(problem[2])
            else:
                result = int(problem[0]) - int(problem[2])
            arranged_problems_list[3] += str(result).rjust(len_line) + ' '*4
    arranged_problems = '\n'.join([i.rstrip() for i in arranged_problems_list])
    return arranged_problems
