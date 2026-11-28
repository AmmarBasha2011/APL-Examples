
# apl-source:1
# مثال 456 — مولد روابط Slug
# apl-source:2
# Slug generator
# apl-source:3
# Demonstrates: عنوان مقال إلى رابط
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/456-slug-generator.apl
# apl-source:6

# apl-source:7
def رابط_لطيف(عنوان):
    # apl-source:8
    ناتج = ""
    # apl-source:9
    for حرف in عنوان.lower():
        # apl-source:10
        if (حرف >= "a" and حرف <= "z") or (حرف >= "0" and حرف <= "9"):
            # apl-source:11
            ناتج = ناتج + حرف
        # apl-source:12
        elif حرف == " ":
            # apl-source:13
            ناتج = ناتج + "-"
    # apl-source:14
    return ناتج
# apl-source:15

# apl-source:16
print(رابط_لطيف("Hello World 2026!"))
# apl-source:17
print(رابط_لطيف("My First Blog Post"))
# apl-source:18
