# مثال 6475 — قائمة: كل الكلمات ثم (حروف كبيرة)
# list of upper over words all
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6475-words-all-upper-list.apl

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
    لو 1 == 1:
      ر = ر + [ك.upper()]
  ارجع ر

تأكد_يساوي(ف("the cat sat on the mat"), ["THE", "CAT", "SAT", "ON", "THE", "MAT"], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["APL", "MAKES", "CODE", "SIMPLE", "AND", "FUN"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["A", "BB", "CCC", "DDDD", "EEEEE"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["TO", "BE", "OR", "NOT", "TO", "BE", "THAT", "IS", "THE", "QUESTION"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["DATA", "DATA", "DATA", "CODE", "CODE", "APL"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["LEARNING", "TO", "PROGRAM", "IS", "LEARNING", "TO", "THINK"], "حالة 7")
تأكد_يساوي(ف("hello"), ["HELLO"], "حالة 8")
