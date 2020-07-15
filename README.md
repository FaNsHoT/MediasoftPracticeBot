# Write to table bot (W2T_Bot)
------------
Version 0.1.4

### About bot

This project is the final assignment of Python courses.
This bot is designed to record customers in a table and then called by their employee

In order to start working with the bot, you need to send him a command / start and follow his instructions

### Functional

This bot supports the following commands:
  + /start - bot start
  + /help - help in the work of the bot
  + /add - add new user
    + /addme - command for command to write user
  + /del - delete user from list
    + /delme - /addme - command for command to write user
    

The bot works according to the following principle:

When adding a user, it will enter data into a text file "datatable"

When a user is deleted, the bot sends the message "this user has unsubscribed" to a text file "deltable"
    
### About version

This version of the bot is a prototype designed to learn the basics of the python programming language and work with telegram bots.

In this project, the functionality is quite small, but it is planned to finalize the bot in the next versions
