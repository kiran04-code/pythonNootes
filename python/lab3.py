def longest_equal_fragment():
    print("Enter numbers ending with 0:")

    prev = None
    current_length = 0
    max_length = 0

    while True:
        num = int(input())

        if num == 0:
            break

        if num == prev:
            current_length += 1
        else:
            current_length = 1  # reset for a new number

        if current_length > max_length:
            max_length = current_length

        prev = num

    print("Length of widest fragment:", max_length)
longest_equal_fragment()
