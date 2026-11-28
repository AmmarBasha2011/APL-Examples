
# apl-source:1
# مثال 1189 — درجة الأقواس
# apl-source:2
# Score of parentheses
# apl-source:3
# Demonstrates: مكدس
# apl-source:4
#
# apl-source:5
# Run:  python apl.py examples/1189-score-of-parentheses.apl
# apl-source:6

# apl-source:7
# الزوج المتجاور بواحد
# apl-source:8
# والمتداخل بضعف ما بداخله
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
def درجة(س):
  # apl-source:19
  مكدس = [0]
  # apl-source:20
  for ح in س:
    # apl-source:21
    if ح == "(":
      # apl-source:22
      مكدس = مكدس + [0]
    # apl-source:23
    else:
      # apl-source:24
      داخل = مكدس.pop()
      # apl-source:25
      قيمة = 1
      # apl-source:26
      if داخل > 0:
        # apl-source:27
        قيمة = 2 * داخل
      # apl-source:28
      مكدس[-1] = مكدس[-1] + قيمة
  # apl-source:29
  return مكدس[0]
# apl-source:30

# apl-source:31
تأكد_يساوي(درجة("()"), 1, "زوج")
# apl-source:32
تأكد_يساوي(درجة("(())"), 2, "متداخل")
# apl-source:33
تأكد_يساوي(درجة("()()"), 2, "متجاور")
# apl-source:34
تأكد_يساوي(درجة("(()(()))"), 6, "مختلط")
# apl-source:35
