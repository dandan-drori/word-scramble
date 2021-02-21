#!/usr/bin/env python3
import sys
import random
import time

# main function


def read_mode(start):
    input("\nPress 'Enter' when you have finished reading.\n")
    end = time.time()
    print("Time: " + str(round(end-start, 2)) + " seconds")
    return "Time: " + str(round(end-start, 2)) + " seconds\n"


def type_mode(unscrambled_words, start):
    text = str(input("\nType the text that appears on the screen as words:\n"))
    count = 0
    for index in range(len(text)):
        if unscrambled_words[index] == text[index]:
            count += 1
    percentage = (count/len(unscrambled_words))*100
    print("Accuracy: " + str(round(percentage, 2)) + "%")
    end = time.time()
    print("Time: " + str(round(end-start, 2)) + " seconds")
    return "Accuracy: " + str(round(percentage, 2)) + "%, " + "Time: " + str(round(end-start, 2)) + " seconds\n"


def main():
    print("This program consists of two game modes:\n\t"
          "1. Read scrambled text as fast as you can.\n\t"
          "2. Read scrambled text and type it unscrambled as fast and as accurate as you can.\n")
    game_mode = input("Choose a game mode:\n\t"
                      "1. Read\n\t"
                      "2. Read and type\n")

    file = open(sys.argv[1], 'r')
    # ignore spaces after each line
    lines = (line.rstrip() for line in file)
    # ignore empty lines
    lines = list(line for line in file if line)
    punctuations = (".", ",", "!", "?", ":", ";", "'")
    unscrambled_words = ""
    new_lines = ""
    for line in lines:
        line_words_list = line.strip().split(" ")
        new_line = ""
        for word in line_words_list:
            new_word = ""
            unscrambled_words += (word + " ")
            if len(word) > 3:
                if word.endswith(punctuations):
                    word1 = word[1:-2]
                    word1 = random.sample(word1, len(word1))
                    word1.insert(0, word[0])
                    word1.append(word[-2])
                    word1.append(word[-1])
                else:
                    word1 = word[1:-1]
                    word1 = random.sample(word1, len(word1))
                    word1.insert(0, word[0])
                    word1.append(word[-1])
                new_word += ''.join(word1) + " "
            else:
                new_word += word + " "
            new_line += new_word
        new_lines += new_line + "\n"
    print(new_lines.rstrip())
    start = time.time()
    file.close()
    results = ""
    if game_mode == '1':
        results += read_mode(start)
    if game_mode == '2':
        results += type_mode(unscrambled_words, start)
    with open(sys.argv[2], 'a') as out_file:
        out_file.write(results)


if __name__ == "__main__":
    main()
