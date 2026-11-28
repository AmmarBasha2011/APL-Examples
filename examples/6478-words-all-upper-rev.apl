# مثال 6478 — القائمة معكوسة: كل الكلمات ثم (حروف كبيرة)
# rev of upper over words all
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6478-words-all-upper-rev.apl

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
    لو 1 == 1:
      ر = ر + [ك.upper()]
  ارجع ر[::-1]

تأكد_يساوي(ف("the cat sat on the mat"), ["MAT", "THE", "ON", "SAT", "CAT", "THE"], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["FUN", "AND", "SIMPLE", "CODE", "MAKES", "APL"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["SIX", "FIVE", "FOUR", "THREE", "TWO", "ONE"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["EEEEE", "DDDD", "CCC", "BB", "A"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["QUESTION", "THE", "IS", "THAT", "BE", "TO", "NOT", "OR", "BE", "TO"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["APL", "CODE", "CODE", "DATA", "DATA", "DATA"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["THINK", "TO", "LEARNING", "IS", "PROGRAM", "TO", "LEARNING"], "حالة 7")
تأكد_يساوي(ف("hello"), ["HELLO"], "حالة 8")
