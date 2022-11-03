mkdir raw_data
mkdir data
cp ${1} raw_data/context.json
cp ${2} raw_data/test.json
python3.9 scripts/reformatting/reformat_unlabeled_to_swag.py
./scripts/prediction/predict_contexts_for_test.sh
python3.9 scripts/reformatting/reformat_datasets_to_squad.py
./scripts/prediction/predict_answers_for_test.sh
python3.9 scripts/reformatting/dump_predictions_to_csv.py
mv data/out.csv ${3}
rm -rf raw_data/
rm -rf data/
rm -rf dummy/
