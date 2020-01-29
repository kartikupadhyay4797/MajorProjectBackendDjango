from rest_framework import viewsets
from .serializers import dealerInfoSerialiser
from .models import dealerInfoTable
import smtplib
import os
class DealerViewSet(viewsets.ModelViewSet):
    queryset = dealerInfoTable.objects.all().order_by('-date_created')
    serializer_class = dealerInfoSerialiser

    def perform_create(self, serializer):
        response=super(DealerViewSet, self).perform_create(serializer)
        #data=self.request.data
        data=serializer.data
        email=data['email']
        password=data['password']
        subject="Water On Click!"
        text="Welcome to Water On Click, \nWe hope you're doing well, you can use following password to login.\nHowever you can change this later after logging in and by navigating to 'my profile' option in our app.\nYour password to login: "
        # here may be placed additional operations for
        # extracting id of the object and using reverse()
        message='Subject: {0}\n\n{1}'.format(subject, text+str(password))
        smtp_server="smtp.gmail.com"
        port=587  # For starttls
        sender_email=os.environ['emailid']
        sender_password=os.environ['emailpass']

        # Create a secure SSL context
        # context = ssl.create_default_context()

        # Try to log in to server and send email
        try:
            server=smtplib.SMTP(smtp_server, port)
            # server.ehlo() # Can be omitted
            server.starttls()  # Secure the connection
            # server.ehlo() # Can be omitted
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, message)
        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            server.quit()
        # here may be placed additional operations for
        # extracting id of the object and using reverse()
        return response
