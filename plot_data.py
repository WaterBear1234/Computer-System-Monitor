import matplotlib.pyplot as plt
import pandas as pd
import os
os.makedirs("plots", exist_ok=True)
df = pd.read_csv("logs/system_usage.csv")
plt.figure(figsize=(10, 6))
plt.plot(df["timestamp"], df["cpu"], label="CPU %")
plt.plot(df["timestamp"], df["memory"], label="Memory %")
plt.legend()
plt.xlabel("Time")
plt.ylabel("Usage (%)")
plt.title("System Performance Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/system_usage.png")
plt.show()