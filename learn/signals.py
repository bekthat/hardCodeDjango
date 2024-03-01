from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Count
from .models import Access, Group


@receiver(post_save, sender=Access)
def distribute_user_to_group(sender, instance, created, **kwargs):
    if created:
        distribute_to_group(instance)


def distribute_to_group(access):
    product = access.product
    user = access.user

    groups = Group.objects.filter(product=product).annotate(users_count=Count('users')).order_by('users_count')
    for group in groups:
        if group.users.count() < group.max_users:
            group.users.add(user)
            return
