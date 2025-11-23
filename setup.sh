#!/bin/bash

# IT Compass - Automated Setup Script
set -e

echo "🧭 IT Compass - начата установка..."

# Проверка Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 не установлен. Установите: https://python.org"
    exit 1
fi

# Проверка версии Python
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "🐍 Найден Python $python_version"

# Создание виртуального окружения
echo "📦 Создание виртуального окружения..."
python3 -m venv compass_venv
source compass_venv/bin/activate

# Обновление pip
echo "🔄 Обновление pip..."
pip install --upgrade pip

# Установка зависимостей
echo "📚 Установка зависимостей..."
pip install -r requirements.txt

# Создание структуры данных
echo "📁 Создание структуры проекта..."
mkdir -p src/data/markers
mkdir -p docs
mkdir -p tests
mkdir -p examples

# Создание базового файла прогресса
cat > src/data/user_progress.json << 'EOF'
{
  "completed_markers": [],
  "in_progress_markers": []
}
EOF

echo "✅ Установка завершена!"
echo ""
echo "🚀 Запуск:"
echo "  source compass_venv/bin/activate"
echo "  python src/main.py"
echo ""
echo "📚 Сгенерируйте первое портфолио:"
echo "  python src/utils/portfolio_gen.py"
echo ""
echo "🧭 Добро пожаловать в IT Compass!"
echo ""
echo "📄 Методология: © 2025 Ekaterina Kudelya, CC BY-ND 4.0"
echo "💻 Код: MIT License"
