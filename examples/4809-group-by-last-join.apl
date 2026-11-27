# مثال 4809 — تجميع الكلمات حسب الحرف الأخير (الكلمات)
# Group words by last letter: words
# Demonstrates: قواميس وتجميع
#
# Run:  python apl.py examples/4809-group-by-last-join.apl

# نمر على الكلمات
# ونحدّث القاموس حسب المفتاح

دالة تأكد_يساوي(فعلي, متوقع, اسم):
  لو فعلي != متوقع:
    اطبع "فشل:", اسم
    اطبع "  متوقع:", متوقع
    اطبع "  فعلي:", فعلي
    قياسي_نظام_اخرج(1)
  اطبع "ناجح:", اسم

دالة ف(ق):
  د = {}
  لكل خ في ق:
    ك = خ[len(خ) - 1]
    لو ك في د:
      د[ك] = د[ك] + [خ]
    والا:
      د[ك] = [خ]
  ارجع د

تأكد_يساوي(ف(["apple", "bob", "cat", "apricot", "bear", "dog", "axe"]), {"e": ["apple", "axe"], "b": ["bob"], "t": ["cat", "apricot"], "r": ["bear"], "g": ["dog"]}, "حالة 1")
تأكد_يساوي(ف(["sun", "moon", "star", "sky", "mars"]), {"n": ["sun", "moon"], "r": ["star"], "y": ["sky"], "s": ["mars"]}, "حالة 2")
تأكد_يساوي(ف(["one", "two", "three", "four", "five", "six"]), {"e": ["one", "three", "five"], "o": ["two"], "r": ["four"], "x": ["six"]}, "حالة 3")
تأكد_يساوي(ف(["kiwi", "lime", "lemon", "kale", "leek"]), {"i": ["kiwi"], "e": ["lime", "kale"], "n": ["lemon"], "k": ["leek"]}, "حالة 4")
