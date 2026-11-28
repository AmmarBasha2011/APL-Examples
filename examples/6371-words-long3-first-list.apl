# مثال 6371 — قائمة: الكلمات الأطول من 3 حروف ثم (أول حرف)
# list of first over words long3
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6371-words-long3-first-list.apl

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
      ر = ر + [ك[0]]
  ارجع ر

تأكد_يساوي(ف("the cat sat on the mat"), [], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["m", "c", "s"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["t", "f", "f"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["d", "e"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["t", "q"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["d", "d", "d", "c", "c"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["l", "p", "l", "t"], "حالة 7")
تأكد_يساوي(ف("hello"), ["h"], "حالة 8")
