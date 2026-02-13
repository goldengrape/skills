import re
import sys
import os

def count_stats(file_path):
    if not os.path.exists(file_path):
        print(f"错误：未找到文件 '{file_path}'。")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"无法读取文件：{e}")
        return

    # 中文字符数 (Chinese characters)
    chinese_chars = re.findall(r'[\u4e00-\u9fa5]', content)
    chinese_count = len(chinese_chars)

    # 英文字符数 (English characters, excluding spaces)
    english_chars = re.findall(r'[a-zA-Z]', content)
    english_char_count = len(english_chars)

    # 英文单词数 (English words)
    english_words = re.findall(r'\b[a-zA-Z]+\b', content)
    english_word_count = len(english_words)
    
    # 总字数 (中文字符数 + 英文单词数)
    total_word_count = chinese_count + english_word_count

    print(f"--- 文档统计报告: {os.path.basename(file_path)} ---")
    print(f"中文字符数: {chinese_count}")
    print(f"英文字符数: {english_char_count}")
    print(f"英文单词数: {english_word_count}")
    print(f"总计字数 (中文字+英文单词): {total_word_count}")
    print(f"--------------------------------------")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python word_count.py <文件路径>")
    else:
        count_stats(sys.argv[1])
