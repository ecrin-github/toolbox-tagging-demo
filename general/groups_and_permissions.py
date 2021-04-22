import os
import sys

if __name__ == '__main__':
    # Setup environ
    dir_path = '/Users/iproger/Projects/ecrin-mdr/toolbox'
    # dir_path = '/var/www/toolbox'
    sys.path.append(dir_path)
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "toolbox.settings")

    import django
    django.setup()

    from users_management.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType
    from users_management.models import User


    # Groups creation
    admin_group, created = Group.objects.get_or_create(name='Administrators')
    content_managers_group, created = Group.objects.get_or_create(name='Content managers')
    tagging_group, created = Group.objects.get_or_create(name='Tagging group')


    # Content type
    ct = ContentType.objects.get_for_model(User)


    # Create custom permissions
    access_to_categories_permission = Permission.objects.create(codename='access_to_categories', name='Access to the Categories sections', content_type=ct)
    access_to_resources_permission = Permission.objects.create(codename='access_to_resources', name='Access to the Resources sections', content_type=ct)
    access_to_tags_permission = Permission.objects.create(codename='access_to_tags', name='Access to the Tags sections', content_type=ct)
    access_to_users_and_groups_permission = Permission.objects.create(codename='access_to_users_and_groups', name='Access to the Users and Groups sections', content_type=ct)
    access_to_waiting_area_permission = Permission.objects.create(codename='access_to_waiting_area', name='Access to the Waiting area', content_type=ct)
    
    add_categories_permission = Permission.objects.create(codename='add_categories', name='Allows to add new categories parameters', content_type=ct)
    view_categories_permission = Permission.objects.create(codename='view_categories', name='Allows to view categories', content_type=ct)
    edit_categories_permission = Permission.objects.create(codename='edit_categories', name='Allows to edit categories parameters', content_type=ct)
    remove_categories_permission = Permission.objects.create(codename='remove_categories', name='Allows to remove categories parameters', content_type=ct)
    
    add_resources_permission = Permission.objects.create(codename='add_resources', name='Allows to add new resources', content_type=ct)
    view_resources_permission = Permission.objects.create(codename='view_resources', name='Allows to view resources', content_type=ct)
    edit_resources_permission = Permission.objects.create(codename='edit_resources', name='Allows to edit resources', content_type=ct)
    remove_resources_permission = Permission.objects.create(codename='remove_resources', name='Allows to remove resources', content_type=ct)
    
    add_tags_permission = Permission.objects.create(codename='add_tags', name='Allows to add new tags', content_type=ct)
    view_tags_permission = Permission.objects.create(codename='view_tags', name='Allows to view tags', content_type=ct)
    edit_tags_permission = Permission.objects.create(codename='edit_tags', name='Allows to edit tags', content_type=ct)
    remove_tags_permission = Permission.objects.create(codename='remove_tags', name='Allows to remove tags', content_type=ct)
    assign_tags_permission = Permission.objects.create(codename='assign_tags', name='Allows to assign tags to resource', content_type=ct)
    
    add_users_permission = Permission.objects.create(codename='add_users', name='Allows to add new users', content_type=ct)
    view_users_permission = Permission.objects.create(codename='view_users', name='Allows to view groups and users', content_type=ct)
    edit_users_permission = Permission.objects.create(codename='edit_users', name='Allows to edit users', content_type=ct)
    remove_users_permission = Permission.objects.create(codename='remove_users', name='Allows to remove users', content_type=ct)

    add_waitings_permission = Permission.objects.create(codename='add_waitings', name='Allows to add waiting resource', content_type=ct)
    view_waitings_permission = Permission.objects.create(codename='view_waitings', name='Allows to view waitings', content_type=ct)
    edit_waitings_permission = Permission.objects.create(codename='edit_waitings', name='Allows to edit waitings', content_type=ct)
    remove_waitings_permission = Permission.objects.create(codename='remove_waitings', name='Allows to remove waitings', content_type=ct)


    # Assing permissions to the groups
    # Admin
    admin_group.permissions.add(access_to_categories_permission)
    admin_group.permissions.add(access_to_resources_permission)
    admin_group.permissions.add(access_to_tags_permission)
    admin_group.permissions.add(access_to_users_and_groups_permission)
    admin_group.permissions.add(access_to_waiting_area_permission)
    
    admin_group.permissions.add(add_categories_permission)
    admin_group.permissions.add(view_categories_permission)
    admin_group.permissions.add(edit_categories_permission)
    admin_group.permissions.add(remove_categories_permission)

    admin_group.permissions.add(add_resources_permission)
    admin_group.permissions.add(view_resources_permission)
    admin_group.permissions.add(edit_resources_permission)
    admin_group.permissions.add(remove_resources_permission)

    admin_group.permissions.add(add_tags_permission)
    admin_group.permissions.add(view_tags_permission)
    admin_group.permissions.add(edit_tags_permission)
    admin_group.permissions.add(remove_tags_permission)

    admin_group.permissions.add(add_users_permission)
    admin_group.permissions.add(view_users_permission)
    admin_group.permissions.add(edit_users_permission)
    admin_group.permissions.add(remove_users_permission)

    admin_group.permissions.add(add_waitings_permission)
    admin_group.permissions.add(view_waitings_permission)
    admin_group.permissions.add(edit_waitings_permission)
    admin_group.permissions.add(remove_waitings_permission)

    # Content managers
    content_managers_group.permissions.add(access_to_categories_permission)
    content_managers_group.permissions.add(access_to_resources_permission)
    content_managers_group.permissions.add(access_to_tags_permission)
    content_managers_group.permissions.add(access_to_waiting_area_permission)

    content_managers_group.permissions.add(add_categories_permission)
    content_managers_group.permissions.add(view_categories_permission)
    content_managers_group.permissions.add(edit_categories_permission)
    content_managers_group.permissions.add(remove_categories_permission)

    content_managers_group.permissions.add(add_resources_permission)
    content_managers_group.permissions.add(view_resources_permission)
    content_managers_group.permissions.add(edit_resources_permission)
    content_managers_group.permissions.add(remove_resources_permission)

    content_managers_group.permissions.add(add_tags_permission)
    content_managers_group.permissions.add(view_tags_permission)
    content_managers_group.permissions.add(edit_tags_permission)
    content_managers_group.permissions.add(remove_tags_permission)

    content_managers_group.permissions.add(add_waitings_permission)
    content_managers_group.permissions.add(view_waitings_permission)

    # Tagging group
    tagging_group.permissions.add(access_to_resources_permission)
    tagging_group.permissions.add(access_to_waiting_area_permission)
    tagging_group.permissions.add(access_to_tags_permission)

    tagging_group.permissions.add(assign_tags_permission)

    tagging_group.permissions.add(view_categories_permission)
    tagging_group.permissions.add(view_tags_permission)
    tagging_group.permissions.add(view_resources_permission)

    tagging_group.permissions.add(add_waitings_permission)
    tagging_group.permissions.add(view_waitings_permission)
    tagging_group.permissions.add(edit_waitings_permission)
    tagging_group.permissions.add(remove_waitings_permission)

    print('Groups and permissions have been created and set!')
