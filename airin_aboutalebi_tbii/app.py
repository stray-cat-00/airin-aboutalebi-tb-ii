import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, simpledialog
from datetime import datetime, timedelta
import os
import webbrowser
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Initialize the main application window
root = tk.Tk()
root.title("Habit Log")
root.geometry("800x600")
root.configure(bg="#E6E6FA")

# Global variables for habit tracking and diary entries
good_habits = {}
bad_habits = {}
diary_entries = {}
message_label = None

# Global variables for calendar functionality
calendar_frame = None
date_colors = {}
year, month = datetime.now().year, datetime.now().month


# Clearing all widgets from the main window
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


# Loading diary entries from a file into the diary_entries dictionary
def load_diary_entries():
    global diary_entries
    if os.path.exists("diary_entries/diary_entries.txt"):
        with open("diary_entries/diary_entries.txt", "r") as file:
            for line in file:
                if ':' in line:
                    entry_date, entry = line.strip().split(":", 1)
                    diary_entries[entry_date] = entry
                else:
                    print(f"Skipping invalid entry: {line.strip()}")


# Saving a diary entry to a file
def save_diary_entries(entry_date, diary_entry):
    if not os.path.exists("diary_entries"):
        os.makedirs("diary_entries")
    with open(os.path.join("diary_entries", "diary_entries.txt"), "a") as file:
        file.write(f"{entry_date}:{diary_entry}\n")


# Displaying the main page with navigation buttons
def show_main_page():
    clear_window()
    top_frame = tk.Frame(root, bg="#E6E6FA")
    top_frame.pack(side=tk.TOP, anchor='ne', pady=10, padx=10)

    # Buttons to open external motivational resources
    tk.Button(top_frame, text="Music for Motivation!",
              command=lambda: webbrowser.open("https://music.apple.com/hk/playlist/wake-me-up/pl.c79a0c8eac46444ea8058d68008ba2d4?l=en-GB"), width=30, bg="#9376cc",
              fg="black").pack(side=tk.TOP, pady=5)
    tk.Button(top_frame, text="Quotes for Motivation!",
              command=lambda: webbrowser.open("https://pin.it/15wHnxhOo"), width=30, bg="#9376cc",
              fg="black").pack(side=tk.TOP, pady=5)
    tk.Button(top_frame, text="Better Habits!", command=show_betterbits_page, width=30, bg="#9376cc", fg="black").pack(
        side=tk.TOP, pady=5)

    # App Title
    tk.Label(root, text="Reflect Rhythm", font=("Georgia", 36), bg="#E6E6FA",
             fg="black").pack(pady=5)

    # Main welcome message (headline)
    tk.Label(root, text="Welcome to Reflect Rhythm where you can make all your dreams come true!", font=("Georgia", 24), bg="#E6E6FA",
             fg="black").pack(pady=5)

    # Welcome message no.2 (subtitle)
    tk.Label(root, text="... & find delight in pushing your rock up your hill...", font=("Georgia", 16), bg="#E6E6FA",
             fg="black").pack(pady=3)


    # Main navigation buttons...
    button_frame = tk.Frame(root, bg="#E6E6FA")
    button_frame.pack(pady=20)

    tk.Button(button_frame, text="Bit Log", command=show_log_page, width=15, bg="#9376cc", fg="black").pack(side=tk.LEFT,
                                                                                                        padx=10)
    tk.Button(button_frame, text="Bit Progress", command=show_progress_page, width=15, bg="#9376cc", fg="black").pack(
        side=tk.LEFT, padx=10)
    tk.Button(button_frame, text="Mood Diary", command=show_diary_page, width=15, bg="#9376cc", fg="black").pack(
        side=tk.LEFT, padx=10)
    tk.Button(button_frame, text="Mood Tracker", command=show_calendar, width=15, bg="#9376cc", fg="black").pack(
        side=tk.LEFT, padx=10)


