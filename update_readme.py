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

# Colors for shields.io (NO logos to match image)
LANGUAGE_MAP = {
    "Python": "3776AB",
    "Django": "092E20",
    "TypeScript": "3178C6",
    "React": "00D8FF",
    "JavaScript": "F7DF1E",
    "HTML": "E34F26",
    "CSS": "1572B6",
    "Java": "007396",
    "C++": "00599C",
    "C#": "239120",
    "Ruby": "CC342D",
    "Go": "00ADD8",
    "Rust": "000000",
    "PHP": "777BB4",
    "Swift": "F05138",
    "Kotlin": "7F52FF",
    "Dart": "0175C2",
    "Vue": "4FC08D",
    "Angular": "DD0031",
    "Svelte": "FF3E00",
    "Shell": "4EAA25",
    "C": "A8B9CC",
    "Jupyter Notebook": "F37626",
}

tech_stack_md = []
for lang in sorted(languages):
    if lang in LANGUAGE_MAP:
        color = LANGUAGE_MAP[lang]
        lang_url = lang.replace(" ", "%20")
        badge = f'<img src="https://img.shields.io/badge/{lang_url}-{color}?style=flat" />'
        tech_stack_md.append(badge)
    else:
        lang_url = lang.replace(" ", "%20")
        badge = f'<img src="https://img.shields.io/badge/{lang_url}-informational?style=flat" />'
        tech_stack_md.append(badge)

tech_stack_content = " ".join(tech_stack_md)

# Top 2 pinned projects by stargazers
sorted_repos = sorted(repos, key=lambda x: x.get("stargazers_count", 0), reverse=True)
top_repos = sorted_repos[:2]

pinned_projects_md = []
for r in top_repos:
    name = r.get("name")
    url = r.get("html_url")
    pinned_projects_md.append(f'<a href="{url}"><img src="https://github-readme-stats.vercel.app/api/pin/?username={USERNAME}&repo={name}&theme=default&show_owner=false" width="48%" /></a>')

pinned_projects_content = "\n".join(pinned_projects_md).strip()


# SVG Generation for Stats and Connect Buttons to match exactly the image style
def create_stats_svg(filename, repos_count):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="90" viewBox="0 0 800 90">
  <style>
    .card {{ fill: #ffffff; stroke: #d0d7de; stroke-width: 1; rx: 6; ry: 6; }}
    .title {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 13px; fill: #57606a; font-weight: 500; text-anchor: middle; }}
    .value {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 24px; fill: #24292f; font-weight: 600; text-anchor: middle; }}
  </style>
  
  <rect x="0" y="0" width="250" height="85" class="card" />
  <text x="125" y="32" class="title">Repos</text>
  <text x="125" y="65" class="value">{repos_count}</text>
  
  <rect x="275" y="0" width="250" height="85" class="card" />
  <text x="400" y="32" class="title">Contributions</text>
  <text x="400" y="65" class="value">120+</text>
  
  <rect x="550" y="0" width="250" height="85" class="card" />
  <text x="675" y="32" class="title">Streak</text>
  <text x="675" y="65" class="value">3 weeks</text>
</svg>"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg)

def create_button_svg(filename, text, icon_path, width):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="32">
  <style>
    .bg {{ fill: #ffffff; stroke: #d0d7de; stroke-width: 1; rx: 6; ry: 6; }}
    .text {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 13px; fill: #24292f; font-weight: 500; dominant-baseline: central; }}
    .icon {{ fill: #57606a; }}
  </style>
  <rect x="0.5" y="0.5" width="{width - 1}" height="31" class="bg" />
  <path class="icon" d="{icon_path}" transform="translate(10, 8) scale(1)" />
  <text x="32" y="17" class="text">{text}</text>
</svg>"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg)

create_stats_svg("stats.svg", len(repos))

globe_path = "M1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0zM8 0a8 8 0 100 16A8 8 0 008 0zM6.3 14.3a6.5 6.5 0 01-1.7-2.3h2.4a15.7 15.7 0 01-.7 2.3zm1.4 0a15.7 15.7 0 00.7-2.3h3.2a15.7 15.7 0 00.7 2.3a6.5 6.5 0 01-4.6 0zm3.3-3.8h3.3a6.5 6.5 0 000-5h-3.3a14.2 14.2 0 010 5zM8.5 5.5h3.1a14.2 14.2 0 00-.7-2.3A6.5 6.5 0 008.5 2.5v3zM7.5 5.5V2.5a6.5 6.5 0 00-2.4.7 14.2 14.2 0 00-.7 2.3h3.1zm-3.8 0a6.5 6.5 0 000 5h3.3a14.2 14.2 0 010-5H3.7zm3.8 5v3a6.5 6.5 0 002.4-.7 14.2 14.2 0 00.7-2.3H7.5z"
code_path = "M5.5 12.5L.5 8l5-4.5.8.7L2.2 8l4.1 3.8-.8.7zm5 0l-.8-.7L13.8 8l-4.1-3.8.8-.7 5 4.5-5 4.5z"
insta_path = "M4 2a2 2 0 00-2 2v8a2 2 0 002 2h8a2 2 0 002-2V4a2 2 0 00-2-2H4zm8 10.5H4a.5.5 0 01-.5-.5V6.5h1.2a3.5 3.5 0 106.6 0H12.5v5.5a.5.5 0 01-.5.5zM8 11a2 2 0 110-4 2 2 0 010 4z"
mail_path = "M1.75 2A1.75 1.75 0 000 3.75v8.5C0 13.216.784 14 1.75 14h12.5A1.75 1.75 0 0016 12.25v-8.5A1.75 1.75 0 0014.25 2H1.75zM14.5 4.07l-6.5 4a.5.5 0 01-.5 0l-6.5-4A.5.5 0 011.5 3.5h13a.5.5 0 01.5.57zM1.5 5.5v6.75a.25.25 0 00.25.25h12.5a.25.25 0 00.25-.25V5.5l-6.25 3.84a1.5 1.5 0 01-1.5 0L1.5 5.5z"

create_button_svg("btn_portfolio.svg", "Portfolio", globe_path, 98)
create_button_svg("btn_leetcode.svg", "LeetCode", code_path, 105)
create_button_svg("btn_instagram.svg", "Instagram", insta_path, 115)
create_button_svg("btn_email.svg", "Email", mail_path, 80)


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

print("Successfully updated readme.md and generated SVGs.")
