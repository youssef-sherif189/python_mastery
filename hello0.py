{
 "cells": [],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.15.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}


first_name = input("enter your first name; ")
last_name = input("enter your last name; ")
birth_year = input("enter your birth year; ")
age = 2026 - int(birth_year)
job = input("enter your job; ")
print(f"Hello, {first_name} {last_name} \n"
f"You are {age} years old\n"
f"and work as a {job}.")


hello = input("enter  your name: ").strip().title()
email = input("enter your email; ").strip().lower()
age = input("enter your age; ").strip()

print("\n" +"=" * 30)
print("  USER PROFILE REPORT  ")
print("=" * 30)
print(f"Name: {hello}")
print(f"Email: {email}")
print(f"Age: {age}")
print("=" * 30)

