# Notes — Joanne Hoar Resume Repository

*Maintained for Joanne and for any future AI assistant continuing this work.*  
*Last updated: 2026-06-11*

---

## Who This Is

**Joanne K. Hoar** (née **Penner**) — senior software developer, technology educator, and indie game developer based in Hanna, Alberta (remote). Academic publications are under the name **Penner**; all professional and personal use is **Hoar**.

Her husband is **Ricardo Hoar** — they co-founded SuRJE / Silicon Hanna together, and co-author on several papers. Ricardo appears frequently in the record; do not conflate their credits.

---

## Company Identity: SuRJE = Silicon Hanna

This confused an earlier session and will confuse future ones.

- **SuRJE Software Solutions Inc.** and **Silicon Hanna Inc.** are the **same company** at different points in time.
- Founded as SuRJE (backronym: *Swarms under Ricardo and Joanne using Evolution* — a nod to their graduate research in agent-based systems).
- Renamed **Silicon Hanna Inc.** after relocating the studio to Hanna, Alberta.
- Operated **2005–2022**, self-employed, concurrent with:
  - BJ Pipeline full-time employment (2005–2008)
  - Fekete Associates full-time employment (2008–2011)
  - Primary focus from 2011 until joining bitHeads in 2022.
- These are **one entry** in experience.xml — do not split them.

---

## The HCI Career Thread

Joanne's entire career has a continuous HCI spine. When writing application materials, connect these dots:

| Year | Role | HCI Relevance |
|---|---|---|
| 2002 | Nickle Arts Museum web dev | Interactive online catalogue; own generative art exhibited |
| 2004–05 | Codefast | Primary mandate: build GUIs for CLI tools |
| 2005–06 | PlayStarMusic | End-user streaming interface, purchase flow, seamless DRM UX |
| 2005–08 | BJ Pipeline | 3D OpenGL viz for analysts; Excel→LAMP port with interactive maps/forms for non-technical stakeholders |
| 2008–11 | Fekete | MFC UI tools library used as foundation for all internal products |
| 2005–22 | Silicon Hanna | Mobile game UX, touch interfaces, ARKit spatial UI |
| 2022–25 | bitHeads | Widget libraries across 7 UI frameworks (Dear ImGui, UMG, SwiftUI, Android Views, Unity, PlayStation SDK) |
| 2025– | Robertson College | Teaching front-end UI development online |

---

## Things Needing Joanne's Verification

### 1. CPSC course names for TA role ✓ CONFIRMED
The old CV (jkhoar-cv.pdf) lists two TA courses:
- **CPSC 203** — "Introduction to Computers" (confirmed from CV — Joanne recalled this as "Computing for Non-Majors"; official name is Introduction to Computers)
- **CPSC 457** — "Principles of Operating Systems" (confirmed)

Joanne also recalled a third course (Introduction to Programming) not listed on the old CV. experience.xml currently uses Joanne's recalled names. If course codes ever matter (e.g. U of C application), use CPSC 203 and CPSC 457.

### 2. Author order on ACM Crossroads paper ✓ VERIFIED
`Hoar, R., Penner, J.` — Ricardo first, Joanne second. Confirmed by Joanne 2026-06-09.
Note: Jacob is **not** an author on this paper — corrected from earlier incorrect entry of `Hoar, R., Jacob, C.`

### 3. Nickle Arts Museum / swarmart.com
Joanne confirmed her Bacterial Chemotaxis simulation art was displayed in the Gerald Hushlak exhibit alongside the web catalogue she built. Wonderful detail — preserve it.

### 4. "A Private Investor" on the old CV (March 2005 – present)
The old CV lists this as her first post-graduation role. This maps to **PlayStarMusic Corp.** — the investor was a private backer. No action needed unless the investor's identity becomes relevant.

### 5. French language level
Old CV says "advanced French." Current profile.xml says "intermediate." The old CV is from 2004 — her French may have drifted since. Current XML is the more conservative and probably more accurate claim. Worth a quick check if applying to bilingual roles.

