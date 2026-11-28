# مثال 6423 — قائمة: الكلمات التي فيها a ثم (آخر حرف)
# list of last over words has_a
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6423-words-has_a-last-list.apl

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
    لو "a" in ك:
      ر = ر + [ك[len(ك) - 1]]
  ارجع ر

تأكد_يساوي(ف("the cat sat on the mat"), ["t", "t", "t"], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["l", "s", "d"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), [], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["a"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["t"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["a", "a", "a", "l"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["g", "m", "g"], "حالة 7")
تأكد_يساوي(ف("hello"), [], "حالة 8")
