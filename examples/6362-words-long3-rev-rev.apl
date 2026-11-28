# مثال 6362 — القائمة معكوسة: الكلمات الأطول من 3 حروف ثم (كلمة معكوسة)
# rev of rev over words long3
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6362-words-long3-rev-rev.apl

# نقسم النص إلى كلمات
# نصفّي ثم نحوّل كل كلمة
# ونرجع: القائمة معكوسة

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
  ارجع ر[::-1]

تأكد_يساوي(ف("the cat sat on the mat"), [], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["elpmis", "edoc", "sekam"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["evif", "ruof", "eerht"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["eeeee", "dddd"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["noitseuq", "taht"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["edoc", "edoc", "atad", "atad", "atad"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["kniht", "gninrael", "margorp", "gninrael"], "حالة 7")
تأكد_يساوي(ف("hello"), ["olleh"], "حالة 8")
