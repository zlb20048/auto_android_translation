import xml.etree.ElementTree as ET
import logging
import xml.dom.minidom
from pathlib import Path
import pandas as pd

def process_strings_xml(xml_path):
    logging.info(f"处理 strings.xml 文件: {xml_path}")
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        strings = {string.get('name'): string.text for string in root.findall('string')}
        return strings
    except ET.ParseError as e:
        logging.error(f"解析 XML 文件失败: {e}")
        return {}

def update_strings_xml(xml_path, lang_code, updated_excel):
    logging.info(f"更新 strings.xml 文件: {xml_path}")
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        
        for string in root.findall('string'):
            name = string.get('name')
            if name in updated_excel.index:
                new_value = updated_excel.loc[name, lang_code]
                if pd.notna(new_value):
                    string.text = str(new_value)
        
        # 使用 xml.dom.minidom 来格式化 XML
        rough_string = ET.tostring(root, 'utf-8')
        reparsed = xml.dom.minidom.parseString(rough_string)
        pretty_xml = reparsed.toprettyxml(indent="    ")
        
        # 移除空行
        pretty_xml = '\n'.join([line for line in pretty_xml.split('\n') if line.strip()])
        
        # 写入格式化后的 XML
        with open(xml_path, 'w', encoding='utf-8') as f:
            f.write(pretty_xml)
        logging.info(f"更新了 strings.xml 文件: {xml_path}")
    except Exception as e:
        logging.error(f"更新 strings.xml 文件失败: {e}")
