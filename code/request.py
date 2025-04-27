import json
import time
from copy import deepcopy
import replicate
import requests
import zhipuai
from config import OPENAI_API_KEY, OPENAI_API_URL, replicate_model, replicate_model_version


def send_message_cot_gpt_shot(message, instructions, round):

    exit('no shot had been setablished')
    chat_history = []
    answer = []

    chat_history.append(instructions[0])
    t = {"role": "user", "content": instructions[-2] + message}
    chat_history.append(t)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": chat_history,
        "temperature": 0.8,
        "presence_penalty": 0.3
    }

    response = requests.post(OPENAI_API_URL, headers=headers, json=data)
    response_data = json.loads(response.text)

    if "error" in response_data:
        error_message = response_data["error"]["message"]
        print("Error message:", error_message)
        exit(0)
    else:
        reply = response_data["choices"][0]["message"]["content"]
        answer.append(reply)
        time.sleep(2)
        return answer


def send_message_cot_gpt(message, instructions, round):
    chat_history = []
    answer = []
    chat_history.append({"role": "system", "content": instructions[-1] + message + instructions[-2]})

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": chat_history,
        "temperature": 0.7,
        "presence_penalty": 0.3
    }

    for i in range(round):

        chat_history.append(instructions[i])
        response = requests.post(OPENAI_API_URL, headers=headers, json=data)
        response_data = json.loads(response.text)

        if "error" in response_data:
            error_message = response_data["error"]["message"]
            print("Error message:", error_message)
            exit(0)
        else:
            reply = response_data["choices"][0]["message"]["content"]
            chat_history.append({"role": "assistant", "content": reply})
            answer.append(reply)
            time.sleep(2)

    return answer

#
def send_message_cot_llama(message, instructions, round):
    chat_history = []
    answer = []
    # chat_history.append(instructions[0])
    # chat_history.append({"role": "system", "content": message})
    system_p = message + ' According to the given text, each number at the beginning of line represents a clause, complete the following tasks'

    model = replicate.models.get(replicate_model)
    version = model.versions.get(replicate_model_version)

    prompt = ' '

    for i in range(round):

        asrt = instructions[i]
        # chat_history.append({"role": "user", "content": asrt})
        # chat_history.append(asrt)
        prompt += '\n'
        prompt += f"[INST] {asrt['content']} [/INST]"
        prompt += '\n'
        # response = requests.post(API_URL, headers=headers, json=data)
        out = version.predict(system_prompt=system_p, prompt=prompt)
        op = ''
        for i in out:
            op += i
        print('output', op)
        answer.append(op)
        prompt += op
        print('history', prompt)

        time.sleep(1)

    return answer


def send_message_cot_glm(message, instructions, round):
    # copy = instructions.copy()
    copy = deepcopy(instructions)
    chat_history = []
    answer = []
    copy[0]["content"] = message + instructions[0]["content"]
    chat_history.append(
        {"role": "user", "content": instructions[-1] + message + instructions[-2] + instructions[0]['content']})

    for i in range(round):

        response = zhipuai.model_api.invoke(
            model="chatglm_pro",
            prompt=chat_history,
            top_p=0.7,
            temperature=0.7,
        )

        if response["code"] != '200':
            print("Error message:", response)
            exit(0)
        else:

            content = response["data"]['choices'][0]['content']

            cleaned_content0 = content.strip('"')
            cleaned_content1 = cleaned_content0.replace('"', ' !')
            cleaned_content2 = cleaned_content1.replace('\\', ' !')
            cleaned_content3 = cleaned_content2.replace('!n', ' \n')
            reply = cleaned_content3.replace('!', '')

            chat_history.append({"role": "assistant", "content": reply})
            answer.append(reply)
            if i == round - 1:
                break
            chat_history.append({"role": "user", "content": instructions[i + 1]['content']})

            return answer
