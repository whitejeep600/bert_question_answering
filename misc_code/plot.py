import json
import matplotlib
from pathlib import Path

from matplotlib.pyplot import show, savefig
from pandas import DataFrame


def get_accuracy(preds):
    dataset = json.loads(Path(f'../data/valid.json').read_text())
    count = len(dataset)
    correct = len([0 for item in dataset if preds[item['id']] == item['answer']['text']])
    return correct / count
    pass


if __name__ == '__main__':
    # values collected manually from checkpoints.
    train_losses = [
        2.0581,
        1.4157,
        1.1391,
        1.1116,
        0.9005,
        0.9083,
        0.9253,
        0.8579,
        0.8497,
        0.6958
    ]
    matplotlib.pyplot.plot([500 + 2000 * i for i in range(1, 11)], train_losses)
    matplotlib.pyplot.title("Train loss per checkpoint")
    savefig('train_losses.png')
    show()

    # predictions generated manually for each checkpoint
    predictions = [json.loads(Path(f'../data/out{500 + 2000 * i}/predict_predictions.json').read_text())
                   for i in range(10)]
    accuracies = [get_accuracy(pred) for pred in predictions]
    matplotlib.pyplot.plot([500 + 2000 * i for i in range(1, 11)], accuracies)
    matplotlib.pyplot.title("Accuracy per checkpoint")
    savefig('accuracies.png')
    show()


