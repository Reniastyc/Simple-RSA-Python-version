import RdeEM_RandomPrime
import RdeEM_RSA
import tkinter

def MultiLanguage(l_language):
    
    global MultiLang_KeyDigit
    global MultiLang_PublicDigit
    global MultiLang_KeyCalculate
    global MultiLang_PublicKey
    global MultiLang_PrivateKey
    global MultiLang_Module
    global MultiLang_Encoding
    global MultiLang_Decoding
    global MultiLang_File
    
    if l_language == "Traditional Chinese":
        MultiLang_KeyDigit.set("密鑰位數（128 ~ 2048）")
        MultiLang_PublicDigit.set("公鑰位數（32 ~ 1024）")
        MultiLang_KeyCalculate.set("計算密鑰")
        MultiLang_PublicKey.set("公鑰")
        MultiLang_PrivateKey.set("私鑰")
        MultiLang_Module.set("模值")
        MultiLang_Encoding.set("編碼")
        MultiLang_Decoding.set("解碼")
        
    elif l_language == "Simplified Chinese":
        MultiLang_KeyDigit.set("密钥位数（128 ~ 2048）")
        MultiLang_PublicDigit.set("公钥位数（32 ~ 1024）")
        MultiLang_KeyCalculate.set("计算密钥")
        MultiLang_PublicKey.set("公钥")
        MultiLang_PrivateKey.set("私钥")
        MultiLang_Module.set("模值")
        MultiLang_Encoding.set("编码")
        MultiLang_Decoding.set("解码")
        
    else:
        MultiLang_KeyDigit.set("$KeyDigit")
        MultiLang_PublicDigit.set("$PublicDigit")
        MultiLang_KeyCalculate.set("$KeyCalculate")
        MultiLang_PublicKey.set("$PublicKey")
        MultiLang_PrivateKey.set("$PrivateKey")
        MultiLang_Module.set("$Module")
        MultiLang_Encoding.set("$Encoding")
        MultiLang_Decoding.set("$Decoding")
   
def button_KeyCalculateCommand():
    l_RSAn, l_RSAe, l_RSAd = RdeEM_RSA.CalculateRSA(int(entry_RSAdigit.get()), int(entry_Publicdigit.get()))
    text_PublicKey.delete("1.0", "end")
    text_PublicKey.insert("1.0", f"{l_RSAe:X}")
    text_PrivateKey.delete("1.0", "end")
    text_PrivateKey.insert("1.0", f"{l_RSAd:X}")
    text_Module.delete("1.0", "end")
    text_Module.insert("1.0", f"{l_RSAn:X}")
    global g_RSAn, g_RSAe, g_RSAd
    g_RSAn, g_RSAe, g_RSAd = l_RSAn, l_RSAe, l_RSAd
    
def button_EncodingCommand():
    l_code = text_Code.get("1.0", "end")
    l_code = l_code.replace(" ", "").replace("\n", "")
    l_result = RdeEM_RSA.RSAEncoding(int(l_code), g_RSAe, g_RSAn)
    text_Code.delete("1.0", "end")
    text_Code.insert("1.0", l_result)
    
    
def button_DecodingCommand():
    l_code = text_Code.get("1.0", "end")
    l_code = l_code.replace(" ", "").replace("\n", "")
    l_result = RdeEM_RSA.RSADecoding(int(l_code), g_RSAd, g_RSAn)
    text_Code.delete("1.0", "end")
    text_Code.insert("1.0", l_result)
    
def menu_LanguageRadioButton():
    
    MultiLanguage(g_language.get())
    
g_RSAn, g_RSAe, g_RSAd = 0, 0, 0

root = tkinter.Tk()

MultiLang_KeyDigit = tkinter.StringVar()
MultiLang_PublicDigit = tkinter.StringVar()
MultiLang_KeyCalculate = tkinter.StringVar()
MultiLang_PublicKey = tkinter.StringVar()
MultiLang_PrivateKey = tkinter.StringVar()
MultiLang_Module = tkinter.StringVar()
MultiLang_Encoding = tkinter.StringVar()
MultiLang_Decoding = tkinter.StringVar()
MultiLang_File = tkinter.StringVar()

