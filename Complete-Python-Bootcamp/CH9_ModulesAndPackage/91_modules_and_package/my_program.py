from my_module import my_func # 引用同一層其他檔案
from MyMainPackage import MyMainScript # 引用package父層
from MyMainPackage.MySubPackage import MySubScript # 引用package子層

my_func()                   # hey Im in my_module.py
MyMainScript.main_report()  # is from my main script
MySubScript.sub_report()    # is from my sub script
