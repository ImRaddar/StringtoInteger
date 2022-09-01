import re

def myAtoi(s: str) -> int:
    pattern = r"[+-]*\d+"
    if len(s) == 0:
        return 0
    if len(re.findall(pattern, s)) == 0:
        return 0
    num = re.findall(pattern, s)[0]
    resultsign = num.find('+')
    if resultsign == -1: 
        resultsign = num.find('-')
    if resultsign != -1:
        if resultsign != 0:
            return 0
        if num[resultsign+1] == '-' or num[resultsign+1] == '+':
            return 0
    if f".{num}" in s:
        if not f"{num}.{num}" in s:
            return 0
    sign = s.find('+')
    if sign == -1:
        sign = s.find('-')
    if sign != -1:
        if not sign+1 == len(s):
            if s[sign+1] == ' ':
                return 0
    if int(num) > 2**31 - 1:
        num = 2**31 - 1
    elif int(num) < -2**31:
        num = -2**31
    for x in s:
        if x != ' ' and x != '+' and x != '-':
            try:
                int(x)
            except ValueError:
                return 0
            else:
                return num
    return num
