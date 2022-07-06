echo "Making a virtual environment..."
python -m venv pyenv

echo "Pinning your current dependencies..."
source pyenv/Scripts/activate && pip freeze > requirements.txt