import wave_helper, copy, math, os

REVERSE = '1'
NEGATIVE = '2'
FAST = '3'
SLOW = '4'
UP = '5'
DOWN = '6'
DIM = '7'
EXIT_EDIT = '8'
MIN_VOLUME = -32768
MAX_VOLUME = 32767
SAMPLE_RATE = 2000

NOTE_DICT = {'A': 440, 'B': 494, 'C': 523, 'D': 587, 'E': 659, 'F': 698, 'G': 784}
SILENCE = 'Q'


########################################
# ~~~~OPTION 1~~~EDITING MENU~~~~~~~####
########################################

def get_file_for_compose():
    file_to_compose = ""
    done = False
    print("Welcome to compose mode!")
    while not done:
        print("Enter instructions file name to compose: (-1 to cancel) ")
        file_to_compose = input()
        if file_to_compose == '-1':
            done = True
        else:

            if not os.path.isfile(file_to_compose):
                print("----------------------")
                print("-File doesn't exist!--")
                print("----------------------")
            else:
                done = True

    return file_to_compose

def get_file():


    print("Enter filename to edit: (-1 to cancel) ")
    file_name_input = input()
    audio_list = wave_helper.load_wave(file_name_input)
    if audio_list != -1:
        return file_name_input, audio_list[0], audio_list[1]
    while wave_helper.load_wave(file_name_input) == -1:
        print("----------------------")
        print("File is not supported!")
        print("----------------------")
        file_name_input = input("Enter filename to edit: (-1 to cancel) ")
        audio_list = wave_helper.load_wave(file_name_input)
    return file_name_input, audio_list[0], audio_list[1]

"""

def get_file():

    this function gets return wav file according to user input

    file_name_input = ""
    done = False
    while not done:
        audio_list = [-1, -1]
        print("Enter filename to edit: (-1 to cancel) ")
        file_name_input = input()
        if file_name_input == '-1':
            done = True
        else:
            audio_list = wave_helper.load_wave(file_name_input)
            if audio_list == -1:
                print("----------------------")
                print("File is not supported!")
                print("----------------------")
            else:
                done = True
    return file_name_input, audio_list[0], audio_list[1]
"""


def editing_menu(filename, sample_rate, audio_data):
    """
    """
    if audio_data == -1 and sample_rate == -1:
        return

    audio_file = [sample_rate, audio_data]
    audio_file_copy = copy.deepcopy(audio_file)
    keep_edit = True
    print(f"{filename} is ready for some action! ")
    while keep_edit:
        print_menu()
        user_choice = input()
        if user_choice == REVERSE:
            audio_file_copy[1] = reverse_audio(audio_file_copy[1])
            print("~~~~~~~~~~~~~~~~~~~~~")
            print("~~Reverse completed~~")
            print("~~~~~~~~~~~~~~~~~~~~~")

        elif user_choice == NEGATIVE:
            audio_file_copy[1] = negative_audio(audio_file_copy[1])
            print("~~~~~~~~~~~~~~~~~~~~~~")
            print("~~Negative completed~~")
            print("~~~~~~~~~~~~~~~~~~~~~~")

        elif user_choice == FAST:
            audio_file_copy[1] = accelerate_audio(audio_file_copy[1])
            print("~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~Accelerate completed~~")
            print("~~~~~~~~~~~~~~~~~~~~~~~~")

        elif user_choice == SLOW:
            audio_file_copy[1] = slow_down_audio(audio_file_copy[1])
            print("~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~Slow Down completed~~")
            print("~~~~~~~~~~~~~~~~~~~~~~~")

        elif user_choice == UP:
            audio_file_copy[1] = volume_up_audio(audio_file_copy[1])
            print("~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~Volume up completed~~")
            print("~~~~~~~~~~~~~~~~~~~~~~~")

        elif user_choice == DOWN:
            audio_file_copy[1] = volume_down_audio(audio_file_copy[1])
            print("~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~Volume Down completed~~")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~")

        elif user_choice == DIM:
            audio_file_copy[1] = dim_filter_audio(audio_file_copy[1])
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~Low Pass Filter completed~~")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        elif user_choice != EXIT_EDIT:
            print("-------------------------")
            print("Invalid input, try again!")
            print("-------------------------")

        if user_choice == EXIT_EDIT:
            keep_edit = False
            save_audio(filename, audio_file_copy)
            print("~~~~~~~~~~~~~~")
            print("~~File saved~~")
            print("~~~~~~~~~~~~~~")


