
# apl-source:1
# مثال 351 — متجه ثنائي الأبعاد
# apl-source:2
# 2D vector class
# apl-source:3
# Demonstrates: جمع وطول متجهات
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/351-vector2d.apl
# apl-source:6

# apl-source:7
class متجه:
    # apl-source:8
    def __init__(ذات, س, ص):
        # apl-source:9
        ذات.س = س
        # apl-source:10
        ذات.ص = ص
# apl-source:11

    # apl-source:12
    def اجمع(ذات, آخر):
        # apl-source:13
        return متجه(ذات.س + آخر.س, ذات.ص + آخر.ص)
# apl-source:14

    # apl-source:15
    def اضرب_في(ذات, عدد):
        # apl-source:16
        return متجه(ذات.س * عدد, ذات.ص * عدد)
# apl-source:17

    # apl-source:18
    def طول_المتجه(ذات):
        # apl-source:19
        return (ذات.س ** 2 + ذات.ص ** 2) ** 0.5
# apl-source:20

    # apl-source:21
    def كنص(ذات):
        # apl-source:22
        return "(" + str(ذات.س) + ", " + str(ذات.ص) + ")"
# apl-source:23

# apl-source:24
أ = متجه(3, 4)
# apl-source:25
ب = متجه(1, 2)
# apl-source:26
ج = أ.اجمع(ب)
# apl-source:27
print("أ + ب =", ج.كنص())
# apl-source:28
print("طول أ:", أ.طول_المتجه())
# apl-source:29
print("أ × 2 =", أ.اضرب_في(2).كنص())
# apl-source:30
