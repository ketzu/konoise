import csv
from ko_noiser import Konoise, Config
from multiprocessing import Pool
from functools import partial
import tqdm

config = Config()
# g2p errors
config.enable_g2p = True
config.g2p_whole_sentence = True # reduce calles to g2pk, it is slow
config.g2p_probability = 0.2
config.descriptive_probability = 0.5
config.group_vowels_probability = 0.5
config.descriptive_always_group_vowels = False
# typo errors
config.enable_typos = True
config.sentece_typo_rate = 0.93
# spacing errors
config.enable_spacing = True
config.space_del_probability = 0.1
config.space_add_probability = 0.08

noise = Konoise(config=config)

def process_line(row, target_row=0, allow_noerror=True, per_sentence=10, prefix=""):
    results = []
    try:
        for _ in range(per_sentence):
            errored = noise.process(row[target_row])
            if allow_noerror or row[target_row] != errored:
                results.append(prefix + errored + "\t"  + row[target_row]+ "\n")
    except KeyboardInterrupt:
        pass
    return results


def process(reader, target_row=0, allow_noerror=True, per_sentence=10, skip_headers=True, prefix="", total_lines=0, poolsize=8):
        if skip_headers:
            next(reader, None)

        results = []

        closure = partial(process_line, target_row=target_row, allow_noerror=allow_noerror, per_sentence=per_sentence, prefix=prefix)

        with Pool(poolsize) as p:
            for result in tqdm.tqdm(p.imap_unordered(closure, reader), total=total_lines):
                results.append(result)
        
        return results


def main():
    # only print to stdout instead of file
    test=False

    folder = '/home/testuser/'
    filename = 'testdata'
    filesuffix = '.csv'

    with open(folder+filename+filesuffix, encoding="utf-8") as input:
        data = csv.reader(input, delimiter='\t')
        results = process(
                data, # iterable indexable data ->  for x in data: x[0] must be a valid operation 
                allow_noerror=True, # if konoise does not produce an error with our settings, should the sentence still be included (i.e., the original)?
                target_row=0, # which row of the data should be accessed?
                per_sentence=3, # how many errorneous versions should be produced?
                skip_headers=False, # are there headers in the csv file we should skip?
                prefix="correct korean grammar: ", # prefix for a t5 task
                total_lines=466508, # how many lines are there in the file for better output
                poolsize=8 # how many processes should be used?
            )
    
    with open(folder+"synthetic_"+filename+".tsv", "w+", encoding="utf-8") as output:
        # write results to target
        for row in results:
            try:
                for result in row:
                    if test:
                        print(result, end='')
                    else:
                        output.write(result)
            except Exception as e:
                print(e)


if __name__ == "__main__":
    main()