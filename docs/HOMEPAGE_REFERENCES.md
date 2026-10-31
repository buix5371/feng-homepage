# Academic homepage comparison — 2026-10-31

Reference selection: independently leading NLP/language-technology faculty at
the associate-professor career stage. These are design and writing references,
not a claim that researchers have identical standing or interchangeable ranks.

| Reference | Observed homepage organization | Applied decision |
| --- | --- | --- |
| Wei Xu, Georgia Tech — https://cocoxu.github.io/ | Brief first-person introduction; one Research overview; News; Selected Publications; lab, teaching and service | Keep research interests distinct from paper records, with a single overview |
| Graham Neubig, CMU — https://www.phontron.com/ | First-person introduction and a concise Research explanation linking to detailed research/publication/software pages | Keep the homepage concise; method explanations and full figures belong on detail pages |
| Antonis Anastasopoulos, George Mason — https://antonisa.github.io/ | Brief introduction; news with dates in individual rows; selected publications with previews and resources | Use a stable News heading with dates inside rows; retain a small set of representative papers |

The observed examples have different valid layouts. None establishes a rule that
all faculty must use the same order or that News must be restricted to a calendar
year. The site's current three news entries are all from 2026, but future builds
will not delete them just because the calendar changes. Maintain newest items
first and display at most five. Do not duplicate paper summaries as news.

## Implemented homepage

1. Identity, affiliation, short biography and contact/profile links.
2. **Research Interests**: three compact illustrated links to the three research
   directions. The additional Research in focus section has been removed.
3. **Selected Publications**: five representative bibliographic records.
4. **News**: recent appointments and reviewing recognition, with dates per row.
5. **Contact**.

The three overview images are the TableGPT training figure, CodeBERT pretraining
figure and ImplicitMemBench workflow. Each links to its corresponding detailed
research section, which retains full-size figures and sources. This preserves
the requested visual content while removing a second display of the same topics.