### 6. AIIIM 2026 and Robertson academic integrity training ✓ CONFIRMED
Confirmed 2026-06-11: Joanne completed academic integrity training at Robertson and participated in the **Academic Integrity Inter-Institutional Meeting (AIIIM 2026)**. Her takeaways: "authentic" learning and assessment (assignments grounded in real local contexts that generic AI output cannot satisfy), scaffolded assignments with checkpoints, developing ethical AI use, developing professional judgment of AI output, and peer review/peer grading. Now cited in the AI SME resume (md + tex + pdf) and initial email. Strong material for any AI/teaching application; also a candidate for the LD application.

---

## Known Omissions (Deliberate)

- **"50+ students per term"** — removed from the Robertson entry. Joanne was uncertain of the accuracy. Do not re-add without confirming.
- **Nickle Arts Museum** is a short 3-month contract. It is included because of the dual engineering + art exhibited angle. If the resume runs long, it is a candidate for trimming on general-purpose versions (keep on HCI-targeted versions).
- **ATT Program Committee (AAMAS 2004)** — peer-reviewed submissions to the Agents in Traffic and Transportation workshop. Short entry in service.xml; not surfaced in the HCI application resume. Worth adding to any academic CV.

---

## Source of Truth Hierarchy

```
experience.xml          ← authoritative for all work history
publications.xml        ← authoritative; now has all 5 papers with correct author names
honors.xml              ← authoritative; now has 8 entries including travel grants
service.xml             ← authoritative
profile.xml             ← authoritative
education.xml           ← authoritative; has start years and M.Sc. coursework

generate_resume.py      ← reads all 6 XML files → latex/joanne_improved.tex → optional PDF
ufred-hci-application/  ← manually maintained Markdown; must be kept in sync with XML
```

**Do not use** `resume-formatter/jhoar-data.json` — it was the old data source and has been superseded. The file no longer exists in this repo. The resume-formatter app reads it but produces a stale resume.

---

## Session Log: Gemini Pass + Claude Revision (2026-06-11)

Gemini revised `ufred-ai-sme-application/resume.md` (commit `54c203c`) but did not regenerate the PDF. A Claude session the same day assessed each change and made another pass:

