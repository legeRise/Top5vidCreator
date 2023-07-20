# import os
#
# a= os.getcwd()
# os.chdir(os.path.join(a,'images'))
# for i in range(1,6):
#     os.mkdir(i)
#__________________________________________
# a = {'ba':7}
# d = 5
#
# if d >= a['ba']:
#     print('yes')
# else:
#     print('no')

#___________________________________________
# actual = ['zoo',
# 'panda',
# 'zebra',
# 'lion',
# 'tiger',
# 'giraffe']
# timestamps = [
#     {"text": f"5. {actual[1]}", "start_time": 2.0, "end_time": 4.0},
#     {"text": f"4. {actual[2]}", "start_time": 4.0, "end_time": 6.0},
#     {"text": f"3. {actual[3]}", "start_time": 6.0, "end_time": 8.0},
#     {"text": f"2. {actual[4]}", "start_time": 8.0, "end_time": 10.0},
#     {"text": f"1. {actual[5]}", "start_time": 10.0, "end_time": 12.0},
# ]
#
# current = timestamps.pop(0)
# print(current)

#________________________________________
#text wrapping
def wrap_text(text, frame_width):
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) <= frame_width:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "

    # Add the last line
    if current_line:
        lines.append(current_line.strip())

    return lines


text = "lion treat nslkfsf dsf new"
frame_width = 506

wrapped_lines = wrap_text(text, frame_width)
print(wrapped_lines)


