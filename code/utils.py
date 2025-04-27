import os
from request import send_message_cot_gpt, send_message_cot_gpt_shot, send_message_cot_glm, send_message_cot_llama
from prompt import gpt_chi, gpt_eng, llama_eng, glm_chi


def merge_sentences(input_file):
    # with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
    out = os.path.dirname(input_file) + '/merge_sent/' + input_file.split('/')[-1]
    with open(input_file, 'r', encoding='utf-8') as f_in, open(out, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            line = line.strip()
            if line:
                parts = line.split(',')
                if len(parts) != 4:
                    if len(parts) == 1:
                        f_out.write(parts[0])
                        f_out.write('\n')
                    else:
                        f_out.write(line + '\n')
                else:
                    sentence = ''.join(parts[3:])
                    sentence = sentence.replace(' ', '')
                    f_out.write(parts[0] + ',' + parts[1] + ',' + parts[2] + ',' + sentence + '\n')
    return out


def setSelect(testset):

    mg = False
    if testset == 'chi':
        ds = 'chinese'
        mg = True
    elif testset == 'eng':
        ds = 'english'
    elif testset == 'reb':
        ds = 'rebalance'
    else:
        exit('wrong set')

    return ds, mg

def engineSelect(engine, set):

    if engine == 'llama':
        send_message = send_message_cot_llama
        instructions = llama_eng
    elif engine == 'glm':
        send_message = send_message_cot_glm
        instructions = glm_chi
    elif engine == 'gpt':
        if set == 'eng':
            instructions = gpt_eng
        else:
            instructions = gpt_chi

        if len(instructions) <= 3:
            send_message = send_message_cot_gpt_shot
        else:
            send_message = send_message_cot_gpt
    else:
        exit('invalid engine')

    return send_message, instructions