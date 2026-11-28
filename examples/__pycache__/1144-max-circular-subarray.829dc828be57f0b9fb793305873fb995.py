
# apl-source:1
# مثال 1144 — أكبر مجموع دائري
# apl-source:2
# Maximum circular subarray sum
# apl-source:3
# Demonstrates: كادان مزدوج
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1144-max-circular-subarray.apl
# apl-source:6

# apl-source:7
# إما أن تكون القائمة الجزئية عادية
# apl-source:8
# أو تلتف فتساوي المجموع الكلي ناقص أصغر قائمة جزئية
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
def اكبر_دائري(أ):
  # apl-source:19
  كل = 0
  # apl-source:20
  حالي_ك = 0
  # apl-source:21
  حالي_ص = 0
  # apl-source:22
  اكبر_ = أ[0]
  # apl-source:23
  اصغر_ = أ[0]
  # apl-source:24
  for س in أ:
    # apl-source:25
    كل = كل + س
    # apl-source:26
    حالي_ك = max(حالي_ك + س, س)
    # apl-source:27
    حالي_ص = min(حالي_ص + س, س)
    # apl-source:28
    اكبر_ = max(اكبر_, حالي_ك)
    # apl-source:29
    اصغر_ = min(اصغر_, حالي_ص)
  # apl-source:30
  if اكبر_ < 0:
    # apl-source:31
    return اكبر_
  # apl-source:32
  return max(اكبر_, كل - اصغر_)
# apl-source:33

# apl-source:34
تأكد_يساوي(اكبر_دائري([1,-2,3,-2]), 3, "عادي")
# apl-source:35
تأكد_يساوي(اكبر_دائري([5,-3,5]), 10, "ملتف")
# apl-source:36
تأكد_يساوي(اكبر_دائري([-3,-2,-3]), -2, "كلها سالبة")
# apl-source:37
تأكد_يساوي(اكبر_دائري([3,-1,2,-1]), 4, "التفاف")
# apl-source:38
