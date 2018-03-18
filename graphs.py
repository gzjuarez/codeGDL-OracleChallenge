import matplotlib.pyplot as plt
import pandas as pd

def make_graph(data):
    plt.scatter(data["time"])

def make_graphs(data):
        days = {
            "monday": [],
            "tuesday": [],
            "wednesday": [],
            "thursday": [],
            "friday": [],
            "saturday": [],
            "sunday": []
        }

        for d in data:
            days[d["day"]].append(d)
        
        i = 0
        for k, v in days.items():
            v.sort(key = lamda x: x["time"])
            plt.figure(i)
            plt.plot([d["time"] for d in data])

            i += 1
