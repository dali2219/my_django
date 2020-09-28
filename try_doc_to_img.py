# docx to image
import  win32com.client as win32
import pyautogui
import time
import win32gui, os

docfile = os.path.abspath("C:/Users/User/Programming/python/scripts/pdfs/test.docx")
shotfile = os.path.abspath("C:/Users/User/Programming/python/scripts/pdfs/shot.png")

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
    
word = win32.gencache.EnsureDispatch('Word.Application')
word.Visible = True
word.WindowState = 1  # maximize

top_windows = []
win32gui.EnumWindows(windowEnumerationHandler, top_windows)

for i in top_windows:  # all open apps
   if "word" in i[1].lower(): # find word (assume only one)
       try:
          win32gui.ShowWindow(i[0],5)
          win32gui.SetForegroundWindow(i[0])  # bring to front
          break
       except:
          pass
    
doc = word.Documents.Add(docfile) # open file

time.sleep(2)  # wait for doc to load

myScreenshot = pyautogui.screenshot() # take screenshot
myScreenshot.save(shotfile) # save screenshot


# close doc and word app
doc.Close()
word.Application.Quit()


# pdf to image

import fitz, os

pdffile = os.path.abspath("C:/Users/User/Programming/python/scripts/pdfs/test.pdf")
doc = fitz.open(pdffile)
page = doc.loadPage(0)  # number of page
pix = page.getPixmap()
output = "outfile.png"
pix.writePNG(output)

# handle showing image
# add type to edit button and class disableclick

# urls.py
path('', about,name="index"),
path('/<int:id>', about,name="index"),
# views.py
def about(request,id_1=1):
    id_1= request.GET.get("id",False)
    print(id_1)
    form = PersonForm()
    if id_1 is False:
        id_1 = 1
    can = Person.objects.get(id=id_1)
    table = PersonTable(Person.objects.all())
    editForm = PersonForm(instance=can)
    # editForm.save()
    return render(request,'index.html',{"table":table,"form":form,"can":can,"editform":editForm})



# pip install pywin32 win32gui win32core pyautogui fitz PyMuPDF mod_wsgi

######################## deploy
# 1. download wamp
# 2. download from microsoft https://www.microsoft.com/en-sg/download/confirmation.aspx?id=30679
# 2. set "MOD_WSGI_APACHE_ROOTDIR=c:\wamp64\bin\apache\apache2.4.46" 
# 3. find out where server with mod_wsgi-express module-config
# 4. set DEBUD=False and ALLOWED_HOSTS = ["127.0.0.1","localhost","192.168.0.6"]


############################################################################################################3
############################################################################################################3
########################################   FROM YOUTUBE #######################################3
############################################################################################################3
############################################################################################################3
############################################################################################################3

# https://www.youtube.com/watch?v=F6-yJpPEpoE

# Simply host and run django website on WAMP apache server

# In this video i will show you how you can run your django websites on wamp apache server.
# I am using Windows 10, Python 3.6, Django 1.11 and WAMP 3.1.0

# #To install mod_wsgi
# set "MOD_WSGI_APACHE_ROOTDIR=C:\wamp64\bin\apache\apache2.4.27"
# pip install mod_wsgi==4.5.20

# # To check Paths
# mod_wsgi-express module-config
# add to wsgi.py
# sys.path.append('C:/Users/User/AppData/Roaming/Python/Python36/site-packages')


# # Apache httpd-vhosts.conf settings 

Require all granted
Require ip 192.168.0


# # Apache httpd.conf settings 


#Listen 12.34.56.78:80
Listen 192.168.0.6:80
# ServerName gives the name and port that the server uses to identify itself.
# This can often be determined automatically, but we recommend you specify
# it explicitly to prevent problems during startup.
#
# If your host doesn't have a registered DNS name, enter its IP address here.
#
ServerName 192.168.0.6:80

#
LoadModule wsgi_module "c:/program files/python36/lib/site-packages/mod_wsgi/server/mod_wsgi.cp36-win_amd64.pyd"
WSGIScriptAlias / "C:/Users/User/Programming/python/django_projects/tiny_tables/tiny_tables/wsgi.py"

WSGIPythonHome "C:/Program Files/Python36"
WSGIPythonPath "C:/Users/User/Programming/python/django_projects/tiny_tables"

Alias /media/ C:/Users/User/Programming/python/django_projects/tiny_tables/media/
Alias /static/ C:/Users/User/Programming/python/django_projects/tiny_tables/static/

<Directory C:/Users/User/Programming/python/django_projects/tiny_tables/media>
    Require all granted
</Directory>

<Directory C:/Users/User/Programming/python/django_projects/tiny_tables/static>
    Require all granted
