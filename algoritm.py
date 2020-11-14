from fuzzywuzzy import fuzz
import re

is_url = re.compile(
    r'^(?:http|ftp)s?://' # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
    r'localhost|' #localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
    r'(?::\d+)?' # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

def algoritm(task, k=50):
    f = open('DataSet.txt')
    m = 0
    ans = ""
    for line in f:
        reg_ex = re.search('(.*)-(.*)', line)
        if reg_ex:
            tem = reg_ex.group(2)
            vopros = reg_ex.group(1)
            a = fuzz.token_sort_ratio(task, vopros)
            if a > m:
                ans = tem
                m = a
    if re.match(is_url, ans) is not None:  # is url
        return (ans, True, re.match(is_url, ans))
    if m > k:
        return (ans, False)
    else:
        return ('Перевожу на оператора.', False)
    # else:
    #  return 'Повторите вопрос пожалуйста!'
