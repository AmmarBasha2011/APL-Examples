
# apl-source:1
# مثال 1103 — طابور بمكدسين
# apl-source:2
# Queue using two stacks
# apl-source:3
# Demonstrates: نقل عند الحاجة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1103-queue-two-stacks.apl
# apl-source:6

# apl-source:7
# الدفع في مكدس الإدخال
# apl-source:8
# وعند السحب نقلب مكدس الإدخال إلى مكدس الإخراج لو كان فارغاً
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
class طابور_مكدسين:
    # apl-source:19
    def __init__(ذات):
        # apl-source:20
        ذات.داخل = []
        # apl-source:21
        ذات.خارج = []
# apl-source:22

    # apl-source:23
    def ادفع(ذات, س):
        # apl-source:24
        ذات.داخل = ذات.داخل + [س]
# apl-source:25

    # apl-source:26
    def انقل(ذات):
        # apl-source:27
        if len(ذات.خارج) == 0:
            # apl-source:28
            while len(ذات.داخل) > 0:
                # apl-source:29
                ذات.خارج = ذات.خارج + [ذات.داخل.pop()]
# apl-source:30

    # apl-source:31
    def اسحب(ذات):
        # apl-source:32
        ذات.انقل()
        # apl-source:33
        return ذات.خارج.pop()
# apl-source:34

    # apl-source:35
    def اول(ذات):
        # apl-source:36
        ذات.انقل()
        # apl-source:37
        return ذات.خارج[-1]
# apl-source:38

    # apl-source:39
    def فارغ(ذات):
        # apl-source:40
        return (len(ذات.داخل) + len(ذات.خارج)) == 0
# apl-source:41

# apl-source:42
ط = طابور_مكدسين()
# apl-source:43
ط.ادفع(1)
# apl-source:44
ط.ادفع(2)
# apl-source:45
تأكد_يساوي(ط.اول(), 1, "الأول")
# apl-source:46
تأكد_يساوي(ط.اسحب(), 1, "سحب الأول")
# apl-source:47
ط.ادفع(3)
# apl-source:48
تأكد_يساوي(ط.فارغ(), False, "ليس فارغاً")
# apl-source:49
تأكد_يساوي(ط.اسحب(), 2, "سحب الثاني")
# apl-source:50
تأكد_يساوي(ط.اسحب(), 3, "سحب الثالث")
# apl-source:51
تأكد_يساوي(ط.فارغ(), True, "فارغ")
# apl-source:52
