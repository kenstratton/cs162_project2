#!/usr/bin/env python3
# coding=utf-8
"""Holds Car class."""


from typing import _SpecialForm


class Car:
    """Represents the abandoned car."""

    def __init__(self):
        """Set car's initial state."""
        self.driver_door = "Closed"
        self.windows_perc = 0
        self.headlights = "Off"
        self.radio = "On"
        self.gas_ped = 0
        self.brake_ped = 0
        self.gear = "P"
        self.engine_running = "Off"

    def get_car_state(self, user_query):
        """Return state of the car."""
        if user_query.lower() == "engine":
            printout = (f"The engine is {self.engine_running}.")
        elif user_query.lower() == "door":
            printout = (f"The driver door is {self.driver_door}.")
        elif user_query.lower() == "window":
            printout = (f"The windows are {self.windows_perc}% closed.")
        elif user_query.lower() == "gear":
            printout = (f"The current gear is {self.gear}.")
        elif user_query.lower() == "radio":
            if self.engine_running == "On":
                printout = (f"The radio is {self.radio}.")
            else:
                printout = "The radio appears to be Off."
        else:
            printout = "Sorry, I couldn't understand what you said. Try again."
        return printout

    def driver_door(self):
        """Open or close driver door."""
        if self.driver_door == "Closed":
            self.driver_door = "Open"
        else:
            self.driver_door = "Closed"
        printout = (f"The driver door is now {self.driver_door}.")
        return printout

    def toggle_ignition(self):
        """Turn the ignition/engine on or off."""
        if self.engine_running == "Off":
            self.engine_running = "On"
        else:
            self.engine_running = "Off"
        printout = (f"The engine is now {self.engine_running}.")
        return printout

    def raise_windows(self, user_query):
        """Raise or lower the windows."""
        if self.engine_running == "On":
            self.windows_perc = user_query
            printout = (f"The windows are {self.windows_perc}% closed.")
        else:
            printout = (f"The engine is not on, the windows won't move. \
They are {self.windows_perc}% closed.")
        return printout

    def toggle_headlights(self):
        """Turn the headlights on or off."""
        if self.headlights == "Off":
            self.headlights = "On"
        else:
            self.headlights = "Off"
        printout = (f"The headlights are {self.headlights}.")
        return printout

    def toggle_radio(self):
        """Turn the radio on or off."""
        if self.engine_running == "On" and self.radio == "On":
            self.radio = "Off"
            printout = (f"The radio is {self.radio}.")
        elif self.engine_running == "On" and self.radio == "Off":
            self.radio = "On"
            printout = (f"The radio is {self.radio}.")
        else:
            printout = (f"The radio appears to be Off but the car is not running.")
        return printout

    def apply_gas(self):
        """Step on the gas pedal."""
        if self.engine_running == "On":
            self.gas_ped = 1
            self.brake_ped = 0
        printout = "You step on the gas."
        return printout

    def apply_brake(self):
        """Step on the brake pedal."""
        if self.engine_running == "On":
            self.brake_ped = 1
            self.gas_ped = 0
        printout = "You step on the brake."
        return printout

    def change_gear(self, user_query):
        """Change gears."""
        if user_query == "P" or user_query == "R" or user_query == "D":
            self.gear = user_query
            printout = (f"The current gear is {self.gear}.")
        else:
            printout = "Sorry, I couldn't understand what you said. Try again."
        return printout