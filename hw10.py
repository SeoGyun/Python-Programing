import os
import pickle
filename = 'score.bin'

def input_scores():
    scores = []
    i = 1
    while (True):
        n = int(input(f'#{i}? '))
        if n < 0:
            break
        scores.append(n)
        i += 1
    return scores

def get_average(lst):
    total = 0
    for i in lst:
        total += i
    avg = total / len(lst)
    return avg

def show_scores(lst):
    for i in lst:
        print(i,end=' ')
    print()

def save_data(scores):
    with open(filename,'wb') as file:
        pickle.dump(scores,file)

def load_data():
    with open(filename, 'rb') as file:
        scores = pickle.load(file)
    return scores

if os.path.exists(filename):
    print('[파일 읽기]')
    scores = load_data()
    print('\n[점수출력]')
    print('개인점수: ',end = '')
    show_scores(scores)
    avg = get_average(scores)
    print(f'평균: {avg:.1f}')
else:
    print('[점수입력]')
    scores = input_scores()
    print('\n[점수출력]')
    print('개인점수: ',end = '')
    show_scores(scores)
    avg = get_average(scores)
    print(f'평균: {avg:.1f}')
    save_data(scores)



