#!/usr/bin/env python3
"""
generate_resume.py
Reads Joanne's XML data files and generates joanne_improved.tex
using the developercv.cls style.

Usage:
    python generate_resume.py                        # generate .tex only
    python generate_resume.py --compile              # generate .tex and compile to PDF
    python generate_resume.py --output path/to.tex   # custom output path
"""

import xml.etree.ElementTree as ET
import os
import sys
import subprocess
import argparse

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LATEX_DIR  = os.path.join(SCRIPT_DIR, "latex")
DEFAULT_OUT = os.path.join(LATEX_DIR, "joanne_improved.tex")
PDFLATEX    = r"C:\Users\linux\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe"
MARKDOWN_DIR = os.path.join(SCRIPT_DIR, "markdown")
DEFAULT_MD   = os.path.join(MARKDOWN_DIR, "joanne_resume.md")

# ---------------------------------------------------------------------------
# LaTeX escaping
# ---------------------------------------------------------------------------
def t(text):
    """Escape a plain-text string for safe use in LaTeX body text."""
    if not isinstance(text, str) or not text:
        return ""
    # Normalise Unicode punctuation
    text = text.replace("‘", "'").replace("’", "'")
    text = text.replace("“", "``").replace("”", "''")
    text = text.replace("–", "--").replace("—", "---")
    text = text.replace(" ", " ")
    # Escape LaTeX special characters (backslash must come first)
    text = text.replace("\\", r"\textbackslash{}")
    for char, repl in [
        ("&",  r"\&"),
        ("%",  r"\%"),
        ("$",  r"\$"),
        ("#",  r"\#"),
        ("_",  r"\_"),
        ("{",  r"\{"),
        ("}",  r"\}"),
        ("~",  r"\textasciitilde{}"),
        ("^",  r"\textasciicircum{}"),
        ("<",  r"\textless{}"),
        (">",  r"\textgreater{}"),
    ]:
        text = text.replace(char, repl)
    return text

# ---------------------------------------------------------------------------
# XML helpers
# ---------------------------------------------------------------------------
def parse(filename):
    path = os.path.join(SCRIPT_DIR, filename)
    return ET.parse(path).getroot()

def txt(el, tag, default=""):
    child = el.find(tag)
    return (child.text or "").strip() if child is not None else default

# ---------------------------------------------------------------------------
# Data loaders
# ---------------------------------------------------------------------------
def load_profile():
    root = parse("profile.xml")
    pi   = root.find("personal_info")
    return {
        "name":        txt(pi, "name"),
        "title":       txt(pi, "title"),
        "email":       txt(pi, "email"),
        "phone":       txt(pi, "phone"),
        "location":    txt(pi, "location"),
        "linkedin":    txt(pi, "linkedin"),
        "github":      txt(pi, "github"),
        "github_work": txt(pi, "github_work"),
        "youtube":     txt(pi, "youtube"),
        "discord":     txt(pi, "discord"),
        "summary":     (root.find("summary").text or "").strip(),
        "skills":      root.find("skills"),
    }

def load_experience():
    root = parse("experience.xml")
    exps = []
    for exp in root.findall("experience"):
        achievements = [
            a.text.strip()
            for a in exp.findall("achievements/achievement")
            if a.text and a.text.strip()
        ]
        exps.append({
            "title":        txt(exp, "title"),
            "company":      txt(exp, "company"),
            "start":        txt(exp, "start_date"),
            "end":          txt(exp, "end_date"),
            "role_type":    txt(exp, "role_type"),
            "achievements": achievements,
            "technologies": txt(exp, "technologies"),
        })
    return exps

def load_education():
    root = parse("education.xml")
    degs = []
    for deg in root.findall("degree"):
        degs.append({
            "level":       txt(deg, "level"),
            "field":       txt(deg, "field"),
            "institution": txt(deg, "institution"),
            "start":       txt(deg, "start_year"),
            "end":         txt(deg, "graduation_year"),
            "thesis":      txt(deg, "thesis"),
            "coursework":  txt(deg, "relevant_coursework"),
        })
    return degs

def load_honors():
    root = parse("honors.xml")
    return [{
        "title": txt(h, "title"),
        "org":   txt(h, "organization"),
        "year":  txt(h, "year"),
    } for h in root.findall("honor")]

