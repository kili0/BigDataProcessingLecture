#!/usr/bin/env python3
import re
import sys

def convert(download_text):
    binarydata = open(download_text, 'rb').read()
    text = binarydata.decode('shift_jis')
    # ルビ、注釈などの除去
    if '-' in text:
        text = (re.split(r'\-{5,}', text)[2])
    if '底本:' in text:
        text = (re.split(r'底本:', text)[0])

    text = re.sub(r'《.+?》', '', text) text = re.sub(r'[#.+?]', '', text)
    text = text.strip()
    return text

def main():
    text = convert(sys.argv[1])
    # 整形したデータで上書き保存
    open(sys.argv[1], mode="w").write(text)

main()
