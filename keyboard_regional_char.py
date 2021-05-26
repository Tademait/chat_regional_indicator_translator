import keyboard
string = ":regional_indicator_"

print("The program is running, enjoy your spam session")
while True:
    if keyboard.is_pressed('esc'):
        print("============ the program has ended ============")
        break
    if keyboard.is_pressed('space'):
        keyboard.write("   ")
    for char in "abcdefghijklmnopqrstuvwxyz":
        if keyboard.is_pressed(char):
            keyboard.write("\b")
            keyboard.write(string + char + ": ")
