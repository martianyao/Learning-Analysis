#!/usr/bin/env python3
"""
IGCSE Assessment Tool - Project Setup Script
Run this script directly in VS Code to create the complete project structure
"""

import os
import sys
import json
from pathlib import Path
import subprocess

def create_project_structure():
    """Create the complete project structure for IGCSE Assessment Tool"""
    
    # Get current working directory
    current_dir = Path.cwd()
    print(f"Current directory: {current_dir}")
    
    # Ask user where to create the project
    project_name = "igcse-assessment-tool"
    response = input(f"\nCreate project '{project_name}' in current directory? (y/n): ").lower()
    
    if response != 'y':
        custom_path = input("Enter project path (e.g., ~/Desktop/): ").strip()
        if custom_path:
            base_dir = Path(custom_path).expanduser()
            if not base_dir.exists():
                print(f"Path {base_dir} doesn't exist, creating...")
                base_dir.mkdir(parents=True, exist_ok=True)
        else:
            base_dir = current_dir
    else:
        base_dir = current_dir
    
    # Create project root directory
    project_dir = base_dir / project_name
    
    if project_dir.exists():
        response = input(f"\nDirectory {project_dir} already exists. Overwrite? (y/n): ").lower()
        if response != 'y':
            print("Project creation cancelled.")
            return
        else:
            # Remove existing directory (use with caution)
            import shutil
            shutil.rmtree(project_dir)
    
    print(f"\nCreating project directory: {project_dir}")
    project_dir.mkdir(exist_ok=True)
    
    # Change to project directory
    os.chdir(project_dir)
    print(f"Changed to: {project_dir}")
    
    # Create directory structure
    directories = [
        "src",
        "tests", 
        "data",
        "output/student_reports",
        ".vscode"  # VS Code configuration directory
    ]
    
    for dir_path in directories:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        print(f"✓ Created directory: {dir_path}")
    
    # Create __init__.py files
    init_files = ["src/__init__.py", "tests/__init__.py"]
    for init_file in init_files:
        Path(init_file).touch()
        print(f"✓ Created file: {init_file}")
    
    # Initialize Git repository
    try:
        subprocess.run(["git", "init"], check=True, capture_output=True)
        print("✓ Initialized Git repository")
    except subprocess.CalledProcessError:
        print("⚠️  Git initialization failed, please ensure Git is installed")
    except FileNotFoundError:
        print("⚠️  Git command not found, please install Git first")
    
    # Create .gitignore
    create_gitignore()
    
    # Create requirements.txt
    create_requirements()
    
    # Create README.md
    create_readme()
    
    # Create VS Code configuration
    create_vscode_config()
    
    # Create sample data files
    create_sample_data_structure()
    
    print(f"\n✅ Project structure created successfully!")
    print(f"Project location: {project_dir}")
    print("\nNext steps:")
    print("1. Open project in VS Code: code .")
    print("2. Create virtual environment: python3 -m venv venv")
    print("3. Activate virtual environment: source venv/bin/activate  (Mac/Linux)")
    print("                              or: venv\\Scripts\\activate  (Windows)")
    print("4. Install dependencies: pip install -r requirements.txt")

def create_gitignore():
    """Create .gitignore file"""
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# IDE
.idea/
*.swp
*.swo
.DS_Store