# Better Habits page with links to resources
def show_betterbits_page():
    clear_window()

    # Creating a frame to hold the content
    container = tk.Frame(root, bg="#E6E6FA")
    container.pack(fill=tk.BOTH, expand=True)

    # Creating a canvas to allow scrolling
    canvas = tk.Canvas(container, bg="#E6E6FA")
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#E6E6FA")
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Title label
    tk.Label(scrollable_frame, text="BetterBits", font=("Arial", 24), bg="#E6E6FA", fg="black").pack(pady=20)

    # Links
    links = [
        ("Better Habits for Better Life!", lambda: webbrowser.open("https://www.thesimplicityhabit.com/15-good-habits-to-have-in-your-life/")),
        ("Better Habits for Better Mental Health!", lambda: webbrowser.open("https://www.healthline.com/health/mental-health/habits-to-improve-mental-health#connect-with-friends")),
        ("Better Habits for Better Studying!", lambda: webbrowser.open("https://summer.harvard.edu/blog/top-10-study-tips-to-study-like-a-harvard-student/")),
        ("Better Habits for Healthier Eating!", lambda: webbrowser.open("https://www.nhs.uk/live-well/eat-well/how-to-eat-a-balanced-diet/eight-tips-for-healthy-eating/")),
        ("Better Habits for Healthier Skin!", lambda: webbrowser.open("https://www.revivalabs.com/10-daily-habits-for-achieving-great-skin/")),
        ("Better Habits for Better Self Confidence!", lambda: webbrowser.open("https://www.laurensauder.com/journal/the-best-habits-to-practice-to-improve-self-confidence")),
        ("Better Habits for More Self Love!", lambda: webbrowser.open("https://www.healthline.com/health/13-self-love-habits-every-woman-needs-to-have")),
        ("Better Habits to Fight Procrastination!", lambda: webbrowser.open("https://www.mindtools.com/a5plzk8/how-to-stop-procrastinating")),
        ("Back to Main Page", show_main_page)
    ]

    # Creating and packing each button
    for text, command in links:
        button = tk.Button(scrollable_frame, text=text, command=command, bg="#9376cc", fg="black")
        button.pack(pady=5, padx=20, anchor="center")


# Clearing the window
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()
######End of Better Habits Button...


# Displaying the Habit Log page with options for good and bad habits
def show_log_page():
    clear_window()
    tk.Label(root, text="Habit Log", font=("Arial", 24), bg="#E6E6FA").pack(pady=20)

    button_frame = tk.Frame(root, bg="#E6E6FA")
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Good Habits", command=show_good_habits_page, width=15, bg="#9376cc", fg="black").pack(
        side=tk.LEFT, padx=10)
    tk.Button(button_frame, text="Bad Habits", command=show_bad_habits_page, width=15, bg="#9376cc", fg="black").pack(
        side=tk.LEFT, padx=10)
    tk.Button(button_frame, text="Back", command=show_main_page, width=15, bg="#9376cc", fg="black").pack(pady=20)


# Displaying the good habits page
def show_good_habits_page():
    show_habits_page("Good Habits", good_habits, add_good_habit, increment_good_habit)


# Displaying the bad habits page
def show_bad_habits_page():
    show_habits_page("Bad Habits", bad_habits, add_bad_habit, increment_bad_habit)


# Displaying habits (either good or bad)
def show_habits_page(title, habits, add_habit_func, increment_habit_func):
    clear_window()
    container = tk.Frame(root, bg="#E6E6FA")
    container.pack(fill=tk.BOTH, expand=True)

    # Making Page Scrollable
    canvas = tk.Canvas(container, bg="#E6E6FA")
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#E6E6FA")

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Title label
    tk.Label(scrollable_frame, text=title, font=("Arial", 24), bg="#E6E6FA").pack(pady=20)

    # Input field & button to add a new habit
    habit_name_var = tk.StringVar()
    tk.Label(scrollable_frame, text=f"Enter {title.lower()} name:", font=("Arial", 18), bg="#E6E6FA").pack(pady=10)
    entry_frame = tk.Frame(scrollable_frame, bg="#E6E6FA")
    entry_frame.pack(pady=10)
    tk.Entry(entry_frame, textvariable=habit_name_var, width=30).pack(side=tk.LEFT, padx=5)
    tk.Button(entry_frame, text=f"Add {title}", command=lambda: add_habit_func(habit_name_var), width=15, bg="#9376cc",
              fg="black").pack(side=tk.LEFT, padx=5)

    # Displaying the list of habits
    display_habits(habits, increment_habit_func, scrollable_frame)

    # Back button
    button_frame = tk.Frame(scrollable_frame, bg="#E6E6FA")
    button_frame.pack(pady=20)
    tk.Button(button_frame, text="Back", command=show_log_page, width=15, bg="#9376cc", fg="black").pack(side=tk.LEFT,
                                                                                                         padx=10)


