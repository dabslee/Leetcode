import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# dark mode toggle
darkmode = False

# theme colors
class Colors:
    alpha = "dd"
    GREEN = "#32a852" + alpha
    YELLOW = "#c9a132" + alpha
    RED = "#ad2626" + alpha
    BLUE = "#3399ff" + alpha
    BACKGROUND = (0.133, 0.153, 0.18) if darkmode else None

# creates a pie chart from an iterable
def agr_pie(lst, labels=None, colors=None, background=None):
    if background != None:
        plt.figure().patch.set_facecolor(background)
    lst = list(lst)
    if labels == None:
        labels = list(set(lst))
    plt.pie(
        list( [lst.count(val) for val in labels] ),
        labels = list(
            [f"{label}\n{lst.count(label)} ({round(lst.count(label)/len(lst)*100, 1)}%)" for label in labels]
        ),
        colors = colors,
        labeldistance = 0.5,
        
    )
    plt.tight_layout()

# global formatting
matplotlib.rcParams['text.color'] = 'w'
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = 'Segoe UI'
matplotlib.rcParams['font.size'] = '12'
matplotlib.rcParams['font.weight'] = 'bold'

# import data
df = pd.read_csv('analysis.csv')

# solved problems by difficulty
agr_pie(
    df["Difficulty"],
    labels=["Easy", "Medium", "Hard"],
    colors=[Colors.GREEN, Colors.YELLOW, Colors.RED],
    background=Colors.BACKGROUND
)
plt.savefig('analysis_visualizations/pie_difficulty.png')
