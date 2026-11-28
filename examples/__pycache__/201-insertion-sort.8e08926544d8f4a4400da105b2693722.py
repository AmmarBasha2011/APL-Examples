
# apl-source:1
# مثال 201 — الترتيب بالإدراج
# apl-source:2
# Insertion sort
# apl-source:3
# Demonstrates: طالما المتداخلة، الإدراج في الموضع الصحيح
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/201-insertion-sort.apl
# apl-source:6

# apl-source:7
def إدراج(قائمة):
    # apl-source:8
    for ي in range(1, len(قائمة)):
        # apl-source:9
        مفتاح = قائمة[ي]
        # apl-source:10
        ز = ي - 1
        # apl-source:11
        while ز >= 0 and قائمة[ز] > مفتاح:
            # apl-source:12
            قائمة[ز + 1] = قائمة[ز]
            # apl-source:13
            ز = ز - 1
        # apl-source:14
        قائمة[ز + 1] = مفتاح
    # apl-source:15
    return قائمة
# apl-source:16

# apl-source:17
أرقام = [12, 11, 13, 5, 6]
# apl-source:18
print("قبل:", أرقام)
# apl-source:19
print("بعد:", إدراج(أرقام))
# apl-source:20
