import os

def create_stats_svg():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="90" viewBox="0 0 800 90">
  <style>
    .card { fill: #ffffff; stroke: #d0d7de; stroke-width: 1; rx: 6; ry: 6; }
    .title { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 13px; fill: #57606a; font-weight: 500; text-anchor: middle; }
    .value { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 24px; fill: #24292f; font-weight: 600; text-anchor: middle; }
  </style>
  
  <rect x="0" y="0" width="250" height="85" class="card" />
  <text x="125" y="32" class="title">Repos</text>
  <text x="125" y="65" class="value">11</text>
  
  <rect x="275" y="0" width="250" height="85" class="card" />
  <text x="400" y="32" class="title">Contributions</text>
  <text x="400" y="65" class="value">120+</text>
  
  <rect x="550" y="0" width="250" height="85" class="card" />
  <text x="675" y="32" class="title">Streak</text>
  <text x="675" y="65" class="value">3 weeks</text>
</svg>"""
    with open("stats.svg", "w", encoding="utf-8") as f:
        f.write(svg)

def create_pin_svg(filename, title, desc, lang, lang_color, stars):
    # Book icon path from GitHub
    book_path = "M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"
    # Star icon path
    star_path = "M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z"

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="400" height="120" viewBox="0 0 400 120">
  <style>
    .card {{ fill: #ffffff; stroke: #d0d7de; stroke-width: 1; rx: 6; ry: 6; }}
    .title {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 14px; fill: #0969da; font-weight: 600; text-decoration: none; }}
    .desc {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 12px; fill: #57606a; }}
    .lang-text {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 12px; fill: #57606a; }}
    .icon {{ fill: #57606a; }}
  </style>
  <rect x="0.5" y="0.5" width="399" height="119" class="card" />
  
  <path class="icon" d="{book_path}" transform="translate(16, 16) scale(1)" />
  <text x="40" y="27" class="title">{title}</text>
  
  <text x="16" y="55" class="desc">
    <tspan x="16" dy="0">{desc[:50]}</tspan>
    <tspan x="16" dy="16">{desc[50:]}</tspan>
  </text>
  
  <circle cx="20" cy="95" r="5" fill="{lang_color}" />
  <text x="32" y="99" class="lang-text">{lang}</text>
  
  <path class="icon" d="{star_path}" transform="translate({32 + len(lang)*7.5 + 10}, 86) scale(1)" />
  <text x="{32 + len(lang)*7.5 + 30}" y="99" class="lang-text">{stars}</text>
</svg>"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg)

create_stats_svg()
create_pin_svg("pin1.svg", "AI-Agents-for-Business", "AI agents for business workflows using LangChain, OpenAI and Streamlit.", "Python", "#3572A5", "12")
create_pin_svg("pin2.svg", "CloudOptix", "Cloud cost optimization & anomaly detection platform with dashboard and alerts.", "TypeScript", "#3178C6", "7")

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

code_path = "M5.5 12.5L.5 8l5-4.5.8.7L2.2 8l4.1 3.8-.8.7zm5 0l-.8-.7L13.8 8l-4.1-3.8.8-.7 5 4.5-5 4.5z"
insta_path = "M4 2a2 2 0 00-2 2v8a2 2 0 002 2h8a2 2 0 002-2V4a2 2 0 00-2-2H4zm8 10.5H4a.5.5 0 01-.5-.5V6.5h1.2a3.5 3.5 0 106.6 0H12.5v5.5a.5.5 0 01-.5.5zM8 11a2 2 0 110-4 2 2 0 010 4z"
mail_path = "M1.75 2A1.75 1.75 0 000 3.75v8.5C0 13.216.784 14 1.75 14h12.5A1.75 1.75 0 0016 12.25v-8.5A1.75 1.75 0 0014.25 2H1.75zM14.5 4.07l-6.5 4a.5.5 0 01-.5 0l-6.5-4A.5.5 0 011.5 3.5h13a.5.5 0 01.5.57zM1.5 5.5v6.75a.25.25 0 00.25.25h12.5a.25.25 0 00.25-.25V5.5l-6.25 3.84a1.5 1.5 0 01-1.5 0L1.5 5.5z"

create_button_svg("btn_leetcode.svg", "LeetCode", code_path, 105)
create_button_svg("btn_instagram.svg", "Instagram", insta_path, 115)
create_button_svg("btn_email.svg", "Email", mail_path, 80)

# Build readme.md statically
readme = """# Hi, I'm Sunil 👋

Building AI agents and web apps • open to opportunities

---

**💻 Tech Stack**

<img src="https://img.shields.io/badge/Python-3776AB?style=flat" /> <img src="https://img.shields.io/badge/Django-092E20?style=flat" /> <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat" /> <img src="https://img.shields.io/badge/React-61DAFB?style=flat" /> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat" />

---

**🧑🏻‍💻 About me**

I'm an AI & Web Developer who enjoys building intelligent agents and modern web applications.
I work with LangChain, LLMs, Django, and React to solve real-world problems.
Always learning, always building.

---

**📊 GitHub stats**

<p align="center">
  <img src="./stats.svg" width="100%" />
</p>

---

**📌 Pinned projects**

<p align="center">
  <img src="./pin1.svg" width="48%" />
  <img src="./pin2.svg" width="48%" />
</p>

---

**🔗 Connect**

<a href="https://leetcode.com/u/sunilkumarrana"><img src="./btn_leetcode.svg" /></a> &nbsp; <a href="https://instagram.com/sunil_kumar_rana_01"><img src="./btn_instagram.svg" /></a> &nbsp; <a href="mailto:sunilkumarrana6592@gmail.com"><img src="./btn_email.svg" /></a>
"""

with open("readme.md", "w", encoding="utf-8") as f:
    f.write(readme)

print("Created completely static pixel-perfect SVGs and readme.md.")
