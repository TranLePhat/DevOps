# Bash Scripting Fundamentals

## Objective

Learn the fundamentals of Bash scripting and understand how shell scripts can be used to automate tasks in Linux environments.

---
## Topics Covered

### 1. Bash Script Structure

Learned the basic structure of a Bash script:

* Script files use the `.sh` extension.
* Scripts should start with a shebang:

```bash
#!/bin/bash
```

* Scripts require execute permission before running:

```bash
chmod u+x script.sh
```

---
### 2. Script Ownership and Permissions

Learned how to restrict script modification by other users.

Example:

```bash
cp script.sh /usr/local/bin
chown root /usr/local/bin/script.sh
chgrp root /usr/local/bin/script.sh
chmod u=rwx,go=rx /usr/local/bin/script.sh
```

Result:

* Root has full control.
* Other users can only read and execute the script.

---
### 3. Variables

Studied different types of variables:

#### System Variables

Managed by Linux and typically written in uppercase.

Examples:

```bash
HOME
PATH
BASH
USER
```

#### User Variables

Created and managed by users.

Examples:

```bash
name="Jayz"
age=22
```

#### Variable Naming Rules

* Must start with a letter or underscore.
* No spaces around `=`.
* Case-sensitive.
* Null variables can be declared as:

```bash
var=""
```

or

```bash
var=
```

* Avoid special characters such as `?` and `*`.

---
### 4. Output with Echo

Learned how to display text and variables.

Examples:

```bash
echo "Hello World"
echo $name
```

Common options:

```bash
echo -n
echo -e
```

Escape sequences:

```text
\n  New line
\t  Tab
\\  Backslash
\r  Carriage return
\a  Alert
\b  Backspace
```

---
### 5. User Input with Read

Learned how to accept user input.

Example:

```bash
read username
echo $username
```

---
### 6. Arithmetic Operations

Studied multiple methods for performing calculations.

Using expr:

```bash
expr 5 + 2
expr $a + $b
```

Using let:

```bash
let "z=z+3"
```

Using arithmetic expansion:

```bash
z=$((z+3))
z=$(($a*$b))
```

---
### 7. Exit Status

Learned how Linux commands return status codes.

Example:

```bash
echo $?
```

Common values:

```text
0  Success
1  Error
```

---
### 8. String and Numeric Comparisons

#### String Comparisons

```bash
=
!=
-n
-z
```

Examples:

```bash
[ "$a" = "$b" ]
[ -n "$name" ]
[ -z "$name" ]
```
#### Numeric Comparisons

```bash
-eq
-ne
-gt
-ge
-lt
-le
```

Examples:

```bash
[ $a -gt $b ]
[ $a -eq $b ]
```

---
### 9. Conditional Statements

#### Simple If

```bash
if condition
then
    commands
fi
```
#### If Else

```bash
if condition
then
    commands
else
    commands
fi
```
#### If Elif Else

```bash
if condition1
then
    commands
elif condition2
then
    commands
else
    commands
fi
```

---
### 10. Case Statement

Learned how to handle multiple conditions using case.

Example:

```bash
case $option in
    start)
        ;;
    stop)
        ;;
    *)
        ;;
esac
```

---
### 11. Loops

#### For Loop

```bash
for item in value1 value2 value3
do
    commands
done
```
#### While Loop

```bash
while condition
do
    commands
done
```
#### Until Loop

```bash
until condition
do
    commands
done
```

---
### 12. Functions

Learned how to organize reusable code using functions.

Example:

```bash
greeting() {
    echo "Hello"
}
```

Benefits:

* Code reuse
* Better readability
* Easier maintenance

---
