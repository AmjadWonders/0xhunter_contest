This is just a simple Web Exploit challenge made by @0xhunter on twitter (challenge link: https://pass4exam.net/challenge/, twitter link: https://cutt.ly/km5iqSs).

The php code used in this challenge is set up for disabling the user from trying to login more than 10 times, however the mechanism that is used by this code is weak and can be
skipped by the script code attached by me as "0x_web.py"

So how does this work?
Well, the php code used simply uses a cookie based verification system which needs a key code called as "PHPSSID". Each and everytime a login is attempted. this session id is 
unique to each and every user and it's being copied to the "https://pass4exam.net/challenge/sessid.txt" as a way of logging this attempt.

So, how can you exploit this code?
Simply, just change the cookie file "PHPSSID" to any kind of value, you will be recognised as a new computer and you wont be blocked from more than 10 attempts.
Rather then that, you can just renew the session by re-identifying the variable which is much more clean I would say, thats what I did in my attached script.

This image shows the most important part for skipping this attempt-block, which is about renewing the session after this function (check) is run by the counter for-loop.

![alt text](https://github.com/amjad-developer/0xhunter_contest/blob/main/code_imp_part.png)
