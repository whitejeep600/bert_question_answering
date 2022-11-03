python3.9 scripts/prediction/predict_contexts_for_test.py \
--model_name_or_path models/context_selection \
--do_eval \
--max_seq_length=512 \
--output_dir dummy/ \
--validation_file=data/test_swag_format.json
