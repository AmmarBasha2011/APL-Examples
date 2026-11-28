
# apl-source:1
# مثال 433 — محاذاة النصوص
# apl-source:2
# Text alignment
# apl-source:3
# Demonstrates: يمين ويسار ووسط
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/433-column-align.apl
# apl-source:6

# apl-source:7
def حاذي(نص_الدخل, عرض_مطلوب, اتجاه):
    # apl-source:8
    نقص = عرض_مطلوب - len(نص_الدخل)
    # apl-source:9
    if نقص <= 0:
        # apl-source:10
        return نص_الدخل
    # apl-source:11
    فراغ = ""
    # apl-source:12
    for _ in range(نقص):
        # apl-source:13
        فراغ = فراغ + " "
    # apl-source:14
    if اتجاه == "يمين":
        # apl-source:15
        return فراغ + نص_الدخل
    # apl-source:16
    elif اتجاه == "وسط":
        # apl-source:17
        return نص_الدخل + فراغ
    # apl-source:18
    return نص_الدخل + فراغ
# apl-source:19

# apl-source:20
print("[" + حاذي("42", 8, "يمين") + "]")
# apl-source:21
print("[" + حاذي("42", 8, "يسار") + "]")
# apl-source:22
