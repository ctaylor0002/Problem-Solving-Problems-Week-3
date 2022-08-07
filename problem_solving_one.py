def problem_one(sentence):
    return sentence[::-1]

def problem_two(sentence):
    split_sentence = sentence.split()
    return_data = ""
    for word in split_sentence:
        return_data = return_data + " " + word.title()

    return return_data

def problem_three(data):
    send_data = ""
    str_counter = 0
    counter = 0
    str_len = len(data)

    for character in data:
        if str_counter == str_len - 1:
            send_data = send_data + str(counter + 1) + data[str_counter -1]
            counter = 0
            str_counter = 0
        else:
            if str_counter == 0:
                counter += 1
                str_counter += 1
            elif str_counter == str_len:
                send_data = send_data + str(counter) + character
        
            elif character == data[str_counter-1]:
                counter += 1
                str_counter += 1
            else:
                send_data = send_data + str(counter) + data[str_counter -1]
                counter = 1
                str_counter += 1

    return(send_data)
