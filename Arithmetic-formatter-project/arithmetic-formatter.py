def arithmetic_arranger(problems, show_answers=False):
    first = ''
    second = ''
    lines = ''
    res = ''
    sumx = ''
    string = ''

    if len(problems) > 5:
        return('Error: Too many problems.')

    for problem in problems:
        first_num = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        second_num = problem.split(" ")[2]
        if not first_num.isnumeric() or  not second_num.isnumeric():
            return('Error: Numbers must only contain digits.')
        if operator == '*' or operator == '/':
            return("Error: Operator must be '+' or '-'.")
        if len(first_num) > 4 or len(second_num) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        length = max(len(first_num), len(second_num)) + 2
        top = first_num.rjust(length)
        bottom = operator + second_num.rjust(length-1)

        line = ''
        for _ in range(length):
            line += '-'
        suma = ''
        if operator == '+':
            suma = str(int(first_num) + int(second_num))
        elif operator =='-':
            suma = str(int(first_num) - int(second_num))
        
        res = str(suma).rjust(length)

        if problem != problems[-1]:
            first += top + '    '
            second += bottom + '    '
            lines += line + '    '
            sumx += res + '    '
        else:
            first += top
            second += bottom
            lines += line
            sumx += res

    if show_answers:
        string = first +'\n' + second + '\n' + lines +'\n' + sumx
    else:
        string = first + '\n' + second + '\n' + lines
    return string


  

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
