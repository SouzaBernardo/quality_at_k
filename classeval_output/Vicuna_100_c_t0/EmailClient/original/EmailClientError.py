To complete the class EmailClient in the following code, you need to implement the following functions:

* send\_to()
* fetch()
* is\_full\_with\_one\_more\_email()
* get\_occupied\_size()
* clear\_inbox()

You can start by implementing the send\_to() function, which sends an email to the given email address. The function takes three arguments: the email address of the receiver, the content of the email, and the size of the email. The function returns True if the email is sent successfully, and False if the receiver's email box is full.

Next, implement the fetch() function, which retrieves the first unread email in the email box and marks it as read.

After that, implement the is\_full\_with\_one\_more\_email() function, which determines whether the email box is full after adding an email of the given size.

Finally, implement the get\_occupied\_size() function, which gets the total size of the emails in the email box.

Finally, implement the clear\_inbox() function, which clears the email box by deleting the oldest emails until the email box has enough space to accommodate the given size.