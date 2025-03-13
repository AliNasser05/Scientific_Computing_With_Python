def arithmetic_arranger(problems, solution=False):
    # Handle errors
    if len(problems) > 5:
        return "Error: Too many problems."
    cnt = 0
    alpha = False
    max_digits = 0
    for problem in problems:
        ln, mx = 0, 0
        for char in problem:
            if char == "+" or char == "-":
                cnt += 1
            if char.isalpha():
                alpha = True
            if char.isnumeric():
                ln += 1
            else:
                mx = max(mx, ln)
                ln = 0
        mx = max(mx, ln)
        max_digits = max(mx, max_digits)

    if cnt != len(problems):
        return "Error: Operator must be '+' or '-'."
    if alpha:
        return "Error: Numbers must only contain digits."
    if max_digits > 4:
        return "Error: Numbers cannot be more than four digits."
    # Implementation
    answers_list = []
    top_numbers, bottom_numbers, separator, result = "", "", "", ""

    idx = 0
    for problem in problems:
        first_number, second_number, max_len = 0, 0, 0
        string_first_number, string_second_number = "", ""
        first = True
        operator = "+"
        for char in problem:
            if char == "-":
                operator = char
            if char == "+" or char == "-" or char == " ":
                first = False
                continue
            if first:
                first_number *= 10
                first_number += int(char)
                string_first_number += char
            else:
                second_number *= 10
                second_number += int(char)
                string_second_number += char

        max_length = max(len(string_first_number), len(string_second_number))

        top_numbers += "  "
        if len(string_first_number) != max_length:
            difference = max_length - len(string_first_number)
            while difference > 0:
                top_numbers += " "
                difference -= 1

        top_numbers += string_first_number
        idx += 1
        if idx < len(problems):
            top_numbers += "    "

        bottom_numbers += operator
        bottom_numbers += " "
        if len(string_second_number) != max_length:
            difference = max_length - len(string_second_number)
            while difference > 0:
                bottom_numbers += " "
                difference -= 1

        bottom_numbers += string_second_number
        if idx < len(problems):
            bottom_numbers += "    "

        separator += "--"
        for _ in range(max_length):
            separator += "-"
        if idx < len(problems):
            separator += "    "

        if solution:
            if operator == "+":
                problem_result = first_number + second_number
            else:
                problem_result = first_number - second_number
            difference = max_length + 2 - len(str(problem_result))
            while difference > 0:
                result += " "
                difference -= 1

            result += str(problem_result)
            if idx < len(problems):
                result += "    "

    answers_list.append(top_numbers)
    answers_list.append(bottom_numbers)
    answers_list.append(separator)
    if solution:
        answers_list.append(result)

    return "\n".join(answers_list)


print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
