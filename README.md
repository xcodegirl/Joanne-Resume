# Joanne Hoar — Resume Repository

Source data, generator script, and application packages for Joanne Hoar's professional resume.

---

## Repository Structure

```
Joanne-Resume/
├── generate_resume.py          ← run this to regenerate the resume
├── profile.xml                 ← contact info, summary, skills, languages
├── experience.xml              ← work history with achievements and tech stacks
├── education.xml               ← degrees, thesis, coursework
├── honors.xml                  ← awards and scholarships
├── publications.xml            ← academic papers and published games
├── service.xml                 ← community outreach and leadership
│
├── latex/                      ← generated .tex files and compiled PDFs
│   ├── developercv.cls         ← LaTeX class (developercv style)
│   ├── joanne_improved.tex     ← generated default resume
│   ├── joanne_improved.pdf     ← compiled default resume
│   └── ...                     ← application-specific variants
│
├── ufred-hci-application/      ← University of Fredericton HCI application package
│   ├── README.md
│   ├── cover-letter.md
│   ├── resume.md
│   └── teaching-philosophy.md
│
├── outlines/                   ← Robertson College course outline source files
├── courses/                    ← Robertson College course material archives
└── reports/                    ← Student evaluation reports
```

---

## Generating the Resume

All resume content lives in the XML source files. Edit those, then regenerate:

```bash
# Generate .tex only
python generate_resume.py

# Generate .tex and compile to PDF
python generate_resume.py --compile

# Custom output path
python generate_resume.py --output latex/custom_variant.tex --compile
```

**Requirements:** Python 3, MiKTeX (pdflatex). The pdflatex path is set near the top of `generate_resume.py` — update it if your MiKTeX installation is in a different location.

---

## XML Source Files

The XML files are the single source of truth. Edit them directly, then re-run the generator.

| File | Contents |
|---|---|
| `profile.xml` | Name, title, contact info, summary, skills |
| `experience.xml` | Each role: title, company, dates, achievements, technologies |
| `education.xml` | Degrees, institutions, thesis, relevant coursework |
| `honors.xml` | Awards, scholarships, nominations |
| `publications.xml` | Academic papers, published games, work sample links |
| `service.xml` | Community outreach, volunteer roles, leadership |

---

## Application Packages

Targeted application packages live in their own subfolders as Markdown, which renders natively on GitHub.

| Package | Role | Format |
|---|---|---|
| [`ufred-hci-application/`](ufred-hci-application/) | University of Fredericton — CPSC 2050 HCI Contract Faculty | Markdown |

---

## Style

The resume uses the [`developercv`](https://www.latextemplates.com/template/developer-cv) LaTeX class (MIT licence) with Raleway font and FontAwesome5 icons.

---

## Contact

**Joanne Hoar** · joanne.hoar@gmail.com · [linkedin.com/in/joanne-hoar](https://linkedin.com/in/joanne-hoar/) · [github.com/xcodegirl](https://github.com/xcodegirl)
