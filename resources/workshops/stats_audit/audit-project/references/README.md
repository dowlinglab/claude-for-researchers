# Reference texts

An audit is only as good as what it is checked against. Give Claude these trusted, freely readable references, and ask it to point to the specific chapter, section, or principle behind each finding.

| Reference | What it is | Where to get it |
|---|---|---|
| *Introduction to Modern Statistics*, 2nd ed., Çetinkaya-Rundel and Hardin | Open textbook. The web edition is licensed CC BY-SA 3.0 US. Parts 1 to 5 (Chapters 1 to 23) cover what this audit needs. | [Web edition](https://openintro-ims.netlify.app/). Free PDF from the [OpenIntro book page](https://www.openintro.org/book/ims/): choose the free option and set the price to $0. |
| NIST/SEMATECH *e-Handbook of Statistical Methods* | Reference handbook for scientists and engineers. Chapters 1 (Exploratory Data Analysis) and 7 (Product and Process Comparisons) are the useful ones. | [Handbook](https://www.itl.nist.gov/div898/handbook/). Chapter PDFs: [Chapter 1](https://www.itl.nist.gov/div898/handbook/toolaids/pff/eda.pdf), [Chapter 7](https://www.itl.nist.gov/div898/handbook/toolaids/pff/prc.pdf). |
| Wasserstein and Lazar (2016), *The ASA Statement on p-Values: Context, Process, and Purpose*, The American Statistician 70(2) | A short statement of principles from the American Statistical Association. | [DOI 10.1080/00031305.2016.1154108](https://doi.org/10.1080/00031305.2016.1154108) |

## Put a copy where Claude can read it

Save the files you want to use into `references/pdfs/`. Git ignores that folder, so the texts stay on your computer and out of your repository. A pinned local copy also means Claude cites the same text you can open.

- For the web editions, use your browser's **Print → Save as PDF** on the chapters you want, or download the PDF versions above.
- If you are short on time, one reference is enough. Two make cross-checking possible.
- If Claude can browse the web in your setup, you can instead give it the links. A local file is easier to verify.

Check any citation Claude gives you by opening the section it names. A finding that cites a section that does not say what Claude claims is a finding about Claude.

Do not commit these files. Each has its own license and redistribution terms.
