# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The first impression was good. The game looked interesting and functional with some helpful buttons that makes the game easy to play.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  The game did not handle negative inputs. 
  The game did not handle out of range inputs.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|-1| Error: Negative numbert. Please enter a positive number | Accepted the input and reduced the number of attempts| "none"|
|101| Error: Number out of range. Attempts left remains the same | Accepted the input and reduced the number of possible attempts |"None" |
|Hola| Error: Invalid input. Please just enter numbers | Accepted the input and reduced the number of attempts| "none"|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
It fixed the parse_guess function.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
None.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
After trying the same incorrect input again and see that it is correctly handled.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I run all of them, and they got passed.
- Did AI help you design or understand any tests? How?
No, not really.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I did not understand what Streamlit and state are.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
Edge cases.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
I am not sure, to be honest.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
AI can have errors.