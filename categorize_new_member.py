def open_or_senior(data):
    count = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            count.append('Senior')
        else:
            count.append('Open')
    return count

print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))