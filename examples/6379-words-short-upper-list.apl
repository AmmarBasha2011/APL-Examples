# مثال 6379 — قائمة: الكلمات القصيرة (3 أو أقل) ثم (حروف كبيرة)
# list of upper over words short
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6379-words-short-upper-list.apl

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
    لو len(ك) <= 3:
      ر = ر + [ك.upper()]
  ارجع ر

تأكد_يساوي(ف("the cat sat on the mat"), ["THE", "CAT", "SAT", "ON", "THE", "MAT"], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["APL", "AND", "FUN"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["ONE", "TWO", "SIX"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["A", "BB", "CCC"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["TO", "BE", "OR", "NOT", "TO", "BE", "IS", "THE"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["APL"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["TO", "IS", "TO"], "حالة 7")
تأكد_يساوي(ف("hello"), [], "حالة 8")
