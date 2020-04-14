import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
from utils.Generator import *
import os


class InitWindows(object):

    def __init__(self):

        self.expression_range = ''
        self.expression_number = ''

        self.expression_file_name = ''
        self.answer_file_name = ''

        self.root = tk.Tk()
        self.root.iconbitmap("./views/favicon.ico")
        self.root.geometry(f"220x330+{int(self.root.winfo_screenwidth()/2) - 110}+{int(self.root.winfo_screenheight()/2) - 165}")
        self.root.title("Exercise")
        self.init_widgets()
        self.root.mainloop()

    def init_widgets(self):

        def get_():
            n = int(entry_input_num.get())
            r = int(entry_input_range.get())
            Generator(n, r).multi_processor()
            tk.messagebox.showinfo("Info", "Success")
            os.system("explorer.exe .\\docs")

        # All label
        lb_info_generate = tk.Label(self.root, text="生成四则运算表达式", anchor="center", width=16, fg="red")
        lb_info_select = tk.Label(self.root, text="检查答案", anchor="center", width=16, fg="red")

        lb_input_num = tk.Label(self.root, text="请输入生成表达式数量", anchor="center", width=16)
        lb_input_range = tk.Label(self.root, text="请输入生成表达式范围", anchor="center", width=16)

        # All Entry box
        entry_input_num = tk.Entry(self.root)
        entry_input_range = tk.Entry(self.root)

        # All buttons
        btn_commit_generate = tk.Button(self.root, text="生成", command=get_, anchor="center", width=16)
        btn_commit_inspect = tk.Button(self.root, text="检查", command=self.inspect_dual_file, anchor="center", width=16)

        # All file select buttons
        btn_select_expressions = tk.Button(self.root, text="选择题目文件", command=self.select_expression_file, anchor="center", width=16)
        btn_select_answers = tk.Button(self.root, text="选择答案文件", command=self.select_answer_file, anchor="center", width=16)

        # #########  Create placement

        x_init, y_init, y_step = 90, 10, 30

        lb_info_generate.place(x=50, y=y_init, )
        lb_input_num.place(x=50, y=y_init + y_step, )
        entry_input_num.place(x=50, y=y_init + y_step * 2)
        lb_input_range.place(x=50, y=y_init + y_step * 3)
        entry_input_range.place(x=50, y=y_init + y_step * 4)
        btn_commit_generate.place(x=50, y=y_init + y_step * 5)

        lb_info_select.place(x=50, y=y_init + y_step * 6)
        btn_select_expressions.place(x=50, y=y_init + y_step * 7)
        btn_select_answers.place(x=50, y=y_init + y_step * 8)
        btn_commit_inspect.place(x=50, y=y_init + y_step * 9)

    def select_expression_file(self):
        self.expression_file_name = tkinter.filedialog.askopenfilename()

    def select_answer_file(self):
        self.answer_file_name = tkinter.filedialog.askopenfilename()

    def inspect_dual_file(self):
        if self.expression_file_name != '' and self.answer_file_name != '':
            inspect(self.answer_file_name, self.expression_file_name)
            tk.messagebox.showinfo("Info", "Success")
            os.system("explorer.exe .\\docs")
        else:
            tk.messagebox.showinfo("Info", "Failed")
            return False


if __name__ == '__main__':
    InitWindows()
