# coding=utf-8
import ctypes, sys

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

FOREGROUND_BLUE = 0x09  # blue.
FOREGROUND_GREEN = 0x0a  # green.
FOREGROUND_RED = 0x0c  # red.

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool

def resetColor():
    set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)

def Green(mess):
    set_cmd_text_color(FOREGROUND_GREEN)
    sys.stdout.write(mess)
    resetColor()

def Red(mess):
    set_cmd_text_color(FOREGROUND_RED)
    sys.stdout.write(mess)
    resetColor()



