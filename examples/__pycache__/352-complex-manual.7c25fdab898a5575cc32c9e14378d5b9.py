
# apl-source:1
# مثال 352 — أعداد مركبة يدويا
# apl-source:2
# Manual complex numbers
# apl-source:3
# Demonstrates: جمع وضرب الأعداد المركبة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/352-complex-manual.apl
# apl-source:6

# apl-source:7
class مركب:
    # apl-source:8
    def __init__(ذات, جزء_حقيقي, جزء_تخيلي):
        # apl-source:9
        ذات.جزء_حقيقي = جزء_حقيقي
        # apl-source:10
        ذات.جزء_تخيلي = جزء_تخيلي
# apl-source:11

    # apl-source:12
    def اجمع(ذات, آخر):
        # apl-source:13
        return مركب(ذات.جزء_حقيقي + آخر.جزء_حقيقي, ذات.جزء_تخيلي + آخر.جزء_تخيلي)
# apl-source:14

    # apl-source:15
    def اضرب(ذات, آخر):
        # apl-source:16
        ح = ذات.جزء_حقيقي * آخر.جزء_حقيقي - ذات.جزء_تخيلي * آخر.جزء_تخيلي
        # apl-source:17
        ت = ذات.جزء_حقيقي * آخر.جزء_تخيلي + ذات.جزء_تخيلي * آخر.جزء_حقيقي
        # apl-source:18
        return مركب(ح, ت)
# apl-source:19

    # apl-source:20
    def كنص(ذات):
        # apl-source:21
        if ذات.جزء_تخيلي >= 0:
            # apl-source:22
            return str(ذات.جزء_حقيقي) + "+" + str(ذات.جزء_تخيلي) + "i"
        # apl-source:23
        return str(ذات.جزء_حقيقي) + str(ذات.جزء_تخيلي) + "i"
# apl-source:24

# apl-source:25
أ = مركب(2, 3)
# apl-source:26
ب = مركب(1, -1)
# apl-source:27
print("أ + ب =", أ.اجمع(ب).كنص())
# apl-source:28
print("أ × ب =", أ.اضرب(ب).كنص())
# apl-source:29
