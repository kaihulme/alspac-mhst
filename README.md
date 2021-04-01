# ADSMH - Mental Health and Screen Time

Group coursework for Applied Data Science at the University of Bristol.

## Overview

- The data set that you have was created in order to see what happens when you ask lots of different researchers to answer the same question "__based on this dataset: does screen use at age 16 predict depression at age 18__"? This is called a "crowd sourced data analysis". The idea is that there are lots of different defensible choices when you do any analysis, and we wanted to know: what is the impact of all these different choices?
- This is a "synthetic dataset": no real people: so that we could share it widely.
- It was synthesised from a subset of the ALSPAC (Avon Longitudinal Study of Parents and Children) cohort study dataset. We then re-ran researchers analyses on the real data. The subset was about mental health and screen time, and was chosen based on an already published study on this same question.
- The data wasn't only collected for that one study. The ALSPAC dataset has had many different surveys and clinics. It has been following children since their birth and recording information about them as they age. The  children were born in 1992 (so, data in this data set was mostly collected in 2008 and 2010), so this will obviously effect your interpretation of "screen time", which is obviously very different to 16 year olds now.

### Useful links

- Data collection (ALSPAC)
  - You can investigate the ALSPAC catalogue in detail [here](http://www.bristol.ac.uk/alspac/researchers/our-data/)
  - You can read about how ALSPAC makes ethical decisions [here](http://www.bristol.ac.uk/alspac/researchers/research-ethics/)
- Original investigation
  - [The ALSPAC proposal](https://proposals.epi.bristol.ac.uk/?q=node/127766)
  - The paper for the original proposal is [here](https://bmcpublichealth.biomedcentral.com/articles/10.1186/s12889-018-6321-9)
- Crowd sourced data analysis (MAPS)
  - The ALSPAC proposal allowing us to use the data for the crow sourced data analysis is [here](https://proposals.epi.bristol.ac.uk/?q=node/129851)
  - [Project materials](https://osf.io/buqk8/), including the [description of the creation of the synthetic dataset](https://osf.io/785sx/) and [extra information about data](https://osf.io/jezb5/) (in the data dictionary references folder).
  - [Info for participants website](https://jean-golding-institute.github.io/maps/)

### Data Owner

Natalie Thurlby, Data Science Specialist, Jean Golding Institute, natalie.thurlby@bristol.ac.uk.

## Repository overview

- Data in `/data`
  - Original dataset and dictionary in `/original`
  - Modified datasets in `/altered`
- Figures in `/figures`
- Jupyter notebooks in `/notebooks`
- Coursework specification available in `ads_cw_specification.pdf`

### Requirements

Requirements for notebooks included in `requirements.txt`.

Use pip to install the requirements to your environment:

```bash
pip install -r requirements.txt
```
