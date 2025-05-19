# # import pyautogui
# # import time

# # # Move the mouse to a specific position and click
# # pyautogui.moveTo(500, 500, duration=1)  # Moves to (500, 500) in 1 second
# # pyautogui.click()

# # # Type some text
# # pyautogui.write("Hello, this is an automated message!", interval=0.1)

# # # Press Enter
# # pyautogui.press("enter")

# # # Press a key combination (e.g., Command + C for copy)
# # pyautogui.hotkey("command", "c")

# # import pyautogui

# # for i in range(5):
# #     pyautogui.moveRel(100, 50, duration=0.5)  # Move diagonally down-right
# #     pyautogui.moveRel(-100, 50, duration=0.5)  # Move diagonally down-left

# # print("Zig-zag motion complete!")
# import pyautogui
# import random
# import time

# # Get screen size
# screen_width, screen_height = pyautogui.size()

# # Start at a random position
# x, y = random.randint(100, screen_width - 100), random.randint(100, screen_height - 100)

# for _ in range(50):  # Loop 50 times (adjust as needed)
#     # Generate small random changes in x and y
#     x += random.randint(-200, 200)  # Move in a range of -200 to 200 pixels
#     y += random.randint(-200, 200)

#     # Ensure the mouse stays within screen bounds
#     x = max(0, min(x, screen_width - 1))
#     y = max(0, min(y, screen_height - 1))

#     # Random duration for smoother movement
#     duration = random.uniform(0.1, 0.7)

#     # Move the mouse
#     pyautogui.moveTo(x, y, duration=duration)

#     # Random sleep time to mimic natural movement
#     time.sleep(random.uniform(0.2, 1.0))

# print("Dynamic mouse movement complete!")


