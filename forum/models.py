from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from operator import attrgetter
from django import forms

class AddPostForm(forms.Form):
  body = forms.CharField(max_length=50, widget=forms.Textarea)

class Forum(models.Model):
  title = models.CharField(max_length=100)

  def __unicode__(self):
    return self.title
    
  def num_topics(self):
    return len(self.topic_set.all())
  
  def num_posts(self):
    return sum([t.num_posts() for t in self.topic_set.all()])
    
  def get_last_post(self):
    p = [y[0] for y in [x.post_set.all().order_by('-created') for x in self.topic_set.all()] if y]
    if not p: return None
    p.sort(key=attrgetter('created'), reverse=True)
    return p[0]
      
class Topic(models.Model):
  title = models.CharField(max_length=100)
  forum = models.ForeignKey(Forum)
  created = models.DateTimeField(auto_now_add=True)
  creator = models.ForeignKey(User)

  def __unicode__(self):
    return u"%s - %s (%s - %s)" % (self.forum, self.title, self.creator, self.created)
    
  def num_posts(self):
    return self.post_set.count()
    
  def get_last_post(self):
    if self.post_set.count():
      return self.post_set.latest('created')

class Post(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  creator = models.ForeignKey(User)
  topic = models.ForeignKey(Topic)
  body = models.TextField(max_length=1000)

  def short(self):
    return self.body[0:60]
  short.short_description = "Short Body"

  def __unicode__(self):
    return u"%s %s (%s - %s)" % (self.topic, self.short(), self.creator, self.created)    
    
class PostInline(admin.TabularInline):
  model = Post

class TopicInline(admin.TabularInline):
  model = Topic

class ForumAdmin(admin.ModelAdmin):
  inlines = [TopicInline,]

class TopicAdmin(admin.ModelAdmin):
  list_display = ["title", "forum", "creator", "created"]
  list_filter = ["title", "forum", "creator", "created"]
  inlines = [PostInline,]

class PostAdmin(admin.ModelAdmin):
  search_fields = ["body", "creator"]
  list_display = ["short", "topic", "creator", "created"]

admin.site.register(Forum, ForumAdmin)
admin.site.register(Topic, TopicAdmin)

  
def add_post(request, topic_id):
  print 'add_post'
  form = AddPostForm(request.POST)
  if not form.is_valid(): return form
  else:
    topic = Topic.objects.get(pk=topic_id)
    p = Post(creator=request.user, topic=topic, body=request.POST['body'])
    p.save()
