# مثال 6495 — قائمة: كل الكلمات ثم (آخر حرف)
# list of last over words all
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6495-words-all-last-list.apl

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
      ر = ر + [ك[len(ك) - 1]]
  ارجع ر

تأكد_يساوي(ف("the cat sat on the mat"), ["e", "t", "t", "n", "e", "t"], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["l", "s", "e", "e", "d", "n"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["e", "o", "e", "r", "e", "x"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["a", "b", "c", "d", "e"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["o", "e", "r", "t", "o", "e", "t", "s", "e", "n"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["a", "a", "a", "e", "e", "l"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["g", "o", "m", "s", "g", "o", "k"], "حالة 7")
تأكد_يساوي(ف("hello"), ["o"], "حالة 8")
