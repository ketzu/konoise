# ko_noiser - a synthetic sentence noise generator for korean

Inspired by the operations performed in ["Korean Grammatical Error Correction Based on Transformer with Copying Mechanisms and Grammatical Noise Implantation Methods"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8070563/) and similar efforts to generate synthetic errors in korean sentences.

## dependencies

 * hangul-utils (without optional dependencies)
 * g2pk-kiwipiepy (actual g2pK would work as well) 

## install

Installation should work using:

```
pip install git+https://github.com/ketzu/konoise.git
```

### g2pK(-kiwipiepy)

First install `g2pK` or `g2pK-kiwipiepy` by using

```
pip install g2pK
```

or 

```
pip install git+https://github.com/ketzu/g2pk.git
```

g2pk-kiwipiepy uses the same package name as g2pk (as it is a drop in replacement), so do not install both, it is just to avoid the dependency on python-mecab-ko.

## Usage

Konoise exposes a Konoise and Config class. The Konoise class exposes multiple functions, but the intended interface is `process(sentence[, config])`.
The process function takes a sentence and performs various probabilistic errors based on the configuration.

Example:

```
In [1]: import random
In [2]: random.seed(15)
In [3]: from konoise import Konoise
In [4]: noise = Konoise()
In [5]: test = '나는 집을 깨끗이 청소했다.'
In [6]: noise.process(test)
Out[6]: '나는 집을 깨끋이 청소핻다.'
```

## Inner Workings

Currently Konoise creates errors of 3 types:

 * G2P based errors: Words or whole sentences are changed to a pronounciation based form, using g2pK.
 * Typo based errors: Based on a typo map (see [konoise/config.py](konoise/config.py)) typos are randomly generated on the jamo level.
 * Spacing based: There is a chance any existing space is deleted or a random space is introduced between composed characters. 

## Config

The config object can be passed to the inital creation of the Konoise object or to every call to `process`.

The config has the following, semi self-explanatory options:

```
    # G2P based errors
    g2p_whole_sentence = False
    g2p_probability = 0.3
    descriptive_probability = 0.5
    group_vowels_probability = 0.3
    descriptive_always_group_vowels = False

    # typo errors
    enable_typos = True
    sentece_typo_rate = 0.85

    # spacing errors
    enable_spacing = True
    space_del_probability = 0.05
    space_add_probability = 0.03
```

## Contributions

Contributions are welcome. NLP and korean are not my areas of expertise.