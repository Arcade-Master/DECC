import time

from utils import engineSelect


def run_cot(engine, set,output_file, input_file, batchsize, delay, show):

    send_message, instructions = engineSelect(engine,set)

    round = len(instructions) - 2


    print('load data_file: {}'.format(input_file))
    y_position, y_cause, y_pairs, x, sen_len, doc_len = [], [], [], [], [], []
    time_span = 1
    answer = []
    inputFile = open(input_file, 'r')
    with open(output_file, "w") as f:

        while True:

            if time_span % batchsize == 0:
                time_span = 0
                print('sleeping for overloading.....\n')
                time.sleep(delay)

            sents = []
            line = inputFile.readline()

            if line == '': break

            line = line.strip().split()
            id = line[0]
            d_len = int(line[1])
            f.write(id)
            f.write('\n')
            pairs = eval('[' + inputFile.readline().strip() + ']')
            y_pairs.append(pairs)

            for i in range(d_len):
                line = inputFile.readline().strip().split(',')
                words = line[-1]
                sents.append(str(i + 1) + ' ' + words)

            response = send_message(str(sents), instructions, round)

            print('possessing document ',id)
            if show:
                print(response)
                print(sents)
            for res in response:
                f.write(res)
                f.write('\n')
            time_span += 1

        return answer
