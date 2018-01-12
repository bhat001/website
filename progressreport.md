The GitHub README.md file is an introduction to this repository.

This progressreport.md file is for the purpose of additional documentation to explain the objective of the tasks involved in certain commits.

Commit comment

This is just a demo to use a function based view as index.  Using path instead
of url in urlpatterns[] caused a problem displaying the 'hello world' at both
the root level and the documents level.  the localhost/documents index view
worked easily.  For localhost index view it required the additions to
website/urls.py.
'from documents import views'  and  path('', views.index, name='index'),

Pre Commit comment
issue: favicon.ico did not show in browser tab.  Fixed by creating GIMP .xcf
file and exporting as Microsoft ico.  Image modified to 48x48 (no large format options selected on export).  Favicon then appeared in browser tab.

issue or lack of understanding:  Following other tutorials, created folder
documents/templates/documents and html file gave 404 error.  Django 2.0 seems to
work differently?  Moved html file to documents/templates and it worked ok.

Changes for next commit:
added base.html, home.html and documents.html for main pages.  No database or
menu yet.  Just working on displaying all urls and associated templates.
Including static folders.
