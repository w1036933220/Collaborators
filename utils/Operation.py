# OS操作, 传入表达式/答案/正确率保存到文件
import os
import time
from utils.Calculate import *
import re

# 文件保存位置
if not os.path.exists('./docs'):
    os.mkdir('./docs')


# 检查
def inspect(answer_file, expression_file):
    # 正确错误列表序号
    correct_seq = []
    wrong_seq = []

    try:
        # 读取文件
        with open(expression_file, 'r', encoding='utf-8') as fa:
            expression_content = fa.readlines()
        fa.close()
        # 读取文件
        with open(answer_file, 'r', encoding='utf-8') as fb:
            answer_content = fb.readlines()
        fb.close()

        # for i, c in enumerate(expression_content):
        #     print(i,)

        # 由答案文件获取序号 再在运算式中找到相对应的题目计算答案 再比较
        # 获取列表
        for item_b in answer_content:

            # 当前答案的行数的序列号
            answer_sqe, answer = int(item_b.split('. ')[0]), item_b.split('. ')[1]

            # 找到对应的习题的行数
            expression = expression_content[answer_sqe - 1]
            # print(expression)

            # 分割字符
            pattern = re.split(r'([()×÷+-])+', expression.split('. ')[1].replace(" ", "").replace("\n", ""))
            for index in range(pattern.count('')):
                pattern.remove('')

            # 提取表达式并计算 如若正确存进
            aw = Calculate(pattern).cal_expression()
            print(f"原表达式{expression}\n提取表达式{pattern}\n计算值{aw}\n实际结果{answer}")

            if Calculate(pattern).cal_expression() == answer:
                correct_seq.append(answer_sqe)

        # # 避免漏题情况
        for item_a in expression_content:
            a_sqe = item_a.split('. ')[0]
            if a_sqe not in correct_seq:
                wrong_seq.append(a_sqe)

        # # 保存结果
        # save_inspect(correct_seq, wrong_seq)

    except IOError:
        print('Failed to open file')
        return


# 保存题目 传入序列号以及题目
def save_exercise(expressions_list):
    exercise_file = './docs/Exercises.txt'
    try:
        with open(exercise_file, 'w+', encoding='utf-8') as f:
            for line in expressions_list:
                f.write('{}\n'.format(line))
        f.close()
    except IOError:
        print('Exercise.txt create failed. Please check again')


# 保存答案 传入序列号以及答案
def save_answer(answers_list):
    answer_file = './docs/Answer.txt'
    try:
        with open(answer_file, 'w+', encoding='utf-8') as f:
            for line in answers_list:
                f.write('{}\n'.format(line))
    except IOError:
        print('Answer.txt create failed. Please check again')


# 保存比较结果 传入正确列表以及错误列表
def save_inspect(correct_list, wrong_list):
    inspect_file = './docs/Grade.txt'
    try:
        with open(inspect_file, 'w+', encoding='utf-8') as f:
            f.write(f'Correct: {len(correct_list)}{correct_list}\n'
                    f'Wrong: {len(wrong_list)}{wrong_list}\n'
                    f'Accuracy: {round(len(correct_list) / len(wrong_list), 4) * 100}%\n')
    except IOError:
        print('Grade.txt create failed. Please check again')


if __name__ == '__main__':
    save_exercise(['1+1', '2+3'])
