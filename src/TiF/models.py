from django.db import models


# {'ininprogress':'inprogress', 'done':'done', 'canceled':'canceled', 'blocked_by_admin':'blocked_by_admin'}


class User(models.Model):
    username = models.CharField(max_length=128)
    reg_date = models.DateTimeField(auto_now_add=True)
    ban = models.BooleanField()
    can_post_texts = models.BooleanField()
    publicName = models.CharField(max_length=128, null=False)
    contact = models.CharField(max_length=256, null=True)
    about = models.CharField(max_length=512, null=True)

    def __str__(self):
        return self.username


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Mess')
    message_to = models.ForeignKey(User, on_delete=models.PROTECT)
    txt = models.TextField(max_length=1000)
    timeOfCreate = models.DateTimeField(auto_now_add=True)
    timeOfUpadate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author_id)


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Foundation(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Mpaa(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Choice(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Text(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    status = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='status')
    name = models.CharField(max_length=300)
    mpaa = models.ForeignKey(Mpaa, on_delete=models.PROTECT, related_name='mpaa')
    description = models.TextField(max_length=300)
    notes = models.TextField(max_length=300)
    text = models.TextField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    timeOfCreate = models.DateTimeField(auto_now_add=True)
    timeOfUpadate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text_id = models.ForeignKey(Text, on_delete=models.CASCADE, related_name='comment')
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    text = models.TextField(max_length=300)

    def __str__(self):
        return self.text[:30]


class TextDep(models.Model):
    text = models.ForeignKey(Text, on_delete=models.CASCADE, related_name='text_deps')
    found = models.ForeignKey(Foundation, on_delete=models.CASCADE, related_name='text_deps')


class Hashtag(models.Model):
    text = models.ForeignKey(Text, on_delete=models.CASCADE, related_name='tagname')
    tag_name = models.CharField(max_length=100)

    def __str__(self):
        return self.tag_name
