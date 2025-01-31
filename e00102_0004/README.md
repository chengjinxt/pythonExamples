激活虚拟环境
.venv\Scripts\activate

如果激活虚拟环境，而虚拟环境删除后，要切换回系统下的Python环境，进行如下操作

1.配置 VSCode 的 Python 解释器
选择解释器：
打开 VSCode。
按 Ctrl+Shift+P（Windows/Linux）或 Cmd+Shift+P（Mac），输入 Python: Select Interpreter 并选择它。
在弹出的列表中选择 Enter interpreter path，然后手动输入或浏览到 D:\Python\python.exe。


在 PySide6 中，动态加载 UI 文件是一种常见的做法，它允许你将 UI 设计与逻辑代码分离，便于维护和更新。以下是动态加载 UI 文件的详细方法：

---

## 方法 1：使用 `QUiLoader` 动态加载 `.ui` 文件
`QUiLoader` 是 PySide6 提供的一个工具类，可以直接加载 `.ui` 文件并生成对应的界面。

### 步骤：
1. 确保 `.ui` 文件已通过 Qt Designer 设计并保存。
2. 使用 `QUiLoader` 加载 `.ui` 文件并生成界面。

### 示例代码：
```python
import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class MyWindow(QWidget):
    def __init__(self, ui_file):
        super().__init__()
        self.load_ui(ui_file)

    def load_ui(self, ui_file):
        # 加载 .ui 文件
        loader = QUiLoader()
        ui_file = QFile(ui_file)
        if not ui_file.open(QFile.ReadOnly):
            print(f"Cannot open {ui_file}: {ui_file.errorString()}")
            sys.exit(-1)
        self.ui = loader.load(ui_file, self)
        ui_file.close()
        self.ui.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow("main_window.ui")  # 替换为你的 .ui 文件路径
    sys.exit(app.exec())
```

### 说明：
- `QUiLoader` 会加载 `.ui` 文件并生成对应的界面。
- 你可以通过 `self.ui` 访问界面中的控件。

---

## 方法 2：将 `.ui` 文件转换为 Python 代码并动态加载
另一种方法是将 `.ui` 文件转换为 Python 代码，然后在运行时动态加载。

### 步骤：
1. 使用 `pyside6-uic` 工具将 `.ui` 文件转换为 Python 代码。
2. 在运行时动态加载生成的 Python 代码。

### 示例代码：
#### 1. 转换 `.ui` 文件
在终端运行以下命令，将 `.ui` 文件转换为 Python 代码：
```bash
pyside6-uic main_window.ui > ui_main_window.py
```

#### 2. 动态加载生成的 Python 代码
```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main_window import Ui_MainWindow  # 导入生成的 UI 类

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # 创建 UI 实例
        self.ui.setupUi(self)      # 动态加载 UI

        # 连接信号和槽
        self.ui.pushButton.clicked.connect(self.on_button_click)

    def on_button_click(self):
        self.ui.label.setText("Hello, PySide6!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
```

### 说明：
- `Ui_MainWindow` 是 `pyside6-uic` 生成的类，包含 `setupUi` 方法用于加载 UI。
- 你可以通过 `self.ui` 访问界面中的控件。

---

## 方法 3：动态加载多个 UI 文件
如果你的应用程序需要动态加载多个 UI 文件（如多个窗口），可以将每个 UI 文件转换为 Python 代码，然后在运行时根据需要加载。

### 示例代码：
```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from ui_main_window import Ui_MainWindow  # 主窗口 UI
from ui_dialog import Ui_Dialog           # 对话框 UI

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 连接信号和槽
        self.ui.pushButton.clicked.connect(self.open_dialog)

    def open_dialog(self):
        dialog = QDialog(self)
        dialog_ui = Ui_Dialog()
        dialog_ui.setupUi(dialog)
        dialog.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
```

### 说明：
- 每个 UI 文件都可以通过 `pyside6-uic` 转换为 Python 代码。
- 在运行时根据需要加载不同的 UI。

---

## 方法 4：使用 `loadUiType` 动态加载 `.ui` 文件
`pyside6-uic` 还提供了 `loadUiType` 函数，可以直接加载 `.ui` 文件并返回 UI 类和基类。

### 示例代码：
```python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.uic import loadUiType

# 加载 .ui 文件
Ui_MainWindow, QMainWindowBase = loadUiType("main_window.ui")

class MyWindow(QMainWindowBase, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 连接信号和槽
        self.pushButton.clicked.connect(self.on_button_click)

    def on_button_click(self):
        self.label.setText("Hello, PySide6!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
```

### 说明：
- `loadUiType` 返回两个类：UI 类和基类。
- 你可以通过继承这两个类来动态加载 UI。

---

## 总结
- **方法 1**：使用 `QUiLoader` 直接加载 `.ui` 文件，适合简单的动态加载。
- **方法 2**：将 `.ui` 文件转换为 Python 代码，适合需要频繁修改 UI 的场景。
- **方法 3**：动态加载多个 UI 文件，适合多窗口应用程序。
- **方法 4**：使用 `loadUiType` 动态加载 `.ui` 文件，适合需要灵活控制 UI 的场景。

根据项目需求选择合适的方法即可。