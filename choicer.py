from audio_to_chat import return_choices


def numbered_list_string(lst):
    """
    Returns a string representation of the given list with each element
    numbered by its index.
    """
    return "\n".join([f"{i}. {elem}" for i, elem in enumerate(lst)])


def get_choicer():
    while True:
        try:
            duration_of_recording = int(
                input(
                    "How long would you like you're input recording to be? (in seconds):"
                )
            )

            if duration_of_recording < 1:
                raise Exception("please input a number greater than 1")
            break
        except Exception as e:
            print("please input a valid number")

    while True:
        try:
            number_of_responses = input(
                "How many responses would you like? Or type 'I' for infinite:"
            )

            if number_of_responses == "I":
                break
            number_of_responses = int(number_of_responses)

            if number_of_responses < 1:
                raise Exception("please input a number greater than 1")
            break
        except Exception as e:
            if number_of_responses == "I":
                break
            else:
                print("please input a valid choice")

    choices = list(return_choices())
    print(numbered_list_string(choices))
    while True:
        try:
            choice = int(input("Which voice would you like to use? (type the number):"))

            if choice not in range(0, len(choices)):
                raise Exception("please input a valid choice")
            break
        except Exception as e:
            print("please input a valid choice")

    return duration_of_recording, number_of_responses, choice
