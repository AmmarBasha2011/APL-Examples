
# apl-source:1
# مثال 1125 — محرر بتراجع وإعادة
# apl-source:2
# Editor with undo and redo
# apl-source:3
# Demonstrates: مكدسان
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1125-undo-redo-editor.apl
# apl-source:6

# apl-source:7
# كل كتابة تدفع النص السابق في مكدس التراجع وتمسح مكدس الإعادة
# apl-source:8
# والتراجع والإعادة ينقلان الحالة بين المكدسين
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
class محرر_تراجع:
    # apl-source:19
    def __init__(ذات):
        # apl-source:20
        ذات.نص_ = ""
        # apl-source:21
        ذات.ماضي = []
        # apl-source:22
        ذات.مستقبل = []
# apl-source:23

    # apl-source:24
    def اكتب_حرف(ذات, ح):
        # apl-source:25
        ذات.ماضي = ذات.ماضي + [ذات.نص_]
        # apl-source:26
        ذات.مستقبل = []
        # apl-source:27
        ذات.نص_ = ذات.نص_ + ح
# apl-source:28

    # apl-source:29
    def تراجع(ذات):
        # apl-source:30
        if len(ذات.ماضي) > 0:
            # apl-source:31
            ذات.مستقبل = ذات.مستقبل + [ذات.نص_]
            # apl-source:32
            ذات.نص_ = ذات.ماضي.pop()
# apl-source:33

    # apl-source:34
    def اعد(ذات):
        # apl-source:35
        if len(ذات.مستقبل) > 0:
            # apl-source:36
            ذات.ماضي = ذات.ماضي + [ذات.نص_]
            # apl-source:37
            ذات.نص_ = ذات.مستقبل.pop()
# apl-source:38

# apl-source:39
م = محرر_تراجع()
# apl-source:40
م.اكتب_حرف("a")
# apl-source:41
م.اكتب_حرف("b")
# apl-source:42
م.اكتب_حرف("c")
# apl-source:43
م.تراجع()
# apl-source:44
تأكد_يساوي(م.نص_, "ab", "تراجع أول")
# apl-source:45
م.تراجع()
# apl-source:46
تأكد_يساوي(م.نص_, "a", "تراجع ثان")
# apl-source:47
م.اعد()
# apl-source:48
تأكد_يساوي(م.نص_, "ab", "إعادة")
# apl-source:49
م.اكتب_حرف("z")
# apl-source:50
تأكد_يساوي(م.نص_, "abz", "كتابة جديدة")
# apl-source:51
م.اعد()
# apl-source:52
تأكد_يساوي(م.نص_, "abz", "الإعادة ممسوحة")
# apl-source:53
م.تراجع()
# apl-source:54
م.تراجع()
# apl-source:55
م.تراجع()
# apl-source:56
م.تراجع()
# apl-source:57
تأكد_يساوي(م.نص_, "", "تراجع حتى الفراغ")
# apl-source:58
