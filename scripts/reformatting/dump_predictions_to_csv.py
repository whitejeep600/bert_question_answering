import json
from pathlib import Path

if __name__ == '__main__':
    predictions = json.loads(Path('data/question_answering_out/predict_predictions.json').read_text())
    with open('data/out.csv', 'w', encoding='utf8') as file:
        print('id,answer', file=file)
        for prediction in predictions:
            print(f'{prediction},"{predictions[prediction]}"', file=file)

