from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# import numpy as np
import squarify 
import seaborn as sns

# Plot Style
# plt.style.use("ggplot")

def canvas(fig, title):
    newWindow = Toplevel()
    newWindow.geometry("+%d+%d" % (250, 10))
    newWindow.title(title)

    canvas = FigureCanvasTkAgg(fig, master=newWindow)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH)

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, newWindow)
    toolbar.update()
    toolbar.pack(side=TOP, fill=X)
    
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH) 
    
    
def groupBarChart( title, data, x, ylabel, legend):
    fig, ax = plt.subplots(nrows=1, figsize=(10, 10), sharex=True)
    # x = np.arange(len(data["areaName"]))  # the label locations
    # width = 0.45  # the width of the bars
    # rects1 = ax.bar( x - width/2, data["newCasesBySpecimenDate-0_59"], width, label='Men')
    # rects2 = ax.bar( x - width/2, data["newCasesBySpecimenDate-60+"], width, label='Women')
    ax.set(title=title)
    data.plot.bar( x=x, stacked=False, ax=ax)
    for label in ax.get_xticklabels():
        label.set_rotation(0)

    ax.set(ylabel=ylabel)
    # ax.set_xticks(x, data["areaName"])
    ax.legend(legend)
    # ax.bar_label(rects1, padding=3)
    # ax.bar_label(rects2, padding=3)
    # fig.tight_layout()
    
    canvas(fig, title)
    
def horizontalBarChart( data, groupLabel, title):    
    plt.rcParams.update({'figure.autolayout': True})
    
    fig, ax = plt.subplots()
    ax.barh(groupLabel, data)
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=45, horizontalalignment='right')
    
    canvas(fig, title)

def barChart(df, title, x, y):
    fig, ax0 = plt.subplots(figsize=(10, 10))
    fig.suptitle(title)
    df.plot.line(x=x, y=y, stacked=False, ax=ax0)
    df.plot.bar(x=x, y=y, stacked=False, ax=ax0)
    ax0.set(ylabel="Cases")
    ax0.legend(["Stop Search Cases"])

    canvas(fig, title)
    
def lineChart(title, plotTitleOne, plotTitleTwo, data, x, y, ax0Legend, plotLabel1, plotLabel2, ylabel, legends):
    fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(10, 10), sharex=True)
      
    fig.suptitle(title)
    
    ax0.set(title=plotTitleOne)
    ax1.set(title=plotTitleTwo)

    data.plot.area( x=x, y=y, stacked=False, ax=ax0)
    ax0.set(ylabel="Cases")
    ax0.legend([ax0Legend])

    data[[x, plotLabel1 , plotLabel2]].plot.area(x=x, stacked=False, ax=ax1)
    
    ax1.set(ylabel=ylabel)
    handles, labels = ax1.get_legend_handles_labels()
    ax1.legend(handles, legends)
    
    canvas(fig, title)
    
def TreeMap(title, size, labels ):
    
    # plt.clf()
    # plt.cla()
    plt.close()
    
    colors=['#fae588','#f79d65','#f9dc5c','#e8ac65','#e76f51','#ef233c','#b7094c', '#c7094c', '#b2494c', '#17094c', '#b7005c'] #color palette
    fig = plt.gcf()
    fig.set_size_inches(12, 7.5)
    sns.set_style(style="whitegrid") # set seaborn plot style
    sizes= size
    label= labels
    squarify.plot(sizes=sizes, label=label, alpha=0.6,color=colors).set(title=title)
    plt.title(title, fontsize=14, fontweight="bold")
    plt.axis('off')
    canvas(fig, title)
    # plt.show()
    
def pieChart(title, data, labels):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.pie(data, labels=labels, autopct='%.1f%%',
        wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'},
        textprops={'size': 'x-large'})
    ax.set_title(title, fontsize=14)

    canvas(fig, title)
    

def lollipopChart(x, y, label, max, ylabel, title, data):
    fig, ax = plt.subplots(figsize=(16,16), dpi= 80)
    ax.vlines(x=x, ymin=0, ymax=y, color='firebrick', alpha=0.7, linewidth=2)
    ax.scatter(x=x, y=y, s=75, color='firebrick', alpha=0.7)
    ax.set_title(title, fontdict={'size':16})
    ax.set_ylabel(ylabel)
    ax.set_xticks(x)
    ax.set_xticklabels(label.str.upper(), rotation=60, fontdict={'horizontalalignment': 'right', 'size':12})
    ax.set_ylim(0, int(max) + 20)
    
    # Annotate
    for row in data.itertuples():
        ax.text(row.Index, row.involved_person+3.5, s=round(row.involved_person, 2), horizontalalignment= 'center', verticalalignment='bottom', fontsize=9)

    canvas(fig, title)
    
def dotPlot(x, y, label, max, ylabel, title):
    plt.rcParams.update({'figure.autolayout': True})
    fig, ax = plt.subplots(figsize=(16,10), dpi= 80)
    ax.hlines(y=x, xmin=1, xmax=int(max) + 18, color='gray', alpha=0.7, linewidth=1, linestyles='dashdot')
    ax.scatter(y=x, x=y, s=75, color='firebrick', alpha=0.7)

    # Title, Label, Ticks and Ylim
    ax.set_title(title, fontdict={'size':12})
    ax.set_xlabel(ylabel)
    ax.set_yticks(x)
    ax.set_yticklabels(label.str.title(), fontdict={'horizontalalignment': 'right'})
    ax.set_xlim(10, int(max) + 20)

    canvas(fig, title)