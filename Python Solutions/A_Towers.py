def towers(kit):
    occurrence = {}
    for stick in kit:
        if stick in occurrence:
            occurrence[stick] += 1
        else:
            occurrence[stick] = 1

    max_count = max(occurrence.values())
    frequent = [key for key, value in occurrence.items() if value == max_count]

    return [max_count, frequent]

k = input()
kit = list(map(int, input().split()))

print(towers(kit))