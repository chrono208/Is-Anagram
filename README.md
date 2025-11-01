# Is-Anagram
Checks to see if a word is an anagram

<h1>Overview</h1>
The is_anagram() function checks whether two given words are anagrams of each other.<br>
An anagram means both words contain the same letters in any order and with the same frequency.
<br>
<br>
This implementation works by converting one word into a list of its letters, then removing matching letters from that list based on the second word.

<h2>How it works</h2>
How It Works
<ul>
<li>wordList is initialized as an empty list.</li>
<li>Each letter from word2 is added into wordList.</li>
<li>The function loops through each letter in word1:</li>
    <ul>
        <li>If the letter exists in wordList, it is removed.</li>
        <li>If it doesn’t exist, an exception is caught, "caught exception" is printed, and the function returns False immediately.</li>
    </ul>
<li>After the loop, if wordList is empty, the words are anagrams; otherwise, they are not.</li>
</ul>

<h3>Example</h3>
result = is_anagram("listen", "silent")
print(result)

<h3>Output</h3>
['s', 'i', 'l', 'e', 'n', 't']
0
True


<h3>Example 2</h3>
result = is_anagram("hello", "world")
print(result)
Output:

<h3>Output 2</h3>
['w', 'o', 'r', 'l', 'd']
caught exception
False
