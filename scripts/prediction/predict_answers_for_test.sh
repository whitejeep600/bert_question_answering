python3.9 scripts/prediction/predict_answers_for_test.py \
--model_name_or_path models/question_answering \
--do_predict \
--output_dir 'data/question_answering_out' \
--max_seq_length 384 \
--test_file='data/test_squad_format.json' \
--doc_stride 128 \
--version_2_with_negative
