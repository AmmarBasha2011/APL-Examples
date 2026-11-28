# مثال 6355 — قائمة: الكلمات الأطول من 3 حروف ثم (حروف كبيرة)
# list of upper over words long3
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6355-words-long3-upper-list.apl

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
      ر = ر + [ك.upper()]
  ارجع ر

تأكد_يساوي(ف("the cat sat on the mat"), [], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["MAKES", "CODE", "SIMPLE"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["THREE", "FOUR", "FIVE"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["DDDD", "EEEEE"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["THAT", "QUESTION"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["DATA", "DATA", "DATA", "CODE", "CODE"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["LEARNING", "PROGRAM", "LEARNING", "THINK"], "حالة 7")
تأكد_يساوي(ف("hello"), ["HELLO"], "حالة 8")
