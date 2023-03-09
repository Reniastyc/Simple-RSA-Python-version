import RdeEM_RSA
import tkinter
import tkinter.filedialog
import random

def ValueInRange(l_Value, l_Min, l_Max):
    if l_Value < l_Min:
        return l_Min
    elif l_Value > l_Max:
        return l_Max
    else:
        return l_Value

def MultiLanguage(l_language):
    
    global MultiLang_KeyDigit
    global MultiLang_PublicDigit
    global MultiLang_KeyCalculate
    global MultiLang_PublicKey
    global MultiLang_PrivateKey
    global MultiLang_Module
    global MultiLang_Encoding
    global MultiLang_Decoding
    global MultiLang_SaveKey
    global MultiLang_LoadKey
    global MultiLang_SavePublic
    global MultiLang_SavePrivate
    global MultiLang_LoadPublic
    global MultiLang_LoadPrivate
    global MultiLang_CodeNum
    global MultiLang_CodeText
    
    if l_language == "Traditional Chinese":
        MultiLang_KeyDigit.set(f"密鑰位數（{g_keyMin} ~ {g_keyMax}）")
        MultiLang_PublicDigit.set(f"公鑰位數（{g_pubMin} ~ {g_pubMax}）")
        MultiLang_KeyCalculate.set("計算密鑰")
        MultiLang_PublicKey.set("公鑰")
        MultiLang_PrivateKey.set("私鑰")
        MultiLang_Module.set("模值")
        MultiLang_Encoding.set("編碼")
        MultiLang_Decoding.set("解碼")
        MultiLang_SaveKey.set("保存密鑰")
        MultiLang_LoadKey.set("讀取密鑰")
        MultiLang_SavePublic.set("保存公鑰")
        MultiLang_SavePrivate.set("保存私鑰")
        MultiLang_LoadPublic.set("讀取公鑰")
        MultiLang_LoadPrivate.set("讀取私鑰")
        MultiLang_CodeNum.set("明碼爲數字")
        MultiLang_CodeText.set("明碼爲字符")
    elif l_language == "Simplified Chinese":
        MultiLang_KeyDigit.set(f"密钥位数（{g_keyMin} ~ {g_keyMax}）")
        MultiLang_PublicDigit.set(f"公钥位数（{g_pubMin} ~ {g_pubMax}）")
        MultiLang_KeyCalculate.set("计算密钥")
        MultiLang_PublicKey.set("公钥")
        MultiLang_PrivateKey.set("私钥")
        MultiLang_Module.set("模值")
        MultiLang_Encoding.set("编码")
        MultiLang_Decoding.set("解码")
        MultiLang_SaveKey.set("保存密钥")
        MultiLang_LoadKey.set("读取密钥")
        MultiLang_SavePublic.set("保存公钥")
        MultiLang_SavePrivate.set("保存私钥")
        MultiLang_LoadPublic.set("读取公钥")
        MultiLang_LoadPrivate.set("读取私钥")
        MultiLang_CodeNum.set("明码为数字")
        MultiLang_CodeText.set("明码为字符")
    else:
        MultiLang_KeyDigit.set("$KeyDigit")
        MultiLang_PublicDigit.set("$PublicDigit")
        MultiLang_KeyCalculate.set("$KeyCalculate")
        MultiLang_PublicKey.set("$PublicKey")
        MultiLang_PrivateKey.set("$PrivateKey")
        MultiLang_Module.set("$Module")
        MultiLang_Encoding.set("$Encoding")
        MultiLang_Decoding.set("$Decoding")
        MultiLang_SaveKey.set("$SaveKey")
        MultiLang_LoadKey.set("$LoadKey")
        MultiLang_SavePublic.set("$SavePublic")
        MultiLang_SavePrivate.set("$SavePrivate")
        MultiLang_LoadPublic.set("$LoadPublic")
        MultiLang_LoadPrivate.set("$LoadPrivate")
        MultiLang_CodeNum.set("$CodeAnNum")
        MultiLang_CodeText.set("$CodeAsText")

