import os
os.environ["DJANGO_SETTINGS_MODULE"] = "bloggy.settings"
from blog.models import Post

the_title = "Test of apostrophes"
the_content = "Using single quotes for words like you\'re and there\'s is easy."
p = Post(title=the_title, content=the_content)
p.save()
