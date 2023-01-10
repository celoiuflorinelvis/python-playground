
class CustomException (Exception):
    pass

try:
    1 / 0
except ZeroDivisionError as e:
    print(f"expception = {e}")
except (ZeroDivisionError, TypeError):
    print("Errors")
    raise RuntimeError("Unknown error!")


try:
    sum = 1 + 1
except CustomException as err:
    print(err)
else:
    print("No Exception")
finally:
    print("This block is executed on both cases: with/whithout exception.")


try:
    sum = 1 + 1
    raise(CustomException('Custom exception'))
except CustomException as err:
    print(err)
else:
    print("No Exception")
finally:
    print("This block is executed on both cases: with/whithout exception.")


def f_exception():
    raise ExceptionGroup("group1", 
        [OSError(1), 
        TypeError(2),
        ExceptionGroup("group2", [
            CustomException("Error")
        ])]
    )

try:
    f_exception()
except Exception as e:
    e.add_note("Update: New info")
    raise


