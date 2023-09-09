#! python3
# randomChoreAssignmentEmailer.py - Randomly assigns chores to a list of people (via their email addresses)

import random, smtplib

SENDEREMAIL = 'my_email_address@example.com'
SENDEREMAILPASSWORD = 'email_password'

def choreAssignment(chores, peopleEmails):
    smtpObj = smtplib.SMTP('smtp.example.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(SENDEREMAIL, SENDEREMAILPASSWORD)
    while chores != []:
        randomChore = random.choice(chores)
        chores.remove(randomChore)
        randomPerson = random.choice(peopleEmails)
        sendMailStatus = smtpObj.sendmail(SENDEREMAIL, randomPerson, 'Subject: Chore Assignment\nHi, you have been assigned the %s chore. Thank you in advance for your help! :)\n\n Regards, HobbyMath')
        if sendMailStatus != {}:
            print('There as a problem sending email to %s: %s' % (randomPerson, sendMailStatus))
        else: 
            print('Email sent to %s' % (randomPerson))
    smtpObj.quit()
    print('Assignment finished!')

peopleList = ['person@email.com', 'another_person@email.com', 'person@anotheremail.com', 'another.person@anotheremail.com', 'test.person@test.com']
choresList = ['dishes', 'bathroom', 'vacuum', 'walk dog']

choreAssignment(choresList, peopleList)