def load_publications():
    root = parse("publications.xml")
    result = {"academic": [], "games": [], "work_sample": ""}
    for p in root.findall("publication"):
        ptype = p.get("type", "")
        if ptype == "work_sample":
            result["work_sample"] = txt(p, "notes")
        elif ptype == "game":
            notes    = txt(p, "notes")
            platform = notes.replace("Platforms: ", "").split(".")[0].strip()
            result["games"].append({
                "title":    txt(p, "title"),
                "platform": platform,
                "year":     txt(p, "date"),
            })
        else:  # journal / conference
            result["academic"].append({
                "authors": txt(p, "authors"),
                "title":   txt(p, "title"),
                "venue":   txt(p, "venue"),
                "year":    txt(p, "date"),
                "notes":   txt(p, "notes"),
            })
    return result

def load_service():
    root = parse("service.xml")
    items = []
    for s in root.findall("service"):
        start = txt(s, "start_year")
        end   = txt(s, "end_year")
        if start == end:
            years = start
        elif end.lower() == "present":
            years = f"{start}--present"
        else:
            years = f"{start}--{end}"
        items.append({
            "role":  txt(s, "role"),
            "org":   txt(s, "organization"),
            "years": years,
        })
    return items

# ---------------------------------------------------------------------------
# Renderer
# ---------------------------------------------------------------------------
def render_markdown(profile, experiences, education, honors, publications, service):
    """Render a clean, GitHub-renderable Markdown resume from XML data."""
    L = []
    display_name = profile["name"].title()

    # ---- Header ----
    L += [
        f"# {display_name}",
        f"**{profile['title']}**",
        "",
    ]
    contact = []
    if profile["email"]:
        contact.append(f"[{profile['email']}](mailto:{profile['email']})")
    if profile["phone"]:
        contact.append(profile["phone"])
    if profile["location"]:
        contact.append(profile["location"])
    if contact:
        L.append("  ·  ".join(contact) + "  ")
    links = []
    if profile["linkedin"]:
        handle = profile["linkedin"].rstrip("/").split("/")[-1]
        links.append(f"[linkedin.com/in/{handle}]({profile['linkedin']})")
    gh1 = profile.get("github", "")
    gh2 = profile.get("github_work", "")
    if gh1:
        h1 = gh1.rstrip("/").split("/")[-1]
        links.append(f"[github.com/{h1}]({gh1})")
    if gh2:
        h2 = gh2.rstrip("/").split("/")[-1]
        links.append(f"[github.com/{h2}]({gh2})")
    if profile.get("youtube"):
        links.append(f"[YouTube: linuxcodegirl]({profile['youtube']})")
    if profile.get("discord"):
        links.append(f"Discord: {profile['discord']}")
    if links:
        L.append("  ·  ".join(links))
    L.append("")
    L.append("---")
    L.append("")

    # ---- Summary ----
    L += ["## Summary", "", profile["summary"].strip(), "", "---", ""]

    # ---- Skills ----
    skills_root = profile.get("skills")
    if skills_root is not None:
        L += ["## Technical Skills", ""]
        L += ["| Category | Skills |", "|---|---|"]
        for cat in skills_root.findall("category"):
            name = cat.get("name", "")
            if name == "Languages":
                continue  # rendered separately below
            skills = [sk.text.strip() for sk in cat.findall("skill") if sk.text]
            if skills:
                L.append(f"| **{name}** | {', '.join(skills)} |")
        L += ["", "---", ""]

    # ---- Experience ----
    L += ["## Experience", ""]
    for exp in experiences:
        date = f"{exp['start']} – {exp['end']}"
        L.append(f"### {exp['title']}  ·  {exp['company']}")
        L.append(f"**{date}**")
        if exp.get("role_type"):
            L.append(f"*{exp['role_type']}*")
        L.append("")
        for a in exp["achievements"]:
            L.append(f"- {a}")
        if exp["technologies"]:
            techs = [f"`{tech.strip()}`" for tech in exp["technologies"].split(",") if tech.strip()]
            L.append("")
            L.append("  ".join(techs))
        L += ["", "---", ""]

    # ---- Education ----
    L += ["## Education", ""]
    for deg in education:
        start = deg.get("start", "")
        end   = deg.get("end", "")
        date  = f"{start}–{end}" if start else end
        L.append(f"**{deg['level']}, {deg['field']}**  ·  {deg['institution']}  ·  {date}")
        if deg["thesis"]:
            L.append(f"*Thesis: {deg['thesis']}*")
        if deg["coursework"]:
            L.append(f"*Relevant coursework: {deg['coursework']}*")
        L.append("")
    L += ["---", ""]

    # ---- Publications ----
    academic = publications.get("academic", [])
    if academic:
        L += ["## Publications", ""]
        for pub in academic:
            note = f" *({pub['notes']})*" if pub.get("notes") else ""
            L.append(f"- {pub['authors']}. \"{pub['title']},\" *{pub['venue']}*, {pub['year']}.{note}")
        L += ["", "---", ""]

    # ---- Honours ----
    L += ["## Honours & Awards", ""]
    L += ["| Award | Organisation | Year |", "|---|---|---|"]
    for h in honors:
        L.append(f"| {h['title']} | {h['org']} | {h['year']} |")
    L += ["", "---", ""]

    # ---- Service ----
    L += ["## Community Outreach & Leadership", ""]
    for s in service:
        org = f", {s['org']}" if s["org"] else ""
        L.append(f"- {s['role']}{org} · {s['years']}")
    L += ["", "---", ""]

    # ---- Languages ----
    if skills_root is not None:
        for cat in skills_root.findall("category"):
            if cat.get("name") == "Languages":
                L += ["## Languages", ""]
                for sk in cat.findall("skill"):
                    if sk.text:
                        lang = sk.text.strip()
                        if "(" in lang:
                            name_part, prof = lang.split("(", 1)
                            L.append(f"- **{name_part.strip()}** — {prof.rstrip(')')}")
                        else:
                            L.append(f"- **{lang}**")
                L += ["", "---", ""]

    # ---- Published Games ----
    games = publications.get("games", [])
    if games:
        L += ["## Published Interactive Applications", ""]
        L.append("*Silicon Hanna Inc. (founded as SuRJE Software Solutions Inc.)*")
        L.append("")
        L += ["| Title | Platform | Year |", "|---|---|---|"]
        for g in games:
            L.append(f"| {g['title']} | {g['platform']} | {g['year']} |")
        L += ["", "---", ""]

    # ---- Work Samples ----
    if publications.get("work_sample"):
        url = publications["work_sample"]
        L += ["## Work Samples", ""]
        L.append(f"[xcodegirl/career — work-samples]({url})")
        L.append("")

    return "\n".join(L)


