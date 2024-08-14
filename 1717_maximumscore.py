s = 'aabbaaxybbaabb'
x, y = 5, 4

if x > y:
    top = x
    bot = y
    top_s = 'ab'
    bot_s = 'ba'
else:
    top = y
    bot = x
    top_s = 'ba'
    bot_s = 'ab'

result = 0
stack = []

for char in s:
    if char == top_s[1] and stack and stack[-1] == top_s[0]:
        result += top
        stack.pop()
    else:
        stack.append(char)

new_stack = []

for char in stack:
    if char == bot_s[1] and new_stack and new_stack[-1] == bot_s[0]:
        result += bot
        new_stack.pop()
    else:
        new_stack.append(char)

print(result)