# Learning Analysis
 This is trail for pupil's performance analysis
IGCSE Assessment Tool
A lightweight command-line and notebook tool for Cambridge IGCSE teachers to diagnose student weaknesses in multiple-choice tests and automatically generate personalized practice papers.
Features

📊 Multi-stream Data Ingestion: Combines MCQ results, assignment marks, and participation scores
🔍 Intelligent Weakness Detection: Uses item response analysis to identify knowledge gaps
🎯 Topic Mapping: Maps weaknesses to Cambridge IGCSE syllabus topics (e.g., Math 0580)
📝 Personalized Papers: Automatically assembles custom practice papers from past CIE questions
🤖 AI Integration (Optional): Uses ChatGPT for fine-grained topic tagging and explanations
📈 Visual Reports: Generates heat maps and teacher summaries

Quick Start
Installation
bash# Clone the repository
git clone https://github.com/yourusername/igcse-assessment-tool.git
cd igcse-assessment-tool

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
Basic Usage
Command Line
bash# Generate sample data for testing
igcse-assess generate-samples --output data/

# Run full analysis on a class
igcse-assess analyze --data-dir data/ --output-dir output/

# Generate personalized papers for all students
igcse-assess generate-papers --data-dir data/ --max-questions 15

# Create teacher report with visualizations
igcse-assess report --data-dir data/ --format pdf
Python API
pythonfrom pathlib import Path
from src.ingestion import DataIngestion
from src.diagnostics import WeaknessAnalyzer
from src.paper_generator import PaperGenerator

# Load data
ingestion = DataIngestion(Path("data/"))
class_data = ingestion.merge_all_data()

# Analyze weaknesses
analyzer = WeaknessAnalyzer(class_data)
weakness_profiles = analyzer.identify_weaknesses()

# Generate personalized papers
generator = PaperGenerator(question_bank_path="data/past_questions.json")
for student_id, profile in weakness_profiles.items():
    paper = generator.create_paper(student_id, profile, max_questions=15)
    paper.save(f"output/papers/{student_id}_practice.pdf")
Jupyter Notebook
See demo.ipynb for a complete walkthrough of the analysis pipeline.
Data Format
MCQ Results (mcq_results.csv)
csvstudent_id,q1,q2,q3,...,q50,total_score
S001,1,0,1,...,0,35
S002,1,1,0,...,1,42
Assignment Marks (assignments.csv)
csvstudent_id,assignment_1,assignment_2,assignment_3,total
S001,85.5,78.0,92.5,256.0
S002,91.0,88.5,87.0,266.5
Participation Scores (participation.csv)
csvstudent_id,week_1,week_2,...,week_12,average
S001,4,5,3,...,4,4.2
S002,5,5,4,...,5,4.8
Project Structure
igcse-assessment-tool/
├── src/
│   ├── ingestion.py       # Data loading and validation
│   ├── diagnostics.py     # Weakness analysis algorithms
│   ├── mapping.py         # Topic mapping to syllabus
│   ├── paper_generator.py # Custom paper assembly
│   ├── visualization.py   # Charts and reports
│   └── cli.py            # Command-line interface
├── data/                  # Sample data and question banks
├── tests/                 # Unit and integration tests
├── output/               # Generated reports and papers
└── demo.ipynb           # Interactive demonstration
API Integration (Optional)
To enable ChatGPT integration for enhanced topic analysis:

Create a .env file in the project root:

envOPENAI_API_KEY=your_api_key_here

Install API dependencies:

bashpip install -e ".[api]