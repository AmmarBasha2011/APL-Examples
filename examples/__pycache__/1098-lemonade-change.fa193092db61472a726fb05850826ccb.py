
# apl-source:1
# مثال 1098 — الباقي في كشك الليمونادة
# apl-source:2
# Lemonade change
# apl-source:3
# Demonstrates: جشع في الفكة
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1098-lemonade-change.apl
# apl-source:6

# apl-source:7
# الكوب بخمسة والزبائن يدفعون 5 أو 10 أو 20
# apl-source:8
# نفضل إرجاع ورقة عشرة مع خمسة قبل ثلاث أوراق خمسة
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
def نعطي_باقي(اوراق):
  # apl-source:19
  خمسات = 0
  # apl-source:20
  عشرات = 0
  # apl-source:21
  for ورقة in اوراق:
    # apl-source:22
    if ورقة == 5:
      # apl-source:23
      خمسات = خمسات + 1
    # apl-source:24
    elif ورقة == 10:
      # apl-source:25
      if خمسات == 0:
        # apl-source:26
        return False
      # apl-source:27
      خمسات = خمسات - 1
      # apl-source:28
      عشرات = عشرات + 1
    # apl-source:29
    else:
      # apl-source:30
      if (عشرات > 0) and (خمسات > 0):
        # apl-source:31
        عشرات = عشرات - 1
        # apl-source:32
        خمسات = خمسات - 1
      # apl-source:33
      elif خمسات >= 3:
        # apl-source:34
        خمسات = خمسات - 3
      # apl-source:35
      else:
        # apl-source:36
        return False
  # apl-source:37
  return True
# apl-source:38

# apl-source:39
تأكد_يساوي(نعطي_باقي([5, 5, 5, 10, 20]), True, "ينجح")
# apl-source:40
تأكد_يساوي(نعطي_باقي([5, 5, 10, 10, 20]), False, "يفشل")
# apl-source:41
تأكد_يساوي(نعطي_باقي([10]), False, "بلا فكة")
# apl-source:42
تأكد_يساوي(نعطي_باقي([5, 5, 5, 5, 20, 20]), False, "فكة تنفد")
# apl-source:43
