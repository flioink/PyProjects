import ctypes


MessageBoxA = ctypes.windll.user32.MessageBoxA
# var = ctypes.c_bool(True)
NULL = 0
MB_OK = 0

MessageBoxA(NULL, ctypes.c_char_p(b"Hello from Python"), ctypes.c_char_p(b"Alert"), MB_OK)
