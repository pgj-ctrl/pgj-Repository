# try:
#     num = int(input("number: "))
#     result = 100 / num
#     print(result)
#     print("Done")
# except (ValueError,ZeroDivisionError):
#     print("plase input number ok ? fuck")
# except (EOFError,KeyboardInterrupt):
#     print("\nBye-bye my son")

try:
    num = int(input("number: "))
    result = 100 / num
except (ValueError,ZeroDivisionError)as e:
    print("plase input number ok ? fuck",e)
except (EOFError,KeyboardInterrupt):
    print("\nBye-bye my son")
    exit(1)
else:
    print(result)
finally:
    print("Done")