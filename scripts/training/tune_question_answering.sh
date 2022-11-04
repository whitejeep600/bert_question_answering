mkdir raw_data
mkdir data

cp ${1} raw_data/context.json
cp ${2} raw_data/train.json
cp ${3} raw_data/valid.json

python3.9 scripts/reformatting/reformat_labeled_datasets_to_squad.py

# I realized I could use the same script as for prediction, which is why
# it's in the prediction directory despite being used to training here.
python3.9 scripts/prediction/run_qa.py \
--model_name_or_path hfl/chinese-roberta-wwm-ext-large \
--do_train \
--do_eval \
--learning_rate 3e-5 \
--num_train_epochs 1 \
--output_dir ${4} \
--max_seq_length 384 \
--train_file='data/train_squad_format.json' \
--validation_file='data/valid_squad_format.json' \
--per_device_train_batch_size=2 \
--doc_stride 128 \
--version_2_with_negative

rm -rf data/
rm -rf raw_data/
