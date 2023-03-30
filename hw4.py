def rep_char(char, num) :
    print(char * num);




def draw_line_string(char) :
    msg1 = f'Hello {char},'
    msg2 = 'Welcome to Seoul.'
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    rep_char('-', nstr)
    print(f'{msg1}')
    print(f'{msg2}')
    rep_char('-', nstr);

char = input('Input his/her name: ');
draw_line_string(char);


