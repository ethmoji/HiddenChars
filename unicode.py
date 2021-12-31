from hiddenchars import HiddenChars

def main():
    hiddenChars = HiddenChars("unicodeEmojis.json")
    print(hiddenChars.getReveal("🐋️🐋️🐋️"))

if __name__ == '__main__':
    main()