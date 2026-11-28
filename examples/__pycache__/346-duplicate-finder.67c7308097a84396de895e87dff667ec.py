
# apl-source:1
# مثال 346 — كاشف المحتوى المكرر
# apl-source:2
# Duplicate content finder
# apl-source:3
# Demonstrates: تجميع بالمحتوى
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/346-duplicate-finder.apl
# apl-source:6

# apl-source:7
ملفات = {
    # apl-source:8
    "أ.txt": "مرحبا بالعالم",
    # apl-source:9
    "ب.txt": "نص مختلف",
    # apl-source:10
    "ج.txt": "مرحبا بالعالم",
    # apl-source:11
    "د.txt": "نص مختلف",
    # apl-source:12
    "ه.txt": "فريد"
# apl-source:13
}
# apl-source:14

# apl-source:15
بالمحتوى = {}
# apl-source:16
for اسم in ملفات:
    # apl-source:17
    محتوى = ملفات[اسم]
    # apl-source:18
    if محتوى in بالمحتوى:
        # apl-source:19
        بالمحتوى[محتوى].append(اسم)
    # apl-source:20
    else:
        # apl-source:21
        بالمحتوى[محتوى] = [اسم]
# apl-source:22

# apl-source:23
for محتوى in بالمحتوى:
    # apl-source:24
    if len(بالمحتوى[محتوى]) > 1:
        # apl-source:25
        print("مكرر:", بالمحتوى[محتوى])
# apl-source:26
