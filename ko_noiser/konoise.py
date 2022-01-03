import g2pk
from hangul_utils import split_syllables, join_jamos
import random
from .config import Config, typomap


class Konoise():
    def __init__(self, config: Config = None) -> None:
        if config:
            self.config = config
        else:
            self.config = Config()
        
        try:
            self.g2p = g2pk.G2p()
        except Exception as ex:
            print("Konoise needs g2pk or g2pk-kiwipiepy... try pip install g2pk")
            raise ex

    def piece_to_phoneme(self, piece:str, config: Config):
        descriptive = random.random() <= config.descriptive_probability
        group_vowels = descriptive if config.descriptive_always_group_vowels else random.random() <= config.group_vowels_probability 
        return self.g2p(piece, descriptive=descriptive, group_vowels=group_vowels)
    
    def typo(self, sentence:str, config:Config):
        if len(set(sentence).intersection(typomap)) <= 1:
            return sentence

        jamos = split_syllables(sentence)

        while random.random() <= config.sentece_typo_rate:
            err_pos = -1
            while err_pos == -1:
                cand = random.randint(0, len(jamos)-1)
                if jamos[err_pos] in typomap:
                    err_pos = cand
            typolist = typomap.get(jamos[err_pos], [])
            if len(typolist) < 1:
                return sentence
            jamos = jamos[:err_pos] + typolist[random.randint(0,len(typolist)-1)] + jamos[err_pos+1:]

        return join_jamos(jamos)

    def spacing(self, sentence:str, config:Config):
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

    def process(self, sentence: str, config: Config = None):
        if config is None:
            config = self.config

        if config.g2p_whole_sentence:
            if random.random() <= config.g2p_probability:
                sentence = self.piece_to_phoneme(sentence, config)
        else:
            syllables = []
            for syllable in sentence:
                if random.random() <= config.g2p_probability:
                    syllables.append(self.piece_to_phoneme(syllable, config))
                else:
                    syllables.append(syllable)
            sentence = ''.join(syllables)
            
        if config.enable_typos:
            sentence = self.typo(sentence, config)
        
        return sentence
        


