import json
import os
from pathlib import Path

class CareerTracker:
    def __init__(self):
        self.markers_dir = Path("src/data/markers")
        self.progress_file = Path("src/data/user_progress.json")
        self.markers = self._load_all_markers()
        self.progress = self._load_progress()
    
    def _load_all_markers(self):
        """Загрузка всех маркеров из JSON файлов"""
        markers = {}
        for file_path in self.markers_dir.glob("*.json"):
            with open(file_path, 'r', encoding='utf-8') as f:
                skill_data = json.load(f)
                skill_name = skill_data["skill_name"]
                markers[skill_name] = skill_data
        return markers
    
    def _load_progress(self):
        """Загрузка прогресса пользователя"""
        if self.progress_file.exists():
            with open(self.progress_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def _save_progress(self):
        """Сохранение прогресса"""
        with open(self.progress_file, 'w', encoding='utf-8') as f:
            json.dump(self.progress, f, ensure_ascii=False, indent=2)
    
    def show_progress(self):
        """Показать прогресс по всем навыкам"""
        print("\n📊 ВАШ ПРОГРЕСС:")
        print("-" * 40)
        
        for skill_name, skill_data in self.markers.items():
            completed = 0
            total = 0
            
            for level in ["1", "2", "3"]:
                level_markers = skill_data["levels"].get(level, [])
                total += len(level_markers)
                for marker in level_markers:
                    if self.progress.get(marker["id"]):
                        completed += 1
            
            percentage = (completed / total * 100) if total > 0 else 0
            bars = "█" * int(percentage / 5) + "░" * (20 - int(percentage / 5))
            
            print(f"{skill_name:.<20} {bars} {percentage:.0f}% ({completed}/{total})")
    
    def mark_completed(self, marker_id):
        """Отметить маркер как выполненный"""
        self.progress[marker_id] = True
        self._save_progress()
        print(f"✅ Маркер {marker_id} отмечен как выполненный!")
    
    def show_recommendations(self):
        """Показать рекомендации по развитию"""
        print("\n🎯 РЕКОМЕНДАЦИИ:")
        print("-" * 40)
        
        for skill_name, skill_data in self.markers.items():
            # Найти первый невыполненный маркер высокого приоритета
            for level in ["1", "2", "3"]:
                level_markers = skill_data["levels"].get(level, [])
                for marker in level_markers:
                    if not self.progress.get(marker["id"]) and marker.get("priority") == "high":
                        print(f"• {skill_name}: {marker['marker']}")
                        print(f"  📎 Ресурсы: {', '.join(marker.get('resources', []))}")
                        break
