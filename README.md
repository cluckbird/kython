# Kython

## 超級簡化版本的Python，尚未完成

- 目標是讓任何操作都能用簡單的函數調用實現
- 一鍵完成打包為Windows exe，Linux so等

-----

## 安裝運行環境
Kython部分依賴Python環境，請部署Python環境變量（其實Windows EXE版本可能僅依賴pyinstaller）
 ```
 pip install pyinstaller
 ```
 
### 使用Kython
```Python3
build YourFileName - Build KythonScript
   build File open - Do not close after running (compiled .exe)
   build File down - close after running (compiled .exe)
   *No parameter is closed by default!
version - View current KythonScript version
```
