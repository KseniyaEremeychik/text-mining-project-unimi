import re
from collections import defaultdict

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_data(self):
        with open(self.filepath, encoding="utf-8") as file:
            text = file.read()
            abstracts = [line for line in text.split("\n\n") if line]
        return abstracts

    def parse_data(self, abstracts):
        parsed_data = defaultdict(lambda: defaultdict(list))
        for item in abstracts:
            lines = item.split("\n")
            pid, abstract = lines[0].strip(), lines[1].strip()
            parsed_data[pid]["text"] = abstract

            re_sentences = re.split(r'(?<=[.!?])\s+', abstract)
            sentences = [sentence.strip() for sentence in re_sentences]
            parsed_data[pid]["sentences"] = sentences

            for line in lines[2:]:
                data = line.split("\t")
                if len(data) == 3:
                    start, end, mention = data
                    parsed_data[pid]["annotations"].append({
                        "span": start + ":" + end,
                        "mention": mention
                    })
        return parsed_data