#!/usr/bin/env python
# coding: utf-8

# In[2]:


import smtplib


# In[3]:


smtp_object  = smtplib.SMTP("smtp.gmail.com", 587)


# In[5]:


smtp_object.ehlo()


# In[6]:


smtp_object.starttls()


# In[7]:


import getpass


# In[8]:


password = getpass.getpass("Please input your password: ")


# In[10]:


#yxhquttywtuhbjxa
email = getpass.getpass("Please input your email: ")
password = getpass.getpass("Please input your password: ")
smtp_object.login(email,password)


# In[13]:


from_address = email 
to_address = "bidemielelu05@gmail.com"
subject = input("enter the subject: ")
message = input("enter the message: ")
msg = "Subject: " + subject + "\n" + message 

smtp_object.sendmail(from_address,to_address,msg)


# In[14]:


smtp_object.quit()


# In[15]:


import imaplib


# In[16]:


M = imaplib.IMAP4_SSL("imap.gmail.com")


# In[17]:


import getpass


# In[18]:


#uxvxvifkjjcftday
email = getpass.getpass("Please input your email: ")
password = getpass.getpass("Please input your password: ")


# In[19]:


M.login(email,password)


# In[20]:


M.list()


# In[21]:


M.select("inbox")


# In[24]:


typ, data = M.search(None, "SINCE 09-SEP-2023")


# In[25]:


typ


# In[29]:


data[0]


# In[31]:


result, email_data = M.fetch("30181","(RFC822)")


# In[32]:


email_data


# In[58]:


raw_email = email_data[0][0]


# In[59]:


raw_email_string = raw_email.decode("utf-8")


# In[60]:


import email 


# In[61]:


email_message = email.message_from_string(raw_email_string)


# In[62]:


for part in email_message.walk(): 
    
    if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode=True)
        print(body)


# In[ ]:




