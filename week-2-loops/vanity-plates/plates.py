def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)<2 or len(s)>6:
        return False
    else:
        if not s[0].isalpha() or not s[1].isalpha():
            return False
        for index,char in enumerate(s):
            if not char.isalnum():
                return False
            if char.isdigit():
                position = index
                for j in s[position:]:
                    if(position==index and s[position]=="0"):
                        return False
                    if not j.isdigit():
                        return False
                
        return True
main()