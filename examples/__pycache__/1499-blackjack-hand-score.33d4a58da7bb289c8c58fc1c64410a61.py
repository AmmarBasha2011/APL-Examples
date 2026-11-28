
# apl-source:1
# مثال 1499 — نتيجة يد البلاك جاك
# apl-source:2
# Blackjack hand score
# apl-source:3
# Demonstrates: ألعاب
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1499-blackjack-hand-score.apl
# apl-source:6

# apl-source:7
# الصور بعشرة والآص بأحد عشر أولاً
# apl-source:8
# إن تجاوزنا 21 نخفض كل آص بعشرة
# apl-source:9

# apl-source:10
def تأكد_يساوي(فعلي, متوقع, اسم):
  # apl-source:11
  if فعلي != متوقع:
    # apl-source:12
    print("فشل:", اسم)
    # apl-source:13
    print("  متوقع:", متوقع)
    # apl-source:14
    print("  فعلي:", فعلي)
    # apl-source:15
    قياسي_نظام_اخرج(1)
  # apl-source:16
  print("ناجح:", اسم)
# apl-source:17

# apl-source:18
def قيمة_اليد(أوراق):
  # apl-source:19
  مجموع = 0
  # apl-source:20
  آصات = 0
  # apl-source:21
  for ك in أوراق:
    # apl-source:22
    if ك == "A":
      # apl-source:23
      مجموع = مجموع + 11
      # apl-source:24
      آصات = آصات + 1
    # apl-source:25
    elif ك == "K" or ك == "Q" or ك == "J":
      # apl-source:26
      مجموع = مجموع + 10
    # apl-source:27
    else:
      # apl-source:28
      مجموع = مجموع + int(ك)
  # apl-source:29
  while مجموع > 21 and آصات > 0:
    # apl-source:30
    مجموع = مجموع - 10
    # apl-source:31
    آصات = آصات - 1
  # apl-source:32
  return مجموع
# apl-source:33

# apl-source:34
تأكد_يساوي(قيمة_اليد(["A", "K"]), 21, "بلاك جاك")
# apl-source:35
تأكد_يساوي(قيمة_اليد(["A", "A", "9"]), 21, "آصان")
# apl-source:36
تأكد_يساوي(قيمة_اليد(["K", "Q", "5"]), 25, "تجاوز")
# apl-source:37
تأكد_يساوي(قيمة_اليد(["5", "7"]), 12, "عادية")
# apl-source:38
