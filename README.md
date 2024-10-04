# Android 翻译管理工具

这个 Python 脚本用于管理 Android 项目的字符串资源翻译。它可以自动下载代码仓库、处理 strings.xml 文件、更新 Excel 翻译表格，并将更新后的翻译写回 strings.xml 文件。

## 功能

1. 克隆指定的代码仓库
2. 处理项目中的所有 strings.xml 文件并提取字符串资源
3. 创建临时 Excel 文件，每个项目模块对应一个 sheet
4. 从主翻译 Excel 文件匹配翻译并更新临时 Excel 文件
5. 将更新后的翻译写回 strings.xml 文件
6. 支持多个项目模块的翻译管理
7. 使用 git 根目录来确定项目结构
8. 提供详细的日志记录

## 环境要求

- Python 3.6+
- pandas
- openpyxl
- repo 工具
- git
- 配置好的 SSH 密钥

## 安装

1. 克隆此仓库：
   ```
   git clone <repository_url>
   ```

2. 安装所需的 Python 库：
   ```
   pip install pandas openpyxl
   ```

3. 确保已安装 repo 工具、git，并配置好 SSH 密钥。

## 使用方法

1. 根据需要修改脚本中的常量：
   - `REPO_URL`: 代码仓库的 URL
   - `USERNAME`: 您的用户名
   - `BRANCH`: 要使用的分支
   - `TRANSLATION_EXCEL_PATH`: 主翻译 Excel 文件的路径
   - `BASE_DIR`: 基础目录路径
   - `TEMP_EXCEL_PATH`: 临时 Excel 文件路径

2. 运行脚本：
   ```
   python android_translation_manager.py
   ```

## 主要更新

- 支持多个项目模块的翻译管理。
- 使用 git 根目录来确定项目结构。
- 改进了 Excel 文件的处理逻辑。
- 优化了 strings.xml 文件的更新过程。
- 增加了详细的日志记录。

## 注意事项

- 脚本会将代码仓库下载到指定的 `BASE_DIR` 目录中。
- 确保在运行脚本之前备份重要数据，因为脚本会覆盖现有的 strings.xml 文件。
- 主翻译 Excel 文件应包含所有需要的翻译。
- 脚本会创建一个临时 Excel 文件来处理翻译，确保有足够的磁盘空间。

## 贡献

如果您发现任何问题或有改进建议，请创建一个 issue 或提交一个 pull request。

## 许可

[MIT License](LICENSE)

