# مثال 6494 — القائمة معكوسة: كل الكلمات ثم (أول حرف)
# rev of first over words all
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6494-words-all-first-rev.apl

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
      ر = ر + [ك[0]]
  ارجع ر[::-1]

تأكد_يساوي(ف("the cat sat on the mat"), ["m", "t", "o", "s", "c", "t"], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["f", "a", "s", "c", "m", "a"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["s", "f", "f", "t", "t", "o"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["e", "d", "c", "b", "a"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["q", "t", "i", "t", "b", "t", "n", "o", "b", "t"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["a", "c", "c", "d", "d", "d"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["t", "t", "l", "i", "p", "t", "l"], "حالة 7")
تأكد_يساوي(ف("hello"), ["h"], "حالة 8")
