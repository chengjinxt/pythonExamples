激活虚拟环境
.venv\Scripts\activate

如果激活虚拟环境，而虚拟环境删除后，要切换回系统下的Python环境，进行如下操作

1.配置 VSCode 的 Python 解释器
选择解释器：
打开 VSCode。
按 Ctrl+Shift+P（Windows/Linux）或 Cmd+Shift+P（Mac），输入 Python: Select Interpreter 并选择它。
在弹出的列表中选择 Enter interpreter path，然后手动输入或浏览到 D:\Python\python.exe。


基于 PySide6 开发软件的步骤可以分为以下几个阶段：**环境准备**、**开发**、**测试**、**打包发布**。以下是详细的步骤说明：

---

## 1. **环境准备**
### 1.1 安装 Python
- 确保已安装 Python 3.7 或更高版本。
- 可以从 [Python 官网](https://www.python.org/downloads/) 下载并安装。

### 1.2 创建虚拟环境
- 使用虚拟环境隔离项目依赖。
- 在项目目录下运行以下命令：
  ```bash
  python -m venv .venv
  ```
- 激活虚拟环境：
  - Windows:
    ```bash
    .venv\Scripts\activate
    ```
  - macOS/Linux:
    ```bash
    source .venv/bin/activate
    ```

### 1.3 安装 PySide6
- 在虚拟环境中安装 PySide6：
  ```bash
  pip install PySide6
  ```

### 1.4 安装开发工具（可选）
- 安装代码编辑器或 IDE，如 **VS Code**、**PyCharm**。
- 安装 Qt Designer（PySide6 自带）用于设计 UI。

---

## 2. **开发**
### 2.1 设计 UI
- 使用 **Qt Designer** 设计界面：
  - 运行 `pyside6-designer` 启动 Qt Designer。
  - 设计界面并保存为 `.ui` 文件（如 `main_window.ui`）。
- 将 `.ui` 文件转换为 Python 代码：
  ```bash
  pyside6-uic main_window.ui > ui_main_window.py
  ```

### 2.2 编写主程序
- 创建一个 Python 文件（如 `main.py`），加载 UI 文件并实现逻辑：
  ```python
  import sys
  from PySide6.QtWidgets import QApplication, QMainWindow
  from ui_main_window import Ui_MainWindow

  class MainWindow(QMainWindow):
      def __init__(self):
          super().__init__()
          self.ui = Ui_MainWindow()
          self.ui.setupUi(self)

          # 连接信号和槽
          self.ui.pushButton.clicked.connect(self.on_button_click)

      def on_button_click(self):
          self.ui.label.setText("Hello, PySide6!")

  if __name__ == "__main__":
      app = QApplication(sys.argv)
      window = MainWindow()
      window.show()
      sys.exit(app.exec())
  ```

### 2.3 运行程序
- 在终端运行：
  ```bash
  python main.py
  ```

---

## 3. **测试**
- 使用单元测试框架（如 `unittest` 或 `pytest`）测试代码逻辑。
- 手动测试 UI 功能，确保界面交互正常。

---

## 4. **打包发布**
### 4.1 安装打包工具
- 使用 `PyInstaller` 打包应用程序：
  ```bash
  pip install pyinstaller
  ```

### 4.2 打包应用程序
- 在项目目录下运行：
  ```bash
  pyinstaller --onefile --windowed main.py
  ```
  - `--onefile`：将所有文件打包成一个可执行文件。
  - `--windowed`：不显示命令行窗口（适用于 GUI 程序）。

- 打包完成后，可执行文件会生成在 `dist` 目录中。

### 4.3 处理资源文件（可选）
- 如果程序使用了资源文件（如图片、配置文件），需要确保它们被打包：
  - 在代码中使用相对路径引用资源。
  - 使用 `PyInstaller` 的 `--add-data` 参数：
    ```bash
    pyinstaller --onefile --windowed --add-data "resources/*;resources" main.py
    ```

### 4.4 测试打包后的程序
- 运行 `dist` 目录中的可执行文件，确保功能正常。

### 4.5 分发应用程序
- 将 `dist` 目录中的可执行文件分发给用户。
- 如果需要跨平台分发，可以在不同操作系统上重复打包步骤。

---

## 5. **其他注意事项**
### 5.1 跨平台支持
- PySide6 支持 Windows、macOS 和 Linux。
- 在不同平台上打包时，确保使用对应平台的 Python 和 PyInstaller。

### 5.2 减小打包体积
- 使用 `UPX` 压缩可执行文件：
  - 下载 [UPX](https://upx.github.io/)。
  - 在打包时添加 `--upx-dir` 参数：
    ```bash
    pyinstaller --onefile --windowed --upx-dir /path/to/upx main.py
    ```

### 5.3 处理依赖问题
- 如果打包后程序运行报错，可能是缺少依赖库。
- 使用 `--hidden-import` 参数显式导入缺失的模块：
  ```bash
  pyinstaller --onefile --windowed --hidden-import=module_name main.py
  ```

---

## 总结
1. **环境准备**：安装 Python、PySide6，创建虚拟环境。
2. **开发**：使用 Qt Designer 设计 UI，编写主程序逻辑。
3. **测试**：测试功能和界面。
4. **打包发布**：使用 PyInstaller 打包，分发可执行文件。

通过以上步骤，你可以完成一个基于 PySide6 的桌面应用程序的开发、测试和发布。

# 动态加载 UI 文件
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