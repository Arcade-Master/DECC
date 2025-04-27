## DECC
#### Enhancing Large Language Model with Decomposed Reasoning for Emotion Cause Pair Extraction
https://arxiv.org/abs/2401.17716

Before start, you should make sure necessary configurations are prepared in
`./code/config.py`


Get your own **API Key** in their corresponding website :
- OpenAI https://openai.com
- ZhiPu https://open.bigmodel.cn
- Replicate https://replicate.com


**Run the framework by :** `./code/main.py`



Select a LLM as framework base :
- `gpt` indicate GPT-3.5-turbo
- `glm` indicates ChatGLM-STD
- `llama` indicates LLaMA 70B-chat

Select a dataset as test set :
- `chi` indicate the Chinese ECPE dataset
- `eng` indicates the English ECPE dataset
- `reb` indicates the Rebalanced ECPE dataset

**The results are preserved in `./result`**
