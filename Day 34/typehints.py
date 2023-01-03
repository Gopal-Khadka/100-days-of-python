def drive(age:int) -> bool:
    if age>18:
        can_drive=True
    else:
        can_drive=False
  
    return can_drive


print(drive(18))