**Kept from Gemini:** "Joanne Hoar, M.Sc." title (smart given the Ph.D.-preferred posting); spelled-out conference names in publications and honours (helps non-CS business readers); bolded **Penner, J.** in publications; "career-changing adult learners" detail; the AIIIM 2026 reference and assessment-design themes (confirmed real by Ricardo 2026-06-11 — see Verification #6), rewritten in plain language.

**Reverted from Gemini:** em dashes (banned); US spellings ("specialize", "modeling"); buzzword inflation ("Advanced deployment", "hyper-local", "non-invertible", "utilizing", "upskill", bold label on every bullet); false claims ("structural engineering concepts" as a TA; Silicon Hanna as "consulting practice for regional business clients" — it was games; "Managed cross-team communication for major business integrations"); deletion of verified evidence (Perkins et al. framework, AI-code citation examples, ToS/copyright specifics, "hired in part for educational background", the "(published under maiden name Penner)" note).

**Also done:** all em dashes removed from the .tex; resume rebalanced to 3 pages at 10pt/0.7in margins; PDF recompiled and re-synced to `ufred-ai-sme-application/joanne_hoar_resume.pdf`; AIIIM sentence added to `initial-email.md`; accidental `$outdir/` build folder deleted.

**Completeness pass (same day):** fixed markdown hard line breaks in resume.md; brought resume.md to parity with the PDF (5 honours, 5 publications, UDL spelled out); wrote `ufred-ai-sme-application/cover-letter.md` in the formal register, held until Dr. Khaliq responds; added a package README; listed all three packages in the repo README. Created a reusable **jo-voice skill** at `C:\Users\linux\.claude\skills\jo-voice\SKILL.md` distilling the Writing Voice section below - future sessions can invoke it when drafting anything in Joanne's voice (NOTES.md remains the master copy).

---

## Pending Tasks (as of last session)

- [x] **UFred AI SME application** — package built in `ufred-ai-sme-application/`. **Next action: send `initial-email.md` to Amna.Khaliq@UFred.ca.** Deadline was May 21 but posting still live; acknowledge gracefully in email. Contact is Dr. Amna Khaliq (named, warm outreach appropriate).
- [ ] **LinkedIn profile update** — Chrome extension was not connected during the session. Joanne's LinkedIn profile has not been reviewed or updated. The GitHub handle on LinkedIn may still say `xcodegirl` only (the work GitHub `jo-codegirl` should also be listed).
- [ ] **CBE / U of C Continuing Education posting** — Joanne asked about a possible technical writer role at CBE (Calgary Board of Education). Not pursued; user interrupted the fetch attempt. Revisit if still relevant.
- [ ] **PDF compilation check** — confirm `joanne_improved.pdf` renders cleanly with the now-longer publications section (5 papers) and new Nickle Arts Museum entry. May need a layout review.

---

## Application Packages

| Package | Folder | Status |
|---|---|---|
| University of Fredericton — CPSC 2050 HCI Contract Faculty | `ufred-hci-application/` | Complete; proofread |
| University of Fredericton — Learning Design Consultant (closes Jun 26, 2026) | `ufred-ld-application/` | Complete; proofread |
| University of Fredericton — AI SME / Course Developer (deadline passed, post still live) | `ufred-ai-sme-application/` | Complete — initial email ready to send to Dr. Amna Khaliq (Amna.Khaliq@UFred.ca); follow-up cover letter drafted; PDF in sync |

---

## Key Work Samples

| Sample | Location | Notes |
|---|---|---|
| Academic Integrity slideshow | `C:\Users\linux\Downloads\Academic Integrity.txt` | Slide deck for student-facing sessions on citing code, AI tools, and integrity at scale. Uses a 3-level AI assessment scale (Perkins et al. 2024). 7 citation examples including AI-generated code. Strong evidence for AI pedagogy and curriculum design. Cite in UFred LD and AI SME applications. |
| Course outlines (7 courses) | `outlines/*.md` | Clean markdown versions of all Robertson College course outlines: T0507 Git, T0508 C#, T0509 .NET, T0502 OOP/Java, T0510 ASP.NET Core, T0511 FEF, B0979 Data Collection |
| Public course materials | [github.com/xcodegirl](https://github.com/xcodegirl) | Open-source course materials, sample code, and corrected live-session examples |
| Work samples index | [github.com/xcodegirl/career — xcodegirl-work-samples.md](https://github.com/xcodegirl/career/blob/main/xcodegirl-work-samples.md) | Master index of work samples |

---

## Joanne's Writing Voice

*Built from actual writing samples: Getty cover letter (2022), Special Areas cover letter, Arista cover letter, Wizards/Hasbro cover letter, skills questionnaire (C++/OpenGL/Qt), teaching philosophy statement, spice blend gift booklet. Future AI: do not revert to AI defaults - use these patterns.*

### Two registers - she code-switches deliberately

**Formal register** (universities, government, academic):
- No contractions: "I am", "I would", "I have", "I will"
- Opens with: "I am interested in [role] and feel that I would be a great fit within [org] as a [title]"
- Second paragraph: "I am formally educated in Computer Science and am an experienced software developer, with additional experience in [relevant area]"
- Transition: "Please find my resume attached. I have demonstrated success in..."
- Closes with: "Thank you for considering me to become a member of your team, Joanne Hoar"
- No bullet points in cover letters - flowing paragraphs
- No bold headers in cover letter body

**Casual register** (tech companies, creative companies, startups):
- Contractions throughout: "I'm", "I've", "I'd", "I'll", "I know I'll fit in"
- Opens directly: "My name is Joanne, I'm a software developer in Alberta"
- Mentions specific product/company details that prove she did her homework
- Closes by opening a door: "I'd love to find out more!", "I would love to tell you more stories", "Contact me with a time to meet"

### Punctuation
- **No em dashes** - she has never used one in pre-AI writing; confirmed across all samples
- Normal hyphen with spaces for a dash: "Don't worry - I've been working"
- Comma-heavy, long clauses chained naturally
- Parenthetical asides: "(now S&P Global)", "(a huge shock since I was leading the Client API team)"
- Scare quotes: "vibe coding", "impossible", "really neat"
- "et cetera" written out
- Exclamation marks used genuinely when excited, not decoratively

### Self-promotion style
- Confident but not aggressive: "I feel that I would be a great fit", "I know I'll fit in well"
- Honest about gaps with immediate pivot to learning ability: "somewhat familiar", "a bit of dust on my hat", "I am a fast and thorough learner so have no fear"
- Enthusiasm is specific and earned: "The EOS is really neat", "I was genuinely excited to see this in my inbox this morning"
- Names people, supervisors, colleagues: Dr. Jacob, Dr. Prusinkiewicz, Dr. Hushlak, Kevin Jameson

### Humour and personality
- Self-deprecating: "a fair amount of cussing about timing", "This is a first revision after all!"
- Playful self-corrections: "I play it by ear, er I mean tastebud"
- Dry observations: "I'm neither Vietnamese nor French Canadian so I'm not sure if I was even allowed to do this"
- Parenthetical jokes: "(choose a mortar and pestle if you need exercise, have a lot of free time or are old-fashioned)"
- Rhetorical questions: "How much more can I think of?"

### Personal context
- Mentions family naturally and without apology: three children including a neurodivergent son, husband Ricardo, rural Alberta, Hanna
- "Truly" as a sentence opener when expressing genuine feeling
- Builds arguments from first principles before arriving at the personal
- Instructional writing is naturally clear, practical, and engaging - she writes good how-to content

### Signs off as
- "Joanne Hoar" on formal applications (cover letters, CVs)
- "Joanne" in semi-formal professional writing
- "Jo" broadly - warm outreach emails, students, anyone she wants to be friends with, Facebook, meeting people in person. Not reserved for close friends only - it's her general informal identity. Use "Jo Hoar" when the register is warm/personal rather than formal.

### What AI writes that she doesn't
- Em dashes (---)
- "I am passionate about"
- "I would welcome the opportunity"
- "not peripheral to my work - they are central to it" (dramatic contrast constructions)
- Bold paragraph headers in cover letters
- "I am comfortable with [gerund phrase]"
- Perfect parallel bullet lists with identical grammatical structure
- "an uncommon combination of"
- "I bring X and Y to this role"

---

## Style and Tone Notes

- **Canadian English** throughout: "Honours", "organisation", "student-centred", "well-organised"
- Spell out numbers under 10; spell out round numbers: "more than twenty years"
- Avoid "passionate about" — show it through the work
- The Bacterial Chemotaxis art-in-gallery detail is a genuine differentiator — lead with it when writing creative/HCI applications
- Robertson satisfaction rating is **4.5/5.0** — use the exact figure, not a rounded description
- The `\maiden name` note on publications is internal (XML `<notes>` field only) — do not print it on the face of the resume; the published record speaks for itself

---

## Quick Reference — Key Facts

| | |
|---|---|
| Current role | Technology Instructor, Robertson College (contract, Jan 2025–present) |
| Location | Hanna, Alberta (fully remote) |
| Years experience | 20+ (since 2004) |
| Degrees | M.Sc. Computer Science, U of C, 2004; B.Sc. Computer Science, U of C, 2001 |
| Thesis | Agent-based Development of Natural Transportation Networks |
| M.Sc. supervisor | Dr. Christian Jacob |
| VLAB supervisor | Dr. Przemyslaw Prusinkiewicz |
| TA supervisors | Craig Schock (CPSC 203), Dr. Jim Bradley (CPSC 457) |
| Games published | 11 titles (2008–2020), iOS and Android, under SuRJE / Silicon Hanna |
| Games unreleased | 2 additional titles in development, never shipped: Climate Crisis (old-west resource/economy/open-world, starring historical Albertan cowboy John Ware) and Cubey (open-world math-learning game, original story where Zero saves the world) |
| Papers published | 5 (all 2002–2003, under maiden name Penner) |
| Best paper award | ACAL 2003 — "Bacterial Chemotaxis in Silico" |
| NSERC award | Postgraduate Scholarship D3, 2005 |
| Governor General's Gold Medal | Departmental nomination, Faculty of Graduate Studies, 2005 |
