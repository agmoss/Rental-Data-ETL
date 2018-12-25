import plotly.plotly as py
import matplotlib.pyplot as plt
import seaborn as sns


def boxplot_vertical_categorical(df):

    ax = sns.boxplot(x="community", y="price", data=df)

    # Plot formatting
    fig = ax.get_figure()
    # fig.legend(prop={'size': 3}, title = 'Status')
    fig.suptitle('Boxplot1')
    # fig.xlabel('KM Traveled per Day')
    # fig.ylabel('Density')
    fig.savefig("boxplot1.png")
