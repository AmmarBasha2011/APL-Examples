# مثال 6394 — القائمة معكوسة: الكلمات القصيرة (3 أو أقل) ثم (طول الكلمة)
# rev of len over words short
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6394-words-short-len-rev.apl

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
      ر = ر + [len(ك)]
  ارجع ر[::-1]

تأكد_يساوي(ف("the cat sat on the mat"), [3, 3, 2, 3, 3, 3], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), [3, 3, 3], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), [3, 3, 3], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), [3, 2, 1], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), [3, 2, 2, 2, 3, 2, 2, 2], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), [3], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), [2, 2, 2], "حالة 7")
تأكد_يساوي(ف("hello"), [], "حالة 8")
