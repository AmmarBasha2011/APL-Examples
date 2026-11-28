# مثال 6491 — قائمة: كل الكلمات ثم (أول حرف)
# list of first over words all
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6491-words-all-first-list.apl

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
      ر = ر + [ك[0]]
  ارجع ر

تأكد_يساوي(ف("the cat sat on the mat"), ["t", "c", "s", "o", "t", "m"], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["a", "m", "c", "s", "a", "f"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["o", "t", "t", "f", "f", "s"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["a", "b", "c", "d", "e"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["t", "b", "o", "n", "t", "b", "t", "i", "t", "q"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["d", "d", "d", "c", "c", "a"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["l", "t", "p", "i", "l", "t", "t"], "حالة 7")
تأكد_يساوي(ف("hello"), ["h"], "حالة 8")
