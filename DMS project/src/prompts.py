SYSTEM_MESSAGE_EXTRACT = """
Your task is to identify and extract all disease mentions in the text provided within triple backticks. Format the output as the following JSON object:
```json:\n{"diseases": "a semicolon-separated list of specific disease names or disease classes."}```
Avoid adding any additional remarks and explanations.

### Example:
Text:
```
The tumor suppressor gene Brca1 is required for embryonic cellular proliferation in the mouse. Mutations of the BRCA1 gene in humans are associated with predisposition to breast and ovarian cancers.
```
Output:
```
json:
{"diseases": "tumor; breast and ovarian cancers"}
```
"""


SYSTEM_MESSAGE_MARKUP = """
Your task is to identify and mark up all disease mentions in the text provided within triple backticks using the following HTML tags:
Use the <entity type=disease></entity> tag to mark all specific disease names or disease classes.
Avoid adding any additional remarks and explanations.

### Example:
Text:
```
The tumor suppressor gene Brca1 is required for embryonic cellular proliferation in the mouse. Mutations of the BRCA1 gene in humans are associated with predisposition to breast and ovarian cancers.
```
Text with markup:
```
The <entity type=disease>tumor</entity> suppressor gene Brca1 is required for embryonic cellular proliferation in the mouse. Mutations of the BRCA1 gene in humans are associated with predisposition to <entity type=disease>breast and ovarian cancers</entity>.
```
"""


POSITIVE_RULES_EXTRACT_MESSAGE = """
Please follow the rules below to extract all disease mentions correctly from the input text.

### Extraction Rules:
1. Extract Multiple Disease Mentions together if cannot be separated:
### Examples:
Text:
```
The conference highlighted recent advancements in treating Alzheimer's and Lewy body dementia to improve patient quality of life.
```
Output:
```
json:
{"diseases": "Alzheimer's and Lewy body dementia"}
```

Text:
```
The patient was diagnosed with liver, kidney, and pancreatic cancer after a series of tests.
```
Output:
```
json:
{"diseases": "liver, kidney, and pancreatic cancer"}
```

Text:
```
The study investigated the prevalence of lupus and rheumatoid arthritis among women of childbearing age.
```
Output:
```
json:
{"diseases": "lupus and rheumatoid arthritis"}
```
2. Extract ONLY the Disease Mention when it modifies other concepts:
### Examples:
Text:
```
Diabetes patients often experience complications in their cardiovascular health.
```
Output:
```
json:
{"diseases": "Diabetes"}
```

Text:
```
The various forms of epilepsy can lead to distinct seizure types and management strategies.
```
Output:
```
json:
{"diseases": "epilepsy"}
```

Text:
```
Swelling, breast pain, and nipple retraction are included in the list of possible breast cancer symptoms.
```
Output:
```
json:
{"diseases": "breast cancer"}
```
3. Extract All Disease Mentions, even if repeated:
- Ensure that every instance of a disease is extracted, even if it appears multiple times in the text.
### Examples:
Text:
```
Breast cancer is often diagnosed through mammograms, and breast cancer awareness is crucial for early detection.
```
Output:
```
json:
{"diseases": "Breast cancer; breast cancer"}
```

Text:
```
Patients with diabetes must monitor their blood sugar levels, as diabetes can lead to serious complications if not managed properly.
```
Output:
```
json:
{"diseases": "diabetes; diabetes"}
```

Text:
```
The treatment options for lung cancer vary, and lung cancer research continues to advance our understanding of the disease.
```
Output:
```
json:
{"diseases": "lung cancer; lung cancer"}
```
4. Extract the Full, Specific Disease Mention:
### Examples:
Text:
```
Individuals with chronic obstructive pulmonary disease frequently experience shortness of breath and require ongoing management to maintain their quality of life.
```
Output:
```
json:
{"diseases": "chronic obstructive pulmonary disease"}
```

Text:
```
The effects of end-stage renal disease on a patient's health can be profound, necessitating dialysis or kidney transplantation.
```
Output:
```
json:
{"diseases": "end-stage renal disease"}
```

Text:
```
Individuals diagnosed with idiopathic pulmonary fibrosis often face progressive lung decline, making early intervention and specialized care critical.
```
Output:
```
json:
{"diseases": "idiopathic pulmonary fibrosis"}
```
5. Extract Disease Full Names and Abbreviations Separately:
### Examples:
Text:
```
Patients diagnosed with rheumatoid arthritis (RA) often experience chronic joint pain and inflammation that can affect their daily activities.
```
Output:
```
json:
{"diseases": "rheumatoid arthritis; RA"}
```

Text:
```
The effects of human immunodeficiency virus (HIV) on the immune system can lead to serious health complications if left untreated.
```
Output:
```
json:
{"diseases": "human immunodeficiency virus; HIV"}
```

Text:
```
Papillary thyroid carcinoma (PTC) requires a multidisciplinary approach for treatment, including surgery, radioactive iodine therapy, and ongoing monitoring for recurrence.
```
Output:
```
json:
{"diseases": "Papillary thyroid carcinoma; PTC"}
```

Please ensure that all disease entities are extracted following these rules.
"""


