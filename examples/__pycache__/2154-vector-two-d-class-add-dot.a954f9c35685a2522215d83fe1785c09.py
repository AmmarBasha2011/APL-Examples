
# apl-source:1
# مثال 2154 — صنف متجه ثنائي الأبعاد
# apl-source:2
# 2D vector class
# apl-source:3
# Demonstrates: أصناف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2154-vector-two-d-class-add-dot.apl
# apl-source:6

# apl-source:7
# # المتجه مركبتان
# apl-source:8
# # العمليات ترجع قيما جديدة
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
    def اجمع(ذات, ا):
        # apl-source:24
        return متجه(ذات.س + ا.س, ذات.ص + ا.ص)
# apl-source:25

    # apl-source:26
    def نقطي(ذات, ا):
        # apl-source:27
        return ذات.س * ا.س + ذات.ص * ا.ص
# apl-source:28

    # apl-source:29
    def طول_مربع(ذات):
        # apl-source:30
        return ذات.نقطي(ذات)
# apl-source:31

# apl-source:32
ا = متجه(1, 2)
# apl-source:33
ب = متجه(3, 4)
# apl-source:34
ج = ا.اجمع(ب)
# apl-source:35
تأكد_يساوي([ج.س, ج.ص], [4, 6], "الجمع")
# apl-source:36
تأكد_يساوي(ا.نقطي(ب), 11, "نقطي")
# apl-source:37
تأكد_يساوي(ب.طول_مربع(), 25, "طول مربع")
# apl-source:38
