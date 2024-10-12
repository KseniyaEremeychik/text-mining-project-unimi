### Disease Mention Recognition using open-source LLMs

> Instructor: Darya Shlyk, *Department of Computer Science, Università degli Studi di Milano*

Disease Mention Recognition (DMR) is a key task in biomedical NLP, focusing on identifying disease mentions from unstructured text. For example, in the sentence "The patient was diagnosed with diabetes and hypertension" the terms "diabetes" and "hypertension" should be labeled as disease mentions.

Manual disease annotation is a complex and time-consuming process that relies on expert knowledge and strict annotation guidelines, such as those used in the NCBI and BC5CDR datasets. 

This project aims to determine whether open-source Large Language Models (LLMs) can effectively perform the DMR task using prompt engineering (without instruction-tuning), and achieve annotation accuracy comparable to that of human experts.

#### Dataset

The available datasets are [NCBI](https://www.ncbi.nlm.nih.gov/CBBresearch/Dogan/DISEASE/), [BC5CDR](https://github.com/JHnlp/BioCreative-V-CDR-Corpus).

#### References

- Wang, Shuhe, et al. "Gpt-ner: Named entity recognition via large language models." arXiv preprint arXiv:2304.10428 (2023).
- Keloth, Vipina K., et al. "Advancing entity recognition in biomedicine via instruction tuning of large language models." Bioinformatics 40.4 (2024): btae163.
- Luo, Ling, et al. "AIONER: all-in-one scheme-based biomedical named entity recognition using deep learning." Bioinformatics 39.5 (2023): btad310.
- Ashok, D., and Z. C. Lipton. "PromptNER: Prompting For Named Entity Recognition. arXiv 2023." arXiv preprint arXiv:2305.15444.
- Dogan, Rezarta Islamaj, and Zhiyong Lu. "An improved corpus of disease mentions in PubMed citations." BioNLP: Proceedings of the 2012 Workshop on Biomedical Natural Language Processing. 2012.
