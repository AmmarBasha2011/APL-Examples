# مثال 6402 — القائمة معكوسة: الكلمات القصيرة (3 أو أقل) ثم (آخر حرف)
# rev of last over words short
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6402-words-short-last-rev.apl

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
    لو len(ك) <= 3:
      ر = ر + [ك[len(ك) - 1]]
  ارجع ر[::-1]

تأكد_يساوي(ف("the cat sat on the mat"), ["t", "e", "n", "t", "t", "e"], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["n", "d", "l"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["x", "o", "e"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["c", "b", "a"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["e", "s", "e", "o", "t", "r", "e", "o"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["l"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["o", "s", "o"], "حالة 7")
تأكد_يساوي(ف("hello"), [], "حالة 8")
