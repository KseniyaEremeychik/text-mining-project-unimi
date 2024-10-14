from openai import OpenAI
from tqdm import tqdm
from model_names import GEMMA_2

class LLMInference:
    def __init__(self, model_name, api_key="noapikey", base_url="http://localhost:11434/v1"):
        self.client = OpenAI(base_url=base_url, api_key=api_key)
        self.model_name = model_name

    def _call_llm(self, sentences, system_message, is_gemma=False):
        response_all = []
        for sentence in tqdm(sentences):
            if is_gemma:
                message = {"role": "user", "content": system_message + f"\nText:\n```{sentence}```"}
            else:
                message = [
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": f"\nText:\n```{sentence}```"}
                ]

            response = self.client.chat.completions.create(
                model=self.model_name,
                temperature=0,
                n=1,
                messages=message
            )
            response_all.append(response.choices[0].message.content)
        return response_all

    def inference(self, sentences, system_message_markup, system_message_extract):
        is_gemma = GEMMA_2 in self.model_name.lower()

        markup_results = self._call_llm(sentences, system_message_markup, is_gemma)
        extract_results = self._call_llm(sentences, system_message_extract, is_gemma)

        return markup_results, extract_results

    def process_parsed_data(self, parsed_data, system_message_markup, system_message_extract):
        for pid in tqdm(list(parsed_data)):
            parsed_data[pid]["response_markup"] = self.inference(
                parsed_data[pid]["sentences"], system_message_markup, system_message_extract
            )[0] 
            parsed_data[pid]["response_extract"] = self.inference(
                parsed_data[pid]["sentences"], system_message_markup, system_message_extract
            )[1] 
        return parsed_data