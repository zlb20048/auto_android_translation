# Android Translation Manager

Android Translation Manager 是一个用于管理和自动化 Android 项目字符串资源翻译的工具。它能够从多个 Android 项目中提取字符串资源，与现有翻译匹配，并将更新后的翻译应用回项目中。

## 功能特点

- 自动克隆和同步 Android 项目仓库
- 从多个 `strings.xml` 文件中提取字符串资源
- 创建临时 Excel 文件以管理所有提取的字符串
- 与主翻译 Excel 文件匹配并更新翻译
- 将更新后的翻译写回到相应的 `strings.xml` 文件中
- 支持多语言翻译管理
- 日志记录以跟踪整个过程

## 项目结构

```
android_translation_manager/
├── config.py              # 配置文件，包含常量和日志设置
├── git_utils.py           # Git 相关操作工具
├── xml_utils.py           # XML 文件处理工具
├── excel_utils.py         # Excel 文件处理工具
├── translation_manager.py # 翻译管理核心逻辑
└── main.py                # 主程序入口
```

## 主要模块说明

1. **config.py**: 
   - 定义全局常量如仓库 URL、分支名、文件路径等
   - 配置日志记录

2. **git_utils.py**:
   - `get_git_root()`: 获取 Git 仓库根目录
   - `clone_repo()`: 克隆和同步代码仓库

3. **xml_utils.py**:
   - `process_strings_xml()`: 处理 strings.xml 文件，提取字符串资源
   - `update_strings_xml()`: 更新 strings.xml 文件中的翻译

4. **excel_utils.py**:
   - `update_temp_excel()`: 更新临时 Excel 文件
   - `match_translations()`: 匹配和更新翻译

5. **translation_manager.py**:
   - `process_all_strings_xml()`: 处理所有 strings.xml 文件
   - `update_project_strings_xml()`: 更新项目中的所有 strings.xml 文件

6. **main.py**:
   - 主程序入口，协调整个翻译管理流程

## 使用方法

1. 确保已安装所有必要的依赖（如 pandas, openpyxl 等）
2. 在 `config.py` 中设置正确的仓库 URL、分支名和文件路径
3. 运行 `main.py`:

## 注意事项

- 确保有足够的磁盘空间来克隆代码仓库
- 需要适当的权限来读写 Excel 文件和 XML 文件
- 建议在运行前备份重要的 strings.xml 文件

## 贡献

欢迎提交 issues 和 pull requests 来改进这个项目。

## 许可

[MIT License](LICENSE)

