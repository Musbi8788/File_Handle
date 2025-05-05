# TODO 1 create a function to do the job
def find_and_replace_word(file_path, old_word, new_word):
    """
     open text file and read through it
     search a specific word and replace it with a new word,
     add file error handling in it for accept errors.
     the function is having three parameter:
     1: file_path = your file path
     2: Old word = str
     3: new word = str
     you can the word to replace at time you want...
     """
    try:
        # TODO 2 open the file as read mode
        with open(file_path, 'r') as text:
            messages = text.read()
            print(f'Old Message: {messages}')
        # check if the word is in the messages and notice the user about it.
        if new_word in messages:
            print(f"The word you're replacing with is already excite in the file, or you can delete the text.txt file.")

        replace_word = messages.replace(old_word, new_word)

        # TODO 3 open the file as write mode and replace the word
        #  and open it in read mode to verify is successfully replaced.
        with open('text.txt', 'w') as text:
            text.write(replace_word)

        with open('text.txt', 'r') as replace_file:
            file_with_new_word = replace_file.read()
            print(f'\nNew Message: {file_with_new_word}')

    # File Not Found and create simple message.
    except FileNotFoundError as bug:
        print(f"Bug {bug} but i will handle it.")
        file_message = "I love coding, Musbi python developer."

        with open('text.txt', 'w') as text:
           text.write(file_message)

        with open('text.txt', 'r') as new_message:
            file_message = new_message.read()
            print(f'New Text Message: {file_message}')

    except TypeError as invalid:
        print(f"\nError: {invalid}\nMake sure types are the same (e.g str str.) or you are trying to change word that is not in the file."
              f"\ncheck both>>\n\tOld word value: {old_word}\n\tNew old word value: {new_word}")


# file_path with old, new word
file_path_ = f'text.txt'
old_word_ = 'coding'
new_word_ = 'programming'

# function call
find_and_replace_word(file_path_, old_word_, new_word_)
