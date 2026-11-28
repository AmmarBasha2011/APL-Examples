# مثال 6451 — قائمة: الكلمات ذات الطول الزوجي ثم (حروف كبيرة)
# list of upper over words even_len
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6451-words-even_len-upper-list.apl

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
    لو len(ك) % 2 == 0:
      ر = ر + [ك.upper()]
  ارجع ر

تأكد_يساوي(ف("the cat sat on the mat"), ["ON"], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["CODE", "SIMPLE"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["FOUR", "FIVE"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["BB", "DDDD"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["TO", "BE", "OR", "TO", "BE", "THAT", "IS", "QUESTION"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["DATA", "DATA", "DATA", "CODE", "CODE"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["LEARNING", "TO", "IS", "LEARNING", "TO"], "حالة 7")
تأكد_يساوي(ف("hello"), [], "حالة 8")
