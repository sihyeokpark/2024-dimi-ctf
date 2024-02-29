chart = {
"か": "ka",
"き": "ki",
"く": "ku",
"け": "ke",
"こ": "ko",
"が": "ga",
"ぎ": "gi",
"ぐ": "gu",
"げ": "ge",
"ご": "go",
"さ": "sa",
"し": "shi",
"す": "su",
"せ": "se",
"そ": "so",
"ざ": "za",
"じ": "ji",
"ず": "zu",
"ぜ": "ze",
"ぞ": "zo",
"た": "ta",
"ち": "chi",
"つ": "tsu",
"て": "te",
"と": "to",
"だ": "da",
"ぢ": "ji",
"づ": "zu",
"で": "de",
"ど": "do",
"な": "na",
"に": "ni",
"ぬ": "nu",
"ね": "ne",
"の": "no",
"は": "ha",
"ひ": "hi",
"ふ": "fu",
"へ": "he",
"ほ": "ho",
"ぱ": "ba",
"ぴ": "bi",
"ぷ": "bu",
"ぺ": "be",
"ぽ": "bo",
"ぱ": "pa",
"ぴ": "pi",
"ぷ": "pu",
"ぺ": "pe",
"ぽ": "po",
"ま": "ma",
"み": "mi",
"む": "mu",
"め": "me",
"も": "mo",
"や": "ya",
"ゆ": "yu",
"よ": "yo",
"ら": "ra",
"り": "ri",
"る": "ru",
"れ": "re",
"ろ": "ro",
"わ": "wa",
"を": "o",
"ん": "n",
"あ": "a",
"い": "i",
"う": "u",
"え": "e",
"お": "o",
}

flag = "DIMI{wanelovesjapanese!!!ineedtomakeflaglongertomakefancier}"

def translateToJapan(what):
    for key, value in chart.items():
        what = what.replace(value, key)
    return what

print("Welcome to Japan! Use this translator to communicate!")
while True:
    print("[1] Translate to Japanese!")
    print("[2] Translate to English!")
    print("[3] Print \'Translated\' Flag!")
    print("[4] Exit")
    resp = int(input("> "))
    if resp == 1:
        plaintext = input("What do you want to translate? ")
        print(translateToJapan(plaintext))
    elif resp == 2:
        print("Sorry, if I give you this feature, the problem is so easy")
    elif resp == 3:
        print(translateToJapan(flag))
    elif resp == 4:
        break
