from config import *
from git_utils import clone_repo
from translation_manager import process_all_strings_xml, update_project_strings_xml
from excel_utils import match_translations  # 添加这行导入
import pandas as pd

def main():
    try:
        clone_repo(BASE_DIR, REPO_URL, BRANCH)
        
        process_all_strings_xml(BASE_DIR, TEMP_EXCEL_PATH)
        
        logging.info(f"临时 Excel 文件已创建: {TEMP_EXCEL_PATH}")
        
        main_excel = pd.read_excel(TRANSLATION_EXCEL_PATH, sheet_name=None, engine='openpyxl')
        temp_excel = pd.read_excel(TEMP_EXCEL_PATH, sheet_name=None, engine='openpyxl')
        
        for sheet_name, df in temp_excel.items():
            updated_df = match_translations(df, main_excel)
            temp_excel[sheet_name] = updated_df
        
        with pd.ExcelWriter(TEMP_EXCEL_PATH, engine='openpyxl') as writer:
            for sheet_name, df in temp_excel.items():
                df.to_excel(writer, sheet_name=sheet_name, index=False)
        logging.info("翻译匹配完成，临时 Excel 文件已更新")

        update_project_strings_xml(temp_excel, BASE_DIR)

        logging.info("所有操作已完成")
    except Exception as e:
        logging.error(f"程序执行过程中发生错误: {e}")
        raise

if __name__ == "__main__":
    main()
