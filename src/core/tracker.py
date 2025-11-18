import json
from pathlib import Path

class CareerTracker:
    def __init__(self):
        self.markers_dir = Path("src/data/markers")
        self.progress_file = Path("src/data/user_progress.json")
        self.markers = self._load_all_markers()
        self.progress = self._load_progress()
    
    def _load_all_markers(self):
        markers = {}
        for file_path in self.markers_dir.glob("*.json"):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    skill_data = json.load(f)
                    skill_name = skill_data.get("skill_name", file_path.stem.capitalize())
                    markers[skill_name] = skill_data
            except: pass
        return markers
    
    def _load_progress(self):
        if self.progress_file.exists():
            try:
                with open(self.progress_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if isinstance(data, dict):
                        return {
                            "completed_markers": data.get("completed_markers", []),
                            "in_progress_markers": data.get("in_progress_markers", [])
                        }
            except: pass
        return {"completed_markers": [], "in_progress_markers": []}
    
    def _save_progress(self):
        with open(self.progress_file, 'w', encoding='utf-8') as f:
            json.dump(self.progress, f, ensure_ascii=False, indent=2)
    
    def show_progress(self):
        print("\n📊 ВАШ ПРОГРЕСС:")
        print("-" * 50)
        if not self.markers:
            print("⚠️ Нет загруженных маркеров")
            return
        for skill_name, skill_data in self.markers.items():
            completed = 0
            total = 0
            for level in skill_data.get("levels", {}).values():
                total += len(level)
                for marker in level:
                    if marker["id"] in self.progress["completed_markers"]:
                        completed += 1
            if total == 0: continue
            percentage = (completed / total * 100)
            bars = "█" * int(percentage // 5) + "░" * (20 - int(percentage // 5))
            print(f"{skill_name:.<20} {bars} {percentage:5.1f}% ({completed}/{total})")

    def mark_completed(self, marker_id):
        if marker_id not in self.progress["completed_markers"]:
            self.progress["completed_markers"].append(marker_id)
            if marker_id in self.progress["in_progress_markers"]:
                self.progress["in_progress_markers"].remove(marker_id)
            self._save_progress()
            print(f"✅ Маркер {marker_id} отмечен как выполненный!")
        else:
            print(f"ℹ️ Маркер {marker_id} уже выполнен.")

    def show_recommendations(self):
        print("\n🎯 РЕКОМЕНДАЦИИ (high priority):")
        print("-" * 50)
        found = False
        for skill_name, skill_data in self.markers.items():
            for level in skill_data.get("levels", {}).values():
                for marker in level:
                    mid = marker["id"]
                    if (mid not in self.progress["completed_markers"] and 
                        marker.get("priority") == "high"):
                        print(f"• {skill_name}: {marker['marker']}")
                        if marker.get("resources"):
                            print(f"  📎 {', '.join(marker['resources'])}")
                        found = True
                        break
                if found: break
            if found: break
        if not found:
            print("🎉 Все high-priority маркеры выполнены!")
