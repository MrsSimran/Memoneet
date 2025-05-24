import os
import subprocess
from datetime import datetime, timedelta

# ✅ Correct path to your MemoNeet folder
repo_path = "C:/Users/win/Desktop/Memoneet"
file_name = "log.txt"

# 📅 Date range
start_date = datetime(2025, 2, 2)
end_date = datetime(2025, 4, 23)

# Go to MemoNeet repo directory
os.chdir(repo_path)

# Loop for each day and commit
current_date = start_date
while current_date <= end_date:
    date_str = current_date.strftime("%Y-%m-%dT%H:%M:%S")

    with open(file_name, "a") as f:
        f.write(f"Fake log on {date_str}\n")

    subprocess.run(["git", "add", file_name])
    subprocess.run(["git", "commit", "--date", date_str, "-m", f"Fake commit on {date_str}"])

    current_date += timedelta(days=1)

print("✅ All fake commits done. Now run:")
print("👉 git push --force origin master")
