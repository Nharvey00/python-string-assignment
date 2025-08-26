print("Enter a sentence")
sentence = input()

while True:
    
        print("Choose an operation:")
        print("1. Reverse the sentence")
        print("2. Count vowels")
        print("3. Check if palindrome")
        print("4. Find and replace a word")
        print("5. Format (Title case)")
        print("6. Split into words")
        print("7. Word frequency counter")
        print("8. Swap case")
        print("9. Exit")
        
        num = input("Enter your choice: ")

        if num == "1":
            print("Reversed: ", sentence[::-1])
            
        elif num == "2":
            vowels = "aeiouAEIOU"
            count = sum(1 for ch in sentence if ch in vowels)
            print("Number of vowels:", count)

        elif num == "3":
            cleaned = ''.join(sentence.lower().split())
            if cleaned == cleaned[::-1]:
                print("Yes, it's a palindrome!")
            else:
                print("No, it's not a palindrome.")

        elif num == "4":
            old_word = input("Enter the word to find: ")
            new_word = input("Enter the new word: ")
            sentence = sentence.replace(old_word, new_word)
            print("Updated sentence:", sentence)

        elif num == "5":
            print("Title case:", sentence.title())

        elif num == "6":
            words = sentence.split()
            print("Split into words:", words)

        elif num == "7":
            words = sentence.lower().split()
            freq = {}
            for word in words:
                freq[word] = freq.get(word, 0) + 1
            print("Word frequency counter:", freq)

        elif num == "8":
            print("Swap case:", sentence.swapcase())

        elif num == "9":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice, try again.")