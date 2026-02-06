import random
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
import numpy as np
from tkinter import ttk

n = []
rolls = []
results = []

def start_simulation():
    global n, rolls, results
    n = []
    num_simulate = int(num_simulate_entry.get())
    num_players = int(num_players_entry.get())
    for numsumulate in range(num_simulate):
        rolls = [random.randint(1, 6) for _ in range(300)]
        results = get_results(num_players, rolls)
        steps_to_match = calculate_steps_to_match(results)
        n.append(steps_to_match)
    messagebox.showinfo("Simulation", "Simulation completed")

def get_results(num_players, rolls):
    results = []
    for i in range(num_players):
        results.append([])
        results[i].append(random.randint(1, 10))
        current_position = results[i][0]
        while current_position < len(rolls):
            results[i].append(rolls[current_position])
            current_position += results[i][-1]
    return results

def calculate_steps_to_match(results):
    steps = 0
    while steps < len(results[0]):
        first_result = results[0][steps]
        match = True
        for player_results in results:
            if steps >= len(player_results) or player_results[steps] != first_result:
                match = False
                break
        if match:
            break
        steps += 1
    return steps

def show_player_steps():
    new_window = tk.Toplevel(window)
    text = tk.Text(new_window)
    text.insert(tk.END, str(results))
    text.pack()

def show_matching_steps():
    new_window = tk.Toplevel(window)
    text = tk.Text(new_window)
    text.insert(tk.END, str(n))
    text.pack()

from collections import Counter

def show_histogram():
    new_window = tk.Toplevel(window)
    fig = plt.Figure(figsize=(12, 8), dpi=100)
    plot = fig.add_subplot(111)
    counts = Counter(n)
    x = list(counts.keys())
    y = list(counts.values())
    plot.set_title('Frequency Distribution of Steps to Match')
    plot.set_xlabel('Steps to Match')
    plot.set_ylabel('Frequency')
    plot.bar(x, y)
    chart = FigureCanvasTkAgg(fig, new_window)
    chart.get_tk_widget().pack()

""" def show_histogram():
    new_window = tk.Toplevel(window)
    fig = plt.Figure(figsize=(6, 5), dpi=100)
    plot = fig.add_subplot(111)
    counts, bins = np.histogram(n, bins='auto')
    plot.bar(bins[:-1], counts)
    plot.set_title('Frequency Distribution of Steps to Match')
    plot.set_xlabel('Steps to Match')
    plot.set_ylabel('Frequency')
    chart = FigureCanvasTkAgg(fig, new_window)
    chart.get_tk_widget().pack()
 """
"""     # اضافه کردن جدول
    new_frame = ttk.Frame(new_window)
    new_frame.pack()
    table = ttk.Table(new_frame, columns=2, width=400)
    table.pack()
    table.insert('', 0, text='Steps', justify='center')
    table.insert('', 1, text='Frequency', justify='center')
    for i in range(len(counts)):
        table.insert(i + 1, 0, text=str(bins[i]), justify='center')
        table.insert(i + 1, 1, text=str(counts[i]), justify='center')
 """    
window = tk.Tk()

num_simulate_label = tk.Label(window, text="Number of Simulations")
num_simulate_label.pack()
num_simulate_entry = tk.Entry(window)
num_simulate_entry.pack()

num_players_label = tk.Label(window, text="Number of Players")
num_players_label.pack()
num_players_entry = tk.Entry(window)
num_players_entry.pack()

start_button = tk.Button(window, text="Start Simulation", command=start_simulation)
start_button.pack()

show_steps_button = tk.Button(window, text="Show Player Steps", command=show_player_steps)
show_steps_button.pack()

show_match_button = tk.Button(window, text="Show Matching Steps", command=show_matching_steps)
show_match_button.pack()

show_hist_button = tk.Button(window, text="Show Frequency Histogram", command=show_histogram)
show_hist_button.pack()

window.mainloop()
