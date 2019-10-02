def menu():
    # 输出菜单
    print('''
    ┌--------------学生信息管理系统--------------┐
                                                
     ==================功能菜单===================
                                                
       1 录入学生信息
       2 查找学生信息
       3 删除学生信息
       4 修改学生信息
       5 排序
       6 统计学生总人数
       7 显示所有学生信息
       0 退出系统
     =============================================
       说明：通过数字键选择菜单                 
    └-------------------------------------------┘
    ''')


def insert():
    # 录入学生信息
    student_list = []
    mark = True
    while mark:
        insert_id = input('请输入ID(如1001):')
        if not insert_id:
            break
        insert_name = input('请输入名字：')
        if not insert_name:
            break
        try:
            english_score = int(input('请输入英语成绩：'))
            python_score = int(input('请输入python成绩：'))
            c_score = int(input('请输入C++成绩：'))
        except:
            print('输入无效，不是整型数值．．．．重新录入信息')
            continue
        student = {'id': insert_id, 'name': insert_name, 'english_score':english_score, 'python_score':python_score, 'c_score':c_score}
        student_list.append(student)
        is_add = input('是否继续添加？（y/n）：')
        if is_add == 'y':
            mark = True
        elif is_add == 'n':
            mark = False
    save(student_list)
    print('学生信息录入完毕！！！')

def save(student_list):
    # 追加保存学生信息
    with open('student.txt', 'a+') as file:
        for info in student_list:
            file.write(str(info) + '\n')


def save_2(student_list):
    # 从新写入学生信息
    with open('student.txt', 'w+') as file:
        for info in student_list:
            if info.strip():
                file.write(str(info) + '\n')


def search():
    # 查找学生信息
    mark = True
    while mark:
        sch = int(input('按ID查输入1；按姓名查输入2：'))
        if sch == 1:
            student_id = input('请输入学生ID：')
            var = 'id'
            search_info(var, student_id)
        elif sch == 2:
            student_name = input('请输入学生姓名：')
            var = 'name'
            search_info(var, student_name)
        else:
            print('您的输入有误，请重新输入！')
            break
        go_on = input('是否继续查询？（y/n）')
        if 'y' in go_on:
            mark = True
        else:
            mark = False


def search_info(var, search_var):
    with open('student.txt', 'r') as file:
        mark = True
        student_info = file.readlines()
        student_query = []
        for info in student_info:
            info = eval(info)
            if search_var == info[var]:
                student_query.append(str(info))
                sw = show_student(student_query)
                mark = False
                break
        if mark:
            print('(o@.@o) 无数据信息 (o@.@o)')


def delete():
    # 删除学生信息
    student = []
    with open('student.txt', 'r+') as file:
        student_info = file.readlines()
        delete_id = input('请输入要删除的学生ID：')
        mark = True
        for info in student_info:
            info = eval(info)
            if delete_id == info['id']:
                print('ID为 {} 的学生信息已经被删除...'.format(info['id']))
                mark = False
                continue
            student.append(str(info))
    save_2(student)

    if mark:
        print('无ID为 {} 的学生信息！'.format(delete_id))
    else:
        sw = show()
    go_on = input('是否继续删除？（y/n）:')
    if 'y' in go_on:
        delete()
    else:
        return


def modify():
    # 修改学生信息
    mark = True
    sw = show()
    student_id = input('请输入要修改的学生ID：')
    for i, student_info in enumerate(sw):
        if student_info.strip():
            temp_info = eval(student_info)
            if temp_info['id'] == student_id:
                print('找到了这名学生，可以修改他的信息！')
                name = input('请输入姓名：')
                english_score = int(input('请输入英语成绩：'))
                python_score = int(input('请输入python成绩：'))
                c_score = int(input('请输入C++成绩：'))
                temp = dict([('id', temp_info['id']), ('name', name), ('english_score', english_score), ('python_score', python_score), ('c_score', c_score)])
                sw[i] = str(temp)
                mark = False
    if mark:
        print('未找到这名学生')
    save_2(sw)
    go_on = input('是否继续修改其他学生信息？（y/n）：')
    if 'y' in go_on:
        modify()
    else:
        return


def sort():
    # 排序
    s = int(input('请选择（0升序；1降序）：'))
    reverse = True if s == 1 else False
    match = int(input('请选择排序方式（1按英语成绩排序；2按Python成绩排序；3按C语言成绩排序；0按总成绩排序）：'))
    with open('student.txt', 'r') as file:
        student_query = file.readlines()
    temp = {0: 'score', 1: 'english_score', 2: 'python_score', 3: 'c_score'}
    temp_key = temp.get(match)
    student_query = [i.strip() for i in student_query if i.strip()]
    for n, i in enumerate(student_query):
        if i.strip():
            i = eval(i)
            i['score'] = i['english_score'] + i['python_score'] + i['c_score']
            student_query[n] = str(i)
    student_query.sort(key=lambda x: eval(x)[temp_key], reverse=reverse)
    show_student(student_query)


def count():
    # 统计学生总人数
    with open('student.txt', 'r') as file:
        student_query = [i for i in file.readlines() if i.strip()]
        print('一共有 {} 名学生！'.format(len(student_query)))


def show():
    # 显示所有学生信息
    with open('student.txt', 'r') as file:
        student_info = file.readlines()
        show_student(student_info)
    return student_info


def show_student(student_query): # student_query是一个列表
    student_title = ('{:^10}\t' * 6).format('ID', '名字', '英语成绩', 'Python成绩', 'C语言成绩', '总成绩')
    print(student_title)

    for info in student_query:
        if info.strip():
            info = eval(info)
            score =info['english_score'] + info['python_score'] + info['c_score']
            for _, i in enumerate(info):
                print('{:^10}\t\t'.format(info[i]), end='')
            if len(info) == 5:
                print('{:^10}'.format(score))
            print()


def main():
    while True:
        menu()
        try:
            option_int = int(input('请选择：'))
            if option_int == 0:
                print('您已退出学生信息管理系统！')
                break
            elif option_int == 1:
                insert()
            elif option_int == 2:
                search()
            elif option_int == 3:
                delete()
            elif option_int == 4:
                modify()
            elif option_int == 5:
                sort()
            elif option_int == 6:
                count()
            elif option_int == 7:
                sw = show()
            else:
                print('请重新选择！')
                print('······················································')
        except:
            print('输入有误！请重新选择！：')
            print('······················································')


if __name__ == '__main__':
    main()