g_keyMax = 4096
g_keyMin = 128
g_pubMax = 1024
g_pubMin = 32

def button_KeyCalculateCommand():
    global g_keyMax, g_keyMin, g_pubMax, g_pubMin
    l_RSAdigit = ValueInRange(int(entry_RSAdigit.get()), g_keyMin, g_keyMax)
    l_Pubdigit = ValueInRange(int(entry_Publicdigit.get()), g_pubMin, g_pubMax)
    if l_Pubdigit >= l_RSAdigit // 2:
        l_Pubdigit = l_RSAdigit // 2
    entry_Publicdigit.delete(0, tkinter.END)
    entry_Publicdigit.insert(0, f"{l_Pubdigit}")
    entry_RSAdigit.delete(0, tkinter.END)
    entry_RSAdigit.insert(0, f"{l_RSAdigit}")
    l_RSAn, l_RSAe, l_RSAd, _ = RdeEM_RSA.CalculateRSA(l_RSAdigit, l_Pubdigit, 3)
    text_PublicKey.delete("1.0", "end")
    text_PublicKey.insert("1.0", f"{l_RSAe:X}")
    text_PrivateKey.delete("1.0", "end")
    text_PrivateKey.insert("1.0", f"{l_RSAd:X}")
    text_Module.delete("1.0", "end")
    text_Module.insert("1.0", f"{l_RSAn:X}")
    
def button_EncodingCommand():
    l_RSAe = int(text_PublicKey.get("1.0", "end").replace("\n", ""), 16)
    l_RSAn = int(text_Module.get("1.0", "end").replace("\n", ""), 16)
    if g_CodeType == 0:
        l_code = text_Code.get("1.0", "end").replace(" ", "").replace("\n", "")
        # l_tail = random.randint(0, 15)
        #l_code = f"{l_code}{l_tail:X}"
        l_num = int(l_code, 16)
    elif g_CodeType == 1:
        l_code = text_Code.get("1.0", "end")[:-1]
        #l_tail = chr(random.randint(33, 126))
        #l_code = f"`{l_code}{l_tail}"
        l_code = f"`{l_code}"
        l_len = l_RSAn.bit_length() // 8 - 2
        l_bytes = bytes(l_code, "utf-8")[:l_len]
        l_num = int.from_bytes(l_bytes, byteorder = "big")
    print(f"{l_num:X}")
    l_result = RdeEM_RSA.RSACoding(l_num, l_RSAe, l_RSAn)
    print(f"{l_result:X}")
    l_hex = f"{l_result:X}"[::-1]
    l_list = []
    for l_loop in range(0, len(l_hex), 3):
        l_ord = int(l_hex[l_loop:l_loop + 3], 16)
        l_list.append(chr(0x0E00 + l_ord + 0x1000 * random.randint(4, 8)))
    l_text = "".join(l_list)
    text_Encode.delete("1.0", "end")
    text_Encode.insert("1.0", l_text)

def button_DecodingCommand():
    l_RSAd = int(text_PrivateKey.get("1.0", "end").replace("\n", ""), 16)
    l_RSAn = int(text_Module.get("1.0", "end").replace("\n", ""), 16)
    l_code = text_Encode.get("1.0", "end")
    l_code = l_code.replace(" ", "").replace("\n", "")
    l_list = []
    for l_loop in l_code[:-1]:
        l_ord = (ord(l_loop) - 0x0E00) & 0x0FFF
        l_str = f"000{l_ord:X}"
        l_list.append(l_str[-3:])
    l_ord = (ord(l_code[-1]) - 0x0E00) & 0x0FFF
    l_list.append(f"{l_ord:X}")
    l_text = "".join(l_list)[::-1]
    l_num = int(l_text, 16)
    print(f"{l_num:X}")
    l_result = RdeEM_RSA.RSACoding(l_num, l_RSAd, l_RSAn)
    print(f"{l_result:X}")
    if g_CodeType == 0:
        l_text = f"{l_result:X}"
    elif g_CodeType == 1:
        l_len = l_RSAn.bit_length() // 4
        l_bytes = int.to_bytes(l_result, l_len, byteorder = "big")
        l_text = str(l_bytes, "utf-8", "ignore")
        l_pos = l_text.find("`") + 1
        l_text = l_text[l_pos:]
    text_Code.delete("1.0", "end")
    text_Code.insert("1.0", l_text)
    
