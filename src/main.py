
#!/usr/bin/env python3
"""
Career Path Tracker - система объективных маркеров компетенций
"""

import os
import json
from src.core.tracker import CareerTracker

def main():
    print("🎯 Career Path Tracker")
    print("=" * 40)
    
    tracker = CareerTracker()
    
    while True:
        print("\n1 - Показать прогресс")
        print("2 - Отметить выполненный маркер") 
        print("3 - Рекомендации по развитию")
        print("4 - Выход")
        
        choice = input("\nВыберите действие: ").strip()
        
        if choice == "1":
            tracker.show_progress()
        elif choice == "2":
            marker_id = input("Введите ID маркера: ").strip()
            tracker.mark_completed(marker_id)
        elif choice == "3":
            tracker.show_recommendations()
        elif choice == "4":
            print("До свидания! 🚀")
            break
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()
