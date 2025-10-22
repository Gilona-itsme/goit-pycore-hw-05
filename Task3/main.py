"Розробіть Python-скрипт для аналізу файлів логів. Скрипт повинен вміти читати лог-файл, переданий як аргумент командного рядка, і виводити статистику за рівнями логування наприклад, INFO, ERROR, DEBUG. Також користувач може вказати рівень логування як другий аргумент командного рядка, щоб отримати всі записи цього рівня."

from pathlib import Path
import sys
from colorama import Fore, Style
import os
from functions import load_logs, filter_logs_by_level, count_logs_by_level, parse_log_line, display_log_counts, display_log_details


def main():
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Використання: python main.py path/to/logfile.log [level]{Style.RESET_ALL}")
        return

    file_path = sys.argv[1]
    level =(sys.argv[2]).upper() if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    if not logs:
        return

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level:
        filtered = filter_logs_by_level(logs, level)
        if filtered:
            display_log_details(filtered, level)
        else:
            print(f"\n{Fore.YELLOW}Немає записів для рівня '{level.upper()}'.{Style.RESET_ALL}")



if __name__ == "__main__":
    main()
    #display_log_counts(count_logs_by_level(load_logs(FILE_NAME)))
    #display_log_details(filter_logs_by_level(load_logs(FILE_NAME), "ERROR"), "ERROR")
    
 