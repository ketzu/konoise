import random
import csv
from hangul_utils import split_syllables, join_jamos
from .config import Config, typomap

class Konoise():
    def __init__(self, config: Config = None) -> None:
        if config:
            self.config = config
        else:
            self.config = Config()
        
        self.idioms = []
        with open('idioms.csv', 'r', encoding='utf-8') as idiom_file:
            idioms = csv.reader(idiom_file, delimiter='\t')
            for idiom in idioms:
                self.idioms.append((idiom[0], idiom[1]))

    def idioms(self, sentence:str, config: Config) -> str:
        def replace_by_idiom(word: str) -> str:
            for idiom in self.idioms:
                word = word.replace(idiom[0], idiom[1])
            return word
        
        return ' '.join([
            replace_by_idiom(word) if random.random() <= config.idiom_probability else word
            for word in sentence.split(' ')
        ])
    
    def replace_jamo(self, jamos:str, jamo:str, pos:int) -> str:
        return jamos[:pos] + jamo + jamos[pos+1:]

    def typo(self, jamos:str, config:Config):
        # are there even jamos in this string?
        if len(set(jamos).intersection(typomap)) <= 1:
            return jamos

        typos = 0
        while random.random() <= config.sentece_typo_rate and typos < config.max_typos:
            err_pos = -1

            failures = 0
            while err_pos == -1:
                # I should add more failsafes
                if failures > 100:
                    return jamos
                cand = random.randint(0, len(jamos)-1)
                if jamos[err_pos] in typomap:
                    err_pos = cand
                else:
                    failures += 1
            typolist = typomap.get(jamos[err_pos], [])

            if len(typolist) < 1:
                # some danger for an infinite loop if typomap has empty entries!
                continue

            jamos = self.replace_jamo(jamos, typolist[random.randint(0,len(typolist)-1)], err_pos)
            typos += 1

        return jamos

    def deletions(self, jamos:str, config:Config) -> str:
        
        dels = 0
        while random.random() <= config.sentence_deletion_rate and dels < config.max_typos:
            err_pos = random.randint(0, len(jamos)-1)
            jamos = self.replace_jamo(jamos, '', err_pos)
            dels += 1
            
        return jamos

    def spacing(self, sentence:str, config:Config) -> str:
        syllables = []
        for syllable in sentence:
            if syllable == ' ': # change to regular expression for whitespace
                if random.random() > config.space_del_probability:
                    syllables.append(syllable)
            else:
                if random.random() <= config.space_add_probability:
                    syllables.append(' ')
                syllables.append(syllable)
        return ''.join(syllables) 

    def process(self, sentence: str, config: Config = None) -> str:
        '''
            Steps to perform:

             * Idiom replacement chance (based on g2pK)
             
             * Split into jamos for further modification
               * 
               * Add random typos based on typo map
             * Recompose from jamos

             * Introduce spacing errors


        '''
        # if no special config is provided, use our own
        if config is None:
            config = self.config

        if config.enable_idiom_replacement:
            sentence = self.idioms(sentence, config)

        jamos = split_syllables(sentence)
        
        # Do G2p things
        

        # G2p things finished

        if config.enable_typos:
            sentence = self.typo(sentence, config)

        if config.enable_deletions:
            sentence = self.deletions(sentence, config)
        
        sentence = join_jamos(jamos)

        if config.enable_spacing:
            sentence = self.spacing(sentence, config)

        return sentence
        


