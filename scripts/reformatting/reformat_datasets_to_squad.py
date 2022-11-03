# todo output treningowy zbierać do porównania modeli
#  a no i loss, żeby stworzyć wykres

import json
from pathlib import Path

if __name__ == '__main__':
    contexts = json.loads(Path('raw_data/context.json').read_text())

    relevant_context_predictions = json.loads(Path('data/test_context_predictions.json').read_text())
    dataset = json.loads(Path(f'raw_data/test.json').read_text())
    result = []
    for item in dataset:
        result.append({'id': item['id'],
                       'title': '',
                       'context': contexts[item['paragraphs'][relevant_context_predictions[item['id']]]],
                       'question': item['question'],
                       })
    result = {'data': result}
    with open(f'data/test_squad_format.json', 'w', encoding='utf8') as output_file:
        output_file.write(json.dumps(result, indent=4, ensure_ascii=False))
