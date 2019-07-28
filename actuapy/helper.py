import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def assert_initialize(obj,category,option):
    return "Set " + category + "\n"\
        + "Try to initalize with "\
        + obj.__class__.__name__ + "("+option+") for example."


def heatmap():
    sns.heatmap(df_flights_pivot, annot=True, fmt='g', cmap='Blues')
