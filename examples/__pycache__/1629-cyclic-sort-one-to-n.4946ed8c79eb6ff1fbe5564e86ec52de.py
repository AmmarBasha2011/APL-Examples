
# apl-source:1
# مثال 1629 — الفرز الدوري
# apl-source:2
# Cyclic sort for 1 to n
# apl-source:3
# Demonstrates: فرز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1629-cyclic-sort-one-to-n.apl
# apl-source:6

# apl-source:7
# الرقم ك مكانه الموضع ك ناقص واحد
# apl-source:8
# نبدل حتى يستقر كل رقم
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
def فرز_دوري(أ):
  # apl-source:19
  ع = 0
  # apl-source:20
  while ع < len(أ):
    # apl-source:21
    موضع = أ[ع] - 1
    # apl-source:22
    if أ[ع] != أ[موضع]:
      # apl-source:23
      ت = أ[ع]
      # apl-source:24
      أ[ع] = أ[موضع]
      # apl-source:25
      أ[موضع] = ت
    # apl-source:26
    else:
      # apl-source:27
      ع = ع + 1
  # apl-source:28
  return أ
# apl-source:29

# apl-source:30
تأكد_يساوي(فرز_دوري([3, 1, 5, 4, 2]), [1, 2, 3, 4, 5], "خمسة")
# apl-source:31
تأكد_يساوي(فرز_دوري([2, 1]), [1, 2], "اثنان")
# apl-source:32
تأكد_يساوي(فرز_دوري([1]), [1], "واحد")
# apl-source:33
