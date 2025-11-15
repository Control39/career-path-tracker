# 🧭 Career Path Navigator

**Data-Driven система объективной навигации в IT-карьере через верифицируемые маркеры компетенций**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Alpha-orange.svg)](https://github.com/Control39/career-path-tracker)

## 🚀 Проблема

Субъективные оценки навыков ("знаю Python на 4/5") не отражают реальные возможности специалистов.

## 💡 Решение

**Career Path Navigator** заменяет субъективные оценки на **объективные маркеры** — конкретные, проверяемые действия:

- ❌ **Вместо:** "Оцени свои знания Python от 1 до 5"
- ✅ **Решение:** "Ты написал скрипт для обработки CSV?"

## 🎯 Для кого

| Аудитория | Польза |
|-----------|--------|
| **Новички в IT** | Четкая дорожная карта через конкретные задачи |
| **HR и рекрутеры** | Объективная оценка по верифицируемым компетенциям |
| **EdTech-компании** | Персонализированные траектории на основе реальных требований рынка |

## 🏗 Архитектура

```
career-path-tracker/
├── src/
│   ├── core/tracker.py           # Ядро системы
│   ├── data/markers/             # База объективных маркеров (JSON)
│   │   ├── docker.json
│   │   ├── python.json
│   │   └── ...
│   └── main.py                   # CLI интерфейс
├── Dockerfile                    # Конфигурация Docker
├── .dockerignore                 # Игнорируемые файлы для Docker
└── requirements.txt              # Зависимости Python
```

## 🚀 Быстрый старт

### Способ 1: Клонирование репозитория
```bash
git clone https://github.com/Control39/career-path-tracker.git
cd career-path-tracker
python src/main.py
```

### Способ 2: Запуск через Docker
```bash
docker build -t career-path-navigator .
docker run -it career-path-navigator
```

## 🐳 Docker как пример маркера

Этот проект служит практическим примером для маркера **"Создал Dockerfile для Python-приложения"** (Docker, уровень 1). 

- **Маркер:** `docker_1_1`
- **Валидация:** Dockerfile в репозитории и работающий контейнер
- **Результат:** Вы можете запустить проект в Docker, что подтверждает практическое умение.

## 📊 Что внутри

**Реализованные направления:**
- 🐳 Docker • 🐍 Python • 🤖 MLOps • 🚀 DevOps

**Пример маркера:**
```json
{
  "id": "docker_1_1",
  "marker": "Создал Dockerfile для Python-приложения",
  "validation": "Dockerfile в репозитории + скриншот работающего контейнера",
  "priority": "high",
  "resources": ["https://docs.docker.com/"]
}
```

## 🎮 Использование

После запуска доступны:
- 📈 Просмотр прогресса — визуализация по всем направлениям
- ✅ Отметка выполненных маркеров — трекинг компетенций  
- 🎯 Рекомендации — что изучать дальше

## 🎯 Методология

Маркеры собираются из **проверяемых источников**:
- Вакансии для Junior ([hh.ru](https://hh.ru), [Habr Career](https://career.habr.com))
- Учебные программы ([Coursera](https://coursera.org), [Stepik](https://stepik.org))
- Профессиональные roadmap ([roadmap.sh](https://roadmap.sh))

## 🔮 Планы развития

- [ ] Веб-интерфейс на Streamlit/Flask
- [ ] Интеграция с GitHub API для валидации
- [ ] Автоматический парсинг вакансий
- [ ] Расширение базы маркеров (8+ направлений)

## 🤝 Участие в разработке

Приветствуется участие в разработке:
- Добавление новых направлений
- Улучшение существующих маркеров
- Предложение идей по улучшению методологии

## 📄 Лицензия

MIT License - смотри файл [LICENSE](LICENSE) для деталей.

---

*Система в активной разработке. База маркеров пополняется.*

**Репозиторий:** [https://github.com/Control39/career-path-tracker](https://github.com/Control39/career-path-tracker)