POSITIVE_RULES_MARKUP_MESSAGE = """
Please follow the rules below to tag all disease mentions correctly in the input text.

### Tagging Rules:
1. Tag Multiple Disease Mentions together if cannot be separated:
### Examples:
Text:
```
The conference highlighted recent advancements in treating Alzheimer's and Lewy body dementia to improve patient quality of life.
```
Text with markup:
```
The conference highlighted recent advancements in treating <entity type=disease>Alzheimer's and Lewy body dementia</entity> to improve patient quality of life.
```

Text:
```
The patient was diagnosed with liver, kidney, and pancreatic cancer after a series of tests.
```
Text with markup:
```
The patient was diagnosed with <entity type=disease>liver, kidney, and pancreatic cancer</entity> after a series of tests.
```

Text:
```
The study investigated the prevalence of lupus and rheumatoid arthritis among women of childbearing age.
```
Text with markup:
```
The study investigated the prevalence of <entity type=disease>lupus and rheumatoid arthritis</entity> among women of childbearing age.
```
2. Tag ONLY the Disease Mention when it modifies other concepts:
### Examples:
Text:
```
Diabetes patients often experience complications in their cardiovascular health.
```
Text with markup:
```
<entity type=disease>Diabetes</entity> patients often experience complications in their cardiovascular health.
```

Text:
```
The various forms of epilepsy can lead to distinct seizure types and management strategies.
```
Text with markup:
```
The various forms of <entity type=disease>epilepsy</entity> can lead to distinct seizure types and management strategies.
```

Text:
```
Swelling, breast pain, and nipple retraction are included in the list of possible breast cancer symptoms.
```
Text with markup:
```
Swelling, breast pain, and nipple retraction are included in the list of possible <entity type=disease>breast cancer</entity> symptoms.
```
3. Tag All Disease Mentions, even if repeated:
- Ensure every instance of the disease in the text is tagged, even if it appears multiple times.
### Examples:
Text:
```
Breast cancer is often diagnosed through mammograms, and breast cancer awareness is crucial for early detection.
```
Text with markup:
```
<entity type=disease>Breast cancer</entity> is often diagnosed through mammograms, and <entity type=disease>breast cancer</entity> awareness is crucial for early detection.
```

Text:
```
Patients with diabetes must monitor their blood sugar levels, as diabetes can lead to serious complications if not managed properly.
```
Text with markup:
```
Patients with <entity type=disease>diabetes</entity> must monitor their blood sugar levels, as <entity type=disease>diabetes</entity> can lead to serious complications if not managed properly.
```

Text:
```
The treatment options for lung cancer vary, and lung cancer research continues to advance our understanding of the disease.
```
Text with markup:
```
The treatment options for <entity type=disease>lung cancer</entity> vary, and <entity type=disease>lung cancer</entity> research continues to advance our understanding of the disease.
```
4. Tag the Full, Specific Disease Mention:
### Examples:
Text:
```
Individuals with chronic obstructive pulmonary disease frequently experience shortness of breath and require ongoing management to maintain their quality of life.
```
Text with markup:
```
Individuals with <entity type=disease>chronic obstructive pulmonary disease</entity> frequently experience shortness of breath and require ongoing management to maintain their quality of life.
```

Text:
```
The effects of end-stage renal disease on a patient's health can be profound, necessitating dialysis or kidney transplantation.
```
Text with markup:
```
The effects of <entity type=disease>end-stage renal disease</entity> on a patient's health can be profound, necessitating dialysis or kidney transplantation.
```

Text:
```
Individuals diagnosed with idiopathic pulmonary fibrosis often face progressive lung decline, making early intervention and specialized care critical.
```
Text with markup:
```
Individuals diagnosed with <entity type=disease>idiopathic pulmonary fibrosis</entity> often face progressive lung decline, making early intervention and specialized care critical.
```
5. Separate Tags for Disease Full Name and its Abbreviation:
### Examples:
Text:
```
Patients diagnosed with rheumatoid arthritis (RA) often experience chronic joint pain and inflammation that can affect their daily activities.
```
Text with markup:
```
Patients diagnosed with <entity type=disease>rheumatoid arthritis</entity> (<entity type=disease>RA</entity>) often experience chronic joint pain and inflammation that can affect their daily activities.
```

Text:
```
The effects of human immunodeficiency virus (HIV) on the immune system can lead to serious health complications if left untreated.
```
Text with markup:
```
The effects of <entity type=disease>human immunodeficiency virus</entity> (<entity type=disease>HIV</entity>) on the immune system can lead to serious health complications if left untreated.
```

Text:
```
Papillary thyroid carcinoma (PTC) requires a multidisciplinary approach for treatment, including surgery, radioactive iodine therapy, and ongoing monitoring for recurrence.
```
Text with markup:
```
<entity type=disease>Papillary thyroid carcinoma</entity> (<entity type=disease>PTC</entity>) requires a multidisciplinary approach for treatment, including surgery, radioactive iodine therapy, and ongoing monitoring for recurrence.
```

Please ensure that all disease entities adhere to these rules.
"""

