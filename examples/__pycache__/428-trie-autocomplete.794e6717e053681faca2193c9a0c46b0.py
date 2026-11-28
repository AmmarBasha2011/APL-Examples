
# apl-source:1
# مثال 428 — إكمال تلقائي بشجرة البادئات
# apl-source:2
# Trie autocomplete
# apl-source:3
# Demonstrates: اقتراح كلمات ببادئة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/428-trie-autocomplete.apl
# apl-source:6

# apl-source:7
def أدرج(جذر_شجرة, كلمة):
    # apl-source:8
    عقدة = جذر_شجرة
    # apl-source:9
    for حرف in كلمة:
        # apl-source:10
        if عقدة.get(حرف) == None:
            # apl-source:11
            عقدة[حرف] = {}
        # apl-source:12
        عقدة = عقدة[حرف]
    # apl-source:13
    عقدة["*"] = True
# apl-source:14

# apl-source:15
def اجمع_كلمات(عقدة, بادئة_حالية, نتائج):
    # apl-source:16
    if عقدة.get("*") == True:
        # apl-source:17
        نتائج.append(بادئة_حالية)
    # apl-source:18
    for مفتاح in عقدة.keys():
        # apl-source:19
        if مفتاح != "*":
            # apl-source:20
            اجمع_كلمات(عقدة[مفتاح], بادئة_حالية + مفتاح, نتائج)
# apl-source:21

# apl-source:22
جذر_شجرة = {}
# apl-source:23
أدرج(جذر_شجرة, "باب")
# apl-source:24
أدرج(جذر_شجرة, "بحر")
# apl-source:25
أدرج(جذر_شجرة, "بيت")
# apl-source:26
أدرج(جذر_شجرة, "شجرة")
# apl-source:27

# apl-source:28
عقدة = جذر_شجرة["ب"]
# apl-source:29
اقتراحات = []
# apl-source:30
اجمع_كلمات(عقدة, "ب", اقتراحات)
# apl-source:31
print("اقتراحات بـ ب:", اقتراحات)
# apl-source:32
