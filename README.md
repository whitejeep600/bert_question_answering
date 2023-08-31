DISCLAIMER: the Python scripts in scripts/prediction and scripts/training are either directly copied from the publicly available Huggingface scripts, or copied and slightly modified for the purposes of this task.

The description below was prepared for task graders.

Packages required to run:
- datasets
- gdown
- huggingface transformers. This project requires a source install:

pip install git+https://github.com/huggingface/transformers

which I hope is not a problem.

To download the models from my GoogleDrive:

./download.sh

To run the whole prediction after downloading:

./run.sh [path to context file in json] [path to test dataset in json] [path to result]

Here I would like to note that I ran this prediction on a csie lab computer and uploaded its result to Kaggle as the submission 'potezny_papaj.csv', scored 0.7839. One slight problem with this is that the lab computers use Python3.10, and I have noticed some discrepancies in Kaggle scores for predictions run on Python3.10 or Python3.10 and ones run on Python3.5 (which is used by Google Colab, where I trained all my models). I have not been able to test the final models on Python3.9 on my own laptop due to small computational power. That said, I noticed no difference between Python3.9 and Python3.10, so this result should be reproducible.

To finetune context selection, call:

./scripts/training/tune_context_selection.sh [path to context] [path to train file] [path to validation file] [output directory]

The script will handle preprocessing the datasets into the swag format required by the training script. The files are expected in json format, just like the one defined in the task.

To finetune question answering, call:

./scripts/training/tune_question_answering.sh [path to context] [path to train file] [path to validation file] [output directory]

The context, train and validation files are expected in the same format as above.

A BIT IMPORTANT: for prediction/training of question answering, I adapted the Huggingface scripts and preprocessed the datasets to the required SQuAD format. The preprocessing works and training is performed - however, I must have misunderstood something about the format, since prediction/training  gives the following error:

ValueError: Predictions and/or references don't match the expected format. [...]

This error is expected. It does not impact the training results, and I could not understand its cause, so I have not removed it.
