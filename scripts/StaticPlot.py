import plotly.plotly as py
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

class StaticPlot:

    def __init__(self,df,write_path):
        self.df = df
        self.write_path = write_path


    def boxplot_price_quadrant(self):

        pal = sns.color_palette("coolwarm", 7)

        sns.set(rc={'figure.figsize':(11.7,8.27)})

        sns.boxplot(
            y="quadrant", 
            x="price", 
            orient="h",
            palette=pal,
            data=self.df
            ).set(
                xlabel='Rent',
                ylabel='Quadrant',
                title = "Rent Per Quadrant"
            )
        plt.tight_layout()
        plt.savefig(self.write_path + 'boxplot_price_quadrant.png')


    def distplot_price(self):

        sns.set(rc={'figure.figsize':(11.7,8.27)})

        sns.distplot(
            self.df['price'],rug=True, rug_kws={"color": "lightskyblue"},
            kde_kws={"color": "k", "lw": 3, "label": "KDE"},
            hist_kws={"histtype": "step", "linewidth": 3,
            "alpha": 1, "color": "tomato"}
            
        ).set(
            xlabel='Price',
            ylabel='Density',
            title = "Rental Price Distribution"
        )
        plt.tight_layout()
        plt.savefig(self.write_path+'distplot_price.png')


    def corr_heat(self):

        #sns.set(rc={'figure.figsize':(11.7,8.27)})
        sns.set(style="white")

        self.df.drop(["latitude","longitude","address_hidden","email","id","userId"], axis = 1, inplace  = True)

        corr = self.df.corr()

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
        plt.savefig(self.write_path+'corr_heat.png')

    def bar_community(self):

        pal = sns.color_palette("coolwarm", 7)

        community_count  = self.df['community'].value_counts()
        community_count = community_count[:10,]
        plt.figure(figsize=(10,5))

        sns.barplot(community_count.index, 
            community_count.values, 
            palette=pal,
            alpha=0.8)

        plt.title('Frequency of Rental Listings by Community')
        plt.ylabel('Number of Occurrences', fontsize=12)
        plt.xlabel('Community', fontsize=12)

        plt.tight_layout()
        plt.savefig(self.write_path+'bar_community.png')