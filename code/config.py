import zhipuai
import os


''' GPT-3.5-turbo'''
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
OPENAI_API_URL = os.getenv('OPENAI_API_URL', '')

'''ChatGLM'''
zhipuai.api_key = os.getenv('ZHIPU_API_KEY', '')

'''LLaMA-2'''
'''Please get the full configs under the guidance of official website'''
os.environ['DASHSCOPE_API_KEY'] = os.getenv('DASHSCOPE_API_KEY', '')
os.environ["REPLICATE_API_TOKEN"] = os.getenv('REPLICATE_API_TOKEN', '')
replicate_model = os.getenv('REPLICATE_MODEL', '')
replicate_model_version = os.getenv('REPLICATE_MODEL_VERSION', '')