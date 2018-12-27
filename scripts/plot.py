import plotly.plotly as py
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# TODO: Plot class?

def boxplot_price_quadrant(df):

    pal = sns.color_palette("coolwarm", 7)

    sns.set(rc={'figure.figsize':(11.7,8.27)})

    sns.boxplot(
        y="quadrant", 
        x="price", 
        orient="h",
        palette=pal,
        data=df
        ).set(
            xlabel='Rent',
            ylabel='Quadrant',
            title = "Rent Per Quadrant"
        )
    plt.tight_layout()
    plt.show()



def distplot_price(df):

    sns.set(rc={'figure.figsize':(11.7,8.27)})

    sns.distplot(
        df['price'],rug=True, rug_kws={"color": "lightskyblue"},
        kde_kws={"color": "k", "lw": 3, "label": "KDE"},
        hist_kws={"histtype": "step", "linewidth": 3,
        "alpha": 1, "color": "tomato"}
        
    ).set(
        xlabel='Price',
        ylabel='Density',
        title = "Rental Price Distribution"
    )
    plt.tight_layout()
    plt.show()


def corr_heat(df):

    #sns.set(rc={'figure.figsize':(11.7,8.27)})
    sns.set(style="white")

    df.drop(["latitude","longitude","address_hidden","email","id","userId"], axis = 1, inplace  = True)

    corr = df.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))

    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(220, 10, as_cmap=True)

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, 
        mask=mask, 
        cmap=cmap, 
        vmax=.3, 
        center=0,
        square=True, 
        linewidths=.5, 
        cbar_kws={"shrink": .5},
        annot = True).set(
            title = "Correlation of Variables"
        )

    plt.tight_layout()
    plt.show()

