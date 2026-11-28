# مثال 6474 — القائمة معكوسة: الكلمات ذات الطول الزوجي ثم (آخر حرف)
# rev of last over words even_len
# Demonstrates: معالجة النصوص
#
# Run:  python apl.py examples/6474-words-even_len-last-rev.apl

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
    لو len(ك) % 2 == 0:
      ر = ر + [ك[len(ك) - 1]]
  ارجع ر[::-1]

تأكد_يساوي(ف("the cat sat on the mat"), ["n"], "حالة 1")
تأكد_يساوي(ف("apl makes code simple and fun"), ["e", "e"], "حالة 2")
تأكد_يساوي(ف("one two three four five six"), ["e", "r"], "حالة 3")
تأكد_يساوي(ف("a bb ccc dddd eeeee"), ["d", "b"], "حالة 4")
تأكد_يساوي(ف("to be or not to be that is the question"), ["n", "s", "t", "e", "o", "r", "e", "o"], "حالة 5")
تأكد_يساوي(ف("data data data code code apl"), ["e", "e", "a", "a", "a"], "حالة 6")
تأكد_يساوي(ف("learning to program is learning to think"), ["o", "g", "s", "o", "g"], "حالة 7")
تأكد_يساوي(ف("hello"), [], "حالة 8")
