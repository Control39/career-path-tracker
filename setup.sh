#!/bin/bash
# IT Compass - Automated Setup Script
set -e
echo "🧭 IT Compass - начата установка..."
# Проверка Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 не установлен. Установите: https://python.org"
    exit 1
fi
# Создание виртуального окружения
echo "🐍 Создание виртуального окружения..."
python3 -m venv compass_venv
source compass_venv/bin/activate
# Установка зависимостей
echo "📦 Установка зависимостей..."
pip install -r requirements.txt
# Создание структуры данных
echo "📁 Создание структуры проекта..."
mkdir -p src/data/markers
mkdir -p docs
# Базовые маркеры Python со SMART-критериями
cat > src/data/markers/python.json << EOF
{
  "skill_name": "Python",
  "description": "Программирование на Python",
  "levels": {
    "1": [
      {
        "id": "python_1_1",
        "marker": "Написал скрипт для обработки CSV-файла (>100 строк)",
        "validation": "Скрипт выложен на GitHub",
        "priority": "high",
        "resources": ["https://docs.python.org/3/"],
        "smart_criteria": {
          "specific": "Написать скрипт для обработки CSV-файла с реальными данными",
          "measurable": "Скрипт обрабатывает более 100 строк данных",
          "achievable": "Задача уровня Junior, выполнимая за 2-3 часа",
          "relevant": "Требуется в 85% вакансий Junior Python разработчика",
          "time_bound": "Выполнение за 2-3 часа практики"
        }
      }
    ]
  }
}
EOF
# Файл прогресса с демо-данными
cat > src/data/user_progress.json << EOF
{
  "completed_markers": ["python_1_1", "docker_1_1", "mlops_1_1", "devops_1_1"],
  "in_progress_markers": []
}
EOF
echo "✅ Установка завершена!"
echo ""
echo "🚀 Запуск:"
echo "   source compass_venv/bin/activate"
echo "   python src/main.py"
echo ""
echo "📚 Сгенерируйте первое портфолио:"
echo "   python src/utils/portfolio_gen.py"
echo ""
echo "🧭 Добро пожаловать в IT Compass!"
