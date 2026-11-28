# مثال 6358 — القائمة معكوسة: الكلمات الأطول من 3 حروف ثم (حروف كبيرة)
# rev of upper over words long3
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6358-words-long3-upper-rev.apl

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
      ر = ر + [ك.upper()]
  ارجع ر[::-1]

تأكد_يساوي(ف("the cat sat on the mat"), [], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["SIMPLE", "CODE", "MAKES"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["FIVE", "FOUR", "THREE"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["EEEEE", "DDDD"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["QUESTION", "THAT"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["CODE", "CODE", "DATA", "DATA", "DATA"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["THINK", "LEARNING", "PROGRAM", "LEARNING"], "حالة 7")
تأكد_يساوي(ف("hello"), ["HELLO"], "حالة 8")