# function 1 of 7
def reverse_audio(edited_wave_file):
    """
    1.
    """
    return edited_wave_file[::-1]


# function 2 of 7
def negative_audio(audio_list):
    """
    2.
    """
    for i in range(len(audio_list)):
        value_1 = audio_list[i][0]
        value_2 = audio_list[i][1]
        if value_1 == MIN_VOLUME:
            value_1 += 1
        if value_2 == MIN_VOLUME:
            value_2 += 1
        audio_list[i][0] = -1 * value_1
        audio_list[i][1] = -1 * value_2
    return audio_list


# function 3 of 7
def accelerate_audio(edited_wave_file):
    """
    3.
    """
    accelerate_wave = list()
    for i in range(len(edited_wave_file)):
        if i % 2 == 0:
            accelerate_wave.append(edited_wave_file[i])

    return accelerate_wave


# function 4 of 7
def slow_down_audio(audio_list):
    """ 4. this function get wav list and add between each pair new item which is the average of them"""
    samples_len = len(audio_list)
    for i in range(1, 2 * samples_len - 1, 2):
        avg1 = int((audio_list[i - 1][0] + audio_list[i][0]) / 2)
        avg2 = int((audio_list[i - 1][1] + audio_list[i][1]) / 2)
        audio_list.insert(i, [avg1, avg2])
    return audio_list


# function 5 of 7
def volume_up_audio(audio_list):
    """
    5
    """
    for i in range(len(audio_list)):
        if len(audio_list[i]) >= 1:
            if int(audio_list[i][0] * 1.2) < MAX_VOLUME and int(audio_list[i][0] * 1.2) > MIN_VOLUME:
                audio_list[i][0] = int(audio_list[i][0] * 1.2)
            elif int(audio_list[i][0] * 1.2) > MAX_VOLUME:
                audio_list[i][0] = MAX_VOLUME
            else:
                audio_list[i][0] = MIN_VOLUME
            if int(audio_list[i][1] * 1.2) < MAX_VOLUME and int(audio_list[i][1] * 1.2) > MIN_VOLUME:
                audio_list[i][1] = int(audio_list[i][1] * 1.2)
            elif int(audio_list[i][1] * 1.2) > MAX_VOLUME:
                audio_list[i][1] = MAX_VOLUME
            else:
                audio_list[i][1] = MIN_VOLUME
    return audio_list


# function 6 of 7
def volume_down_audio(audio_list):
    """
    6
    """
    for i in range(len(audio_list)):
        if len(audio_list[i]) >= 1:
            audio_list[i][0] = int(audio_list[i][0] / 1.2)
            audio_list[i][1] = int(audio_list[i][1] / 1.2)

    return audio_list


# function 7 of 7
def dim_filter_audio(audio_list):
    """
    7
    """
    dimmed_wav_list = list()
    if len(audio_list) == 0 or len(audio_list) == 1:
        return audio_list
    for i in range(len(audio_list)):
        if i == 0:
            left_avg = int((audio_list[i][0] + audio_list[i + 1][0]) / 2)
            right_avg = int((audio_list[i][1] + audio_list[i + 1][1]) / 2)
        elif i == len(audio_list) - 1:
            left_avg = int((audio_list[i - 1][0] + audio_list[i][0]) / 2)
            right_avg = int((audio_list[i - 1][1] + audio_list[i][1]) / 2)
        else:
            left_avg = int((audio_list[i - 1][0] + audio_list[i][0]
                            + audio_list[i + 1][0]) / 3)
            right_avg = int((audio_list[i - 1][1] + audio_list[i][1]
                             + audio_list[i + 1][1]) / 3)
        dimmed_wav_list.append([left_avg, right_avg])
    return dimmed_wav_list


