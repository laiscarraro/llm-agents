def get_syllable_dict():
    dict_filename = 'src/utils/cmudict.rep'
    syllable_dict = {}

    with open(dict_filename) as f:
        for line in f:
            line = line.strip()
            line = line.lower()

            # ignore comments
            if line.startswith('##'):
                continue
            
            try:
                word, phones = line.split('  ')
                syll = phones.split(' - ')
                syllable_dict[word] = syll
            except:
                print('error parsing word ' + word)
    return syllable_dict