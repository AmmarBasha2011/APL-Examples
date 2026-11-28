
# apl-source:1
# مثال 296 — عد وقل
# apl-source:2
# Count and say sequence
# apl-source:3
# Demonstrates: بناء الحد التالي من السابق
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/296-count-and-say.apl
# apl-source:6

# apl-source:7
def التالي(حد):
    # apl-source:8
    نتيجة = ""
    # apl-source:9
    ي = 0
    # apl-source:10
    while ي < len(حد):
        # apl-source:11
        عدد = 1
        # apl-source:12
        while ي + عدد < len(حد) and حد[ي + عدد] == حد[ي]:
            # apl-source:13
            عدد = عدد + 1
        # apl-source:14
        نتيجة = نتيجة + str(عدد) + حد[ي]
        # apl-source:15
        ي = ي + عدد
    # apl-source:16
    return نتيجة
# apl-source:17

# apl-source:18
حد = "1"
# apl-source:19
for ن in range(5):
    # apl-source:20
    print(ن + 1, ":", حد)
    # apl-source:21
    حد = التالي(حد)
# apl-source:22
