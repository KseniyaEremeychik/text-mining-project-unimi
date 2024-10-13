from src.data_loader import DataLoader
from src.llm_inference import LLMInference
from src.prompts import SYSTEM_MESSAGE_MARKUP, SYSTEM_MESSAGE_EXTRACT, ANNOTATION_GUIDELINES_EXTRACT_MESSAGE, ANNOTATION_GUIDELINES_MARKUP_MESSAGE
from src.model_names import LLAMA_3_1
import json

if __name__ == "__main__":
    data_loader = DataLoader(filepath="data/Artificial_dataset_DISEASE.tsv")
    abstracts = data_loader.load_data()
    parsed_data = data_loader.parse_data(abstracts)
    
    llm_inference = LLMInference(
        model_name=LLAMA_3_1,
        api_key="noapikey"
    )
    processed_data = llm_inference.process_parsed_data(
        parsed_data,
        SYSTEM_MESSAGE_MARKUP + ANNOTATION_GUIDELINES_MARKUP_MESSAGE,
        SYSTEM_MESSAGE_EXTRACT + ANNOTATION_GUIDELINES_EXTRACT_MESSAGE
    )

    with open('llama3.1_results_all_rules_3_shot.json', 'w') as json_file:
        json.dump(processed_data, json_file, indent=4)