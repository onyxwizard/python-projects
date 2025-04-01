# 🔄 Palindrome Checker 🔄

  

Welcome to the **Palindrome Checker**! This interactive Python program allows you to check whether a given string or integer is a palindrome. A palindrome is a sequence that reads the same backward as forward, such as "radar" or `121`.

  

---

  

## 🌟 Features

  

- ✅ **String Palindrome Check**: Verify if a string (alphabetic characters only) is a palindrome.

- ✅ **Integer Palindrome Check**: Verify if a positive integer is a palindrome.

- 🔍 **Input Validation**: Ensures valid inputs with clear error messages for invalid entries.

- 💬 **Interactive Interface**: User-friendly prompts guide you through the process.

- 🎨 **Decorative Output**: Clean and visually appealing output with separators.

  

---

  

## 🚀 How to Use

  

### Step 1: Run the Program

Make sure you have Python installed on your system. Then, run the script using the following command:

  

```bash

python  palindrome_checker.py

  ```
  

### Step 2: Follow the Prompts

  

-  **Choose  Input  Type**:

-  Enter  `1`  to  check  a  **string**.

-  Enter  `2`  to  check  an  **integer**.

  
```bash
Example:  Check  Palindrome  for

1:  String

2:  Integer ->
```
  
 
-  **Provide  Input**:

-  For  strings:  Enter  a  word  or  phrase  containing  only  alphabetic  characters (e.g., `radar`,  `level`).

-  For  integers:  Enter  a  positive  integer (e.g., `121`,  `12321`).

  

-  **View  Results**:

The  program  will  inform  you  whether  the  input  is  a  palindrome  or  not.

  
  

---

  

## 🛠️ Code Structure

  

The  program  is  organized  into  the  following  methods:

  

-  **`string_palindrome`**

Checks  if  a  string  is  a  palindrome  using  a  two-pointer  approach.

  

-  **`integer_palindrome`**

Reverses  an  integer  and  checks  if  it  matches  the  original  value.

  

-  **`string_validation`**

Validates  that  the  string  contains  only  alphabetic  characters (`isalpha`).

  

-  **`integer_validation`**

Validates  that  the  integer  is  a  positive  number.

  

-  **`choice_validation`**

Routes  input  validation  based  on  user  choice (string or  integer).

  

-  **`checker`**

Main  method  to  handle  user  interaction  and  display  results.

  

---

  

## 📝 Example Usage

  

### Example 1: String Palindrome

```
======================================

Welcome  to  the  Palindrome  Checker!

Check  Palindrome  for

1:  String

2:  Integer -> 1

Enter  the  string  value -> radar

The  Given  value  is  a  palindrome

  ```
  

### Example 2: Integer Palindrome

```
======================================

Welcome  to  the  Palindrome  Checker!

Check  Palindrome  for

1:  String

2:  Integer -> 2

Enter  the  integer  value -> 121

The  Given  value  is  a  palindrome
```
  
  

---

  

## 🧪 Testing

  

To  ensure  the  program  works  correctly,  test  it  with  the  following  cases:
```
--------------------------------------------------------------
| Input Type | Input       | Expected Output                 |
|------------|-------------|---------------------------------|
| String     | `radar`     | The Given value is a palindrome |
| String     | `hello`     | Not a palindrome                |
| Integer    | `121`       | The Given value is a palindrome |
| Integer    | `123`       | Not a palindrome                |
| Invalid    | `1ab`       | Invalid input (retry prompt)    |
--------------------------------------------------------------
  ```

---

  

## 🌱 Future Enhancements

  

-  🆕  Add  support  for  alphanumeric  strings (e.g., `A man, a plan, a canal: Panama`).

-  🔄  Allow  negative  integers  or  floating-point  numbers  for  palindrome  checks.

-  🎨  Improve  the  user  interface  with  colors  or  a  GUI.

-  📊  Add  unit  tests  for  better  code  reliability.

  

---

  

## 🤝 Contribution

  

Contributions  are  welcome!  If  you  have  ideas  for  improvements  or  find  any  bugs,  feel  free  to  open  an  issue  or  submit  a  pull  request.

  

---

  

## 📄 License

  

This  project  is  licensed  under  the  MIT  License.  See  the [LICENSE](LICENSE) file for details.

  

---

  

🎉  **Happy  Palindrome  Checking!**  🎉
