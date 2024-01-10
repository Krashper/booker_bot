import os
import sys
import re

BOOK_PATH = 'book/book.txt'
book: dict[int, str] = {}
PAGE_SIZE = 1050

def _get_part_text(text: str, start: int, page_size: int):
    start_page = text[start:]
    if len(start_page) <= page_size:
        return start_page, len(start_page)
    
    max_page: str = text[start:start+page_size]
    next_symbol: str = text[start+page_size]
    signs: list[str] = [',', '.', '!', ':', ';', '?']
    if max_page[-1] in signs and next_symbol in signs:
        for i in range (2, len(max_page)):
            if max_page[-i] not in signs:
                max_page = max_page[:-i+1]
                break
    last_index: int = max([max_page.rfind(sign) for sign in signs]) + 1
    result_page = max_page[:last_index]
    return result_page, last_index

# Дополните эту функцию, согласно условию задачи
def prepare_book(path: str) -> dict[int, str]:
    with open(path, encoding='utf-8') as f:
        text = f.read()
    start = 0
    page_num = 1
    while start < len(text):
        page, size = _get_part_text(text, start, PAGE_SIZE)
        clean_page = page.lstrip()
        book[page_num] = clean_page
        page_num += 1
        start += size
    return book

prepare_book(BOOK_PATH)