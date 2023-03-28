from input import*
from Parser import*

text = non_empty_input("Enter the text to analiz: ")
print("Sentence count: ", sentences_count(text))
print("Non declarative sentence count: ", non_declarative_sentences_count(text))
print("Average sentence length: ", average_sentence_length(text))
print("Average word length: ", average_word_length(text))

k = pos_int_input("Enter top size: ")
n = pos_int_input("Enter subsentence length: ")
print("Top subsentence: ", sub_sentences_top(text, k, n))


