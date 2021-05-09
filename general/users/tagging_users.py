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
    from users_management.models import TaggingUser


    group = Group.objects.get(name='Tagging group')

    id_1 = 4
    username_1 = 'tagging_user_1'
    password_1 = 'ECRIN_Watt13!!'
    first_name_1 = ''
    last_name_1 = ''
    email_1 = ''

    user_1 = TaggingUser(
        id=id_1,
        username=username_1, 
        first_name=first_name_1, 
        last_name=last_name_1,
        email=email_1
    )

    user_1.is_staff = True
    user_1.is_active = True
    user_1.is_superuser = True

    user_1.set_password(password_1)

    user_1.save()

    selected_user_1 = TaggingUser.objects.get(id=id_1)
    
    group.user_set.add(selected_user_1)


    id_2 = 5
    username_2 = 'tagging_user_2'
    password_2 = 'ECRIN_Watt13!!'
    first_name_2 = ''
    last_name_2 = ''
    email_2 = ''

    user_2 = TaggingUser(
        id=id_2,
        username=username_2, 
        first_name=first_name_2, 
        last_name=last_name_2,
        email=email_2
    )

    user_2.is_staff = True
    user_2.is_active = True
    user_2.is_superuser = True

    user_2.set_password(password_2)

    user_2.save()

    selected_user_2 = TaggingUser.objects.get(id=id_2)
    
    group.user_set.add(selected_user_2)

    print('Tagging users has been created!')
