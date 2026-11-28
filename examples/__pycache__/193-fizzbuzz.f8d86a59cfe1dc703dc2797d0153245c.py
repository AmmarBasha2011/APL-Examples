
# apl-source:1
# مثال 193 — فيزباز
# apl-source:2
# FizzBuzz
# apl-source:3
# Demonstrates: الشروط المركبة، الباقي
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/193-fizzbuzz.apl
# apl-source:6

# apl-source:7
for ن in range(1, 21):
    # apl-source:8
    if ن % 15 == 0:
        # apl-source:9
        print("فيزباز")
    # apl-source:10
    elif ن % 3 == 0:
        # apl-source:11
        print("فيز")
    # apl-source:12
    elif ن % 5 == 0:
        # apl-source:13
        print("باز")
    # apl-source:14
    else:
        # apl-source:15
        print(ن)
# apl-source:16
