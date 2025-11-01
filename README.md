# Is-Anagram
Checks to see if it's an anagram

<h1>Overview</h1>
The is_anagram() function checks whether two given words are anagrams of each other.
An anagram means both words contain the same letters in any order and with the same frequency.

This implementation works by converting one word into a list of its letters, then removing matching letters from that list based on the second word.

<h2>How it works</h2>
How It Works
<ul>
<li>wordList is initialized as an empty list.</li>
<li>Each letter from word2 is added into wordList.</li>
<li>The function loops through each letter in word1:</li>
    If the letter exists in wordList, it is removed.
    If it doesn’t exist, an exception is caught, "caught exception" is printed, and the function returns False immediately.
<li>After the loop, if wordList is empty, the words are anagrams; otherwise, they are not.</li>
</ul>

<h3>Example</h3>

<h3>Output</h3>
