import re    
def strip_function(string, c=''):
        if c != '':
            my_regex = re.compile('^['+ c +']*|['+ c +']*$')
            stripped_value = my_regex.sub('', string)
            print(stripped_value)
        else:
            my_regex = re.compile('^(\s)*|(\s)*$')
            stripped_value = my_regex.sub('', string)
            print(stripped_value)


strip_function('  Hello World   ', '')