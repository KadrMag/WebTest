from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('published_data', 'user')


form = PostForm()
print(form)
