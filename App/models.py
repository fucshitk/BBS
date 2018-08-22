from datetime import datetime
from django.db import models

# Create your models here.
from DjangoUeditor.models import UEditorField


class User(models.Model):
    uname = models.CharField(verbose_name='姓名',max_length=20,unique=True)
    upwd = models.CharField(verbose_name='密码',max_length=255)
    uicon = models.ImageField(verbose_name='头像',upload_to='uicon/',null=True, blank=True,default='uicon/default.jpg')
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女"),('unkown',u'未知')), default="unkown", verbose_name="性别")
    signature = UEditorField(verbose_name='个性签名',default='暂无个性签名')
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    bgimg = models.ImageField(verbose_name='主页背景图片',upload_to='bgimg/',null=True,blank=True,default='bgimg/welcome.gif')


    class Meta:
        db_table = 'user'


        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.uname


class TextType(models.Model):
    name = models.CharField(verbose_name='类型名',max_length=10,null=True,blank=True)

    class Meta:
        db_table = 'TextType'
        verbose_name = '文章类别'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(verbose_name='标题',max_length=100,default='标题不能为空')
    content = UEditorField(u"文章正文", height=300, width=1000, default=u'', blank=True, imagePath="uploads/blog/images/",
                           toolbars='besttome', filePath='uploads/blog/files/')
    A_type = models.ForeignKey(TextType,verbose_name='类别',null=True,blank=True,on_delete=models.CASCADE)
    add_time = models.DateTimeField(verbose_name='发表时间',default=datetime.now)
    author = models.ForeignKey(User,verbose_name='发表者',null=True,blank=True,on_delete=models.CASCADE)


    class Meta:
        db_table = 'Article'
        ordering = ['-add_time']
        verbose_name = '文章'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return

class Comment(models.Model):
    belong_art = models.ForeignKey(Article,verbose_name='被评论的文章',on_delete=models.CASCADE)
    belong_user = models.ForeignKey(User,verbose_name='评论者',on_delete=models.CASCADE)
    # to_user = models.ForeignKey(User,verbose_name='回复者',null=True,blank=True)
    pinglun = models.CharField(max_length=255,verbose_name='评论',null=True)
    add_time = models.DateTimeField(default=datetime.now(),verbose_name='评论的时间')


    class Meta:
        db_table = 'Comment'
        verbose_name = '评论'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.pinglun

class Poll(models.Model):
    ip = models.CharField(max_length=100, null=True, blank=True)
    art = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.art)

class Likes(models.Model):
    like_num = models.IntegerField(verbose_name='点赞数',null=True,blank=True,default=0)
    art = models.ForeignKey(Article,verbose_name='被赞文章',on_delete=models.CASCADE)
    author = models.ForeignKey(User,verbose_name='点赞用户',on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True,verbose_name='点赞时间')


    def __str__(self):
        return self.like_num

class Message(models.Model):
    name = models.CharField(verbose_name="留言者姓名",max_length=20,null=True,blank=True,default='-_-')
    email = models.CharField(verbose_name='留言者邮箱',max_length=30,null=True,blank=True,default='-_-')
    massage = UEditorField(verbose_name = '留言',null=True,blank='-_-')
    add_time = models.DateTimeField(verbose_name='留言时间',auto_now_add=True)

    class Meta:
        db_table = 'Message'
        verbose_name = '留言'
        verbose_name_plural = verbose_name
