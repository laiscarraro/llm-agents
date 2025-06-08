from src.utils.syllable_split import get_syllable_dict
from src.utils.rhythm_utils import (
    get_words,
    get_keywords,
    process_syllables,
    get_mean_syllables
)
from smolagents import tool
from typing import Dict, List


@tool
def divide_syllables(verse: str) -> Dict[str, int]:
    """
    Divides a verse into syllables.
    Returns a dictionary with the verse text divided into syllables and syllable count.

    Args:
        verse: A verse of a song.
    """
    words = get_words(verse)
    keywords = get_keywords(verse)
    syllable_dict = get_syllable_dict()
    phonemes = [syllable_dict.get(word, '') for word in words]
    syllables = ''
    
    for i in range(len(words)):
        is_keyword = words[i] in keywords
        if len(phonemes[i]) == 1:
            if is_keyword:
                words[i] = words[i].upper()
            syllables += words[i] + ' '
        else:
            syllables += process_syllables(
                words[i], phonemes[i], is_keyword
            ) + ' '
    syllables = syllables.strip()
    syllables_count = syllables.count(' ') + syllables.count('-') + 1
    return {
        'text': syllables,
        'syllables': syllables_count
    }


@tool
def get_possible_time_signatures(verses_syllables: List[Dict[str, str]]) -> List[str]:
    """
    Determines the possible time signatures for the song depending on the number of syllables in the verse list.
    Returns a list of strings that represent the possible time signatures that can be chosen to these particular lyrics.

    Args:
        verses_syllables: a list of dictionaries that contain the syllable division of each verse
    """
    mean_syllables = get_mean_syllables(verses_syllables)
    signatures = {
        2: "2/4",
        3: "3/4",
        4: "4/4",
        6: "6/8",
        9: "9/8",
        12: "12/8"
    }

    answer = []
    for k in signatures.keys():
        if mean_syllables%k == 0:
            answer.append(signatures[k])
    
    return answer


@tool
def get_number_of_compasses(verses_syllables: List[Dict[str, str]], time_signature: str) -> int:
    """
    Given the list of verse syllables and a chosen time signature, this function calculates how many compasses are going to be created.
    Returns an integer that represents the number of compasses to be created.

    Args:
        verses_syllables: a list of dictionaries that contain the syllable division of each verse
        time_signature: a string in the format 'digit/digit' that represents the chosen time signature
    """
    number_of_notes, type_of_notes = time_signature.split('/')
    note_type = int(int(type_of_notes)/4)

    mean_syllables = get_mean_syllables(verses_syllables)
    compasses = round(mean_syllables/float(number_of_notes))
    n_compasses = len(verses_syllables)*compasses
    
    print(compasses, 'compasses per verse')
    print(number_of_notes, '1/'+str(note_type), 'notes per compass')
    print(n_compasses, 'compasses in total')

    return n_compasses