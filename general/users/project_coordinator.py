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
    from users_management.models import ProjectCoordinator


    group = Group.objects.get(name='Project coordinators')

    id = 1
    username = 'project_coordinator'
    password = 'ECRIN_Watt13!!'
    first_name = 'Sergei'
    last_name = 'Gorianin'
    email = 'sergei.gorianin@ecrin.org'

    user = ProjectCoordinator(
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

    selected_user = ProjectCoordinator.objects.get(id=id)
    
    group.user_set.add(selected_user)

    print('Project coordinator user has been created!')
