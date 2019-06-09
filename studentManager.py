import re
import os

fileName = "book.txt"

def menu():
    # 输出菜单
    print('''
                     │
       │   =============== 功能菜单 ============╔———————学生信息管理系统————————╗
       │                                ===   │
       │                                              │
       │   1 录入学生信息                             │
       │   2 查找学生信息                             │
       │   3 删除学生信息                             │
       │   4 修改学生信息                             │
       │   5 排序                                     │
       │   6 统计学生总人数                           │
       │   7 显示所有学生信息                         │
       │   0 退出系统                                 │
       │  ==========================================  │
       │  说明：通过数字或↑↓方向键选择菜单          │
       ╚———————————————————————╝
       ''')

#退出系统

#录入学生信息
def insert():
    student_list = []
    mark = True
    while mark:
        id = input("请输入学生ID:")
        if not id:
            break
        name = input("请输入学生姓名:")
        if not name:
            break
        try:
            english = int(input("请输入英语成绩:"))
            python = int(input("请输入python成绩:"))
            c = int(input("请输入c语言成绩:"))
        except:
            print("请输入正确格式")
            continue
        #学生信息正确，保存到字典
        student_info = {"id":id,"name":name,"english":english,"python":python,"c":c}
        student_list.append(student_info)
        #添加完一个人了，询问是否继续
        while(1):
            inputMark = input("请问是否继续添加?(y/n)")
            if inputMark not in ["y","n"]:
                print("输入错误")
                continue
            else:
                break
        if inputMark == "y":
            mark = True
        else:
            mark = False
    save(student_list)
    print("信息保存完毕")




#查找学生信息
def search():
    return
#删除学生信息
def delete():
    return
#修改学生信息
def modify():
    return
#信息排序
def sort():
    return
#统计人数
def total():
    return
#显示学生信息
def show():
    student_new = []
    if os.path.exists(fileName):
        with open(fileName,'r') as rfile:
            student_old = rfile.readlines()
        for list in student_old:
            student_new.append(eval(list))
        if student_new:#有数据
            show_student(student_new)
    else:
        print("没有数据")

def show_student(student_list):
    if not student_list:
        print("没有数据")

#保存学生信息到文件,student为list文件
def save(student):
    try:
        student_txt = open(fileName,"a")#有文件则追加
    except:
        student_txt = open(fileName,"w")#无文件则新建
    for stu_info in student:
        student_txt.write(str(stu_info)+'\n')
    student_txt.close()



def main():
    ctrl = True
    while(ctrl):
        menu()
        option = input("请输入选项的数字：")
        #option_str = re.sub("\D","",option)
        try:
            option_int = int(option)
            if option_int not in [0,1,2,3,4,5,6,7]:
                print("输入错误，请输入正确序号")
                continue
        except:
            print("输入错误，请输入数字")
            continue
        #输入的数字正确，开始执行
        if option_int == 0: #退出系统
            print("已退出系统")
            ctrl = False
        if option_int == 1:
            insert()#新建信息
        if option_int == 2:
            search()#查询信息
        if option_int == 3:
            delete()#删除信息
        if option_int == 4:
            modify()#修改信息
        if option_int == 5:
            sort()#排序
        if option_int == 6:
            total()#统计信息
        if option_int == 7:
            show()#显示所有信息



if __name__ == "__main__":
    main()
