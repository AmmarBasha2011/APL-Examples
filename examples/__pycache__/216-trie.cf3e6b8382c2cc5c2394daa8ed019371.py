
# apl-source:1
# مثال 216 — شجرة البادئات (Trie)
# apl-source:2
# Prefix tree
# apl-source:3
# Demonstrates: قواميس متداخلة، إدراج كلمات وبحث بالبادئة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/216-trie.apl
# apl-source:6

# apl-source:7
def أدرج(جذر, كلمة):
    # apl-source:8
    حالي = جذر
    # apl-source:9
    for حرف in كلمة:
        # apl-source:10
        if حرف not in حالي:
            # apl-source:11
            حالي[حرف] = {}
        # apl-source:12
        حالي = حالي[حرف]
    # apl-source:13
    حالي["#"] = True
# apl-source:14

# apl-source:15
def ابحث(جذر, كلمة):
    # apl-source:16
    حالي = جذر
    # apl-source:17
    for حرف in كلمة:
        # apl-source:18
        if حرف not in حالي:
            # apl-source:19
            return False
        # apl-source:20
        حالي = حالي[حرف]
    # apl-source:21
    return "#" in حالي
# apl-source:22

# apl-source:23
def يبدأ_بـ(جذر, بادئة):
    # apl-source:24
    حالي = جذر
    # apl-source:25
    for حرف in بادئة:
        # apl-source:26
        if حرف not in حالي:
            # apl-source:27
            return False
        # apl-source:28
        حالي = حالي[حرف]
    # apl-source:29
    return True
# apl-source:30

# apl-source:31
جذر = {}
# apl-source:32
for ك in ["car", "card", "care", "dog"]:
    # apl-source:33
    أدرج(جذر, ك)
# apl-source:34

# apl-source:35
print("care:", ابحث(جذر, "care"))
# apl-source:36
print("ca:", ابحث(جذر, "ca"))
# apl-source:37
print("بادئة ca:", يبدأ_بـ(جذر, "ca"))
# apl-source:38
print("بادئة da:", يبدأ_بـ(جذر, "da"))
# apl-source:39
