import os
os.environ["DJANGO_SETTINGS_MODULE"] = "bloggy.settings"
from blog.models import Post

the_title = "What Am I Good At"
the_content = "What am I good at? What is my talent? What makes me stand out?  \
These are the questions we ask ourselves over and over again and somehow can not \
seem to come up with the perfect answer. This is because we are blinded, we are \
blinded by our own bias on who we are and what we should be. But discovering the \
answers to these questions is crucial in branding yourself. You need to know what \
your strengths are in order to build upon them and make them better"
p = Post(title=the_title, content=the_content)
p.save()
the_title = "Charting Best Practices"
the_content = "Charting data and determining business progress is an \
important part of measuring success.  From recording financial statistics \
to webpage visitor tracking, finding the best practices for charting your \
data is vastly important for your company's success. Here is a look at five \
charting best practices for optimal data visualization and analysis."
p = Post(title=the_title, content=the_content)
p.save()
the_title = "Understand Your Support System Better With Sentiment Analysis"
the_content = "There's more to evaluating success than monitoring your bottom \
line. While analyzing your support system on a macro level helps to ensure your \
costs are going down and earnings are rising, taking a micro approach to your \
business gives you a thorough appreciation of your business's performance. \
Sentiment analysis helps you to clearly see whether your business practices \
are leading to higher customer satisfaction, or if you're on the verge of \
running clients away"
p = Post(title=the_title, content=the_content)
p.save()

