The GitHub README.md file is an introduction to this repository.

This progressreport.md file is for the purpose of additional documentation to explain
the objective of the tasks involved in certain commits.

Commit 3 extended comment

This is just a demo to use a function based view as index.  Using path instead
of url in urlpatterns[] caused a problem displaying the 'hello world' at both
the root level and the documents level.  the localhost/documents index view
worked easily.  For localhost index view it required the additions to
website/urls.py.
'from documents import views'  and  path('', views.index, name='index'),

