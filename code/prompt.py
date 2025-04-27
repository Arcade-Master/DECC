
gpt_chi = [{"role": "user","content":" 抽取其中表达最明显的情绪，只能输出原文中的字符，禁止概括不存在的情绪"},
            {'role': 'user', 'content': '每个情绪词对应一个情绪子句，找出情绪子句，这个子句必须是包含上述情绪词的，不包括情感子句不要输出'},
            {'role': 'user', 'content': '根据这个情绪子句，一步一步分析其中情感产生原因'},
            {'role': 'user', 'content': '选出最有可能的原因子句，输出置信度最高的情绪和原因子句对（带序号），如果在原文中找不到具体的原因子句则不输出'},
             '; 其中一个序号代表一个子句，请综合文章内容完成下列任务：',
             '文章：']

glm_chi = [{'role': 'user','content':'结合所给文章，从文章原词中抽取最能形容情感的词，不要提炼概括'},
            {'role': 'user', 'content': '接下来只围绕上文抽取到的情感，找出每个词出现的那一个子句，不要输出没有情感词的子句'},
            {'role': 'user', 'content': '结合全文内容，一步一步分析上一步情绪产生的原因，请输出合理的推理过程，并选出最有可能导致情感的原因句'},
            {'role': 'user', 'content': '总结分析内容，以（情绪句-原因句）格式输出，和他们的序号对，如（3,7)，只输出最确定的内容'},
           '; 其中一个序号代表一个子句，请综合文章内容完成下列任务：',
           '文章：']

gpt_eng = [{"role": "user","content":"please extract one or two most literally explicit emotions referred from the given context, do not summarize, just use given words to output"},
            {'role': 'user', 'content': 'locate the clauses where the emotions literally occur by number, we call them emotion clauses, if an emotion have no origin clause, then this emotion should be trimmed out'},
            {'role': 'user', 'content': 'based on those emotions, analyses why each emotion could happen, step by step'},
            {'role': 'user', 'content': 'for each of the emotion, select a most probable clause to be its explanation , and output the pair of emotion clause and reason clause by number, do not output uncertain pairs'},
                'According to the given context, each number at the beginning of line represents a clause, complete the following tasks: ',
           'Context: ']

llama_eng = [{"role": "user","content":"please extract  most literally explicit emotions referred from the given context, do not summarize, just only output words among given words"},
            {'role': 'user', 'content': 'locate the clauses where the emotions literally occur by number, we call them emotion clauses'},
            {'role': 'user', 'content': 'then, based on those emotions, analyses why each emotion could happen, step by step'},
            {'role': 'user', 'content': 'for each of the emotion, select a most probable clause to be its explanation , and output the pair of emotion clause and reason clause by number'}]





