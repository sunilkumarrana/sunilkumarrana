import json
import urllib.request
import re
import os

USERNAME = "sunilkumarrana"
API_URL = f"https://api.github.com/users/{USERNAME}/repos?per_page=100&type=owner"
token = os.environ.get("GITHUB_TOKEN")

headers = {"Accept": "application/vnd.github.v3+json"}
if token:
    headers["Authorization"] = f"token {token}"

req = urllib.request.Request(API_URL, headers=headers)
try:
    with urllib.request.urlopen(req) as response:
        repos = json.loads(response.read().decode())
except Exception as e:
    print(f"Error fetching repos: {e}")
    exit(1)

# Filter out forks
repos = [r for r in repos if not r.get("fork", False)]

# Collect languages
languages = set()
for r in repos:
    lang = r.get("language")
    if lang:
        languages.add(lang)

# Colors and logos for shields.io
LANGUAGE_MAP = {
    "Python": ("3776AB", "python", "white"),
    "Django": ("092E20", "django", "white"),
    "TypeScript": ("3178C6", "typescript", "white"),
    "React": ("61DAFB", "react", "black"),
    "JavaScript": ("F7DF1E", "javascript", "black"),
    "HTML": ("E34F26", "html5", "white"),
    "CSS": ("1572B6", "css3", "white"),
    "Java": ("007396", "java", "white"),
    "C++": ("00599C", "c%2B%2B", "white"),
    "C#": ("239120", "c-sharp", "white"),
    "Ruby": ("CC342D", "ruby", "white"),
    "Go": ("00ADD8", "go", "white"),
    "Rust": ("000000", "rust", "white"),
    "PHP": ("777BB4", "php", "white"),
    "Swift": ("F05138", "swift", "white"),
    "Kotlin": ("7F52FF", "kotlin", "white"),
    "Dart": ("0175C2", "dart", "white"),
    "Vue": ("4FC08D", "vuedotjs", "white"),
    "Angular": ("DD0031", "angular", "white"),
    "Svelte": ("FF3E00", "svelte", "white"),
    "Shell": ("4EAA25", "gnu-bash", "white"),
    "C": ("A8B9CC", "c", "white"),
    "Jupyter Notebook": ("F37626", "jupyter", "white"),
}

tech_stack_md = []
for lang in sorted(languages):
    if lang in LANGUAGE_MAP:
        color, logo, logo_color = LANGUAGE_MAP[lang]
        lang_url = lang.replace(" ", "%20")
        badge = f'<img src="https://img.shields.io/badge/{lang_url}-{color}?style=flat&logo={logo}&logoColor={logo_color}" />'
        tech_stack_md.append(badge)
    else:
        lang_url = lang.replace(" ", "%20")
        badge = f'<img src="https://img.shields.io/badge/{lang_url}-informational?style=flat" />'
        tech_stack_md.append(badge)

tech_stack_content = "\n".join(tech_stack_md)

# Top 2 pinned projects by stargazers
sorted_repos = sorted(repos, key=lambda x: x.get("stargazers_count", 0), reverse=True)
top_repos = sorted_repos[:2]

pinned_projects_md = []
for r in top_repos:
    name = r.get("name")
    url = r.get("html_url")
    pinned_projects_md.append(f'<a href="{url}"><img src="https://github-readme-stats.vercel.app/api/pin/?username={USERNAME}&repo={name}&theme=default&show_owner=false" width="48%" /></a>')

pinned_projects_content = "\n".join(pinned_projects_md).strip()

# Read readme.md
with open("readme.md", "r", encoding="utf-8") as f:
    readme = f.read()

# Replace tech stack
tech_stack_pattern = r"(<!--START_TECH_STACK-->)(.*?)(<!--END_TECH_STACK-->)"
readme = re.sub(tech_stack_pattern, f"\\1\n{tech_stack_content}\n\\3", readme, flags=re.DOTALL)

# Replace pinned projects
pinned_projects_pattern = r"(<!--START_PINNED_PROJECTS-->)(.*?)(<!--END_PINNED_PROJECTS-->)"
readme = re.sub(pinned_projects_pattern, f"\\1\n{pinned_projects_content}\n\\3", readme, flags=re.DOTALL)

# Write readme.md
with open("readme.md", "w", encoding="utf-8") as f:
    f.write(readme)

print("Successfully updated readme.md")
