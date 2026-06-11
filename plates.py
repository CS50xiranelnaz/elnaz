def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # طول بین 2 و 6
    if len(s) < 2 or len(s) > 6:
        return False

    # دو کاراکتر اول باید حرف باشند
    if not s[:2].isalpha():
        return False

    number_started = False

    for char in s:

        # فقط حرف و عدد مجاز است
        if not char.isalnum():
            return False

        if char.isdigit():

            if not number_started:
                number_started = True

                # اولین عدد نباید صفر باشد
                if char == "0":
                    return False

        else:
            # بعد از شروع عدد نباید حرف بیاید
            if number_started:
                return False

    return True


main()