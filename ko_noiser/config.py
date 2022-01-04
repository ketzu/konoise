

class Config():
    def __init__(self) -> None:
        # G2P config
        self.enable_idiom_replacement = True
        self.idiom_probability = 0.3

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


typomap = {
 'ᅙ': ['ᅙ'], # ???
 'ᆞ': ['ᆞ'], # ???
 'ᆡ': ['ᆡ'], # ???

 # Keyboard proximity based
 'ᅵ': ['ㅏ','ㅐ'],
 'ㅇ': ['ㄷ','ㄹ','ㅊ','ㄴ'],
 'ᄋ': ['ㄷ','ㄹ','ㅊ','ㄴ'],
 'ㅂ': ['ㅃ','ㅈ','ㅁ'],
 'ᆸ': ['ㅃ','ㅈ','ㅁ'],
 'ㅍ': ['ㅠ','ㅊ','ㄹ','ㅎ'],
 'ᆯ': ['ㅇ', 'ㅎ','ㅍ','ㄱ'],
 'ㄹ': ['ㅇ', 'ㅎ','ㅍ','ㄱ'],
 'ㅊ': ['ㅌ','ㅇ','ㅍ'],
 'ㅈ': ['ㅉ','ㅂ','ㄷ','ㄴ'],
 'ㅎ': ['ㅠ','ㅗ','ㅅ','ㄹ'],
 'ᄒ': ['ㅠ','ㅗ','ㅅ','ㄹ'],
 'ㅌ': ['ㅋ','ㅊ','ㄴ'],
 'ㄷ': ['ㅈ','ㄱ','ㅇ','ㄸ'],
 'ᄃ': ['ㅈ','ㄱ','ㅇ','ㄸ'],
 'ㅅ': ['ㅎ','ㄱ','ㅠ','ㅆ'],
 'ㄴ': ['ㅌ','ㅁ','ㅈ','ㅇ'],
 'ㅁ': ['ㅂ','ㅋ','ㄴ'],
 'ㅋ': ['ㅁ', 'ㅌ'],
 'ㄱ': ['ㄲ','ㅅ','ㅎ','ㅛ'],
 'ㅑ': ['ㅐ','ㅏ','ㅕ'],
 'ㅗ': ['ㅠ','ㅜ','ㅛ','ㅓ','ㅎ'],
 'ㅣ': ['ㅏ','ㅐ'],
 'ㅖ': ['ㅒ','ㅔ'],
 'ㅐ': ['ㅣ','ㅒ','ㅑ'],
 'ㅒ': ['ㅖ','ㅐ'],
 'ㅛ': [ 'ㅗ','ㅅ','ㅕ'],
 'ㅠ': ['ㅜ','ㅍ'],
 'ㅏ': ['ㅣ','ㅓ','ㅑ'],
 'ㅓ': [ 'ㅗ','ㅜ','ㅏ','ㅕ'],
 'ㅜ': [ 'ㅗ','ㅠ','ㅡ','ㅓ'],
 'ㅕ': ['ㅓ','ㅛ','ㅑ'],
 'ㅡ': ['ㅜ','ㅓ','ㅏ'],
 'ㅔ': ['ㅖ','ㅐ'],

 'ㄵ': ['ㅉ','ㅈ'],
 'ㄺ': ['ㄱ','ㄹ','ㄲ'],
 'ㄾ': ['ㄹ','ㅌ'],
 'ㅉ': ['ㅈ','ㅃ'],
 'ㄸ': ['ㄷ','ㅉ','ㄲ'],
 'ㄼ': ['ᆸ','ㄹ'],
 'ㅃ': ['ᆸ','ㅉ'],
 'ㄻ': ['ㄹ','ㅁ'],
 'ㄲ': ['ㄱ','ㅆ','ㄸ'],
 'ㄳ': ['ㅅ','ㄱ'],
 'ㄶ': ['ㄴ','ㅎ','ㄲ'],
 'ㅀ': ['ㄹ','ㅎ'],
 'ㅄ': ['ㅅ','ᆸ'],
 'ㅆ': ['ㅅ','ㄲ'],

# Random
 'ㅝ': ['ㅙ','ㅢ','ㅟ','ㅘ','ㅞ','ㅚ'],
 'ㅙ': ['ㅝ','ㅢ','ㅟ','ㅘ','ㅞ','ㅚ'],
 'ㅢ': ['ㅝ','ㅙ','ㅟ','ㅘ','ㅞ','ㅚ'],
 'ㅟ': ['ㅝ','ㅙ','ㅢ','ㅘ','ㅞ','ㅚ'],
 'ㅘ': ['ㅝ','ㅙ','ㅢ','ㅟ','ㅞ','ㅚ'],
 'ㅞ': ['ㅝ','ㅙ','ㅢ','ㅟ','ㅘ','ㅚ'],
 'ㅚ': ['ㅝ','ㅙ','ㅢ','ㅟ','ㅘ','ㅞ'],

}