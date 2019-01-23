from tkinter import *
import tkinter.filedialog

def show():
    print("文本框1:<< % s>>" % e1.get())
    print("文本框2:<< % s>>" % e2.get())
    e1.delete(0, END)
    e2.delete(0, END)

def get_new_file_path():
    e1.select_clear()
    selectFileName = tkinter.filedialog.askopenfilename(title='选择文件')  # 选择文件
    e1.insert(0,selectFileName)

def get_old_file_path():
    e2.select_clear()
    selectFileName = tkinter.filedialog.askopenfilename(title='选择文件')  # 选择文件
    e2.insert(0,selectFileName)

if __name__ == "__main__":
    root = Tk()
    root.geometry("1000x400")
    # Thinker总共提供了三种布局组件的方法：pack(),grid()和place()
    # grid()方法允许你用表格的形式来管理组件的位置
    # row选项代表行，column选项代表列
    # 例如row=1，column=2表示第二行第三列(0表示第一行)
    Label(root, text="新文件:").grid(row=0)
    Label(root, text="旧文件:").grid(row=1)
    e1 = Entry(root,width=100)
    e2 = Entry(root,width=100)
    e1.grid(row=0, column=1, padx=10, pady=5)
    e2.grid(row=1, column=1, padx=10, pady=5)
    Button(root, text="浏览", width=10, command=get_new_file_path).grid(row=0, column=2, padx=10, pady=5)
    Button(root, text="浏览", width=10, command=get_old_file_path).grid(row=1, column=2, padx=10, pady=5)

    # 如果表格大于组件，那么可以使用sticky选项来设置组件的位置
    # 同样你需要使用N，E，S,W以及他们的组合NE，SE，SW，NW来表示方位
    Button(root, text="对比", width=10, command=show).grid(row=3, column=0, sticky=W, padx=10, pady=5)
    Button(root, text="退出", width=10, command=root.quit).grid(row=3, column=1, sticky=E, padx=10, pady=5)

    mainloop()