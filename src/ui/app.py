#!/usr/bin/env python3
"""
IT Compass - Streamlit Web Interface for Dashboard Visualization
Методология: © 2025 Ekaterina Kudelya, CC BY-ND 4.0
"""

import streamlit as st
from pathlib import Path
import sys

# Добавляем src в путь для импорта
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from src.core.tracker import CareerTracker
    from src.utils.portfolio_gen import generate_portfolio
except ImportError as e:
    st.error(f"❌ Ошибка импорта модулей: {e}")
    st.error("Убедитесь, что вы находитесь в корневой директории проекта")
    st.stop()

# --- Конфигурация Страницы ---
st.set_page_config(
    page_title="IT Compass Dashboard",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Инициализация Трекера ---
@st.cache_resource
def get_tracker():
    """Кэшируем трекер для производительности."""
    try:
        return CareerTracker()
    except Exception as e:
        st.error(f"❌ Не удалось инициализировать CareerTracker: {e}")
        st.error("Проверьте наличие файлов маркеров в src/data/markers/")
        return None

def render_progress_dashboard():
    """Отображает прогресс в виде дашборда."""
    st.header("🧭 Ваш Карьерный Прогресс: Объективные Маркеры")
    
    if not tracker.markers:
        st.warning("⚠️ База маркеров пуста. Проверьте файлы в src/data/markers/.")
        return
    
    st.markdown("---")
    
    # Общий прогресс
    total_completed = len(tracker.progress.get("completed_markers", []))
    total_markers = sum(
        len(marker) for skill_data in tracker.markers.values()
        for level_markers in skill_data.levels.values()
        for marker in level_markers
    )
    
    if total_markers > 0:
        overall_percentage = (total_completed / total_markers) * 100
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("✅ Выполнено", f"{total_completed}")
        with col2:
            st.metric("🎯 Всего маркеров", f"{total_markers}")
        with col3:
            st.metric("📊 Общий прогресс", f"{overall_percentage:.1f}%")
    
    st.markdown("---")
    
    # Прогресс по навыкам
    st.subheader("📈 Детализация по направлениям")
    
    # Автоматически создаем колонки
    skills = list(tracker.markers.keys())
    if skills:
        cols = st.columns(len(skills))
        
        for i, skill_name in enumerate(skills):
            skill_data = tracker.markers[skill_name]
            completed = 0
            total = 0
            
            for level_markers in skill_data.levels.values():
                total += len(level_markers)
                for marker in level_markers:
                    if marker.id in tracker.progress["completed_markers"]:
                        completed += 1
            
            with cols[i]:
                if total > 0:
                    percentage = (completed / total) * 100
                    st.markdown(f"**{skill_name}**")
                    st.progress(percentage / 100)
                    st.caption(f"{percentage:.0f}% ({completed}/{total})")
                else:
                    st.info(f"**{skill_name}**\n\n(нет маркеров)")
    
    st.markdown("---")
    
    # Быстрые действия
    st.subheader("⚡ Быстрые действия")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📄 Сгенерировать портфолио", use_container_width=True):
            try:
                success = generate_portfolio()
                if success:
                    st.balloons()
                    st.success("✅ Портфолио обновлено! Файл: `docs/my_portfolio.md`")
                else:
                    st.error("❌ Не удалось создать портфолио")
            except Exception as e:
                st.error(f"❌ Ошибка: {e}")
    
    with col2:
        if st.button("🎯 Показать рекомендации", use_container_width=True):
            st.info("Рекомендации по развитию (high priority):")
            high_priority = []
            for skill_name, skill_data in tracker.markers.items():
                for level_markers in skill_data.levels.values():
                    for marker in level_markers:
                        if (marker.id not in tracker.progress["completed_markers"] 
                            and marker.priority == "high"):
                            high_priority.append((skill_name, marker))
            
            if high_priority:
                for skill_name, marker in high_priority[:5]:  # Показываем первые 5
                    st.markdown(f"• **{skill_name}**: {marker.marker}")
            else:
                st.success("🎉 Все high-priority маркеры выполнены!")

def render_documentation():
    """Отображает документацию проекта."""
    st.header("📚 Документация IT Compass")
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Методология")
        st.markdown("""
        - [🧠 Методология SMART](./docs/METHODOLOGY.md)
        - [💭 Психологическая поддержка](./docs/PSYCHOLOGICAL_SUPPORT.md)
        - [🚀 Готовность к карьере](./docs/CAREER_READINESS.md)
        """)
        
        if st.button("📖 Открыть методологию", use_container_width=True):
            try:
                with open("docs/METHODOLOGY.md", "r", encoding="utf-8") as f:
                    st.markdown(f.read())
            except:
                st.warning("Файл METHODOLOGY.md не найден")
    
    with col2:
        st.subheader("🛠 Утилиты")
        st.markdown("""
        - [🤝 Как внести вклад](./docs/CONTRIBUTING.md)
        - [📄 Текущее портфолио](./docs/my_portfolio.md)
        - [⚙️ Настройки проекта](./docs/SETUP.md)
        """)
        
        if st.button("📋 Посмотреть портфолио", use_container_width=True):
            try:
                with open("docs/my_portfolio.md", "r", encoding="utf-8") as f:
                    st.markdown(f.read())
            except:
                st.warning("Портфолио ещё не сгенерировано")

def render_strategy():
    """Отображает стратегическую информацию."""
    st.header("🚀 Стратегия выхода на рынок")
    
    st.info("""
    **Ваша цель** — не просто найти работу, а доказать статус **«Когнитивного Архитектора»** — 
    специалиста, который проектирует системы мышления и оценки в IT.
    """)
    
    st.markdown("---")
    
    tab1, tab2, tab3 = st.tabs(["🎤 Питч", "📱 LinkedIn", "🔮 Планы"])
    
    with tab1:
        st.subheader("Питч для собеседования")
        st.code("""
«Я разработала IT Compass — систему объективной оценки навыков 
на основе верифицируемых артефактов. 

Вместо субъективных оценок вроде "знаю Python на 4/5" 
я показываю конкретные маркеры: "написал скрипт, собрал в Docker, 
выложил на GitHub".

Вот моё портфолио, подтверждающее X% покрытия рыночных требований 
по ключевым направлениям: Python, Docker, MLOps, DevOps...»
        """, language="markdown")
        
        st.markdown("**Ключевые тезисы:**")
        st.markdown("✅ Объективность вместо субъективности  ")
        st.markdown("✅ Верифицируемые артефакты  ")
        st.markdown("✅ Соответствие рыночным требованиям  ")
    
    with tab2:
        st.subheader("Публикация в LinkedIn")
        st.warning("Используйте готовый шаблон для продвижения проекта:")
        
        if st.button("📋 Показать шаблон поста"):
            st.markdown("""
**🎯 Я создала IT Compass — систему, которая заменяет "знаю на 4/5" на факты**

После полугода обучения многие IT-специалисты спрашивают: 
"Хватит ли мне знаний для собеседования?"

Проблема в субъективных оценках. Работодатели хотят артефакты, а не самооценку.

**Решение:** IT Compass — open-source система объективных маркеров:
- ✅ Вместо "знаю Python" → "написал скрипт для CSV и выложил на GitHub"
- ✅ Вместо "умею в Docker" → "создал Dockerfile + запустил контейнер"
- ✅ Вместо "разбираюсь в MLOps" → "настроил логирование в MLflow"

Каждый маркер — конкретное, проверяемое действие с SMART-критериями.

🚀 Проект уже включает:
- CLI-интерфейс с прогрессом и рекомендациями
- Генератор портфолио для резюме
- Docker-валидацию навыков
- 8 направлений развития (Python, Docker, MLOps, DevOps, Git, Linux, BA, QA)

**Для кого:**
- Новички: видят реальный прогресс к собеседованию
- HR/тимлиды: объективно оценивают кандидатов
- EdTech: создают релевантные траектории

🔗 GitHub: [ссылка на репозиторий]
🧠 Методология: © Ekaterina Kudelya, CC BY-ND 4.0

#IT #Career #Development #Python #Docker #MLOps #DevOps #OpenSource
            """)
    
    with tab3:
        st.subheader("Следующие шаги развития")
        st.markdown("""
        ### 🔄 В разработке:
        - [ ] Веб-интерфейс (Streamlit) ← **мы здесь!**
        - [ ] Интеграция GitHub API
        - [ ] Парсинг вакансий в реальном времени
        
        ### 🎯 Планируется:
        - [ ] Новые направления: Frontend, Data Engineering
        - [ ] Система менторства
        - [ ] Корпоративная версия
        """)
        
        st.success("""
        **Текущий фокус:** Завершение MVP Streamlit-интерфейса 
        для демонстрации на собеседованиях.
        """)

def main():
    """Главная функция приложения."""
    st.sidebar.title("🧭 IT Compass")
    st.sidebar.markdown("Объективная карта IT-роста")
    st.sidebar.markdown("---")
    
    # Навигация
    menu_option = st.sidebar.selectbox(
        "Навигация",
        ["📊 Прогресс", "📚 Документация", "🚀 Стратегия"],
        index=0
    )
    
    # Информация о проекте
    st.sidebar.markdown("---")
    st.sidebar.markdown("### ℹ️ О проекте")
    st.sidebar.markdown("Методология: © 2025 Ekaterina Kudelya  ")
    st.sidebar.markdown("Лицензия: CC BY-ND 4.0  ")
    st.sidebar.markdown("Версия: 1.0.0")
    
    # Быстрые действия в сайдбаре
    st.sidebar.markdown("---")
    st.sidebar.markdown("### ⚡ Быстрые действия")
    
    if st.sidebar.button("🔄 Обновить данные", use_container_width=True):
        st.rerun()
    
    # Отображение выбранной страницы
    if menu_option == "📊 Прогресс":
        render_progress_dashboard()
    elif menu_option == "📚 Документация":
        render_documentation()
    elif menu_option == "🚀 Стратегия":
        render_strategy()

# Инициализация трекера
tracker = get_tracker()
if tracker is None:
    st.stop()

if __name__ == "__main__":
    main()
```
