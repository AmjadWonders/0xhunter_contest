This is just a simple coding challenge made by @0xhunter on twitter,
the php code used in this challenge is set up for disabling the user from trying to login more than 10 times, however the mechanism that is used by this code is weak and can be
skipped by the script code attached by me as "0x_web.py"

So how does this work?
Well, the php code used simply uses a cookie based verification system which needs a key code called as "PHPSSID". Each and everytime a login is attempted. this session id is 
unique to each and every user and it's being copied to the "https://pass4exam.net/challenge/sessid.txt" as a way of logging this attempt.

So, how can you exploit this code?
Simply, just change the cookie file "PHPSSID" to any kind of value, you will be recognised as a new computer and you wont be blocked from more than 10 attempts.
Rather then that, you can just renew the session by re-identifying the variable which is much more clean I would say, thats what I did in my attached script.