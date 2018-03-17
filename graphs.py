import matplotlib.pyplot as plt   

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
            plt.plot()

            i += 1
