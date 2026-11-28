
# apl-source:1
# مثال 401 — لعبة الجلاد
# apl-source:2
# Hangman game
# apl-source:3
# Demonstrates: حلقة تخمين بمحاولات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/401-hangman-game.apl
# apl-source:6

# apl-source:7
كلمة = "برمجة"
# apl-source:8
مخفي = ["_", "_", "_", "_", "_"]
# apl-source:9
تخمينات = ["ب", "م", "ر", "ج", "ة", "س"]
# apl-source:10
أخطاء = 0
# apl-source:11

# apl-source:12
for حرف_تخمين in تخمينات:
    # apl-source:13
    أصاب = False
    # apl-source:14
    for ي in range(len(كلمة)):
        # apl-source:15
        if كلمة[ي] == حرف_تخمين:
            # apl-source:16
            مخفي[ي] = حرف_تخمين
            # apl-source:17
            أصاب = True
    # apl-source:18
    if أصاب == False:
        # apl-source:19
        أخطاء = أخطاء + 1
    # apl-source:20
    print("".join(مخفي), "(أخطاء:", str(أخطاء) + ")")
# apl-source:21

# apl-source:22
print("انتهت اللعبة")
# apl-source:23