# Project specific
.env
*.log
output/*.pdf
output/*.png
data/real_*  # Real data files

# Jupyter
.ipynb_checkpoints/
*.ipynb_checkpoints

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/

# Distribution
build/
dist/
*.egg-info/
"""
    
    with open(".gitignore", "w") as f:
        f.write(gitignore_content)
    print("✓ Created file: .gitignore")

def create_requirements():
    """Create requirements.txt file"""
    requirements_content = """# Core dependencies
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0

# CLI and utilities
click>=8.1.0
python-dotenv>=1.0.0

# Testing
pytest>=7.4.0
pytest-cov>=4.1.0

# Documentation
jupyter>=1.0.0
nbconvert>=7.0.0

# PDF generation
reportlab>=4.0.0

# Data validation
pydantic>=2.0.0

# Type checking (optional)
mypy>=1.5.0
"""
    
    with open("requirements.txt", "w") as f:
        f.write(requirements_content)
    print("✓ Created file: requirements.txt")

def create_readme():
    """Create README.md file"""
    readme_content = """# IGCSE Assessment Tool

A lightweight assessment tool for Cambridge IGCSE teachers to diagnose student weaknesses in multiple-choice tests and automatically generate personalized practice papers.

## Features

- 📊 Multi-stream data integration: Combines MCQ results, assignment marks, and classroom participation
- 🔍 Intelligent weakness detection: Uses item response analysis to identify knowledge gaps  
- 🎯 Topic mapping: Maps weaknesses to Cambridge IGCSE syllabus topics
- 📝 Personalized papers: Automatically assembles custom practice papers from past CIE questions
- 📈 Visual reports: Generates heatmaps and teacher summaries

## Quick Start

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# or
venv\\Scripts\\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run example
python src/ingestion.py
```

## Project Structure

```
igcse-assessment-tool/
├── src/               # Source code
├── tests/             # Test files
├── data/              # Sample data
├── output/            # Generated reports
└── demo.ipynb         # Demo notebook
```
"""
    
    with open("README.md", "w") as f:
        f.write(readme_content)
    print("✓ Created file: README.md")

def create_vscode_config():
    """Create VS Code configuration files"""
    # Create settings.json
    settings = {
        "python.linting.enabled": True,
        "python.linting.pylintEnabled": False,
        "python.linting.flake8Enabled": True,
        "python.formatting.provider": "black",
        "python.testing.pytestEnabled": True,
        "python.testing.unittestEnabled": False,
        "editor.formatOnSave": True,
        "files.exclude": {
            "**/__pycache__": True,
            "**/*.pyc": True
        }
    }
    
    with open(".vscode/settings.json", "w") as f:
        json.dump(settings, f, indent=4)
    print("✓ Created file: .vscode/settings.json")
    
    # Create launch.json for debugging
    launch = {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Current File",
                "type": "python",
                "request": "launch",
                "program": "${file}",
                "console": "integratedTerminal"
            },
            {
                "name": "Python: Run Tests",
                "type": "python",
                "request": "launch",
                "module": "pytest",
                "args": ["-v"],
                "console": "integratedTerminal"
            }
        ]
    }
    
    with open(".vscode/launch.json", "w") as f:
        json.dump(launch, f, indent=4)
    print("✓ Created file: .vscode/launch.json")

def create_sample_data_structure():
    """Create sample data file structure"""
    # Create syllabus topics file
    syllabus = {
        "subject": "Mathematics",
        "code": "0580",
        "topics": {
            "1": {
                "name": "Number",
                "subtopics": ["Integers", "Fractions", "Decimals", "Percentages"]
            },
            "2": {
                "name": "Algebra & Graphs", 
                "subtopics": ["Linear equations", "Quadratics", "Inequalities", "Graphs"]
            },
            "3": {
                "name": "Coordinate Geometry",
                "subtopics": ["Distance", "Midpoint", "Gradient", "Equations of lines"]
            },
            "4": {
                "name": "Geometry",
                "subtopics": ["Angles", "Triangles", "Quadrilaterals", "Circles"]
            }
        }
    }
    
    with open("data/syllabus_topics.json", "w") as f:
        json.dump(syllabus, f, indent=4)
    print("✓ Created file: data/syllabus_topics.json")
    
    # Create empty CSV templates
    csv_templates = {
        "data/sample_mcq_results.csv": "student_id,q1,q2,q3,q4,q5,total_score\n",
        "data/sample_assignments.csv": "student_id,assignment_1,assignment_2,assignment_3,total\n",
        "data/sample_participation.csv": "student_id,week_1,week_2,week_3,week_4,average\n"
    }
    
    for filepath, content in csv_templates.items():
        with open(filepath, "w") as f:
            f.write(content)
        print(f"✓ Created file: {filepath}")

if __name__ == "__main__":
    print("="*50)
    print("IGCSE Assessment Tool - Project Setup Script")
    print("="*50)
    
    try:
        create_project_structure()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled.")
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        