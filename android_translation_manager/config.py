import logging
from pathlib import Path

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 常量定义
REPO_URL = "ssh://zixiangliu@10.10.96.213:29418/projects/Pateo-APP-MainInteraction-Hyundai/manifest"
USERNAME = "zixiangliu"
BRANCH = "master"
TRANSLATION_EXCEL_PATH = "/home/zixiangliu/文档/文言/translation.xlsx"
BASE_DIR = Path("/work/11") / Path(REPO_URL.split('/')[-2])
TEMP_EXCEL_PATH = BASE_DIR / "temp_translations.xlsx"