# Displaying habits and their current tally counts
def display_habits(habits, increment_func, parent_frame):
    habits_frame = tk.Frame(parent_frame, bg="#E6E6FA")
    habits_frame.pack(pady=20)
    for habit_name, habit_data in habits.items():
        frame = tk.Frame(habits_frame, bg="#E6E6FA", relief=tk.RIDGE, borderwidth=1)
        frame.pack(fill=tk.X, pady=5, padx=10)
        tk.Label(frame, text=f"{habit_name}: +{habit_data['plus']} -{habit_data['minus']}", font=("Arial", 18),
                 bg="#E6E6FA").pack(side=tk.LEFT, padx=10)
        tk.Button(frame, text="+", command=lambda hn=habit_name: increment_func(hn, "plus"), width=5, bg="#9376cc",
                  fg="black").pack(side=tk.RIGHT, padx=5)
        tk.Button(frame, text="-", command=lambda hn=habit_name: increment_func(hn, "minus"), width=5, bg="#9376cc",
                  fg="black").pack(side=tk.RIGHT, padx=5)


# Adds a new good habit
def add_good_habit(habit_name_var):
    add_habit(habit_name_var, good_habits, "good_habits.txt", show_good_habits_page)


# Adds a new bad habit
def add_bad_habit(habit_name_var):
    add_habit(habit_name_var, bad_habits, "bad_habits.txt", show_bad_habits_page)


# Function that adds a new habit
def add_habit(habit_name_var, habits, file_name, refresh_page):
    habit_name = habit_name_var.get()
    if habit_name:
        habits[habit_name] = {"plus": 0, "minus": 0, "date": datetime.now().strftime("%Y-%m-%d")}
        save_habits(habits, file_name)
        habit_name_var.set("")
        refresh_page()


# Incrementing the count of a good habit
def increment_good_habit(habit_name, type):
    increment_habit(habit_name, type, good_habits, "good_habits.txt", show_good_habits_page)


# Incrementing the count of a bad habit
def increment_bad_habit(habit_name, type):
    increment_habit(habit_name, type, bad_habits, "bad_habits.txt", show_bad_habits_page)


# Function that increments the count of a habit
def increment_habit(habit_name, type, habits, file_name, refresh_page):
    if type == "plus":
        habits[habit_name]["plus"] += 1
    else:
        habits[habit_name]["minus"] += 1
    habits[habit_name]["date"] = datetime.now().strftime("%Y-%m-%d")
    save_habits(habits, file_name)
    refresh_page()
    show_message(type)


# Displaying a motivational message based on the habit increment type
def show_message(type):
    global message_label
    if message_label:
        message_label.destroy()
    if type == "plus":
        message = random.choice([
            "Great job! Keep it up!",
            "You're on the right track!",
            "Well done!",
            "Keep pushing forward!",
            "You got it!"
        ])
    else:
        message = random.choice([
            "Don't worry, you can do it!",
            "Stay strong!",
            "Keep trying!",
            "Don't give up!",
            "You'll get there! Just keep trying!"
        ])
    message_label = tk.Label(root, text=message, font=("Arial", 14), bg="#E6E6FA", fg="green")
    message_label.pack(pady=5)
    root.after(2000, clear_message)


# Clearing the motivational message after a few seconds
def clear_message():
    global message_label
    if message_label:
        message_label.destroy()
        message_label = None


