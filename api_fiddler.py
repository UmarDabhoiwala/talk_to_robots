def fiddle_with_api_keys():

    open_ai_key = input("Enter Your openAI API Key")
    eleven_labs_key = input("Enter Your elevenLabs API Key")

    # open the input file for reading
    with open("config.py", "r") as f_in:
        # read the contents of the file
        file_contents = f_in.read()

    # find the variable you want to change
    old_value = "<YOUR_OPENAI_API_KEY>"
    new_value = open_ai_key

    file_contents = file_contents.replace(old_value, new_value)

    old_value = "<YOUR_ELEVENLABS_API_KEY>"
    new_value = eleven_labs_key
    file_contents = file_contents.replace(old_value, new_value)

    # open the output file for writing
    with open("audioToChat.py", "w") as f_out:
        # write the modified contents to the output file
        f_out.write(file_contents)