def render(profile, experiences, education, honors, publications, service):
    L = []

    # ---- Preamble ----
    display_name = profile["name"].title()
    L += [
        f"% Resume: {display_name}  |  generated by generate_resume.py",
        r"% Edit the XML source files, then re-run this script to regenerate.",
        r"",
        r"\documentclass[9pt]{developercv}",
        r"\usepackage{enumitem}",
        r"\begin{document}",
        r"",
    ]

    # ---- Header ----
    parts = display_name.split()
    first = t(parts[0])  if parts          else ""
    last  = t(parts[-1]) if len(parts) > 1 else ""

    L += [
        r"% ===== HEADER =====",
        r"\begin{minipage}[t]{0.45\textwidth}",
        f"\\colorbox{{gray}}{{\\HUGE\\textcolor{{white}}{{\\textbf{{{first}}}}}}} \\\\",
        f"\\colorbox{{gray}}{{\\HUGE\\textcolor{{white}}{{\\textbf{{{last}}}}}}}",
        r"\end{minipage}",
        r"\begin{minipage}[t]{0.275\textwidth}",
    ]
    if profile["location"]:
        L.append(f"\\icon{{MapMarker}}{{12}}{{{t(profile['location'])}}}\\\\")
    if profile["phone"]:
        ph = profile["phone"].replace(" ", "")
        L.append(f"\\icon{{Phone}}{{12}}{{\\href{{tel:{ph}}}{{{t(profile['phone'])}}}}}\\\\")
    if profile["email"]:
        em = profile["email"]
        L.append(f"\\icon{{At}}{{12}}{{\\href{{mailto:{em}}}{{{em}}}}}\\\\")
    L.append(r"\end{minipage}")
    L.append(r"\begin{minipage}[t]{0.275\textwidth}")
    if profile["linkedin"]:
        L.append(f"\\icon{{Globe}}{{12}}{{\\href{{{profile['linkedin']}}}{{linkedin: joanne-hoar}}}}\\\\")
    gh1 = profile.get("github", "")
    gh2 = profile.get("github_work", "")
    if gh1 and gh2:
        h1 = gh1.rstrip("/").split("/")[-1]
        h2 = gh2.rstrip("/").split("/")[-1]
        L.append(f"\\icon{{Github}}{{12}}{{\\href{{{gh1}}}{{{h1}}} / \\href{{{gh2}}}{{{h2}}}}}\\\\")
    elif gh1:
        h1 = gh1.rstrip("/").split("/")[-1]
        L.append(f"\\icon{{Github}}{{12}}{{\\href{{{gh1}}}{{{h1}}}}}\\\\")
    if profile["youtube"]:
        L.append(f"\\icon{{Youtube}}{{12}}{{\\href{{{profile['youtube']}}}{{linuxcodegirl}}}}\\\\")
    if profile["discord"]:
        L.append(f"\\icon{{Discord}}{{12}}{{{t(profile['discord'])}}}\\\\")
    L += [
        r"\end{minipage}",
        r"",
        f"{{\\huge {t(profile['title'])}}}",
        r"",
    ]

    # ---- Summary ----
    L += [
        r"% ===== SUMMARY =====",
        r"\cvsect{Who Am I?}",
        t(profile["summary"]),
        r"",
    ]

    # ---- Experience ----
    L += [r"% ===== EXPERIENCE =====", r"\cvsect{Experience}", r"\begin{entrylist}"]
    for exp in experiences:
        date    = t(f"{exp['start']} -- {exp['end']}")
        title   = t(exp["title"])
        company = t(exp["company"])

        desc_parts = []
        if exp["achievements"]:
            desc_parts.append(
                r"\begin{itemize}[noitemsep,topsep=2pt,leftmargin=1em,parsep=0pt]"
            )
            for a in exp["achievements"]:
                desc_parts.append(f"  \\item {t(a)}")
            desc_parts.append(r"\end{itemize}")
        if exp["technologies"]:
            techs = [
                f"\\texttt{{{t(tech.strip())}}}"
                for tech in exp["technologies"].split(",")
                if tech.strip()
            ]
            desc_parts.append("\\slashsep".join(techs))

        desc = "\n\t\t\t".join(desc_parts)
        L += [
            "\t\\entry",
            f"\t\t{{{date}}}",
            f"\t\t{{{title}}}",
            f"\t\t{{{company}}}",
            f"\t\t{{{desc}}}",
        ]
    L += [r"\end{entrylist}", r""]

    # ---- Education ----
    L += [r"% ===== EDUCATION =====", r"\cvsect{Education}", r"\begin{entrylist}"]
    for deg in education:
        start = deg.get("start", "")
        end   = deg.get("end",   "")
        date  = t(f"{start}--{end}") if start else t(end)
        desc  = t(deg["field"])
        if deg["thesis"]:
            desc += f"\\\\[2pt]\\footnotesize{{\\textit{{Thesis:}} {t(deg['thesis'])}}}"
        if deg["coursework"]:
            desc += f"\\\\\\footnotesize{{\\textit{{Coursework:}} {t(deg['coursework'])}}}"
        L += [
            "\t\\entry",
            f"\t\t{{{date}}}",
            f"\t\t{{{t(deg['level'])}}}",
            f"\t\t{{{t(deg['institution'])}}}",
            f"\t\t{{{desc}}}",
        ]
    L += [r"\end{entrylist}", r""]

    # ---- Publications ----
    if publications["academic"]:
        L += [r"% ===== PUBLICATIONS =====", r"\cvsect{Selected Publications}"]
        for pub in publications["academic"]:
            note_str = (
                f" \\textit{{({t(pub['notes'])})}}" if pub["notes"] else ""
            )
            L.append(
                f"$\\bullet$ {t(pub['authors'])}. ``{t(pub['title'])},'' "
                f"\\textit{{{t(pub['venue'])}}}, {t(pub['year'])}.{note_str}\\\\"
            )
        L.append(r"")

    # ---- Honours ----
    L += [r"% ===== HONOURS =====", r"\cvsect{Honours \& Awards}"]
    for h in honors:
        org  = f", {t(h['org'])}"  if h["org"]  else ""
        year = f", {t(h['year'])}" if h["year"] else ""
        L.append(f"$\\bullet$ {t(h['title'])}{org}{year}\\\\")
    L.append(r"")

    # ---- Service ----
    L += [r"% ===== SERVICE =====", r"\cvsect{Community Outreach \& Leadership}"]
    for s in service:
        org = f", {t(s['org'])}" if s["org"] else ""
        L.append(f"$\\bullet$ {t(s['role'])}{org}, {t(s['years'])}\\\\")
    L.append(r"")

    # ---- Languages + Work Samples | Published Games (two-column) ----
    L += [r"% ===== LANGUAGES / GAMES =====", r"\begin{minipage}[t]{0.45\textwidth}"]
    L.append(r"\cvsect{Languages}")
    skills_root = profile.get("skills")
    if skills_root is not None:
        for cat in skills_root.findall("category"):
            if cat.get("name") == "Languages":
                for sk in cat.findall("skill"):
                    if sk.text:
                        lang = sk.text.strip()
                        if "(" in lang:
                            name_part, prof = lang.split("(", 1)
                            L.append(
                                f"\\textbf{{{t(name_part.strip())}}} --- "
                                f"{t(prof.rstrip(')'))}\\\\")
                        else:
                            L.append(f"\\textbf{{{t(lang)}}}\\\\")

    if publications.get("work_sample"):
        url = publications["work_sample"]
        L += [
            r"",
            r"\cvsect{Work Samples}",
            f"\\icon{{Github}}{{12}}{{\\href{{{url}}}{{xcodegirl/career: work-samples}}}}.",
        ]
    L.append(r"\end{minipage}")
    L.append(r"\hfill")

    L.append(r"\begin{minipage}[t]{0.5\textwidth}")
    L.append(r"\cvsect{Published Interactive Applications}")
    L.append(r"\footnotesize{\textit{Silicon Hanna Inc. (founded as SuRJE Software Solutions Inc.)}}\\[4pt]")
    for g in publications["games"]:
        L.append(f"$\\bullet$ {t(g['title'])} --- {t(g['platform'])} ({t(g['year'])})\\\\")
    L += [r"\end{minipage}", r""]

    L.append(r"\end{document}")
    return "\n".join(L)

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Generate Joanne's resume from XML source files."
    )
    parser.add_argument(
        "--format", choices=["tex", "md", "all"], default="tex",
        help="Output format: tex (default), md, or all (both)"
    )
    parser.add_argument(
        "--output",
        help="Custom output path (overrides default for the chosen format)"
    )
    parser.add_argument(
        "--compile", action="store_true",
        help="Compile the generated .tex to PDF using pdflatex (tex/all only)"
    )
    args = parser.parse_args()

    print("Reading XML source files...")
    profile      = load_profile()
    experiences  = load_experience()
    education    = load_education()
    honors       = load_honors()
    publications = load_publications()
    service      = load_service()

    do_tex = args.format in ("tex", "all")
    do_md  = args.format in ("md",  "all")

    # ---- LaTeX ----
    if do_tex:
        tex_path = os.path.abspath(args.output if args.output and not do_md else DEFAULT_OUT)
        os.makedirs(os.path.dirname(tex_path), exist_ok=True)
        print("Generating LaTeX...")
        tex = render(profile, experiences, education, honors, publications, service)
        with open(tex_path, "w", encoding="utf-8") as f:
            f.write(tex)
        print(f"  Written: {tex_path}")

        if args.compile:
            out_dir = os.path.dirname(tex_path)
            print("Compiling with pdflatex...")
            result = subprocess.run(
                [PDFLATEX, "-interaction=nonstopmode",
                 f"-output-directory={out_dir}", tex_path],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                pdf = tex_path.replace(".tex", ".pdf")
                print(f"  PDF generated: {pdf}")
            else:
                errors = [l for l in result.stdout.splitlines() if l.startswith("!")]
                print("  pdflatex errors:")
                for e in errors:
                    print(f"    {e}")
                print("  (check the .log file for details)")

    # ---- Markdown ----
    if do_md:
        md_path = os.path.abspath(args.output if args.output and not do_tex else DEFAULT_MD)
        os.makedirs(os.path.dirname(md_path), exist_ok=True)
        print("Generating Markdown...")
        md = render_markdown(profile, experiences, education, honors, publications, service)
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"  Written: {md_path}")

if __name__ == "__main__":
    main()
