# مثال 6390 — القائمة معكوسة: الكلمات القصيرة (3 أو أقل) ثم (أول حرف كبير)
# rev of cap over words short
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6390-words-short-cap-rev.apl

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
      ر = ر + [ك[0].upper() + ك[1:]]
  ارجع ر[::-1]

تأكد_يساوي(ف("the cat sat on the mat"), ["Mat", "The", "On", "Sat", "Cat", "The"], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["Fun", "And", "Apl"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["Six", "Two", "One"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["Ccc", "Bb", "A"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["The", "Is", "Be", "To", "Not", "Or", "Be", "To"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["Apl"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["To", "Is", "To"], "حالة 7")
تأكد_يساوي(ف("hello"), [], "حالة 8")
