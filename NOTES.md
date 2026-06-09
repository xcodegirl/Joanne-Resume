# Notes — Joanne Hoar Resume Repository

*Maintained for Joanne and for any future AI assistant continuing this work.*  
*Last updated: 2026-06-09*

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

### 1. CPSC course names for TA role
The old CV (jkhoar-cv.pdf) lists two TA courses:
- **CPSC 203** — "Introduction to Computers"
- **CPSC 457** — "Principles of Operating Systems"

Joanne recalled three courses: *Introduction to Programming*, *Computing for Non-Majors*, and *Operating Systems*. CPSC 203 may have been known by multiple names, or there was a third course not on the old CV. The experience.xml entry currently reflects what Joanne recalled. **Verify course names and numbers if this becomes relevant** (e.g. for a U of C application where they'd recognise CPSC course codes).

### 2. Author order on ACM Crossroads paper ✓ VERIFIED
`Hoar, R., Penner, J.` — Ricardo first, Joanne second. Confirmed by Joanne 2026-06-09.
Note: Jacob is **not** an author on this paper — corrected from earlier incorrect entry of `Hoar, R., Jacob, C.`

### 3. Nickle Arts Museum / swarmart.com
Joanne confirmed her Bacterial Chemotaxis simulation art was displayed in the Gerald Hushlak exhibit alongside the web catalogue she built. Wonderful detail — preserve it.

### 4. "A Private Investor" on the old CV (March 2005 – present)
The old CV lists this as her first post-graduation role. This maps to **PlayStarMusic Corp.** — the investor was a private backer. No action needed unless the investor's identity becomes relevant.

### 5. French language level
Old CV says "advanced French." Current profile.xml says "intermediate." The old CV is from 2004 — her French may have drifted since. Current XML is the more conservative and probably more accurate claim. Worth a quick check if applying to bilingual roles.

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

## Pending Tasks (as of last session)

- [ ] **LinkedIn profile update** — Chrome extension was not connected during the session. Joanne's LinkedIn profile has not been reviewed or updated. The GitHub handle on LinkedIn may still say `xcodegirl` only (the work GitHub `jo-codegirl` should also be listed).
- [ ] **AI SME cover letter** — Joanne asked for a cover letter targeting an AI Subject Matter Expert role. Not yet built.
- [ ] **CBE / U of C Continuing Education posting** — Joanne asked about a possible technical writer role at CBE (Calgary Board of Education). Not pursued; user interrupted the fetch attempt. Revisit if still relevant.
- [ ] **PDF compilation check** — confirm `joanne_improved.pdf` renders cleanly with the now-longer publications section (5 papers) and new Nickle Arts Museum entry. May need a layout review.

---

## Application Packages

| Package | Folder | Status |
|---|---|---|
| University of Fredericton — CPSC 2050 HCI Contract Faculty | `ufred-hci-application/` | Complete; proofread |

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
| Papers published | 5 (all 2002–2003, under maiden name Penner) |
| Best paper award | ACAL 2003 — "Bacterial Chemotaxis in Silico" |
| NSERC award | Postgraduate Scholarship D3, 2005 |
| Governor General's Gold Medal | Departmental nomination, Faculty of Graduate Studies, 2005 |
