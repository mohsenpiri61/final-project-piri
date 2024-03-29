from django.contrib.sitemaps import Sitemap
from blog.models import Post
from django.utils import timezone
from django.urls import reverse


class BlogSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(published_date__lt=timezone.now(), status=True)

    def lastmod(self, obj):
        return obj.published_date
"""
    def location(self, item):
        return reverse('blog_show:single_blog', kwargs={'pid': item.id})
"""