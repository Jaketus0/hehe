def runner_up(a, b, c, d, e):  # 5, 3, 2, 1, 0
    if a < b:
        win1 = a
        win2 = b
    else:
        win1 = b
        win2 = a
    # win1 = 3
    # win2 = 5
    if c < win1:
        win2 = win1  # win2 = 3
        win1 = c  # win1 = 2
    elif c < win2:
        win2 = c

    if d < win1:
        win2 = win1
        win1 = d
    elif d < win2:
        win2 = d

    if e < win1:
        win2 = win1
        win1 = e
    elif e < win2:
        win2 = e

    return win2
