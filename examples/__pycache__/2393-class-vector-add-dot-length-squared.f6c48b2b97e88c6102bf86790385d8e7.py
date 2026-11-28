
# apl-source:1
# مثال 2393 — صنف متجه ثنائي
# apl-source:2
# Vector class dot product
# apl-source:3
# Demonstrates: أصناف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2393-class-vector-add-dot-length-squared.apl
# apl-source:6

# apl-source:7
# # نعرف صنفا
# apl-source:8
# # ونختبر سلوكه
# apl-source:9

# apl-source:10
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:11
  if فعلي != متوقع:
    # apl-source:12
    print("فشل:", اسم)
    # apl-source:13
    print("  متوقع:", متوقع)
    # apl-source:14
    print("  فعلي:", فعلي)
    # apl-source:15
    قياسي_نظام_اخرج(1)
  # apl-source:16
  print("ناجح:", اسم)
# apl-source:17

# apl-source:18
class متجه:
    # apl-source:19
    def __init__(ذات, س, ص):
        # apl-source:20
        ذات.س = س
        # apl-source:21
        ذات.ص = ص
# apl-source:22

    # apl-source:23
    def جمع(ذات, ق):
        # apl-source:24
        return متجه(ذات.س + ق.س, ذات.ص + ق.ص)
# apl-source:25

    # apl-source:26
    def داخلي(ذات, ق):
        # apl-source:27
        return ذات.س * ق.س + ذات.ص * ق.ص
# apl-source:28

# apl-source:29
أ = متجه(1, 2)
# apl-source:30
ب = متجه(3, 4)
# apl-source:31
ج = أ.جمع(ب)
# apl-source:32
تأكد_يساوي(ج.س, 4, "س")
# apl-source:33
تأكد_يساوي(ج.ص, 6, "ص")
# apl-source:34
تأكد_يساوي(أ.داخلي(ب), 11, "داخلي")
# apl-source:35
