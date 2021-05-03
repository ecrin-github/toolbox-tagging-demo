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

    from django.contrib.auth.models import Group
    from django.contrib.contenttypes.models import ContentType
    from users_management.models import ContentManager

    id = 2
    username = 'content_manager'
    password = 'ECRIN_Watt13!!'
    first_name = ''
    last_name = ''
    email = 'mail@mail.org'

    group = Group.objects.get(name='Content managers')

    user = ContentManager(
        id=id,
        username=username, 
        first_name=first_name, 
        last_name=last_name,
        email=email
    )

    user.is_staff = True
    user.is_active = True
    user.is_superuser = True

    user.set_password(password)

    user.save()

    selected_user = ContentManager.objects.get(id=id)
    
    group.user_set.add(selected_user)

    print('Content manager has been created!')
