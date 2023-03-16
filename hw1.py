#개념 확인 과제 조건1
def get_radius(prompt):
    r = int(prompt);
    return r**2*3.14;

input_r = input('넓이를 구하고자 하는 원의 반지름은? ');
result = get_radius(input_r);
print('반지름이', input_r, '인 원의 넓이 = 3.14 *', input_r, '*', input_r, '=', result);



#개념 확인 과제 조건2
def get_circle_area():
    c_r = int(input('넓이를 구하고자 하는 원의 반지름은? '));
    c_area = c_r**2*3.14;
    return c_area, c_r;

result = get_circle_area();
print(result);


def get_circle_area2(prompt):
    radius = int(prompt)**2*3.14;
    print('반지름이', prompt, '인 원의 넓이는 = ', radius);

input_r = input('넓이를 구하고자 하는 원의 반지름은? ');
get_circle_area2(input_r);

