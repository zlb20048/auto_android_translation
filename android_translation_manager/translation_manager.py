import logging
from pathlib import Path
import pandas as pd
from config import BASE_DIR, TEMP_EXCEL_PATH
from xml_utils import process_strings_xml, update_strings_xml
from excel_utils import update_temp_excel, match_translations
from git_utils import get_git_root

def process_all_strings_xml(base_dir, temp_excel_path):
    for xml_path in base_dir.rglob('values/strings.xml'):
        strings_dict = process_strings_xml(xml_path)
        
        git_root = get_git_root(xml_path.parent)
        if git_root is None:
            logging.warning(f"跳过文件 {xml_path}，无法确定 git 根目录")
            continue
        
        relative_path = xml_path.relative_to(base_dir)
        project_folder = relative_path.parts[2]
        internal_folder = relative_path.parts[3]
        sheet_name = f"{project_folder}_{internal_folder}"
        
        update_temp_excel(strings_dict, sheet_name, xml_path, temp_excel_path)
        logging.info(f"处理了文件: {xml_path}, sheet 名称: {sheet_name}")

def update_project_strings_xml(temp_excel, base_dir):
    logging.info("开始更新项目中的 strings.xml 文件")
    try:
        for sheet_name, df in temp_excel.items():
            lang_columns = [col for col in df.columns if col.startswith('values-')]

            for lang_column in lang_columns:
                grouped = df.groupby('FilePath')
                
                for file_path, group in grouped:
                    xml_path = Path(file_path).parent.parent / lang_column / 'strings.xml'
                    xml_path.parent.mkdir(parents=True, exist_ok=True)

                    update_strings_xml(xml_path, lang_column, group)

        logging.info("所有 strings.xml 文件更新完成")
    except Exception as e:
        logging.error(f"更新项目 strings.xml 文件失败: {e}")
        raise