def radio_LanguageRadioButton():
    MultiLanguage(g_language.get())

def radio_CodeTypeRadioButton():
    global g_CodeType
    l_codetype = g_codetype.get()
    if l_codetype == "Code Number":
        g_CodeType = 0
    elif l_codetype == "Code Text":
        g_CodeType = 1
   
def button_SaveKeyCommand():
    l_RSAn = int(text_Module.get("1.0", "end").replace("\n", ""), 16)
    l_RSAe = int(text_PublicKey.get("1.0", "end").replace("\n", ""), 16)
    l_RSAd = int(text_PrivateKey.get("1.0", "end").replace("\n", ""), 16)
    l_file = tkinter.filedialog.asksaveasfile(filetypes = [("*.TXT", ".TXT")], defaultextension = ".TXT")
    l_file.write(hex(l_RSAn))
    l_file.write("\n")
    l_file.write(hex(l_RSAe))
    l_file.write("\n")
    l_file.write(hex(l_RSAd))
    l_file.close

def button_LoadKeyCommand():
    l_file = tkinter.filedialog.askopenfile(filetypes = [("*.TXT", ".TXT")])
    if l_file == None:
        return
    l_str = str(l_file.read())
    l_file.close
    l_strarray = l_str.split("\n")
    l_RSAn = int(l_strarray[0], 0)
    l_RSAe = int(l_strarray[1], 0)
    l_RSAd = int(l_strarray[2], 0)
    text_PublicKey.delete("1.0", "end")
    text_PublicKey.insert("1.0", f"{l_RSAe:X}")
    text_PrivateKey.delete("1.0", "end")
    text_PrivateKey.insert("1.0", f"{l_RSAd:X}")
    text_Module.delete("1.0", "end")
    text_Module.insert("1.0", f"{l_RSAn:X}")
    
def button_SavePublicCommand():
    l_RSAn = int(text_Module.get("1.0", "end").replace("\n", ""), 16)
    l_RSAe = int(text_PublicKey.get("1.0", "end").replace("\n", ""), 16)
    #l_RSAd = int(text_PrivateKey.get("1.0", "end").replace("\n", ""), 16)
    l_file = tkinter.filedialog.asksaveasfile(filetypes = [("*.TXT", ".TXT")], defaultextension = ".TXT")
    l_file.write(hex(l_RSAn))
    l_file.write("\n")
    l_file.write(hex(l_RSAe))
    l_file.write("\n")
    l_file.write(hex(0))
    l_file.close

def button_LoadPublicCommand():
    l_file = tkinter.filedialog.askopenfile(filetypes = [("*.TXT", ".TXT")])
    if l_file == None:
        return
    l_str = str(l_file.read())
    l_file.close
    l_strarray = l_str.split("\n")
    l_RSAn = int(l_strarray[0], 0)
    l_RSAe = int(l_strarray[1], 0)
    l_RSAd = 0
    text_PublicKey.delete("1.0", "end")
    text_PublicKey.insert("1.0", f"{l_RSAe:X}")
    text_PrivateKey.delete("1.0", "end")
    text_PrivateKey.insert("1.0", f"{l_RSAd:X}")
    text_Module.delete("1.0", "end")
    text_Module.insert("1.0", f"{l_RSAn:X}")
    
