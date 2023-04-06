def read_single_digit(n) :
    if n == 0 :
        return '영'
    elif n == 1 :
        return '일'
    elif n == 2 :
        return '이'
    elif n == 3 :
        return '삼'
    elif n == 4 :
        return '사'
    elif n == 5 :
        return '오'
    elif n == 6 :
        return '육'
    elif n == 7 :
        return '칠'
    elif n == 8 :
        return '팔'
    else :
        return '구';


def read_number(s) :
    s_1 = s[0]
    s_2 = s[1]
    s_3 = s[2]
    return f'{read_single_digit(int(s_1))} {read_single_digit(int(s_2))} {read_single_digit(int(s_3))}';

number = input('세자리 정수 입력: ');
res = read_number(number);
print(res);


