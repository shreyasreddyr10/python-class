capacity = float(input("Battery capacity (mAh): "))
load = float(input("Current draw (mA): "))
hours = capacity / load
print(f"Estimated runtime: {hours:.2f} hours")