import json
from pathlib import Path

if __name__ == '__main__':
    contexts = json.loads(Path('raw_data/context.json').read_text())
    dataset = json.loads(Path(f'raw_data/test.json').read_text())
    result = []
    for item in dataset:
        endings = {f'ending{i}': contexts[number] for i, number in enumerate(item['paragraphs'])}
        result.append({'video-id': item['id'],
                       'sent1': item['question'],
                       'sent2': '',
                       'label': 0,
                       **endings})
    with open(f'data/test_swag_format.json', 'w', encoding='utf8') as output_file:
        output_file.write(json.dumps(result, indent=4, ensure_ascii=False))
