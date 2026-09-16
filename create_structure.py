from pathlib import Path

# Current project folder
ROOT = Path.cwd()

folders = [
    "pages",
    "utils",
    "profiles",
    "profiles/chrome_profile"
]

files = [
    "main.py",
    "requirements.txt",
    "pages/medium_page.py",
    "utils/driver_factory.py",
    "README.md"
]

# Create folders safely
for folder in folders:
    path = ROOT / folder

    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
        print(f"[CREATED FOLDER] {path}")
    else:
        print(f"[EXISTS] {path}")

# Create files safely
for file in files:
    path = ROOT / file

    if not path.exists():
        path.touch()
        print(f"[CREATED FILE] {path}")
    else:
        print(f"[EXISTS] {path}")

print("\nProject structure checked successfully.")