import sys, subprocess, os

try:
    c = sys.argv[1]

    if c == "build":
        arg2 = sys.argv[2]
        if arg2 == None:
            raise IndexError
        else:
            pass
        # 获取需要编译的文件
        code = open(arg2,'r',encoding='utf-8').read()
        # 获取当前编译器所在路径
        path = str(os.path.abspath(os.path.dirname(__file__))).replace('\\','/')
        # 读取配置文件（Kython文件头）
        text = str(open(path+'/config/config.ka','r',encoding='utf-8').read())
        # 打开并创建Build目录
        os.system("cd {} && mkdir build".format(path))
        # 在Build目录中写入Py文件（从Kython转换）
        open(path+'/build/build.py','w+',encoding='utf-8').write(text+code)
        # 根据参数添加：是否让编译后的程序在执行完成后关闭
        try:
            buildinfo = sys.argv[3]
            if buildinfo == "down":
                print('Compiler parameters: "Close after running"')
            elif buildinfo == "open":
                print('Compiler parameters: "Do not close after running"')
                open(path+'/build/build.py','a+',encoding='utf-8').write("\ninput()")
        except:
            pass
        # 输出：开始编译
        print("Start Build ...")
        # 开始编译为exe
        # subprocess.call("pyinstaller -i "+path+"/config/logo.ico -F "+path+"/build/build.py", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        os.system('pyinstaller -i config/logo.ico -F build/build.py')
        # 删除历史遗留目录
        os.system("@cd {} && rmdir /s/q build".format(path))
        os.system("@cd {} && del /q build.spec".format(path))
        # OK！
        print("\033[33mOK!\033[0m")
    elif c == "version":
        print("\033[44mKython 0.1 for windows / test 20.11.23\033[0m")
    else:
        print("\033[31mKython: ParameterError\033[0m")
except IndexError:
    print("\033[44mKython 0.1 Bate - Woodpacker\033[0m\n\033[35mbuild\033[0m \033[32mYourFileName\033[0m - Build KythonScript\n   \033[35mbuild\033[0m \033[32mFile\033[0m open - Do not close after running (compiled .exe)\n   \033[35mbuild\033[0m \033[32mFile\033[0m down - close after running (compiled .exe)\n   *No parameter is closed by default!\n\033[35mversion\033[0m - View current KythonScript version")