def button_SavePrivateCommand():
    l_RSAn = int(text_Module.get("1.0", "end").replace("\n", ""), 16)
    #l_RSAe = int(text_PublicKey.get("1.0", "end").replace("\n", ""), 16)
    l_RSAd = int(text_PrivateKey.get("1.0", "end").replace("\n", ""), 16)
    l_file = tkinter.filedialog.asksaveasfile(filetypes = [("*.TXT", ".TXT")], defaultextension = ".TXT")
    l_file.write(hex(l_RSAn))
    l_file.write("\n")
    l_file.write(hex(0))
    l_file.write("\n")
    l_file.write(hex(l_RSAd))
    l_file.close

def button_LoadPrivateCommand():
    l_file = tkinter.filedialog.askopenfile(filetypes = [("*.TXT", ".TXT")])
    if l_file == None:
        return
    l_str = str(l_file.read())
    l_file.close
    l_strarray = l_str.split("\n")
    l_RSAn = int(l_strarray[0], 0)
    l_RSAe = 0
    l_RSAd = int(l_strarray[2], 0)
    text_PublicKey.delete("1.0", "end")
    text_PublicKey.insert("1.0", f"{l_RSAe:X}")
    text_PrivateKey.delete("1.0", "end")
    text_PrivateKey.insert("1.0", f"{l_RSAd:X}")
    text_Module.delete("1.0", "end")
    text_Module.insert("1.0", f"{l_RSAn:X}")

root = tkinter.Tk()

MultiLang_KeyDigit = tkinter.StringVar()
MultiLang_PublicDigit = tkinter.StringVar()
MultiLang_KeyCalculate = tkinter.StringVar()
MultiLang_PublicKey = tkinter.StringVar()
MultiLang_PrivateKey = tkinter.StringVar()
MultiLang_Module = tkinter.StringVar()
MultiLang_Encoding = tkinter.StringVar()
MultiLang_Decoding = tkinter.StringVar()
MultiLang_SaveKey = tkinter.StringVar()
MultiLang_LoadKey = tkinter.StringVar()
MultiLang_SavePublic = tkinter.StringVar()
MultiLang_SavePrivate = tkinter.StringVar()
MultiLang_LoadPublic = tkinter.StringVar()
MultiLang_LoadPrivate = tkinter.StringVar()
MultiLang_CodeNum = tkinter.StringVar()
MultiLang_CodeText = tkinter.StringVar()

g_language = tkinter.StringVar()
g_codetype = tkinter.StringVar()
g_encodetype = tkinter.StringVar()

root.resizable(width = False, height = False)

root.title("Simple RSA v2.0")

g_language.set("Simplified Chinese")
g_codetype.set("Code Text")
g_CodeType = 1

g_font = ("", 13)

radio_Lang_SC = tkinter.Radiobutton(root, text = "简化中文", font = g_font, justify = "center", variable = g_language, value = "Simplified Chinese", command = radio_LanguageRadioButton)
radio_Lang_SC.grid(row = 0, column = 0)

radio_Lang_TC = tkinter.Radiobutton(root, text = "傳統中文", font = g_font, justify = "center", variable = g_language, value = "Traditional Chinese", command = radio_LanguageRadioButton)
radio_Lang_TC.grid(row = 0, column = 1)

radio_code_num = tkinter.Radiobutton(root, textvariable = MultiLang_CodeNum, font = g_font, justify = "center", variable = g_codetype, value = "Code Number", command = radio_CodeTypeRadioButton)
radio_code_num.grid(row = 0, column = 5)

radio_code_text = tkinter.Radiobutton(root, textvariable = MultiLang_CodeText, font = g_font, justify = "center", variable = g_codetype, value = "Code Text", command = radio_CodeTypeRadioButton)
radio_code_text.grid(row = 0, column = 6)

button_SaveKey = tkinter.Button(root, textvariable = MultiLang_SaveKey, font = g_font, justify = "center", command = button_SaveKeyCommand)
button_SaveKey.grid(row = 1, column = 0)

