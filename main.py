import os

ENTRY = "I am out until Monday. I trained my replacement for exactly one afternoon, so good luck to us all."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
