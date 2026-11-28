
# apl-source:1
# مثال 191 — كشف الجناس الناقص
# apl-source:2
# Anagram detection
# apl-source:3
# Demonstrates: مفرز، ضم، تجميع بالقواميس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/191-anagrams.apl
# apl-source:6

# apl-source:7
def مفتاح_جناس(كلمة):
    # apl-source:8
    return "".join(sorted(كلمة))
# apl-source:9

# apl-source:10
def جناس(أ, ب):
    # apl-source:11
    return مفتاح_جناس(أ) == مفتاح_جناس(ب)
# apl-source:12

# apl-source:13
print("listen / silent:", جناس("listen", "silent"))
# apl-source:14
print("hello / world:", جناس("hello", "world"))
# apl-source:15

# apl-source:16
كلمات = ["eat", "tea", "tan", "ate", "nat", "bat"]
# apl-source:17
مجموعات = {}
# apl-source:18
for ك in كلمات:
    # apl-source:19
    م = مفتاح_جناس(ك)
    # apl-source:20
    if م not in مجموعات:
        # apl-source:21
        مجموعات[م] = []
    # apl-source:22
    مجموعات[م].append(ك)
# apl-source:23

# apl-source:24
for م in مجموعات:
    # apl-source:25
    print(مجموعات[م])
# apl-source:26
