Steps for linguistic analysis
=============================

Methods and tools used in the preparation of this paper: 

- John Sullivan, Marcelo M. Wanderley. "Stability, Reliability, Compatibility: Reviewing 40 Years of DMI Design." *Proceedings of the 15th Sound and Music Computing Conference, 2018.* [[link](http://idmil.org/publication/stability-reliability-compatibility-reviewing-40-years-of-dmi-design/)]

Analysis process: 

- [x] Downloaded all papers from ICMC, SMC and NIME
    + Python script to automate ICMC proceedings: `geticmc.py` 
    + [x] OCR scan ICMC papers to make text searchable
        * Adobe Acrobat
    + [x] Rename and organize
        * `rename_NIME_index.py` 
        * `rename_SMC_index.py` 
- [x] Identify ICMC and SMC papers that are relevant to performance with DMIs
- [x] Organize all papers to be included in analysis in one place. 
    + Corpus: `/corpus`
    + Scripts used:
        * `get_corpus.py`
        * `get_nime_corpus.py`
- [ ] Run keyword search for each conference, each year, and save results to .csv
    - [ ] `keyword.sh`
- [ ] Run collocation for each conference by year, and save results to .csv
    - [ ] I think this necessitates converting all dfs to text; there are free applications for this.. 
    - [ ] Associate and code results for final collocation 
    - [ ] Output word clouds for results? 
- [ ] Run concordance analysis, and save results to .csv/.xlsx
- [ ] Group results into categories by years. 
