from forum.models import Forum, Topic, Post, AddPostForm, add_post
from django.shortcuts import render
from django.core.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage

# Display every forum
def index(request):
  f = Forum.objects.all().order_by('title')
  return render(request, 'forum/forum.html', dict(forums=f))
  
def topic_detail(request, forum_id, topic_id):
  topic = Topic.objects.get(pk=topic_id)
  if not topic: return render(request, 'forum/topic_not_found.html')
  if request.method == 'POST': form = add_post(request, topic_id)
  else: form = AddPostForm
  posts = make_paginator(request, Post.objects.filter(topic=topic_id).order_by("created"))
  return render(request, 'forum/topic_detail.html', {'posts':posts, 'topic':topic, 'form':form})
  
def forum_detail(request, forum_id):
  forum = Forum.objects.get(pk=forum_id)
  if not forum: return render(request, 'forum/forum_not_found.html')
  topics = make_paginator(request, Topic.objects.filter(forum=forum_id))
  return render(request, 'forum/forum_detail.html', {'topics': topics, 'forum': forum})

def make_paginator(request, items):
  paginator = Paginator(items, 25)
  page = request.GET.get('page')
  try: items = paginator.page(page)
  except PageNotAnInteger: items = paginator.page(1)
  except TypeError: items = paginator.page(1)
  except EmptyPage: items = paginator.page(paginator.num_pages)
  return items
