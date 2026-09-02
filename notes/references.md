# References

Authoritative sources for claims made in this seminar about AI vendors' products and about Notre Dame policy/access. Per [CLAUDE.md](../CLAUDE.md), track an access date and flag anything not confirmed via a primary source.

## Anthropic / Claude

- [Claude Team Plan for Scientists](https://claude.com/programs/team-plan-for-scientists) — the program this seminar's "Why Claude?" hook refers to. Fetched 2026-09-02. Key facts: standard seats free for 12 months (regularly $20/mo), premium seats $15/mo (regularly $100/mo, 5x usage); PIs at accredited universities/nonprofit research institutes in natural sciences, math, CS, engineering, and related fields apply via an online attestation form, reviewed in ~5–7 business days; excludes for-profit/CRO/industry R&D; capped at 10,000 scientists globally; 1–25 seats per group without contacting sales; promotional pricing can lapse after 90 days of group inactivity. **Re-check before the talk** — pricing/eligibility programs like this can change terms.
- Claude Code, Claude Projects — general product documentation, not yet linked here. TODO: add direct doc links when building the ecosystem slide.

## OpenAI

- ChatGPT, ChatGPT Projects, Codex — general product documentation, not yet linked here. TODO before the ecosystem slide is finalized.

## Google

- Gemini, NotebookLM — general product documentation, not yet linked here. TODO before the ecosystem slide is finalized.
- [Notre Dame gives students access to Google AI tools (Gemini and NotebookLM) — The Observer, April 2025](https://www.ndsmcobserver.com/article/2025/04/notre-dame-gives-students-access-to-google-ai-tools-gemini-and-notebooklm) — student-newspaper reporting, not a primary university source; use for color, verify current status against an ND primary source before citing specifics.

## Notre Dame — AI access and policy

**Tooling note:** the `WebFetch` tool cannot reach `ai.nd.edu` (TLS "unable to get issuer certificate" error, reproduced on multiple pages). The in-app Browser tool (real browser engine) loads it fine. If revisiting these pages in a future session, use the browser, not `WebFetch`.

Confirmed by direct browser read on 2026-09-02 (superseding the earlier search-snippet-only version of this section):

- [AI@ND hub](https://ai.nd.edu/) — Notre Dame's central AI resource site (AI Enablement team).
- [AI@ND — Policies and Guidelines](https://ai.nd.edu/ai-in-action/policies-and-guidelines/). Core rules: work within existing University policy (Responsible Use of Data & IT Resources Policy; students under the Generative AI Policy for Students); most Hesburgh Library third-party license agreements **prohibit** data-mining/AI use on licensed journal articles/e-books without publisher permission (contact `csa-er-management-list@nd.edu` before doing this); protect confidential/copyrighted/personal information — treat entering data into an AI tool as similar to posting it publicly; University information may only be used with an AI tool if the information is classified **Public**, or the tool has completed internal review with data-protection contract terms in place (see Approved AI Tools); users are 100% responsible for AI output and must disclose/document AI use in Notre Dame research, scholarship, or work.
- [AI@ND — Approved AI Tools](https://ai.nd.edu/ai-in-action/approved-ai-tools/). Introduces a four-tier data classification, each tagged with an AI-use verdict:
  - 🟢 **Public** — safe for AI
  - 🟡 **Internal** — safe for AI
  - 🟠 **Sensitive** — safe for AI (role-restricted info; serious privacy/operational risk if leaked)
  - 🔴 **Restricted** — **prohibited** (SSNs, credit cards, health data — never enter into any AI tool)

  "Core AI tools" cleared through Public/Internal/Sensitive: **Google Gemini** (free, all faculty/staff, integrated with Workspace), **ChatGPT EDU** (by request + annual fee, includes agent builder), **NotebookLM** (free, all faculty/staff/students). The broader tools table lists many more with individual cost/review-status/data-tier columns — notably **Claude** is listed there as Cost: Free, Review Status: "Free/Public," Approved Data Types: **Public only** (i.e., not yet cleared for Internal/Sensitive/Restricted data at the institutional level, unlike the three core tools above); **Magai** similarly shows Review Status "Free/Public," Approved Data Types: Public; **GitHub Copilot** shows Review Status "Restricted" despite a broader listed data-type range — status, not just data type, matters and should be read tool-by-tool.
- [AI@ND — Claude (tool detail page)](https://ai.nd.edu/ai-in-action/approved-ai-tools/claude/). Confirms and adds detail beyond the table above:
  - Security Status: "Approved with Conditions." Anthropic discloses personal-data-sharing categories among its affiliates; submitted data is de-identified, stored, and **may be used in generating responses for other users**. "Free or paid licenses should only be using Public data types, no sensitive data types are approved" (i.e., this applies to individual Claude.ai use, including a personal Team-for-Scientists seat obtained directly from Anthropic — not just the free tier).
  - "Enterprise Licenses - Coming Soon!" — ND's AI Enablement team is working to offer a premium Enterprise Claude license requiring departmental funding (a FOAPAL); no confirmed timeline as of 2026-09-02. This is a separate, not-yet-available path from Anthropic's own academic Team-for-Scientists application.
  - **DoD/DoW restriction, quoted verbatim:** "Researchers with new or existing Department of Defense/War (DoD/W) contracts and agreements are prohibited from using all products and services (e.g., Claude.ai, Anthropic API, Claude Code, etc.) provided by Anthropic, PBC (Public Benefit Corporation), and its subordinate, subsidiaries, or affiliated offices or entities in accordance with DoD/W March and April 2026 memos and recent communications from DoD/W components. Project teams are required to remove Anthropic products and services used in the execution of DoD/W contracts or agreements, as applicable." Contact for questions: `researchsecurity@nd.edu`.
- [Faculty and Staff Resources — AI: Usage, Policies, and Resources](https://alresources.nd.edu/all-resources/artificial-intelligence-ai-usage-policies-and-resources/) — not re-verified directly; consistent with the above, not yet re-checked against the primary page.
- [Undergraduate Academic Code of Honor — Statement on Generative AI (May 2023)](https://honorcode.nd.edu/official-statement-regarding-generative-ai-may-2023/) — student academic-integrity policy; background context only, not directly about research use, but useful for framing "authority to define appropriate use rests with the faculty."

**Bottom line for the talk (now confirmed, not just flagged):** under current ND policy, put non-public research data into Gemini, ChatGPT EDU, or NotebookLM, not into Claude — Claude is approved for Public data only until an Enterprise license lands. This is a genuinely useful, concrete, ND-specific slide (see [seminar_design.md](seminar_design.md) and [demo_ideas.md](demo_ideas.md)) and slightly complicates the "Why Claude?" framing in the abstract — worth a direct, honest acknowledgment on the ecosystem slide rather than glossing over it.

## Not yet investigated

- Journal/publisher AI-use policies (relevant to Section 7 of the outline — audit-before-submission). No specific journals identified yet; add if a concrete example is chosen for the audit demo.
- ND-specific data governance / export-control guidance beyond the general "no confidential data in unapproved tools" line above.
