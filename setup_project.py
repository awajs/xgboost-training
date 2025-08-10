# setup_project.py
import os
from pathlib import Path

# Base directory (current working directory or specify)
base_dir = Path.cwd()  # assumes you're inside xgboost-training
print(f"Setting up project in: {base_dir}")

# Define folders
folders = [
    "data/raw",
    "data/processed",
    "notebooks",
    "src"
]

# Create directories
for folder in folders:
    path = base_dir / folder
    path.mkdir(parents=True, exist_ok=True)
    print(f"Created: {path}")

# Create placeholder files if they don't exist
requirements_path = base_dir / "requirements.txt"
if not requirements_path.exists():
    requirements_path.write_text(
        "xgboost\nscikit-learn\nmatplotlib\nshap\njupyter\n"
    )
    print(f"Created: {requirements_path}")

readme_path = base_dir / "README.md"
if not readme_path.exists():
    readme_path.write_text(
        "# XGBoost Training\n\nSelf-training playground for learning XGBoost.\n"
    )
    print(f"Created: {readme_path}")

src_init = base_dir / "src" / "__init__.py"
if not src_init.exists():
    src_init.write_text("# Source code package\n")
    print(f"Created: {src_init}")

print("✅ Project structure ready!")
