#!/usr/bin/env python3
import json
from pathlib import Path

def generate_portfolio():
    progress_file = Path("src/data/user_progress.json")
    markers_dir = Path("src/data/markers")
    
    if not progress_file.exists():
        print("⚠️ Файл прогресса отсутствует. Сначала отметьте маркеры через CLI.")
        return
    
    try:
        with open(progress_file, 'r', encoding='utf-8') as f:
            progress = json.load(f)
    except Exception as e:
        print(f"⚠️ Ошибка чтения прогресса: {e}")
        return

    all_markers = {}
    for json_path in markers_dir.glob("*.json"):
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                skill_data = json.load(f)
                for level in skill_data.get("levels", {}).values():
                    for marker in level:
                        all_markers[marker["id"]] = marker
        except: pass

    completed = [
        all_markers[mid] for mid in progress.get("completed_markers", [])
        if mid in all_markers
    ]

    if not completed:
        print("ℹ️ Нет выполненных маркеров. Отметьте хотя бы один через CLI.")
        return

    by_skill = {}
    for m in completed:
        skill = m.get("skill_name", "Other")
        by_skill.setdefault(skill, []).append(m)

    lines = [
        "# 🎯 Моё IT-портфолио",
        "",
        "> Сформировано автоматически через [IT Compass](https://github.com/Control39/it-compass)",
        "",
        "## ✅ Подтверждённые навыки",
        ""
    ]

    for skill in sorted(by_skill):
        lines.append(f"### {skill}")
        for m in by_skill[skill]:
            lines.append(f"- ✅ **{m['marker']}**")
            if m.get("validation"):
                lines.append(f"  > 🔍 Валидация: {m['validation']}")
        lines.append("")

    skills_done = {m.get("skill_name", "") for m in completed}
    readiness = {
        "Python": "Python" in skills_done,
        "Docker": "Docker" in skills_done,
        "MLOps": "MLOps" in skills_done,
        "DevOps": "DevOps" in skills_done,
    }

    lines.extend([
        "## 🎯 Готовность к junior-позиции",
        ""
    ])
    for skill, done in readiness.items():
        status = "✅" if done else "🟡"
        lines.append(f"- **{skill}**: {status} {'Готов' if done else 'В процессе'}")
    lines.append("")
    lines.append("> 💡 Совет: прикрепите скриншоты и ссылки на GitHub — это усилит ваш кейс.")

    output_path = Path("docs/my_portfolio.md")
    output_path.parent.mkdir(exist_ok=True)
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        print(f"✅ Портфолио сохранено: {output_path.absolute()}")
    except Exception as e:
        print(f"⚠️ Ошибка записи: {e}")

if __name__ == "__main__":
    generate_portfolio()
