Django-Frontdesk
================

Description
-----------

Django-Frontdesk is a project to create an easy-to-use desk diary and scheduling tool for use in a fast-paced retail environment. The aim is to be able to schedule and manage client bookings with available resources as quickly and easily as possible with no fuss.

Design Considerations
---------------------

Ease of use is paramount, because it is intended the application will be used by people unversed in software. Use of the app needs to be simple and intuitive.

Web deployment was decided upon at an early stage, because this enables use of the app from more than one location. The web server may be local or on the internet. One use case I had in mind was being able to check/modify the diary when at home, as well as at work.

The decision for web deployment, coupled with a preference for Python as the main language, led naturally to using Django as the framework. This also gives flexibility of choice for the database engine, as the Django settings will automatically take care of that, provided appropriate Python drivers are installed.

Django-Calendarium was chosen as the calendar/diary engine after some consideration of the options available. Calendarium is flexible enough not to need adaptation of its data models, as hooks to external data models are built in.
