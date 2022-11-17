# mailertesttask
test task for mailganer 
<h1>Starting application<h1>
<h3>
python3 manage.py runserver
  
redis-server
    
python3 -m celery -A mailertesttask worker 
</h3>
<h1> Main page </h1>
http://localhost:8000/mails/inbox 
<h2> Registrated admin user </h2>
login - admin@admin.ru

pass - 123
<h2> Some info</h2>
All required modules are mentioned in requirements.txt (Celery, Django, Redis)
There are some messages from demonica@mail.ru to admin.
If mail in inbox or sent list has grey background it is unread.
Each mail is clickable and redirects to it's detail page.
You can compose a mail to any existing user in data base, multiselect at compose page in receiver field (holding ctrl).
Also, you can pass time delay (in seconds) to send mail later.
If you look at mail, where you are receiver, the mail will be marked as read.
