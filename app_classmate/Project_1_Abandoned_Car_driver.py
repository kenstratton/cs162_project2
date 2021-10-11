#!/usr/bin/env python3
# coding=utf-8
"""Project_1_Abandoned_Car_driver interacts with the Car class.

I meant for there to be a small story associated with this but that didn't end up happening.
I suppose you could consider this to be in Early Access.

Most of the tests I run involve bruteforce debugging with positive and negative testing.
I run through the program, especially methods that I'm not sure about, and stress test it,
feeding in positive and negative variables.
Once I'm satisfied with stepping through the program, I turn off all of the breakpoints
and run the program as if I were a user in order to see if it works as intended.
"""
import Project_1_Abandoned_Car
import os


def narrator(abandoned_car):
    """Set the scene."""
    print(f"You are a camp councelor at Camp Whatafalls. Somewhere around \
midnight, you heard a number of pained screams. After a brief investigation, \
you discovered a monstrous beast is hunting and killing all of the camp \
councelors and you're next. You take off into the forest hoping to lose the \
beast that is undoubtedly hunting you. After a few minutes of panicked running, \
you spot an abandoned car. {abandoned_car.get_car_state('engine')} \
{abandoned_car.get_car_state('door')} {abandoned_car.get_car_state('window')} \
The woods are currently quiet but the beast could be on you at any time, \
you have to act fast.")


def main_menu(abandoned_car):
    """Display main landing for this program. Prompts user to interact and explore."""
    RESPONSES = ["i", "inspect", "a", "act", "e", "exit"]
    while True:
        var_mm = get_user_input(["What do you want to do? [I]nspect, [A]ct, [E]xit ", str]).lower()
        if var_mm in RESPONSES:
            if var_mm == "i" or var_mm == "inspect":
                inspect_car(abandoned_car)
                break
            elif var_mm == "a" or var_mm == "act":
                act_car(abandoned_car)
                break
            elif var_mm == "e" or var_mm == "exit":
                exit_program()
        else:
            print("Sorry, that wasn't an expected response. Please try again.")


def get_user_input(text):
    """Get user input based on provided text. Attempts to enforce compliance \
    to desired format type.

    Args:
        text (list): Text must be a len 2 list. [0] is the input prompt, \
        format as str. [1] is the format type desired from the user input. Format [1] \
        as type (str and int currently supported).

    Returns:
        user_input: String output from the input prompt.
    """
    if text[1] == str:
        while True:
            user_input = input(text[0])
            if user_input.isalpha():
                break
            else:
                print("Sorry, input needs to be proper words. Try again.")
    elif text[1] == int:
        while True:
            user_input = input(text[0])
            if user_input.isnumeric():
                break
            else:
                print("Sorry, input needs to be a number. Try again.")
    return user_input


def inspect_car(abandoned_car):
    """Inpect the car."""
    CAR_PARTS = ["e", "engine", "d", "door", "w", "window", "g", "gear", "r", "radio"]
    while True:
        var_ic = get_user_input(["What do you want to inspect? [E]ngine, [D]oor, [W]indow, [G]ear, \
[R]adio ", str]).lower()
        if var_ic in CAR_PARTS:
            if var_ic == "e" or var_ic == "engine":
                var_ic2 = "engine"
                break
            elif var_ic == "d" or var_ic == "door":
                var_ic2 = "door"
                break
            elif var_ic == "w" or var_ic == "window":
                var_ic2 = "window"
                break
            elif var_ic == "g" or var_ic == "gear":
                var_ic2 = "gear"
                break
            elif var_ic == "r" or var_ic == "radio":
                var_ic2 = "radio"
                break
            else:
                print("Sorry, that wasn't an expected response. Please try again.")
    print(abandoned_car.get_car_state(var_ic2))


def act_car(abandoned_car):
    """Interact with the car."""
    ACTIONS = ["d", "door", "i", "ignition", "w", "windows", "h", "headlights", "r", "radio", "g",
               "gas", "b", "brake", "e", "gears"]
    while True:
        var_ac = get_user_input(["What do you want to do? [D]oor, [I]gnition, [W]indows, \
[H]eadlights, [R]adio, [G]as, [B]rake, G[e]ar ", str]).lower()
        if var_ac in ACTIONS:
            if var_ac == "d" or var_ac == "door":
                """This errors out. Can't figure out why, same structure as others. Others work but
                this doesn't!?"""
                print("The 'Door' command does not work due to a bug that has not been fixed.")
            elif var_ac == "i" or var_ac == "ignition":
                print(abandoned_car.toggle_ignition())
            elif var_ac == "w" or var_ac == "windows":
                window_query = 101
                while not(0 <= window_query <= 100):
                    window_query = int(get_user_input(["How high do you want to raise the windows? \
(0-100%) ", int]))
                    if not(0 <= window_query <= 100):
                        print("Sorry, that wasn't a valid response. Please try again.")
                print(abandoned_car.raise_windows(window_query))
            elif var_ac == "h" or var_ac == "headlights":
                print(abandoned_car.toggle_headlights())
            elif var_ac == "r" or var_ac == "radio":
                print(abandoned_car.toggle_radio())
            elif var_ac == "g" or var_ac == "gas":
                print(abandoned_car.apply_gas())
            elif var_ac == "b" or var_ac == "brake":
                print(abandoned_car.apply_brake())
            elif var_ac == "e" or var_ac == "gear":
                GEARS = ["P", "PARK", "R", "REVERSE", "D", "DRIVE"]
                gear_query = ""
                while gear_query not in GEARS:
                    gear_query = get_user_input(["What gear to you want to shift to? [P]ark, \
[R]everse, [D]rive ", str]).upper()
                    if gear_query not in GEARS:
                        print("Sorry, that wasn't a valid response. Please try again.")
                print(abandoned_car.change_gear(gear_query))
            write_car_state(abandoned_car)
            break


def exit_program():
    """Say goodbye and exit the program."""
    input("You have chosen to exit. Goodbye! (Press Return to close the program.)")
    os.remove("Abandoned_car")   # remove a file with the path just before exit
    raise SystemExit


# Write a file containing the current instance properties
def write_car_state(car):
    with open("Abandoned_car", "w") as f:
        f.write(car.driver_door + "\n")
        f.write(str(car.windows_perc) + "\n")
        f.write(car.headlights + "\n")
        f.write(car.radio + "\n")
        f.write(str(car.gas_ped) + "\n")
        f.write(str(car.brake_ped) + "\n")
        f.write(car.gear + "\n")
        f.write(car.engine_running + "\n")


# Read a file with instance properties, insert each property info into one sentence, and return it
def read_car_state():
    with open("Abandoned_car") as f:
        lines = f.readlines()
        door = lines[0]
        window = lines[1]
        headlights = lines[2]
        radio = lines[3]
        gas = "Off\n" if int(lines[4][0]) == 0 else "On\n"
        brake = "Off\n" if int(lines[5][0]) == 0 else "On\n"
        gear = lines[6]
        engine = lines[7]
        return "\n[Current car state]\nDoor: {}Window Height(0-100%): {}Gear: {}Radio: {}Headlights: {}Gas Peddale: {}Brake Peddale: {}Engine: {}".format(
            door,
            window,
            gear,
            radio,
            headlights,
            gas,
            brake,
            engine
        )

def __main__():
    abandoned_car = Project_1_Abandoned_Car.Car()
    write_car_state(abandoned_car)
    narrator(abandoned_car)
    while True:
        print(read_car_state())
        main_menu(abandoned_car)


if __name__ == "__main__":
    __main__()