ANNOTATION_GUIDELINES_EXTRACT_MESSAGE = """
Please follow the rules below to extract all disease mentions correctly from the input text.

### Extraction Rules:
1. Extract Multiple Disease Mentions together if cannot be separated:
### Examples:
Text:
```
The conference highlighted recent advancements in treating Alzheimer's and Lewy body dementia to improve patient quality of life.
```
Output:
```
json:
{"diseases": "Alzheimer's and Lewy body dementia"}
```

Text:
```
The patient was diagnosed with liver, kidney, and pancreatic cancer after a series of tests.
```
Output:
```
json:
{"diseases": "liver, kidney, and pancreatic cancer"}
```

Text:
```
The study investigated the prevalence of lupus and rheumatoid arthritis among women of childbearing age.
```
Output:
```
json:
{"diseases": "lupus and rheumatoid arthritis"}
```
2. Extract ONLY the Disease Mention when it modifies other concepts:
### Examples:
Text:
```
Diabetes patients often experience complications in their cardiovascular health.
```
Output:
```
json:
{"diseases": "Diabetes"}
```

Text:
```
The various forms of epilepsy can lead to distinct seizure types and management strategies.
```
Output:
```
json:
{"diseases": "epilepsy"}
```

Text:
```
Swelling, breast pain, and nipple retraction are included in the list of possible breast cancer symptoms.
```
Output:
```
json:
{"diseases": "breast cancer"}
```
3. Extract All Disease Mentions, even if repeated:
- Ensure that every instance of a disease is extracted, even if it appears multiple times in the text.
### Examples:
Text:
```
Breast cancer is often diagnosed through mammograms, and breast cancer awareness is crucial for early detection.
```
Output:
```
json:
{"diseases": "Breast cancer; breast cancer"}
```

Text:
```
Patients with diabetes must monitor their blood sugar levels, as diabetes can lead to serious complications if not managed properly.
```
Output:
```
json:
{"diseases": "diabetes; diabetes"}
```

Text:
```
The treatment options for lung cancer vary, and lung cancer research continues to advance our understanding of the disease.
```
Output:
```
json:
{"diseases": "lung cancer; lung cancer"}
```
4. Extract the Full, Specific Disease Mention:
### Examples:
Text:
```
Individuals with chronic obstructive pulmonary disease frequently experience shortness of breath and require ongoing management to maintain their quality of life.
```
Output:
```
json:
{"diseases": "chronic obstructive pulmonary disease"}
```

Text:
```
The effects of end-stage renal disease on a patient's health can be profound, necessitating dialysis or kidney transplantation.
```
Output:
```
json:
{"diseases": "end-stage renal disease"}
```

Text:
```
Individuals diagnosed with idiopathic pulmonary fibrosis often face progressive lung decline, making early intervention and specialized care critical.
```
Output:
```
json:
{"diseases": "idiopathic pulmonary fibrosis"}
```
5. Extract Disease Full Names and Abbreviations Separately:
### Examples:
Text:
```
Patients diagnosed with rheumatoid arthritis (RA) often experience chronic joint pain and inflammation that can affect their daily activities.
```
Output:
```
json:
{"diseases": "rheumatoid arthritis; RA"}
```

Text:
```
The effects of human immunodeficiency virus (HIV) on the immune system can lead to serious health complications if left untreated.
```
Output:
```
json:
{"diseases": "human immunodeficiency virus; HIV"}
```

Text:
```
Papillary thyroid carcinoma (PTC) requires a multidisciplinary approach for treatment, including surgery, radioactive iodine therapy, and ongoing monitoring for recurrence.
```
Output:
```
json:
{"diseases": "Papillary thyroid carcinoma; PTC"}
```
6. Don't extract Organism Names (e.g., species, viruses, bacteria) unless they are a critical part of a Disease Name:
### Examples:
Text:
```
The Human immunodeficiency virus weakens the immune system, prompting researchers to study how the body’s immune response fights off the virus.
```
Output:
```
json:
{"diseases": "Human immunodeficiency virus"}
```

Text:
```
Studies on feline leukemia virus have highlighted its impact on cat health and the need for vaccination.
```
Output:
```
json:
{"diseases": "leukemia"}
```

Text:
```
The team focused on the pathophysiology of canine distemper and its implications for treatment in veterinary medicine.
```
Output:
```
json:
{"diseases": "distemper"}
```
7. Don't extract General Terms like "disease", "syndrome", "deficiency", "complications", "abnormalities", "mutation", etc.
However, terms such as "cancer" and "tumor" should be extracted:
### Examples:
Text:
```
The biopsy revealed cancer cells in the tissue sample, and the doctor noted that the tumor was benign but needed monitoring.
```
Output:
```
json:
{"diseases": "cancer, tumor"}
```

Text:
```
The study examined how a genetic mutation can lead to various complications and increase the risk of developing a serious syndrome.
```
Output:
```
json:
{"diseases": ""}
```

Text:
```
The team discovered a significant mutation associated with cystic fibrosis, which led to multiple disease complications.
```
Output:
```
json:
{"diseases": "cystic fibrosis"}
```
8. Don't extract Biological Processes like "tumorigenesis", "cancerogenesis". etc.:
### Examples:
Text:
```
The researchers studied the role of angiogenesis in tumor growth and its relationship to chronic inflammation in cancer development.
```
Output:
```
json:
{"diseases": "tumor; cancer"}
```

Text:
```
The study focused on the mechanisms of tumorigenesis in breast cancer cells, revealing potential therapeutic targets.
```
Output:
```
json:
{"diseases": "breast cancer"}
```

Text:
```
The analysis focused on the roles of neurogenesis and synaptogenesis in brain development, emphasizing their importance in learning and memory.
```
Output:
```
json:
{"diseases": ""}
```

Please ensure that all disease entities are extracted following these rules.
"""

