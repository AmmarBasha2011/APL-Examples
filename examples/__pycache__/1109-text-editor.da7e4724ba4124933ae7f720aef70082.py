
# apl-source:1
# مثال 1109 — محرر نصوص بمؤشر
# apl-source:2
# Text editor with cursor
# apl-source:3
# Demonstrates: نصان يمين ويسار المؤشر
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1109-text-editor.apl
# apl-source:6

# apl-source:7
# نخزن النص الذي على يسار المؤشر والذي على يمينه
# apl-source:8
# وكل عملية تعيد آخر عشرة أحرف على يسار المؤشر
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
class محرر:
    # apl-source:19
    def __init__(ذات):
        # apl-source:20
        ذات.يسار = ""
        # apl-source:21
        ذات.يمين = ""
# apl-source:22

    # apl-source:23
    def اخر_عشرة(ذات):
        # apl-source:24
        return ذات.يسار[-10:]
# apl-source:25

    # apl-source:26
    def اضف_نص(ذات, نص_):
        # apl-source:27
        ذات.يسار = ذات.يسار + نص_
# apl-source:28

    # apl-source:29
    def امسح(ذات, ك):
        # apl-source:30
        م = ك
        # apl-source:31
        if م > len(ذات.يسار):
            # apl-source:32
            م = len(ذات.يسار)
        # apl-source:33
        ذات.يسار = ذات.يسار[:len(ذات.يسار) - م]
        # apl-source:34
        return م
# apl-source:35

    # apl-source:36
    def حرك_يمين(ذات, ك):
        # apl-source:37
        م = ك
        # apl-source:38
        if م > len(ذات.يمين):
            # apl-source:39
            م = len(ذات.يمين)
        # apl-source:40
        ذات.يسار = ذات.يسار + ذات.يمين[:م]
        # apl-source:41
        ذات.يمين = ذات.يمين[م:]
        # apl-source:42
        return ذات.اخر_عشرة()
# apl-source:43

    # apl-source:44
    def حرك_يسار(ذات, ك):
        # apl-source:45
        م = ك
        # apl-source:46
        if م > len(ذات.يسار):
            # apl-source:47
            م = len(ذات.يسار)
        # apl-source:48
        ذات.يمين = ذات.يسار[len(ذات.يسار) - م:] + ذات.يمين
        # apl-source:49
        ذات.يسار = ذات.يسار[:len(ذات.يسار) - م]
        # apl-source:50
        return ذات.اخر_عشرة()
# apl-source:51

# apl-source:52
م = محرر()
# apl-source:53
م.اضف_نص("leetcode")
# apl-source:54
تأكد_يساوي(م.امسح(4), 4, "مسح أربعة")
# apl-source:55
م.اضف_نص("practice")
# apl-source:56
تأكد_يساوي(م.حرك_يمين(3), "etpractice", "يمين بلا مجال")
# apl-source:57
تأكد_يساوي(م.حرك_يسار(8), "leet", "يسار ثمانية")
# apl-source:58
تأكد_يساوي(م.امسح(10), 4, "مسح ما يمكن")
# apl-source:59
تأكد_يساوي(م.حرك_يسار(2), "", "يسار بلا نص")
# apl-source:60
تأكد_يساوي(م.حرك_يمين(6), "practi", "يمين ستة")
# apl-source:61
