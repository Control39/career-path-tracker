#!/usr/bin/env python3
"""
IT Compass — объективная карта роста в IT через верифицируемые маркеры
"""
import os
import sys
from src.core.tracker import CareerTracker

def main():
    print("🧭 IT Compass")
    print("=" * 40)
    
    tracker = CareerTracker()
    
    while True:
        print("\n1 — Показать прогресс")
        print("2 — Отметить выполненный маркер") 
        print("3 — Рекомендации по развитию")
        print("4 — Сгенерировать портфолио (docs/my_portfolio.md)")
        print("5 — Выход")
        
        choice = input("\nВыберите действие: ").strip()
        
        if choice == "1":
            tracker.show_progress()
        elif choice == "2":
            marker_id = input("Введите ID маркера (например: docker_1_1): ").strip()
            tracker.mark_completed(marker_id)
        elif choice == "3":
            tracker.show_recommendations()
        elif choice == "4":
            try:
                from src.utils.portfolio_gen import generate_portfolio
                generate_portfolio()
            except Exception as e:
                print(f"⚠️ Ошибка генерации: {e}")
        elif choice == "5":
            print("До новых встреч! 🚀")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
