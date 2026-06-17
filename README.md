# Study Habit Analyzer

A Streamlit-based study tracking and analysis app that helps students record daily study sessions, review subject-wise study time, and understand productivity using basic study metrics.

## Project Overview

This project allows users to add study entries through a Streamlit sidebar and analyze study performance from the saved data. The app stores records in a CSV file and uses Pandas and Plotly to show metrics, charts, insights, and a simple recommendation.

## Tools and Libraries Used

- Python
- Streamlit
- Pandas
- Plotly

## Project Files

```text
Study-habit-analyzer/
├── app.py
├── analyzer.py
├── data_manager.py
├── requirements.txt
├── study_log.csv
└── .devcontainer/
    └── devcontainer.json
```

## Features

- Add study entries with date, subject, study hours, and focus level.
- Store study records in `study_log.csv`.
- Display the complete study log inside the Streamlit app.
- Calculate total study hours, average study hours, consistency, and productivity score.
- Show date-wise study hours by subject using a grouped bar chart.
- Show focus level vs study hours using a scatter chart.
- Show subject-wise total study time.
- Highlight the most studied subject.
- Show a recommendation based on the productivity score.

## Data Columns

The project uses `study_log.csv` with the following columns:

| Column | Description |
|---|---|
| `date` | Date of the study session |
| `subject` | Subject studied |
| `hours` | Number of study hours |
| `focus` | Focus level between 1 and 5 |

## Productivity Score Logic

The productivity score is calculated in `analyzer.py` using:

```python
score = (avg_hours * 10) + (avg_focus * 10) - (consistency * 5 if consistency else 0)
```

The final score is rounded and limited between 0 and 100.

## Recommendation Logic

The app shows a recommendation based on the productivity score:

- Score below 40: Increase study time and consistency.
- Score below 70: Improve focus.
- Score 70 or above: Maintain the current routine.

## How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/1ankitrawat1/Study-habit-analyzer.git
```

2. Open the project folder:

```bash
cd Study-habit-analyzer
```

3. Install required libraries:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:

```bash
streamlit run app.py
```

## Requirements

The required Python libraries are listed in `requirements.txt`:

```text
streamlit
pandas
plotly
```

## Project Workflow

1. User enters study details in the sidebar.
2. The app saves the entry in `study_log.csv`.
3. The saved data is loaded using `data_manager.py`.
4. Study metrics are calculated using `analyzer.py`.
5. The dashboard in `app.py` displays metrics, charts, insights, and recommendations.

## Live Demo

View the live Streamlit app here: [Study Habit Analyzer](https://study-habit-analyzer-asr.streamlit.app/)