</Directory>

<Directory C:/Users/User/Programming/python/django_projects/tiny_tables>
    <Files wsgi.py>
        Require all granted
    </Files>
</Directory>

# doc to pdf
from win32com.client import dispatch, constants, gencache
def doc2pdf (input, output):
  w=dispatch ("word.application")
  try:
    #open a file
    doc=w.documents.open (input, readonly=1)
    #Convert files
    doc.exportasfixedformat (output, constants.wdexportformatpdf,                item=constants.wdexportdocumentwithmarkup, createbookmarks=constants.wdexportcreateheadingbookmarks)
    return true
  except:
    return false
  finally:
    w.quit (constants.wddonotsavechanges)
def generatesupport ():
  gencache.ensuremodule ("{00020905-0000-0000-c000-000000000046}", 0, 8, 4)
def main ():
  input=r "xxx \ xxx.docx"
  output=r "xxx \ xxx.pdf"
  #generatesupport ()
  rc=doc2pdf (input, output)
  if rc:
    print ("Successfully converted")
  else:
    print ("Conversion failed")










# render table

    					{% load i18n %}
					{% block table-wrapper %}
					<div class="ui container table-container">
						{% block table %}
						<table {% render_attrs table.attrs class="ui celled table" %}>
							{% block table.thead %}
							{% if table.show_header %}
							<thead {{ table.attrs.thead.as_html }}>
								<tr>
									{% for column in table.columns %}
									<th {{ column.attrs.th.as_html }}>
										{% if column.orderable %}
										<a
											href="{% querystring table.prefixed_order_by_field=column.order_by_alias.next %}">{{ column.header }}</a>
										{% else %}
										{{ column.header }}
										{% endif %}
									</th>
									{% endfor %}
								</tr>
							</thead>
							{% endif %}
							{% endblock table.thead %}
							{% block table.tbody %}
							<tbody {{ table.attrs.tbody.as_html }}>
								{% for row in table.paginated_rows %}
								{% block table.tbody.row %}
								<tr {{ row.attrs.as_html }}>
									{% for column, cell in row.items %}
									<td {{ column.attrs.td.as_html }}>
										{% if column.localize == None %}{{ cell }}{% else %}{% if column.localize %}{{ cell|localize }}{% else %}{{ cell|unlocalize }}{% endif %}{% endif %}
									</td>
									{% endfor %}
								</tr>
								{% endblock table.tbody.row %}
								{% empty %}
								{% if table.empty_text %}
								{% block table.tbody.empty_text %}
								<tr>
									<td colspan="{{ table.columns|length }}">{{ table.empty_text }}</td>
								</tr>
								{% endblock table.tbody.empty_text %}
								{% endif %}
								{% endfor %}
							</tbody>
							{% endblock table.tbody %}
							{% block table.tfoot %}
							<tfoot {{ table.attrs.tfoot.as_html }}>
								{% if table.has_footer %}
								<tr>
									{% for column in table.columns %}
									<td {{ column.attrs.tf.as_html }}>{{ column.footer }}</td>
									{% endfor %}
								</tr>
								{% endif %}
								{% block pagination %}
								{% if table.page and table.paginator.num_pages > 1 %}
								<tr>
									<th colspan="{{ table.columns|length }}">
										<div class="ui right floated pagination menu">
											{% if table.page.has_previous %}
											{% block pagination.previous %}
											<a href="{% querystring table.prefixed_page_field=table.page.previous_page_number %}"
												class="icon item">
												<i class="left chevron icon"></i>
											</a>
											{% endblock pagination.previous %}
											{% endif %}

											{% if table.page.has_previous or table.page.has_next %}
											{% block pagination.range %}
											{% for p in table.page|table_page_range:table.paginator %}
											{% if p == '...' %}
											<a href="#" class="item">{{ p }}</a>
											{% else %}
											<a href="{% querystring table.prefixed_page_field=p %}"
												class="item {% if p == table.page.number %}active{% endif %}">
												{{ p }}
											</a>
											{% endif %}
											{% endfor %}
											{% endblock pagination.range %}
											{% endif %}

											{% if table.page.has_next %}
											{% block pagination.next %}
											<a href="{% querystring table.prefixed_page_field=table.page.next_page_number %}"
												class="icon item">
												<i class="right chevron icon"></i>
											</a>
											{% endblock pagination.next %}
											{% endif %}
										</div>
									</th>
								</tr>
								{% endif %}
								{% endblock pagination %}
							</tfoot>
							{% endblock table.tfoot %}
						</table>
						{% endblock table %}
					</div>
					{% endblock table-wrapper %}
				</div>