import pyautogui

# Get screen size
screenWidth, screenHeight = pyautogui.size()

# Get current mouse position
currentMouseX, currentMouseY = pyautogui.position()

# Move and click at specific locations
pyautogui.moveTo(100, 150)
pyautogui.click()
pyautogui.click(100, 200)

# Move relative and double-click
pyautogui.move(400, 0)
pyautogui.doubleClick()

# Smooth movement with easing
pyautogui.moveTo(500, 500, duration=1, tween=pyautogui.easeInOutQuad)

# Typing and pressing keys
pyautogui.write('ishfaq', interval=0.25)
pyautogui.press('esc')

# Holding a key and pressing multiple times
with pyautogui.hold('shift'):
    pyautogui.press(['left', 'left', 'left', 'left'])

# Pressing hotkeys
pyautogui.hotkey('ctrl', 'c')

# Display an alert
pyautogui.alert('This is the message to display.')

# Draw a spiral pattern using dragging
distance = 200
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.5)   # Move right
    distance -= 5
    pyautogui.drag(0, distance, duration=0.5)   # Move down
    pyautogui.drag(-distance, 0, duration=0.5)  # Move left
    distance -= 5
    pyautogui.drag(0, -distance, duration=0.5)  # Move up

print("Automation complete!")
