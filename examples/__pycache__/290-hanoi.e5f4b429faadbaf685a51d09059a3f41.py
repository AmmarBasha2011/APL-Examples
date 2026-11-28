
# apl-source:1
# مثال 290 — أبراج هانوي
# apl-source:2
# Tower of Hanoi
# apl-source:3
# Demonstrates: عودية كلاسيكية
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/290-hanoi.apl
# apl-source:6

# apl-source:7
def هانوي(ن, من, إلى, مساعد):
    # apl-source:8
    if ن == 1:
        # apl-source:9
        print("انقل قرصا من", من, "إلى", إلى)
        # apl-source:10
        return
    # apl-source:11
    هانوي(ن - 1, من, مساعد, إلى)
    # apl-source:12
    print("انقل قرصا من", من, "إلى", إلى)
    # apl-source:13
    هانوي(ن - 1, مساعد, إلى, من)
# apl-source:14

# apl-source:15
هانوي(3, "أ", "ج", "ب")
# apl-source:16
