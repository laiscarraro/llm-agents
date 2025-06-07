from nltk.tokenize import RegexpTokenizer
from nltk.tag import pos_tag
import numpy as np
import re


def get_words(verse):
    tokenizer = RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(verse)
    lower_words = [w.lower() for w in words]
    return lower_words


def get_keywords(verse):
    words = get_words(verse)
    tags = pos_tag(words)
    keyword_tags = [
        'JJ', 'RB', 'VB', 'NN', 'UH'
    ]
    to_be = [
        'am', 'im', 'm', 'are', 're', 'is', 's',
        'be', 'was', 'were'
    ]
    
    keywords = []
    for t in tags:
        match_keyword = any([
            a in t[1] for a in keyword_tags
        ]) and not any([
            be == t[0] for be in to_be
        ])
        if match_keyword and len(t[0]) > 1:
            keywords.append(t[0])
    
    return keywords


def get_similar_cut(word, cut):
    sim_cuts = {
        'k': {
            'gh': 'g',
            'cl': 'c',
            'cq': 'c',
            'cr': 'c',
            'ch': 'c',
            'cc': 'c',
            'ca': 'c',
            'co': 'c',
            'cu': 'c',
            'ci': 'c',
            'cy': 'c',
            'mc': 'm',
            'q': 'q' 
        },
        'e': {
            'ar$': 'a',
            'er$': 'e',
            'or$': 'o',
            'on$': 'o',
            'ir$': 'i',
            'ard$': 'a',
            'ors$': 'o',
            'ary$': 'a',
            'ation$': 'a',
            'war': 'w',
            'our': 'o',
            'abl': 'a',
            'ban': 'b',
            'aco': 'a',
            'ach': 'a',
            'ack': 'a',
            'ua': 'u',
            'ra': 'r',
            'ia': 'i',
            'ya': 'y',
            'iu': 'i',
        },
        's': {
            'ti': 't',
            'tual': 't',
            'ci': 'c',
            'ch': 'c',
            'cc': 'c',
            'ce': 'c',
            'ct': 'c',
            'cy': 'c',
            'zz': 'z',
            'x': 'x',    
        },
        'j': {
            'gi': 'g',
            'dge': 'd',
            'ge': 'g',
            'dua': 'd',
            'dul': 'd',
            'adu': 'a',
            'edu': 'e',
            'ndu': 'n',
            'rdu': 'r',
            'gy': 'g',
        },
        'z': {
            's': 's',
            'kz': 'k',
            'x': 'x',
        },
        'd': {
            'th': 't'
        },
        'f': {
            'ph': 'p'
        }
    }
    candidates_dict = sim_cuts.get(cut, None)
    if candidates_dict is not None:
        for key in candidates_dict.keys():
            if '$' in key:
                if word.endswith(key[:-1]):
                    return candidates_dict[key]
            else:
                if key in word:
                    return candidates_dict[key]
    return cut


def remove_trailing(word):
    if word[0] == '-':
        return word[1:]
    if word[-4:] == '----':
        return word[:-4]
    elif word[-3:] == '---':
        return word[:-3]
    elif word[-2:] == '--':
        return word[:-2]
    elif word[-1:] == '-':
        return word[:-1]
    else:
        return word


def process_syllables(word, phonemes, is_keyword):
    preprocessed_phonemes = [
        re.sub('0|2', '', re.sub(' ', '', p)) if is_keyword
        else re.sub('\d', '', re.sub(' ', '', p)) for p in phonemes
    ]
    accents = [
        True if '1' in p else False for p in preprocessed_phonemes
    ]
    cut_points = [
        p[0] for p in preprocessed_phonemes
    ]

    final_word = ''
    cut_word = word

    for i in range(1, len(accents)):
        cut = cut_points[i]
        was_accent = accents[i-1]
        if cut not in cut_word:
            try:
                prev_cut = cut_points[i-1]
                isolate_syl = ''.join(re.split(prev_cut, cut_word)[1:])
                cut = get_similar_cut(isolate_syl, cut)
            except:
                cut = get_similar_cut(cut_word, cut)

        splitted = re.split(cut, cut_word)
        rest = [cut + s for s in splitted[1:]]
        cut_word = ''.join(rest)

        if was_accent:
            splitted[0] = splitted[0].upper()
        final_word += splitted[0] + '-'
    
    if len(accents) > 0:
        if accents[-1]:
            cut_word = cut_word.upper()
    
    final_word += cut_word

    return remove_trailing(final_word)


def get_mean_syllables(verses_syllables):
    syllables_in_stanza = [
        verse['syllables'] for verse in verses_syllables
    ]

    mean_syllables = np.round(
        np.mean(syllables_in_stanza)
    )

    return mean_syllables
