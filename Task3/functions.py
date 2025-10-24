import os
from collections import Counter

from colors_rules import log_colors, Fore, Style

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "logs.txt")


def parse_log_line(line: str) -> dict:
    try:
        date, time, level, message = line.strip().split(" ", 3)
        return {
            "date": date,
            "time": time,
            "level": level,
            "message": message
            }  
    except ValueError:
        return  print(f'{Fore.RED}Invalid format in the file:{line}')
    
#print(parse_log_line("2024-10-01 12:00:00 INFO Application started"))


def load_logs(file_path: str) -> list:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            logs = [parse_log_line(line) for line in file if parse_log_line(line)]
            return logs
    except FileNotFoundError:
        print(f'{Fore.RED}File not found: {file_path}')
        return []
    

#print(load_logs(FILE_NAME))

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log["level"] == level, logs))

#print(filter_logs_by_level(load_logs(FILE_NAME), "ERROR"))

def count_logs_by_level(logs: list) -> dict:
    levels = [log["level"] for log in logs]
    return dict(Counter(levels))

def display_log_counts(counts: dict):
    print(f'Logging level| Amount')
    print("-----------------|----------")
    for level, count in counts.items():
        color = log_colors.get(level, "")
        print(f"{color}{level:<16}{Style.RESET_ALL} | {count}")

def display_log_details(logs: list, level: str):
    result = [f'\nLog details for a specific level: {level}']
    color = log_colors.get(level.upper(), "")
    for log in logs:
        result.append(f"{log['date']} {log['time']} {color}{log['level']}{Style.RESET_ALL} {log['message']}")
    return print("\n".join(result))


#print(count_logs_by_level(load_logs(FILE_NAME)))
#print(display_log_counts(count_logs_by_level(load_logs(FILE_NAME))))
#print(display_log_details(filter_logs_by_level(load_logs(FILE_NAME), "ERROR"), "ERROR"))