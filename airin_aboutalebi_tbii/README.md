# Reflect Rhythm - Habit Log and Mood Tracker

Reflect Rhythm is an application designed to help you grow to become the best version of yourself. This project is built using Tkinter in Python and provides a user-friendly interface to manage your daily routines and reflections.

## Features

- **Habit Log**: Be true to yourself and track your good and bad habits.
- **Diary**: Save and view diary entries to remember your journey.
- **Progress Visualization**: See your progress displayed in graphs.
- **Mood Tracker**:TRack your mood daily with a customisable color coded calendar.
- **Motivational Resources**: Access links to motivational music, quotes, and articles for building better habits.

## Installation

### Prerequisites

- Python 3.9.0
- Virtual Environment 

### Steps

1. **Clone the repository**:
    ```sh
    git clone https://github.com/stray-cat-00/airin-aboutalebi-tb-ii.git
    cd airin_aboutalebi_tbii
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```sh
    python3 app.py
    ```

## Project Structure

airin_aboutalebi_tbii/
├── diary_entries/
│ └── diary_entries.txt
├── good_habits.txt
└── bad_habits.txt
├── venv/ (This will be created after setting up the virtual environment)
├── README.md
├── requirements.txt
├── .gitignore
└── app.py


### Description of Files

- **app.py**: The main application code.
- **diary_entries/**: Directory containing the diary entries file.
- **bad_habits/good_habits**: Directory containing the habit tracking files.
- **README.md**: Instructions and information about the project.
- **requirements.txt**: List of dependencies required for the project.
- **.gitignore**: Specifies files and directories to be ignored by Git.

## Usage

### Habit Log

- **Log Habits**: Track your good and bad habits with a simple interface.
- **Increment Counts**: Easily increment the counts of your habits.
- **Motivational Messages**: Receive motivational messages based on your habit tracking.

### Diary

- **Save Entries**: Write and save diary entries.
- **View Entries**: View and search through your saved diary entries.

### Progress Visualization

- **Graphs**: Visualize your habit progress with graphs.

### Mood Tracker

- **Calendar View**: Track your mood on a calendar.
- **Custom Colors**: Assign custom colors to different dates to represent your mood.

### Motivational Resources

- **Links**: Access links to motivational music, quotes, and articles for building better habits.
