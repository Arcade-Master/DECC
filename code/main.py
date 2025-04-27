from utils import setSelect, merge_sentences
from frame import run_cot
import os

if __name__ == '__main__':


    '''gpt / llama / glm'''
    engine = input('choose a LLM base (gpt / llama / glm) : ')
    set = input(' choose a test dataset (chi / eng / reb) :')
    path = os.path.dirname(os.path.abspath('.'))

    ds, mg = setSelect(set)

    for i in range(1,10):
        if mg:
            input_file = merge_sentences(path + f'/data/{ds}/fold{i}_test.txt')
        else:
            input_file = path + f'/data/{ds}/fold{i}_test.txt'

        output_file = path+f'/result/{ds}/fold{i}_test_result.txt'

        run_cot(engine,set, output_file, input_file, batchsize=3, delay=3, show=False)