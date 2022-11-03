mkdir raw_data
mkdir data

cp ${1} raw_data/context.json
cp ${2} raw_data/train.json
cp ${3} raw_data/valid.json

python3.9 scripts/reformatting/reformat_labeled_to_swag.py

python3.9 scripts/training/run_swag.py \
--model_name_or_path hfl/chinese-roberta-wwm-ext \
--do_train \
--do_eval \
--learning_rate 3e-5 \
--num_train_epochs 1 \
--output_dir ${4} \
--per_gpu_eval_batch_size=16 \
--per_gpu_train_batch_size=2 \
--per_device_train_batch_size=2 \
--max_seq_length=512 \
--train_file='data/train_swag_format.json' \
--validation_file='data/valid_swag_format.json' \
--overwrite_output

rm -rf data/
rm -rf raw_data/

