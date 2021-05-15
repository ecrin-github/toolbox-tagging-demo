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


    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType
    from users_management.models import User


    # Groups creation
    project_coordinators_group, created = Group.objects.get_or_create(name='Project coordinators')
    content_managers_group, created = Group.objects.get_or_create(name='Content managers')
    tagging_group, created = Group.objects.get_or_create(name='Tagging group')


    # Content type
    ct = ContentType.objects.get_for_model(User)


    # Create custom permissions
    # Categories and tagging access
    access_to_categories_permission = Permission.objects.create(codename='access_to_categories', name='Access to the Categories sections', content_type=ct)
    add_categories_permission = Permission.objects.create(codename='add_categories', name='Allows to add new categories parameters', content_type=ct)
    view_categories_permission = Permission.objects.create(codename='view_categories', name='Allows to view categories', content_type=ct)
    edit_categories_permission = Permission.objects.create(codename='edit_categories', name='Allows to edit categories parameters', content_type=ct)
    remove_categories_permission = Permission.objects.create(codename='remove_categories', name='Allows to remove categories parameters', content_type=ct)
    add_categories_comments_permission = Permission.objects.create(codename='add_categories_comments', name='Allows to comment categories', content_type=ct)
    view_categories_comments_permission = Permission.objects.create(codename='view_categories_comments', name='Allows to view categories comments', content_type=ct)
    edit_categories_comments_permission = Permission.objects.create(codename='edit_categories_comments', name='Allows to edit categories comments', content_type=ct)
    remove_categories_comments_permission = Permission.objects.create(codename='remove_categories_comments', name='Allows to remove categories comments', content_type=ct)
    assign_categories_permission = Permission.objects.create(codename='assign_categories', name='Allows to assign categories to resource', content_type=ct)

    # Resources
    access_to_resources_permission = Permission.objects.create(codename='access_to_resources', name='Access to the Resources sections', content_type=ct)
    add_resources_permission = Permission.objects.create(codename='add_resources', name='Allows to add new resources', content_type=ct)
    view_resources_permission = Permission.objects.create(codename='view_resources', name='Allows to view resources', content_type=ct)
    edit_resources_permission = Permission.objects.create(codename='edit_resources', name='Allows to edit resources', content_type=ct)
    remove_resources_permission = Permission.objects.create(codename='remove_resources', name='Allows to remove resources', content_type=ct)
    add_resources_comments_permission = Permission.objects.create(codename='add_resources_comments', name='Allows to comment resources', content_type=ct)
    edit_resources_comments_permission = Permission.objects.create(codename='edit_resources_comments', name='Allows to edit resources comments', content_type=ct)
    view_resources_comments_permission = Permission.objects.create(codename='view_resources_comments', name='Allows to view resources comments', content_type=ct)
    remove_resources_comments_permission = Permission.objects.create(codename='remove_resources_comments', name='Allows to remove resources comments', content_type=ct)
    assign_tagging_user_permission = Permission.objects.create(codename='assign_tagging_user', name='Allows to assign tagging user(s)', content_type=ct)
    change_tagging_user_permission = Permission.objects.create(codename='change_tagging_user', name='Allows to change tagging user(s)', content_type=ct)
    remove_tagging_user_permission = Permission.objects.create(codename='remove_tagging_user', name='Allows to remove tagging user(s)', content_type=ct)
    approve_resource_permission = Permission.objects.create(codename='approve_resource', name='Allows to approve resource', content_type=ct)
    decline_resource_permission = Permission.objects.create(codename='decline_resource', name='Allows to decline resource', content_type=ct)

    # Users and groups
    access_to_users_and_groups_permission = Permission.objects.create(codename='access_to_users_and_groups', name='Access to the Users and Groups sections', content_type=ct)
    add_users_permission = Permission.objects.create(codename='add_users', name='Allows to add new users', content_type=ct)
    view_users_permission = Permission.objects.create(codename='view_users', name='Allows to view groups and users', content_type=ct)
    edit_users_permission = Permission.objects.create(codename='edit_users', name='Allows to edit users', content_type=ct)
    remove_users_permission = Permission.objects.create(codename='remove_users', name='Allows to remove users', content_type=ct)


    # Assing permissions to the groups
    # Project coordinators
    # Categories permissions
    project_coordinators_group.permissions.add(access_to_categories_permission)
    project_coordinators_group.permissions.add(add_categories_permission)
    project_coordinators_group.permissions.add(view_categories_permission)
    project_coordinators_group.permissions.add(edit_categories_permission)
    project_coordinators_group.permissions.add(remove_categories_permission)
    project_coordinators_group.permissions.add(add_categories_comments_permission)
    project_coordinators_group.permissions.add(view_categories_comments_permission)
    project_coordinators_group.permissions.add(edit_categories_comments_permission)
    project_coordinators_group.permissions.add(remove_categories_comments_permission)
    project_coordinators_group.permissions.add(assign_categories_permission)

    # Resources permissions
    project_coordinators_group.permissions.add(access_to_resources_permission)
    project_coordinators_group.permissions.add(add_resources_permission)
    project_coordinators_group.permissions.add(view_resources_permission)
    project_coordinators_group.permissions.add(edit_resources_permission)
    project_coordinators_group.permissions.add(remove_resources_permission)
    project_coordinators_group.permissions.add(add_resources_comments_permission)
    project_coordinators_group.permissions.add(edit_resources_comments_permission)
    project_coordinators_group.permissions.add(view_resources_comments_permission)
    project_coordinators_group.permissions.add(remove_resources_comments_permission)
    project_coordinators_group.permissions.add(assign_tagging_user_permission)
    project_coordinators_group.permissions.add(change_tagging_user_permission)
    project_coordinators_group.permissions.add(remove_tagging_user_permission)
    project_coordinators_group.permissions.add(approve_resource_permission)
    project_coordinators_group.permissions.add(decline_resource_permission)

    # Users and groups permissions
    project_coordinators_group.permissions.add(access_to_users_and_groups_permission)
    project_coordinators_group.permissions.add(add_users_permission)
    project_coordinators_group.permissions.add(view_users_permission)
    project_coordinators_group.permissions.add(edit_users_permission)
    project_coordinators_group.permissions.add(remove_users_permission)


    # Content managers
    # Categories
    content_managers_group.permissions.add(access_to_categories_permission)
    content_managers_group.permissions.add(view_categories_permission)
    content_managers_group.permissions.add(add_categories_comments_permission)
    content_managers_group.permissions.add(view_categories_comments_permission)
    content_managers_group.permissions.add(edit_categories_comments_permission)
    content_managers_group.permissions.add(remove_categories_comments_permission)
    content_managers_group.permissions.add(assign_categories_permission)

    # Resources
    content_managers_group.permissions.add(access_to_resources_permission)
    content_managers_group.permissions.add(add_resources_permission)
    content_managers_group.permissions.add(view_resources_permission)
    content_managers_group.permissions.add(edit_resources_permission)
    content_managers_group.permissions.add(remove_resources_permission)
    content_managers_group.permissions.add(add_resources_comments_permission)
    content_managers_group.permissions.add(edit_resources_comments_permission)
    content_managers_group.permissions.add(view_resources_comments_permission)
    content_managers_group.permissions.add(remove_resources_comments_permission)
    content_managers_group.permissions.add(assign_tagging_user_permission)
    content_managers_group.permissions.add(change_tagging_user_permission)
    content_managers_group.permissions.add(remove_tagging_user_permission)
    content_managers_group.permissions.add(approve_resource_permission)
    content_managers_group.permissions.add(decline_resource_permission)
    

    # Tagging group users
    # Categories
    tagging_group.permissions.add(access_to_categories_permission)
    tagging_group.permissions.add(view_categories_permission)
    tagging_group.permissions.add(add_categories_comments_permission)
    tagging_group.permissions.add(view_categories_comments_permission)
    tagging_group.permissions.add(edit_categories_comments_permission)
    tagging_group.permissions.add(remove_categories_comments_permission)
    tagging_group.permissions.add(assign_categories_permission)
    
    # Resources
    tagging_group.permissions.add(access_to_resources_permission)
    tagging_group.permissions.add(view_resources_permission)
    tagging_group.permissions.add(add_resources_comments_permission)
    tagging_group.permissions.add(edit_resources_comments_permission)
    tagging_group.permissions.add(view_resources_comments_permission)
    tagging_group.permissions.add(remove_resources_comments_permission)


    # Printing out the opertation's result
    print('Groups and permissions have been created and set!')
