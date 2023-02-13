import pyautogui
import time
import webcolors
import keyboard

def get_color():
    x, y = pyautogui.position()
    color = pyautogui.screenshot().getpixel((x, y))
    hex_color = webcolors.rgb_to_hex(color)
    return hex_color, color

def main():
    print("Press 'F8' to get color values under cursor.")
    print("Press 'F9' to exit.")
    while True:
        if keyboard.is_pressed('f8'):
            hex_color, color = get_color()
            print(f"HEX: {hex_color}")
            print(f"RGB: {color}")
            time.sleep(1)
        if keyboard.is_pressed('f9'):
            print('Exit!')
            break

if __name__ == "__main__":
    main()
