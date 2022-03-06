alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

encode_decode_info = []
enc_msgs = [""]
dec_msgs = [""]


def print_header():
    print("\n\t=================")
    print("\t  Caesar Cipher")
    print("\t=================\n")


def encrypt():
    for elm in encode_decode_info:
        msg = elm[0]
        shift = elm[1]
        enc_msg = ""
        for ch in msg:
            pos = (alphabets.index(ch) + shift) % 26
            enc_msg += alphabets[pos]
        enc_msgs[0] = enc_msg
    print(enc_msgs[0] + "\n")


def decrypt():
    for elm in encode_decode_info:
        msg = enc_msgs[0]
        shift = elm[1]
        dec_msg = ""
        for ch in msg:
            pos = (alphabets.index(ch) - shift) % 26
            dec_msg += alphabets[pos]
        dec_msgs[0] = dec_msg
    print(dec_msgs[0] + "\n")


def get_user_inputs(choice):
    if choice == "encode":
        msg = input("Type your message:\n")
        shift = int(input("Type your shift number: "))
        encode_decode_info.append([msg, shift])
        encrypt()
        return True
    elif choice == 'decode':
        if len(encode_decode_info) == 0:
            print(
                "\nYou haven't entered any message to encrpyt. Please first select the \"encode\" option\n")
            return True
        else:
            decrypt()
            return True
    elif choice == "-1":
        print("\nExiting the application.")
        return False
    else:
        print("\nWrong choice, type either \"encode\" or \"decode\"")
        return True


def main():
    print_header()
    while True:
        user_choice = input(
            "Type \"encode\" to encrypt, type \"decode\" to decrypt, or \"-1\" to quit: ")
        print()
        if user_choice != "-1":
            user_choice = get_user_inputs(user_choice)
        else:
            print("Exiting the application.")
            exit(0)


main()