# Displaying the progress page with habit tracking graphs
def show_progress_page():
    clear_window()
    container = tk.Frame(root, bg="#E6E6FA")
    container.pack(fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(container, bg="#E6E6FA")
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#E6E6FA")

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    tk.Label(scrollable_frame, text="Progress", font=("Arial", 24), bg="#E6E6FA", fg="black").pack(pady=20)

    # Graph for good habits
    fig_good, ax_good = plt.subplots()
    ax_good.set_title("Good Habits")
    ax_good.set_xlabel("Date")
    ax_good.set_ylabel("Count")

    # Graph for bad habits
    fig_bad, ax_bad = plt.subplots()
    ax_bad.set_title("Bad Habits")
    ax_bad.set_xlabel("Date")
    ax_bad.set_ylabel("Count")

    # Plotting data for good habits
    good_habits_data = get_habits_data(good_habits)
    bad_habits_data = get_habits_data(bad_habits)

    ax_good.plot(good_habits_data["dates"], good_habits_data["counts"], label="Good Habits", marker='o')
    ax_bad.plot(bad_habits_data["dates"], bad_habits_data["counts"], label="Bad Habits", marker='o')

    # Displaying the graphs
    canvas_good = FigureCanvasTkAgg(fig_good, master=scrollable_frame)
    canvas_good.draw()
    canvas_good.get_tk_widget().pack(side=tk.TOP, pady=20)

    canvas_bad = FigureCanvasTkAgg(fig_bad, master=scrollable_frame)
    canvas_bad.draw()
    canvas_bad.get_tk_widget().pack(side=tk.TOP, pady=20)

    tk.Button(scrollable_frame, text="Back to Main Page", command=show_main_page, width=20, bg="#9376cc",
              fg="black").pack(pady=20)


# Function that gets habit data for plotting graphs
def get_habits_data(habits):
    dates = []
    counts = []
    for habit_name, habit_data in habits.items():
        dates.append(habit_data["date"])
        counts.append(habit_data["plus"] - habit_data["minus"])
    return {"dates": dates, "counts": counts}


# Displaying the diary page with options to save and view entries
def show_diary_page():
    show_scrollable_page("Diary", [
        ("Save Entry", save_diary_entry),
        ("View Entries", view_diary_entries),
        ("Back to Main Page", show_main_page)
    ], True)


# Saving diary entries
def save_diary_entry():
    global diary_entries
    current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    diary_entry = diary_entry_text.get("1.0", "end-1c")
    diary_entries[current_datetime] = diary_entry
    save_diary_entries(current_datetime, diary_entry)
    diary_entry_text.delete("1.0", "end")


# Viewing diary entries
def view_diary_entries():
    clear_window()
    container = tk.Frame(root, bg="#E6E6FA")
    container.pack(fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(container, bg="#E6E6FA")
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#E6E6FA")

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    tk.Label(scrollable_frame, text="Diary Entries", font=("Arial", 24), bg="#E6E6FA", fg="black").pack(pady=10)

    search_frame = tk.Frame(scrollable_frame, bg="#E6E6FA")
    search_frame.pack(pady=10)

    global search_entry
    search_entry = tk.Entry(search_frame, width=20)
    search_entry.pack(side=tk.LEFT, padx=5)
    tk.Button(search_frame, text="Search", command=search_diary_entry, width=10, bg="#9376cc", fg="black").pack(
        side=tk.LEFT, padx=5)
    tk.Button(search_frame, text="Back", command=show_diary_page, width=10, bg="#9376cc", fg="black").pack(side=tk.LEFT,
                                                                                                           padx=5)

    global entry_frame
    entry_frame = tk.Frame(scrollable_frame, bg="#E6E6FA")
    entry_frame.pack(pady=20)

    for entry_date, entry in sorted(diary_entries.items()):
        tk.Label(entry_frame, text=entry_date, font=("Arial", 12), bg="#E6E6FA").pack(pady=5)
        tk.Label(entry_frame, text=entry, font=("Arial", 14), bg="#E6E6FA", wraplength=600, justify="left").pack(
            pady=10)


# Searches diary entries by date
def search_diary_entry():
    search_term = search_entry.get().strip().lower()
    for widget in entry_frame.winfo_children():
        widget.destroy()

    found_entries = False
    for entry_date, entry in diary_entries.items():
        if search_term in entry_date.lower():
            tk.Label(entry_frame, text=entry_date, font=("Arial", 12), bg="#E6E6FA").pack(pady=5)
            tk.Label(entry_frame, text=entry, font=("Arial", 14), bg="#E6E6FA", wraplength=600, justify="left").pack(
                pady=10)
            found_entries = True

    if not found_entries:
        messagebox.showinfo("Search Result", f"No entries found for the search term: {search_term}")


# Displaying the calendar for mood tracking
def show_calendar():
    clear_window()

    # Navigation buttons for the calendar
    nav_frame = tk.Frame(root)
    nav_frame.pack(pady=10)
    tk.Button(nav_frame, text="<< Previous Month", command=prev_month).pack(side=tk.LEFT, padx=10)
    tk.Button(nav_frame, text="Next Month >>", command=next_month).pack(side=tk.RIGHT, padx=10)
    tk.Button(nav_frame, text="Back", command=show_main_page).pack(side=tk.LEFT, padx=10)

    create_calendar(year, month)


# Creating & displaying the calendar
def create_calendar(year, month):
    global calendar_frame
    if calendar_frame:
        calendar_frame.destroy()

    calendar_frame = tk.Frame(root)
    calendar_frame.pack(pady=20)

    # Calendar header displaying (current month & year)
    header = tk.Label(calendar_frame, text=f"{datetime(year, month, 1).strftime('%B %Y')}", font=("Arial", 16))
    header.grid(row=0, column=0, columnspan=7)

    # Days of the week labels
    days_of_week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    for i, day in enumerate(days_of_week):
        tk.Label(calendar_frame, text=day, font=("Arial", 12)).grid(row=1, column=i)

    # Calculating the start day & number of days in the month
    start_day = datetime(year, month, 1).weekday()
    days_in_month = (datetime(year, month + 1, 1) - timedelta(days=1)).day if month != 12 else 31

    # Buttons for each day
    row = 2
    for day in range(1, days_in_month + 1):
        col = (day + start_day) % 7
        if col == 0 and day > 1:
            row += 1
        date = datetime(year, month, day)
        color = date_colors.get(date.strftime("%Y-%m-%d"), "#FFFFFF")
        create_date_button(calendar_frame, date, color, row, col)


# Creating a button for each specific date
def create_date_button(parent, date, color, row, col):
    date_str = date.strftime("%Y-%m-%d")
    btn = tk.Button(parent, text=date.day, bg=color, command=lambda d=date_str: change_date_color(d))
    btn.grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10)


# Changing the color of a date button
def change_date_color(date_str):
    global date_colors
    color = simpledialog.askstring("Input", f"Enter color for {date_str} (e.g., #FF0000):")
    if color:
        date_colors[date_str] = color
        update_calendar()


# Updating the calendar display
def update_calendar():
    create_calendar(year, month)


# Moving to the next month in the calendar
def next_month():
    global year, month
    month += 1
    if month > 12:
        month = 1
        year += 1
    create_calendar(year, month)


# MOving to the previous month in the calendar
def prev_month():
    global year, month
    month -= 1
    if month < 1:
        month = 12
        year -= 1
    create_calendar(year, month)


# Showing a scrollable page with a title & buttons
def show_scrollable_page(title, buttons, is_diary_page=False):
    clear_window()
    container = tk.Frame(root, bg="#E6E6FA")
    container.pack(fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(container, bg="#E6E6FA")
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#E6E6FA")

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    tk.Label(scrollable_frame, text=title, font=("Arial", 24), bg="#E6E6FA", fg="black").pack(pady=20)

    if is_diary_page:
        global diary_entry_text
        diary_entry_text = tk.Text(scrollable_frame, width=60, height=10)
        diary_entry_text.pack(pady=20)

    for text, command in buttons:
        tk.Button(scrollable_frame, text=text, command=command, width=20, bg="#9376cc", fg="black").pack(pady=10)


# Loading habits from a file into a dictionary
def load_habits(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            habits = {}
            for line in file:
                parts = line.strip().split(":")
                if len(parts) == 4:
                    habit_name, plus, minus, date = parts
                    habits[habit_name] = {"plus": int(plus), "minus": int(minus), "date": date}
                else:
                    print(f"Skipping invalid entry: {line.strip()}")
            return habits
    return {}


# Saving habits from a dictionary to a file
def save_habits(habits, file_name):
    with open(file_name, "w") as file:
        for habit_name, habit_data in habits.items():
            file.write(f"{habit_name}:{habit_data['plus']}:{habit_data['minus']}:{habit_data['date']}\n")


# Initializing diary entries and habits from files
load_diary_entries()
good_habits.update(load_habits("good_habits.txt"))
bad_habits.update(load_habits("bad_habits.txt"))

# Showing the main page initially
show_main_page()

# Running the Tkinter loop
root.mainloop()
