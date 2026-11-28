# مثال 6359 — قائمة: الكلمات الأطول من 3 حروف ثم (كلمة معكوسة)
# list of rev over words long3
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6359-words-long3-rev-list.apl

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
    لو len(ك) > 3:
      ر = ر + [ك[::-1]]
  ارجع ر

تأكد_يساوي(ف("the cat sat on the mat"), [], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["sekam", "edoc", "elpmis"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["eerht", "ruof", "evif"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["dddd", "eeeee"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["taht", "noitseuq"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["atad", "atad", "atad", "edoc", "edoc"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["gninrael", "margorp", "gninrael", "kniht"], "حالة 7")
تأكد_يساوي(ف("hello"), ["olleh"], "حالة 8")