ANNOTATION_GUIDELINES_MARKUP_MESSAGE = """
Please follow the rules below to tag all disease mentions correctly in the input text.

### Tagging Rules:
1. Tag Multiple Disease Mentions together if cannot be separated:
### Examples:
Text:
```
The conference highlighted recent advancements in treating Alzheimer's and Lewy body dementia to improve patient quality of life.
```
Text with markup:
```
The conference highlighted recent advancements in treating <entity type=disease>Alzheimer's and Lewy body dementia</entity> to improve patient quality of life.
```

Text:
```
The patient was diagnosed with liver, kidney, and pancreatic cancer after a series of tests.
```
Text with markup:
```
The patient was diagnosed with <entity type=disease>liver, kidney, and pancreatic cancer</entity> after a series of tests.
```

Text:
```
The study investigated the prevalence of lupus and rheumatoid arthritis among women of childbearing age.
```
Text with markup:
```
The study investigated the prevalence of <entity type=disease>lupus and rheumatoid arthritis</entity> among women of childbearing age.
```
2. Tag ONLY the Disease Mention when it modifies other concepts:
### Examples:
Text:
```
Diabetes patients often experience complications in their cardiovascular health.
```
Text with markup:
```
<entity type=disease>Diabetes</entity> patients often experience complications in their cardiovascular health.
```

Text:
```
The various forms of epilepsy can lead to distinct seizure types and management strategies.
```
Text with markup:
```
The various forms of <entity type=disease>epilepsy</entity> can lead to distinct seizure types and management strategies.
```

Text:
```
Swelling, breast pain, and nipple retraction are included in the list of possible breast cancer symptoms.
```
Text with markup:
```
Swelling, breast pain, and nipple retraction are included in the list of possible <entity type=disease>breast cancer</entity> symptoms.
```
3. Tag All Disease Mentions, even if repeated:
- Ensure every instance of the disease in the text is tagged, even if it appears multiple times.
### Examples:
Text:
```
Breast cancer is often diagnosed through mammograms, and breast cancer awareness is crucial for early detection.
```
Text with markup:
```
<entity type=disease>Breast cancer</entity> is often diagnosed through mammograms, and <entity type=disease>breast cancer</entity> awareness is crucial for early detection.
```

Text:
```
Patients with diabetes must monitor their blood sugar levels, as diabetes can lead to serious complications if not managed properly.
```
Text with markup:
```
Patients with <entity type=disease>diabetes</entity> must monitor their blood sugar levels, as <entity type=disease>diabetes</entity> can lead to serious complications if not managed properly.
```

Text:
```
The treatment options for lung cancer vary, and lung cancer research continues to advance our understanding of the disease.
```
Text with markup:
```
The treatment options for <entity type=disease>lung cancer</entity> vary, and <entity type=disease>lung cancer</entity> research continues to advance our understanding of the disease.
```
4. Tag the Full, Specific Disease Mention:
### Examples:
Text:
```
Individuals with chronic obstructive pulmonary disease frequently experience shortness of breath and require ongoing management to maintain their quality of life.
```
Text with markup:
```
Individuals with <entity type=disease>chronic obstructive pulmonary disease</entity> frequently experience shortness of breath and require ongoing management to maintain their quality of life.
```

Text:
```
The effects of end-stage renal disease on a patient's health can be profound, necessitating dialysis or kidney transplantation.
```
Text with markup:
```
The effects of <entity type=disease>end-stage renal disease</entity> on a patient's health can be profound, necessitating dialysis or kidney transplantation.
```

Text:
```
Individuals diagnosed with idiopathic pulmonary fibrosis often face progressive lung decline, making early intervention and specialized care critical.
```
Text with markup:
```
Individuals diagnosed with <entity type=disease>idiopathic pulmonary fibrosis</entity> often face progressive lung decline, making early intervention and specialized care critical.
```
5. Separate Tags for Disease Full Name and its Abbreviation:
### Examples:
Text:
```
Patients diagnosed with rheumatoid arthritis (RA) often experience chronic joint pain and inflammation that can affect their daily activities.
```
Text with markup:
```
Patients diagnosed with <entity type=disease>rheumatoid arthritis</entity> (<entity type=disease>RA</entity>) often experience chronic joint pain and inflammation that can affect their daily activities.
```

Text:
```
The effects of human immunodeficiency virus (HIV) on the immune system can lead to serious health complications if left untreated.
```
Text with markup:
```
The effects of <entity type=disease>human immunodeficiency virus</entity> (<entity type=disease>HIV</entity>) on the immune system can lead to serious health complications if left untreated.
```

Text:
```
Papillary thyroid carcinoma (PTC) requires a multidisciplinary approach for treatment, including surgery, radioactive iodine therapy, and ongoing monitoring for recurrence.
```
Text with markup:
```
<entity type=disease>Papillary thyroid carcinoma</entity> (<entity type=disease>PTC</entity>) requires a multidisciplinary approach for treatment, including surgery, radioactive iodine therapy, and ongoing monitoring for recurrence.
```
6. Don't tag Organism Names (e.g., species, viruses, bacteria) unless they are a critical part of a Disease Name:
### Examples:
Text:
```
The Human immunodeficiency virus weakens the immune system, prompting researchers to study how the body’s immune response fights off the virus.
```
Text with markup:
```
The <entity type=disease>Human immunodeficiency virus</entity> weakens the immune system, prompting researchers to study how the body’s immune response fights off the virus.
```

Text:
```
Studies on feline leukemia virus have highlighted its impact on cat health and the need for vaccination.
```
Text with markup:
```
Studies on feline <entity type=disease>leukemia</entity> virus have highlighted its impact on cat health and the need for vaccination.
```

Text:
```
The team focused on the pathophysiology of canine distemper and its implications for treatment in veterinary medicine.
```
Text with markup:
```
The team focused on the pathophysiology of canine <entity type=disease>distemper</entity> and its implications for treatment in veterinary medicine.
```
7. Don't tag General Terms like "disease", "syndrome", "deficiency", "complications", "abnormalities", "mutation", etc.
However, terms such as "cancer" and "tumor" should be tagged:
### Examples:
Text:
```
The biopsy revealed cancer cells in the tissue sample, and the doctor noted that the tumor was benign but needed monitoring.
```
Text with markup:
```
The biopsy revealed <entity type=disease>cancer</entity> cells in the tissue sample, and the doctor noted that the <entity type=disease>tumor</entity> was benign but needed monitoring.
```

Text:
```
The study examined how a genetic mutation can lead to various complications and increase the risk of developing a serious syndrome.
```
Text with markup:
```
The study examined how a genetic mutation can lead to various complications and increase the risk of developing a serious syndrome.
```

Text:
```
The team discovered a significant mutation associated with cystic fibrosis, which led to multiple disease complications.
```
Text with markup:
```
The team discovered a significant mutation associated with <entity type=disease>cystic fibrosis</entity>, which led to multiple disease complications.
```
8. Don't tag Biological Processes like "tumorigenesis", "cancerogenesis". etc.:
### Examples:
Text:
```
The researchers studied the role of angiogenesis in tumor growth and its relationship to chronic inflammation in cancer development.
```
Text with markup:
```
The researchers studied the role of angiogenesis in <entity type=disease>tumor</entity> growth and its relationship to chronic inflammation in <entity type=disease>cancer</entity> development.
```

Text:
```
The study focused on the mechanisms of tumorigenesis in breast cancer cells, revealing potential therapeutic targets.
```
Text with markup:
```
The study focused on the mechanisms of tumorigenesis in <entity type=disease>breast cancer</entity> cells, revealing potential therapeutic targets.
```

Text:
```
The analysis focused on the roles of neurogenesis and synaptogenesis in brain development, emphasizing their importance in learning and memory.
```
Text with markup:
```
The analysis focused on the roles of neurogenesis and synaptogenesis in brain development, emphasizing their importance in learning and memory.
```

Please ensure that all disease entities adhere to these rules.
"""