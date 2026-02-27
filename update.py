import os
from subprocess import run

UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "main")
UPSTREAM_REPO = os.environ.get(
    "UPSTREAM_REPO",
    "",
)


if os.path.exists(".git"):
    run(["rm", "-rf", ".git"], check=False)

# Backup old requirements.txt if exists


# Git update commands
commands = [
    "git init -q",
    "git config --global user.email yesiamshojib@gmail.com",
    "git config --global user.name 5hojib",
    "git add .",
    "git commit -sm update -q",
    f"git remote add origin {UPSTREAM_REPO}",
    "git fetch origin -q",
    f"git reset --hard origin/{UPSTREAM_BRANCH} -q",
]

update = run(" && ".join(commands), shell=True, check=False)

try:
    update = run(
        "git diff HEAD~1 HEAD -- requirements.txt | grep '^+' | grep -v '^+#' | grep -v '+++' | sed 's/^+//' | xargs pip3 install",
        shell=True,
        check=False,
    )
except Exception as e:
    print(f"While installing requirements.txt thus ckme :- \n {e}")

if update.returncode == 0:
    print("Successfully updated with the latest commit from UPSTREAM_REPO")


else:
    print("Something went wrong while updating. Check if UPSTREAM_REPO is valid.")