########################################
# ~~~~OPTION 2~~~COMPOSE MENU~~~~~~~####
########################################


def convert_to_list_of_tuples(note_file):
    """
    """
    new_note_file = list()
    for i in range(0, len(note_file), 2):
        new_note_file.append((note_file[i], int(note_file[i + 1])))

    return new_note_file


def read_notes_for_compose(filename):
    """
    this function gets txt file, read it and converts the content into list
    """

    with open(filename, 'r') as notes_file:
        note_file = []
        for char in notes_file.read():
            note_file.extend(char.strip().split())
        note_file = convert_to_list_of_tuples(fix_list(note_file))

    return note_file


def fix_list(note_file):
    fixed_list = []
    for i in range(len(note_file) + 1):
        if i < len(note_file):
            if note_file[i].isalpha():
                fixed_list.append(note_file[i])
            elif i < len(note_file) - 1:
                if note_file[i].isdigit() and note_file[i + 1].isdigit():
                    fixed_list.append(note_file[i] + note_file[i + 1])
                    note_file.remove(note_file[i + 1])
                else:
                    fixed_list.append(note_file[i])

            else:
                fixed_list.append(note_file[i])

    return fixed_list


def compose_melody(filename):
    """
    """
    notes_list = read_notes_for_compose(filename)
    composed_audio_list = list()

    for note in range(0, len(notes_list)):

        char, duration = notes_list[note]
        if char != SILENCE:
            frequency_rate = NOTE_DICT[char]  # Note
            sample_for_sound = duration * 125  # number
            samples_per_cycle = SAMPLE_RATE / frequency_rate
        elif char == SILENCE:
            sample_for_sound = duration * 125
            samples_per_cycle = 0

        for i in range(sample_for_sound):
            if samples_per_cycle == 0:
                composed_audio_list.append([0, 0])
            else:
                formula = int(MAX_VOLUME * math.sin((2 * math.pi * i) / samples_per_cycle))
                composed_audio_list.append([formula, formula])
    print(len(composed_audio_list))
    return composed_audio_list


def start_menu():
    """ this function is the start menu of the program """

    keep_it_active = True
    while keep_it_active:

        print("Welcome! \n --press 1 for editing wav file \n --press 2 for composing a melody \n --press 3 to exit \n")
        user_input = input()
        if user_input == '1':
            filename, sample_rate, audio_data = get_file()
            editing_menu(filename, sample_rate, audio_data)
        elif user_input == '2':
            composed_file_input = get_file_for_compose()
            if composed_file_input == '-1':
                continue
            composed_file = [SAMPLE_RATE, []]
            composed_file[1] = compose_melody(composed_file_input)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~Composition completed. Refering to editing menu...~~")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            editing_menu(composed_file_input, composed_file[0], composed_file[1])
        elif user_input != '3':
            print("-------------------------")
            print("Invalid input, try again!")
            print("-------------------------")
        if user_input == '3':
            keep_it_active = False
    print("GOODBYE")


def print_menu():
    """print menu information"""
    print("Welcome to editing menu!")
    print("1. Reverse audio")
    print("2. Negative")
    print("3. Accelerate")
    print("4. Slow down")
    print("5. Volume up")
    print("6. Volume down")
    print("7. Low-Pass Filter")
    print("8. Save File and return to main menu")
    print(" -- pick your choice: ")


def save_audio(filename, wav_list):
    """
    """
    valid_file = False
    temp_file = filename
    print(f"File name: {filename}.  Do you want to change the name?")
    while not valid_file:
        temp_file = input("enter valid filename: ")
        if temp_file != "":
            valid_file = True
        #if ".wav" not in temp_file:
         #   temp_file += ".wav"
    wave_helper.save_wave(wav_list[0], wav_list[1], temp_file)


if __name__ == '__main__':
    start_menu()
