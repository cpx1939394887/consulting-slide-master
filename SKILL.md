---
name: consulting-slide-master
description: Create consulting-grade, high-density executive PowerPoint decks from complex business materials. Use for strategy reviews, operating reviews, investment reviews, post-investment evaluations, turnaround plans, board decks, business diagnosis, market research, and management decision presentations. This skill combines consulting reasoning, evidence-to-claim workflows, McKinsey/BCG-inspired visual systems, a decomposed 10,000+ PPT component library architecture, content-driven layout recomposition, and rendered contact-sheet QA. Do not use for simple decorative slides, generic marketing decks, or template-only PPT generation.
metadata:
  short-description: Consulting-grade executive PowerPoint decks
  maturity_tier: production
  artifact_family: executive-consulting-presentation
---

# Consulting Slide Master

Most AI slide tools start from a template.

This skill starts from the management question.

## Own The Following Job

- Read complex business materials and build an evidence library.
- Convert evidence into consulting-style executive claims.
- Treat every slide as a proof unit, not a content box.
- Search across decomposed PPT component roles instead of obeying one fixed template.
- Recompose slides based on content logic.
- Apply a restrained McKinsey/BCG-inspired visual system.
- Build dense but readable editable PPTX decks.
- Render previews, generate a contact sheet, self-review, and revise weak pages before delivery.

## Do Not Route Here

- Simple decorative slide beautification
- Generic marketing landing decks
- Pure image-heavy brand storytelling
- One-off chart rendering without a deck
- File conversion without slide reasoning
- School assignments or casual topic decks unless the user explicitly wants consulting-style business slides

## Default Workflow

1. Read `references/consulting-thinking-method.md`.
2. Build evidence using `references/evidence-to-claim-workflow.md`.
3. Identify the executive decision question and claim spine.
4. Plan each slide with `references/page-proof-model.md`.
5. Choose slide structures using `references/content-to-layout-decision-tree.md`.
6. Search component roles using `component-library/component-taxonomy.md`.
7. Apply `references/consulting-color-system.md`.
8. Apply density rules from `references/density-and-hierarchy-rules.md`.
9. Build an editable PowerPoint deck.
10. Render slide previews.
11. Generate a contact sheet.
12. Validate against `references/contact-sheet-qa.md`.
13. Revise weak slides before final delivery.

## Hard Rules

- Every slide title must be a conclusion sentence.
- Every slide must answer one management question.
- Every slide must have one primary proof object.
- Do not repeat one fixed page layout across the deck.
- Do not force fixed bottom "So What" boxes unless the content naturally needs them.
- Do not use a template as a cage; decompose and recompose components based on content.
- Default minimum font size is 12 pt unless the user explicitly allows smaller type.
- All numbers must carry source, unit, time, and scope notes.
- If source data conflicts, mark the issue as a scope or definition difference rather than silently choosing one value.
- Generate rendered previews and a contact sheet before handoff.

## Output Contract

For substantial deck creation, deliver:

- editable `.pptx`
- rendered preview images
- `contact_sheet.jpg`
- evidence library or source notes
- quality report or self-check notes
- optional speaker notes, executive Q&A, and data gap list when requested

