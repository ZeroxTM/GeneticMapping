"""
 @Time : 11/12/2020 15:13
 @Author : Alaa Grable
 """
from PySide2 import QtWidgets
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as
                                                FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from matplotlib.patches import Ellipse, Rectangle

from controllers.FileBrowserController import FileBrowserController
from controllers.MarkersTabController import MarkersTabController
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
import sys
import numpy as np
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QMainWindow, QApplication
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as
                                                FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import seaborn as sns
import pandas as pd


# comparison_tab
# import_btn
# map_widget
class MapComparisonController:
    ui = None
    plotted = False
    ax = None

    @staticmethod
    def compare_maps(path):
        map1 = list()
        map2 = list()
        map2_markers = list()
        data = FileBrowserController.read_map_file(path)
        for _, row in data.iterrows():
            map2_markers.append((row['marker_name'], row['genetic_coord']))
        map1_markers = MarkersTabController.markers

        for marker1 in map1_markers:
            for marker2 in map2_markers:
                if marker1.name == marker2[0]:
                    map1.append(marker1.coordinateGenet)
                    map2.append(float(marker2[1]))
                    break
        #map1_markers = [1, 3, 5, 7]
        #MapComparisonController.map2_markers = [20, 9, 11, 25]
        df = pd.DataFrame({'Map A': map1, 'Map B': map2})
        data = pd.melt(df)
        # Initialize the plot
        MapComparisonController.ui.map_widget.figure = Figure(tight_layout=True)
        MapComparisonController.ui.map_widget.canvas = FigureCanvas(MapComparisonController.ui.map_widget.figure)
        MapComparisonController.ui.map_widget.graphLayout = QtWidgets.QVBoxLayout()
        MapComparisonController.ui.map_widget.graphLayout.addWidget(
            FigureCanvas(MapComparisonController.ui.map_widget.figure))
        #MapComparisonController.ui.map_widget.graphLayout.addWidget(NavigationToolbar(MapComparisonController.ui.map_widget.canvas, MapComparisonController.ui))
        MapComparisonController.ui.map_widget.setLayout(MapComparisonController.ui.map_widget.graphLayout)
        #MapComparisonController.ui.map_widget.figure.clf()
        if not MapComparisonController.plotted:
            ax = MapComparisonController.ui.map_widget.figure.add_subplot()
            MapComparisonController.ax = ax
            MapComparisonController.plotted = True
        else:
            MapComparisonController.ui.map_widget.figure.clear(keep_observers=True)
            ax = MapComparisonController.ax
        # Scatter all the lines on the plot without lines between them
        sns.stripplot(data=data, x='variable', y='value', ax=ax, jitter=0)
        #sns.swarmplot(data=data, x='variable', y='value', ax=ax)
        # Get the location of both maps on the plot
        locs1 = ax.get_children()[0].get_offsets()
        locs2 = ax.get_children()[1].get_offsets()
        for i in range(locs1.shape[0]):
            x = [locs1[i, 0], locs2[i, 0]]
            y = [locs1[i, 1], locs2[i, 1]]
            ax.plot(x, y, color='black', alpha=0.1)
        try:
            for i in range(2):
                rect = MapComparisonController.draw_rectangle(ax.collections[i])
                ax.add_patch(rect)
        except ValueError:
            pass
        MapComparisonController.ui.map_widget.canvas.draw()
        MapComparisonController.ui.map_widget.canvas.flush_events()


    @staticmethod
    def draw_rectangle(map):
        x, y = np.array(map.get_offsets()).T
        return Rectangle((x.min(), y.min()), x.ptp(), y.ptp(), edgecolor='k', facecolor='None', lw=3)


