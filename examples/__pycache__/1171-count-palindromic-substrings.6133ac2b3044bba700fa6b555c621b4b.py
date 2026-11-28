
# apl-source:1
# مثال 1171 — عد نصوص متناظرة
# apl-source:2
# Count palindromic substrings
# apl-source:3
# Demonstrates: توسع من المركز
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1171-count-palindromic-substrings.apl
# apl-source:6

# apl-source:7
# كل موضع وكل فجوة بين حرفين مركز محتمل
# apl-source:8
# نوسع ما دام الطرفان متساويين
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
def عد_متناظرات(س):
  # apl-source:19
  ع = 0
  # apl-source:20
  ن = len(س)
  # apl-source:21
  for مركز in range(2 * ن - 1):
    # apl-source:22
    ي = مركز // 2
    # apl-source:23
    م = ي + مركز % 2
    # apl-source:24
    while (ي >= 0) and (م < ن):
      # apl-source:25
      if س[ي] != س[م]:
        # apl-source:26
        ي = -5
      # apl-source:27
      else:
        # apl-source:28
        ع = ع + 1
        # apl-source:29
        ي = ي - 1
        # apl-source:30
        م = م + 1
  # apl-source:31
  return ع
# apl-source:32

# apl-source:33
تأكد_يساوي(عد_متناظرات("abc"), 3, "ثلاثة")
# apl-source:34
تأكد_يساوي(عد_متناظرات("aaa"), 6, "ستة")
# apl-source:35
تأكد_يساوي(عد_متناظرات("abba"), 6, "زوجي")
# apl-source:36
تأكد_يساوي(عد_متناظرات(""), 0, "فارغة")
# apl-source:37
