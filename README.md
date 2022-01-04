# ko_noiser - a synthetic sentence noise generator for korean

Inspired by the operations performed in ["Korean Grammatical Error Correction Based on Transformer with Copying Mechanisms and Grammatical Noise Implantation Methods"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8070563/) and similar efforts to generate synthetic errors in korean sentences.

## dependencies

 * hangul-utils (without optional dependencies)

## install

Installation should work using:

```
pip install git+https://github.com/ketzu/konoise.git
```

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

 * G2P based errors: Words or whole sentences are changed to a pronounciation based form.
 * Typo based errors: Based on a typo map (see [konoise/config.py](konoise/config.py)) typos are randomly generated on the jamo level.
 * Deletion errors: there is a small probability to miss a jamo or accidentally delete it.
 * Spacing based: There is a chance any existing space is deleted or a random space is introduced between composed characters. 

## Config

The config object can be passed to the inital creation of the Konoise object or to every call to `process`.

The config has the following, semi self-explanatory options:

```
# G2P config
self.enable_idiom_replacement = True

# typo config
self.enable_typos = True
self.sentece_typo_rate = 0.85
self.max_typos = 10

# deletions config
self.enable_deletions = True
self.sentence_deletion_rate = 0.01
self.max_deletions = 1

# spacing
self.enable_spacing = True
self.space_del_probability = 0.05
self.space_add_probability = 0.03
```

## Alternative to ko_noiser

There seems to exist a project with the same original name `konoise` on [pypi](https://pypi.org/project/konoise/) or [github](https://github.com/wisenut-research/konoise) doing something similar.

## Data sources

The current idioms list is taken from [g2pK](https://github.com/Kyubyong/g2pK), neccesitating a license switch to Apache for simplicity. It's a cool project.

## Contributions

Contributions are welcome. NLP and korean are not my areas of expertise.