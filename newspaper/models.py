from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=25)


    def __str__(self):
        return self.name



class Subcategory(models.Model):
    name = models.CharField(max_length=25)
    category = models.ForeignKey(Category, 
        on_delete=models.CASCADE, related_name='subcategories')


    def __str__(self):
        return self.name



class Article(models.Model):
    thumbnail = models.ImageField(upload_to='%Y/%m/%d/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, 'articles')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, 'articles')
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField()


    def __str__(self):
        return f'{self.title} by {self.author}'



class ArticleVote(models.Model):
    article = models.OneToOneField(Article, models.CASCADE, 'votes')
    

    def __str__(self):
        return article.name + ' votes'


    def get_upvotes_count(self):
        return self.upvotes.count()


    def get_downvotes_count(self):
        return self.downvotes.count()



class ArticleUpvote(models.Model):
    vote = models.ForeignKey(ArticleVote, 
        on_delete=models.CASCADE, 'upvotes')
    user = models.ForeignKey(User, models.CASCADE, 'upvotes')


    def __str__(self):
        return vote.article.name + ' upvote by ' + user.username



class ArticleDownvote(models.Model):
    vote = models.ForeignKey(ArticleVote, 
        on_delete=models.CASCADE, 'downvotes')
    user = models.ForeignKey(User, models.CASCADE, 'downvotes')


    def __str__(self):
        return vote.article.name + ' downvote by ' + user.username



class Comment(models.Model):
    user = models.ForeignKey(User, 
        on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, 
        on_delete=models.CASCADE, related_name='comments')


    def __str__(self):
        return f'Comment {self.pk} for article {self.article.name}'



class Reply(models.Model):
    user = models.ForeignKey(User, 
        on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Article, 
        on_delete=models.CASCADE, related_name='replies')


    def __str__(self):
        return f'Reply {self.pk} for article {self.comment.article.name}'