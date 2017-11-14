# Password Strength Calculator

Result takes values from 1.0 (very weak) to 10.0 (very strong).

## Factors
Script takes into account such factors:
  * length of password
  * usage of uppercase symbols
  * usage of lowercase symbols
  * usage of digits
  * usage of punctuation symbols
  * usage of popular unsafe passwords
  * usage of names, surname and english words

## Algorithm
Evaluates password strength by the next algorithm (1-very weak, 10-max strength)
1. strength = 10 (maximum)
2. strength *= length(password) / 12
3. strength *= ( 1/4 if uppercase symbols found  
+1/4 if lowercase symbols found  
 +1/4 if digits found  
 +1/4 if punctuation symbols found )
4. strength *= 0.75 if names used (searching in './blacklist/names.txt')
5. strength *= 0.75 if surnames used (searching in './blacklist/surnames.txt')
6. strength *= 0.75 if english words used (searching in './blacklist/names.txt')
7. strength = 1 if password in the blacklist (searching in './blacklist/popular10000pass.txt')

## How to use (Unix terminal)
```
$ python password_strength.py 
Type the password to evaluate: ********
-25% PENALTY: uppercase symbols not found!!!
-8% PENALTY: minimum 12 charecters length recommended.
-25% PENALTY: password shouldn't contain english words
The strength of the password: 5.2
```

## Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
