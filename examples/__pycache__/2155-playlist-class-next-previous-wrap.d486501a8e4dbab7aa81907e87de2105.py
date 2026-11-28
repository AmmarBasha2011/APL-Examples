
# apl-source:1
# مثال 2155 — قائمة تشغيل بتالي وسابق دائريين
# apl-source:2
# Playlist class wrap around
# apl-source:3
# Demonstrates: أصناف
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/2155-playlist-class-next-previous-wrap.apl
# apl-source:6

# apl-source:7
# # نحتفظ بموضع الأغنية الحالية
# apl-source:8
# # ونستخدم الباقي للالتفاف
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
class قائمة_تشغيل:
    # apl-source:19
    def __init__(ذات, اغان):
        # apl-source:20
        ذات.اغان = اغان
        # apl-source:21
        ذات.موضع = 0
# apl-source:22

    # apl-source:23
    def حالية(ذات):
        # apl-source:24
        return ذات.اغان[ذات.موضع]
# apl-source:25

    # apl-source:26
    def تالية(ذات):
        # apl-source:27
        ذات.موضع = (ذات.موضع + 1) % len(ذات.اغان)
        # apl-source:28
        return ذات.حالية()
# apl-source:29

    # apl-source:30
    def سابقة(ذات):
        # apl-source:31
        ذات.موضع = (ذات.موضع - 1) % len(ذات.اغان)
        # apl-source:32
        return ذات.حالية()
# apl-source:33

# apl-source:34
ق = قائمة_تشغيل(["a", "b", "c"])
# apl-source:35
تأكد_يساوي(ق.حالية(), "a", "الأولى")
# apl-source:36
تأكد_يساوي(ق.تالية(), "b", "التالية")
# apl-source:37
تأكد_يساوي(ق.سابقة(), "a", "رجوع")
# apl-source:38
تأكد_يساوي(ق.سابقة(), "c", "التفاف للخلف")
# apl-source:39
تأكد_يساوي(ق.تالية(), "a", "التفاف للأمام")
# apl-source:40
