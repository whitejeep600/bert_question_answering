import json
from pathlib import Path

if __name__ == '__main__':
    contexts = json.loads(Path('../data/context.json').read_text())
    dataset = json.loads(Path(f'../data/valid.json').read_text())
    result = []
    for item in dataset:
        result.append({'id': item['id'],
                       'title': '',
                       'context': contexts[item['relevant']],
                       'question': item['question'],
                       })
    result = {'data': result}
    with open(f'../data/stripped_valid_squad_format.json', 'w', encoding='utf8') as output_file:
        output_file.write(json.dumps(result, indent=4, ensure_ascii=False))
