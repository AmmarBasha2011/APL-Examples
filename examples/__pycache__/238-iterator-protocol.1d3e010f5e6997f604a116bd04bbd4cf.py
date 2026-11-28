
# apl-source:1
# مثال 238 — مكرر مخصص (عداد تنازلي)
# apl-source:2
# Custom iterator (countdown)
# apl-source:3
# Demonstrates: صنف يعمل كمكرر في لكل
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/238-iterator-protocol.apl
# apl-source:6

# apl-source:7
class عد_تنازلي:
    # apl-source:8
    def __init__(ذات, من):
        # apl-source:9
        ذات.حالي = من
# apl-source:10

    # apl-source:11
    def __iter__(ذات):
        # apl-source:12
        return ذات
# apl-source:13

    # apl-source:14
    def __next__(ذات):
        # apl-source:15
        if ذات.حالي <= 0:
            # apl-source:16
            raise StopIteration
        # apl-source:17
        ذات.حالي = ذات.حالي - 1
        # apl-source:18
        return ذات.حالي + 1
# apl-source:19

# apl-source:20
for ن in عد_تنازلي(5):
    # apl-source:21
    print(ن)
# apl-source:22
print("انطلاق!")
# apl-source:23
