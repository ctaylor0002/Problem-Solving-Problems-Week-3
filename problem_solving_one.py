def problem_one(sentence):
    return sentence[::-1]

def problem_two(sentence):
    split_sentence = sentence.split()
    return_data = ""
    for word in split_sentence:
        return_data = return_data + " " + word.title()

    return return_data