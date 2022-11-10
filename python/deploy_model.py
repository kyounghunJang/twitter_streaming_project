import elasticsearch
from pathlib import Path
from eland.ml.pytorch import PyTorchModel
from eland.ml.pytorch.transformers import TransformerModel
#hugging face kr_nlp pytorch model 선택
tm= TransformerModel("matthewburke/korean_sentiment", "text_classification")

#모델 폴더 및 파일 생성
tmp_path="models"
Path(tmp_path).mkdir(parents=True, exist_ok=True)
model_path, config, vocab_path = tm.save(tmp_path)

#elastic search로 전송
es= elasticsearch.Elasticsearch("http://172.18.0.2:9200")
ptm= PyTorchModel(es, tm.elasticsearch_model_id())
ptm.import_model(model_path= model_path, config_path=None, vocab_path=vocab_path, config=config)