button_SaveKey = tkinter.Button(root, textvariable = MultiLang_LoadKey, font = g_font, justify = "center", command = button_LoadKeyCommand)
button_SaveKey.grid(row = 1, column = 1)

button_SaveKey = tkinter.Button(root, textvariable = MultiLang_SavePublic, font = g_font, justify = "center", command = button_SavePublicCommand)
button_SaveKey.grid(row = 1, column = 2)

button_SaveKey = tkinter.Button(root, textvariable = MultiLang_LoadPublic, font = g_font, justify = "center", command = button_LoadPublicCommand)
button_SaveKey.grid(row = 1, column = 3)

button_SaveKey = tkinter.Button(root, textvariable = MultiLang_SavePrivate, font = g_font, justify = "center", command = button_SavePrivateCommand)
button_SaveKey.grid(row = 1, column = 4)

button_SaveKey = tkinter.Button(root, textvariable = MultiLang_LoadPrivate, font = g_font, justify = "center", command = button_LoadPrivateCommand)
button_SaveKey.grid(row = 1, column = 5)

label_RSAdigit = tkinter.Label(root, textvariable = MultiLang_KeyDigit, font = g_font, justify = "center")
label_RSAdigit.grid(row = 2, column = 0, columnspan = 2)

entry_RSAdigit = tkinter.Entry(root, width = 10, font = g_font, justify = "center")
entry_RSAdigit.grid(row = 2, column = 2)

label_Publicdigit = tkinter.Label(root, textvariable = MultiLang_PublicDigit, font = g_font, justify = "center")
label_Publicdigit.grid(row = 2, column = 4, columnspan = 2)

entry_Publicdigit = tkinter.Entry(root, width = 10, font = g_font, justify = "center")
entry_Publicdigit.grid(row = 2, column = 6)

button_KeyCalculate = tkinter.Button(root, textvariable = MultiLang_KeyCalculate, font = g_font, justify = "center", command = button_KeyCalculateCommand)
button_KeyCalculate.grid(row = 3, column = 3)

label_PublicKey = tkinter.Label(root, textvariable = MultiLang_PublicKey, font = g_font, justify = "center")
label_PublicKey.grid(row = 4, column = 0)

text_PublicKey = tkinter.Text(root, width = 90, height = 4, font = g_font)
text_PublicKey.grid(row = 4, column = 1, columnspan = 6)

label_PrivateKey = tkinter.Label(root, textvariable = MultiLang_PrivateKey, font = g_font, justify = "center")
label_PrivateKey.grid(row = 5, column = 0)

text_PrivateKey = tkinter.Text(root, width = 90, height = 12, font = g_font)
text_PrivateKey.grid(row = 5, column = 1, columnspan = 6)

label_Module = tkinter.Label(root, textvariable = MultiLang_Module, font = g_font, justify = "center")
label_Module.grid(row = 6, column = 0)

text_Module = tkinter.Text(root, width = 90, height = 12, font = g_font)
text_Module.grid(row = 6, column = 1, columnspan = 6)

button_Encoding = tkinter.Button(root, textvariable = MultiLang_Encoding, font = g_font, justify = "center", command = button_EncodingCommand)
button_Encoding.grid(row = 7, column = 2)

button_Decoding = tkinter.Button(root, textvariable = MultiLang_Decoding, font = g_font, justify = "center", command = button_DecodingCommand)
button_Decoding.grid(row = 7, column = 4)

text_Code = tkinter.Text(root, width = 100, height = 10, font = g_font)
text_Code.grid(row = 8, column = 0, columnspan = 7)

text_Encode = tkinter.Text(root, width = 100, height = 10, font = g_font)
text_Encode.grid(row = 9, column = 0, columnspan = 7)

MultiLanguage(g_language.get())

root.geometry("")

root.update()

window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width, screen_height = root.maxsize()

position_x = int((screen_width - window_width) / 2)
position_y = int((screen_height - window_height) / 2)

root.geometry(f"+{position_x}+{position_y}")

root.mainloop()