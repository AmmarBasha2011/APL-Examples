# مثال 6447 — قائمة: الكلمات التي تبدأ بـ t ثم (آخر حرف)
# list of last over words starts_t
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6447-words-starts_t-last-list.apl

# نقسم النص إلى كلمات
# نصفّي ثم نحوّل كل كلمة
# ونرجع: قائمة

دالة تأكد_يساوي(فعلي, متوقع, اسم):
  لو فعلي != متوقع:
    اطبع "فشل:", اسم
    اطبع "  متوقع:", متوقع
    اطبع "  فعلي:", فعلي
    قياسي_نظام_اخرج(1)
  اطبع "ناجح:", اسم

دالة ف(ن):
  ر = []
  لكل ك في ن.split(" "):
    لو ك[0] == "t":
      ر = ر + [ك[len(ك) - 1]]
  ارجع ر

تأكد_يساوي(ف("the cat sat on the mat"), ["e", "e"], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), [], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["o", "e"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), [], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["o", "o", "t", "e"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), [], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["o", "o", "k"], "حالة 7")
تأكد_يساوي(ف("hello"), [], "حالة 8")
