import random
from utils.constant import *


class Arithmetic(object):

    def __init__(self, domain=10):
        # 运算符个数
        self.operator_num = random.randint(1, 3)
        # 操作数个数
        self.operand_num = self.operator_num + 1
        # 取值范围
        self.domain = domain
        # 是否有括号
        self.has_bracket = random.randint(0, 1)
        # 运算符集
        self.operator_list = []
        # 操作数集
        self.operand_list = []
        # 存放分离化的表达式
        self.expression_split = []

    # 生成随机操作数(自然数0、真分数1)
    def random_number(self):
        num_type = random.randint(0, 1)
        number = ""

        if num_type == 0:
            # 不包括self.domain
            number = str(random.randint(0, self.domain - 1))
        elif num_type == 1:
            # 整数部分
            z = random.randint(0, self.domain - 1)
            # 分母
            denominator = random.randint(2, self.domain - 1)
            # 分子
            molecular = random.randint(1, denominator - 1)

            if z != 0:
                number = str(z) + '\'' + str(molecular) + "/" + str(denominator)
            else:
                number = str(molecular) + "/" + str(denominator)

        return number

    # 生成随机操作数集
    def create_operand_list(self):
        num = self.operand_num

        while num:
            self.operand_list.append(self.random_number())
            num -= 1

    # 生成随机运算符集
    def create_operator_list(self):
        num = self.operator_num

        while num:
            self.operator_list.append(operator[random.randint(0, 3)])
            num -= 1

    # 随机产生括号的位置
    def random_bracket_place(self):
        while 1:
            left_bracket = random.randint(1, self.operand_num - 1)
            right_bracket = random.randint(left_bracket + 1, self.operand_num)

            # 类似(1 + 2 + 3)的位置则重新随机
            if left_bracket == 1 and right_bracket == self.operand_num:
                continue
            else:
                return [left_bracket, right_bracket]

    # 更新位置列表
    def update_operand_place(self, operand_place, bracket_place):
        for i in range(0, self.operand_num):
            if i < bracket_place[0] - 1:
                pass
            elif i <= bracket_place[1] - 1:
                operand_place[i] += 1
            else:
                operand_place[i] += 2

    # 处理括号
    def insert_bracket(self, bracket_num):
        # 操作数的位置
        operand_place = [2 * x - 1 for x in range(1, self.operand_num + 1)]

        while bracket_num:
            # 随机括号位置，相对于数字的位子
            bracket_place = self.random_bracket_place()
            self.expression_split.insert(operand_place[bracket_place[0] - 1] - 1, "(")
            self.expression_split.insert(operand_place[bracket_place[1] - 1] + 1, ")")
            # 更新操作数的位置列表
            self.update_operand_place(operand_place, bracket_place)
            bracket_num -= 1

    def create_arithmetic(self):
        self.create_operand_list()
        self.create_operator_list()

        self.expression_split.append(self.operand_list.pop())
        self.expression_split.append(self.operator_list.pop())
        while self.operator_list:
            self.expression_split.append(self.operand_list.pop())
            self.expression_split.append(self.operator_list.pop())
        self.expression_split.append(self.operand_list.pop())

        if self.operator_num != 1:
            bracket_num = random.randint(1, self.operator_num - 1)
            self.insert_bracket(bracket_num)

        return self.expression_split


print(Arithmetic().create_arithmetic())