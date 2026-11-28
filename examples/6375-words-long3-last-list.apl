# مثال 6375 — قائمة: الكلمات الأطول من 3 حروف ثم (آخر حرف)
# list of last over words long3
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6375-words-long3-last-list.apl

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
      ر = ر + [ك[len(ك) - 1]]
  ارجع ر

تأكد_يساوي(ف("the cat sat on the mat"), [], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["s", "e", "e"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["e", "r", "e"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["d", "e"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["t", "n"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["a", "a", "a", "e", "e"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["g", "m", "g", "k"], "حالة 7")
تأكد_يساوي(ف("hello"), ["o"], "حالة 8")
