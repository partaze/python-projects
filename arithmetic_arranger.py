#Function to display arithmetic problems. It takes a list of strings as an argument, and also has an optional boolean argument which directs
#whether the answers are displayed or not.

def arithmetic_arranger(problems, show=False):

    x = len(problems)
    top = []
    operator = []
    bottom = []
    results = []
    num1 = ""
    op = ""
    num2 = ""
    result = ""
    topline = ""
    midline = ""
    divline = ""
    spacing = " " * 4
    bottomline = ""
    arranged_problems = ""

    if x > 5:
        return ("Error: Too many problems.")

    for c in problems:
        separate = c.split()
        num1 = separate[0].strip()
        op = separate[1].strip()
        num2 = separate[2].strip()

        if op == "/" or op == "*":
            return ("Error: Operator must be '+' or '-'.")
        elif len(num1) > 4 or len(num2) > 4:
            return ("Error: Numbers cannot be more than four digits.")
        elif num1.isdigit() == False or num2.isdigit() == False:
            return ("Error: Numbers must only contain digits.")
        else:
            top.append(num1)
            operator.append(op)
            bottom.append(num2)

            if op == "+":
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            results.append(result)

    for i in range(len(problems)):
        num1 = top[i]
        op = operator[i]
        num2 = bottom[i]
        result = results[i]
        bigger = max(len(num1), len(num2))
        width = bigger + 2
        
        topline += (" " * (width - len(num1))) + num1 + spacing
        midline += op + (" " * (width - len(num2) - 1)) + num2 + spacing
        divline += "-" * width + spacing
        bottomline += (" " * (width - len(result))) + result + spacing

    arranged_problems = topline.rstrip()+'\n'+ midline.rstrip() + '\n' + divline.rstrip()

    if show:
      arranged_problems+='\n'+bottomline.rstrip()
    return arranged_problems
