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
        #学生信息正确，保存到字典
        student_info = {"id":id,"name":name,"english":english,"python":python,"c":c}
        student_list.append(student_info)
        #添加完一个人了，询问是否继续
        while(1):
            inputMark = input("请问是否继续添加?(y/n):")
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
    mark = True
    while mark:
        studentId = input("请输入需要查询的学生的ID:")
        if studentId is not "":
            #开始查询工作
            if os.path.exists(fileName):
                with open(fileName,'r') as rfile:
                    student_old = rfile.readlines()
            else:
                student_old = []
            if student_old:
                #如果有数据
                student_search = []
                for list in student_old:
                    d= dict(eval(list))
                    if d["id"] == studentId:
                        student_search.append(d)
                show_student(student_search)
                student_search.clear()#清空列表
            else:
                #如果没有数据
                print("目前没有数据")
                break
        else:
            print("输入ID错误")
        while (1):
            inputMark = input("请问是否继续查询?(y/n):")
            if inputMark not in ["y", "n"]:
                print("输入错误")
                continue
            else:
                break
        if inputMark == "y":
            mark = True
        else:
            mark = False
#删除学生信息
def delete():
    mark = True
    while mark:
        studentId = input("请输入要删除的学生的ID:")
        if studentId is not "":
            #输入的id有内容
            if os.path.exists(fileName):
                with open(fileName,'r') as rfile:
                    student_old = rfile.readlines()
            else:
                student_old=[]
            ifdel = False#是否删除的标记
            if student_old:
                with open(fileName,'w') as wfile:
                    d= {}
                    for list in student_old:
                        d = dict(eval(list))
                        if d["id"]!=studentId:
                            #该条记录不用删，重新写入文件,只要正常数据，有逐条重新写入
                            wfile.write(str(d)+"\n")
                        else:
                            ifdel = True
                if ifdel:
                    print("该学生信息已经删除")
                else:
                    print("不存在该学生信息")
            else:
                print("目前没有学生数据，无需删除")
                break
        else:
            print("输入ID错误")
        #新的判断，看是否继续
        #显示处理后的结果
        show()
        while (1):
            inputMark = input("请问是否继续删除?(y/n):")
            if inputMark not in ["y", "n"]:
                print("输入错误")
                continue
            else:
                break
        if inputMark == "y":
            mark = True
        else:
            mark = False

#修改学生信息
def modify():
    mark = True
    while mark:
        studentId = input("请输入要修改的学生的ID:")
        if studentId is not "":
            #开始修改数据
            if os.path.exists(fileName):
                with open(fileName,'r') as rfile:
                    student_old = rfile.readlines()
            else:
                student_old = []
            ifmodify = False  # 是否修改完成
            if student_old:
                with open(fileName,'w') as wfile:
                    d= {}
                    for list in student_old:
                        d = dict(eval(list))
                        if d["id"]!=studentId:
                            #该条记录不用删，重新写入文件,只要正常数据，有逐条重新写入
                            wfile.write(str(d)+"\n")
                        else:
                           #开始修改记录
                            ifmodify = True
                            while(1):
                                try:
                                    english = int(input("请输入英语成绩；"))
                                    python = int(input("请输入python成绩:"))
                                    c = int(input("请输入c语言成绩:"))
                                except:
                                    print("请输入正确格式")
                                    continue

                                d["english"] = english
                                d["python"] = python
                                d["c"]= c
                                wfile.write(str(d) + "\n")
                                break
                if ifmodify:
                    print("该学生信息已经修改")
                else:
                    print("不存在该学生信息")


        else:#没有数据
            print("输入ID错误")
        while (1):
            inputMark = input("请问是否继续修改?(y/n):")
            if inputMark not in ["y", "n"]:
                print("输入错误")
                continue
            else:
                break
        if inputMark == "y":
            mark = True
        else:
            mark = False


#信息排序
def sort():
    #先显示目前的数据
    show()
    if os.path.exists(fileName):
        with open(fileName,'r') as rfile:
            student_old = rfile.readlines()
            student_new = []
            for list in student_old:
                d = dict(eval(list))
                student_new.append(d)
    else:
        return
    while(1):
        ascORdsc = input("请选择排序方式(0升序,1降序):")
        if ascORdsc == "0":
            ascORdsc_bool = False
            break
        elif ascORdsc == "1":
            ascORdsc_bool = True
            break
        else:
            print("输入有误，请重新输入")
            continue
    while(1):
        mode = input("请选择排序方式(1 英语；2 python；3 c语言):")
        #########################lambd函数及list的sort函数，需要学习
        if mode == "1":
            student_new.sort(key=lambda  x:x["english"],reverse=ascORdsc_bool)
            break
        elif mode =="2":
            student_new.sort(key=lambda x: x["python"], reverse=ascORdsc_bool)
            break
        elif mode == "3":
            student_new.sort(key=lambda x: x["c"], reverse=ascORdsc_bool)
            break
        else:
            print("输入有误，请重新输入")
            continue
    show_student(student_new)
#统计人数
def total():
    if os.path.exists(fileName):
        with open(fileName,'r') as rfile:
            student_old = rfile.readlines()
            if student_old:
                print("总共有%d名学生"%len(student_old))
            else:
                print("目前没有数据")
    else:
        print("目前没有数据")

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

def show_student(student_list):#sutdent_list为列表，每个元素为一个学生的字典信息
    if not student_list:
        print("没有数据")
        return
    #有数据，则开始处理显示
    format_title = "{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}"#format格式设置
    print(format_title.format("ID","姓名","english","python","c"))
    for student_info in student_list:
        print(format_title.format(student_info.get("id"),
                                  student_info.get("name"),
                                  student_info.get("english"),
                                  student_info.get("python"),
                                  student_info.get("c")))

#保存学生信息到文件,student为list文件
def save(student):
    try:
        student_txt = open(fileName,"a")#有文件则追加
    except:
        student_txt = open(fileName,"w")#无文件则新建
    for stu_info in student:
        student_txt.write(str(stu_info)+'\n')#按行存储
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