g_language = tkinter.StringVar()

screen_width, screen_height = root.maxsize()

window_width = 1105
window_height = 850

position_x = int((screen_width - window_width) / 2)
position_y = int((screen_height - window_height) / 2)

root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

root.resizable(width = False, height = False)

root.title("Simple RSA v1.0")

menu_Main = tkinter.Menu(root, font = ("I.Ming", 10))
menu_Language = tkinter.Menu(menu_Main, tearoff = 0)
cascade_Language = menu_Main.add_cascade(label = "Language", menu = menu_Language)
menu_Language.add_radiobutton(label = "傳統中文", variable = g_language, value = "Traditional Chinese", command = menu_LanguageRadioButton)
menu_Language.add_radiobutton(label = "简化中文", variable = g_language, value = "Simplified Chinese", command = menu_LanguageRadioButton)

g_language.set("Simplified Chinese")

root.config(menu = menu_Main)

label_RSAdigit = tkinter.Label(root, textvariable = MultiLang_KeyDigit, font = ("I.Ming", 20), justify = "center")
label_RSAdigit.grid(row = 0, column = 0, columnspan = 2)

entry_RSAdigit = tkinter.Entry(root, width = 10, font = ("I.Ming", 20), justify = "center")
entry_RSAdigit.grid(row = 0, column = 2)

label_Publicdigit = tkinter.Label(root, textvariable = MultiLang_PublicDigit, font = ("I.Ming", 20), justify = "center")
label_Publicdigit.grid(row = 0, column = 4, columnspan = 2)

entry_Publicdigit = tkinter.Entry(root, width = 10, font = ("I.Ming", 20), justify = "center")
entry_Publicdigit.grid(row = 0, column = 6)

button_KeyCalculate = tkinter.Button(root, textvariable = MultiLang_KeyCalculate, font = ("I.Ming", 20), justify = "center", command = button_KeyCalculateCommand)
button_KeyCalculate.grid(row = 1, column = 3)

label_PublicKey = tkinter.Label(root, textvariable = MultiLang_PublicKey, font = ("I.Ming", 20), justify = "center")
label_PublicKey.grid(row = 2, column = 0)

text_PublicKey = tkinter.Text(root, width = 80, height = 2, font = ("I.Ming", 15))
text_PublicKey.grid(row = 2, column = 1, columnspan = 6)

label_PrivateKey = tkinter.Label(root, textvariable = MultiLang_PrivateKey, font = ("I.Ming", 20), justify = "center")
label_PrivateKey.grid(row = 3, column = 0)

text_PrivateKey = tkinter.Text(root, width = 80, height = 8, font = ("I.Ming", 15))
text_PrivateKey.grid(row = 3, column = 1, columnspan = 6)

label_Module = tkinter.Label(root, textvariable = MultiLang_Module, font = ("I.Ming", 20), justify = "center")
label_Module.grid(row = 4, column = 0)

text_Module = tkinter.Text(root, width = 80, height = 8, font = ("I.Ming", 15))
text_Module.grid(row = 4, column = 1, columnspan = 6)

button_Encoding = tkinter.Button(root, textvariable = MultiLang_Encoding, font = ("I.Ming", 20), justify = "center", command = button_EncodingCommand)
button_Encoding.grid(row = 5, column = 2)

button_Decoding = tkinter.Button(root, textvariable = MultiLang_Decoding, font = ("I.Ming", 20), justify = "center", command = button_DecodingCommand)
button_Decoding.grid(row = 5, column = 4)

text_Code = tkinter.Text(root, width = 90, height = 10, font = ("I.Ming", 15))
text_Code.grid(row = 6, column = 0, columnspan = 7)

MultiLanguage(g_language.get())

root.mainloop()