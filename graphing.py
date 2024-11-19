import numpy as np
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def graph_equation():
    equation = equation_entry.get()
    x = np.linspace(-10, 10, 100)
    y = eval(equation)
    
    figure = Figure(figsize=(5, 4), dpi=100)
    plot = figure.add_subplot(111)
    plot.plot(x, y)
    plot.set_xlabel('x')
    plot.set_ylabel('y')
    plot.set_title('Graph of ' + equation)
    plot.grid(True)
    
    canvas = FigureCanvasTkAgg(figure, master=graph_tab)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

window = tk.Tk()
window.title("Graphing Calculator")

notebook = tk.ttk.Notebook(window)
notebook.pack(fill=tk.BOTH, expand=True)

graph_tab = tk.Frame(notebook)
equation_label = tk.Label(graph_tab, text="Enter an equation:")
equation_label.pack()
equation_entry = tk.Entry(graph_tab)
equation_entry.pack()
graph_button = tk.Button(graph_tab, text="Graph", command=graph_equation)
graph_button.pack()
notebook.add(graph_tab, text="Graph")

basic_calculator_tab = tk.Frame(notebook)
notebook.add(basic_calculator_tab, text="Basic Calculator")

scientific_calculator_tab = tk.Frame(notebook)
notebook.add(scientific_calculator_tab, text="Scientific Calculator")

programming_calculator_tab = tk.Frame(notebook)
notebook.add(programming_calculator_tab, text="Programming Calculator")

window.mainloop()
