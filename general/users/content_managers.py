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


    group = Group.objects.get(name='Content managers')

    # USERS DATA
    # ECRIN
    id_ecrin = 2
    username_ecrin = 'ECRIN_CM'
    password_ecrin = 'ECRIN_CM_1!'
    first_name_ecrin = 'Christian'
    last_name_ecrin = 'Ohmann'
    email_ecrin = ''

    user_ecrin = ContentManager(
        id=id_ecrin,
        username=username_ecrin,
        first_name=first_name_ecrin,
        last_name=last_name_ecrin,
        email=email_ecrin
    )
    user_ecrin.is_staff = True
    user_ecrin.is_superuser = True
    user_ecrin.is_active = True
    user_ecrin.set_password(password_ecrin)
    user_ecrin.save()

    selected_user_ecrin = ContentManager.objects.get(id=id_ecrin)
    group.user_set.add(selected_user_ecrin)

    print('ECRIN content manager has been created!')


    # EATRIS
    id_eatris = 3
    username_eatris = 'EATRIS_CM'
    password_eatris = 'EATRIS_CM_1!!'
    first_name_eatris = ''
    last_name_eatris = ''
    email_eatris = ''

    user_eatris = ContentManager(
        id=id_eatris,
        username=username_eatris,
        first_name=first_name_eatris,
        last_name=last_name_eatris,
        email=email_eatris
    )
    user_eatris.is_staff = True
    user_eatris.is_superuser = True
    user_eatris.is_active = True
    user_eatris.set_password(password_eatris)
    user_eatris.save()

    selected_user_eatris = ContentManager.objects.get(id=id_eatris)
    group.user_set.add(selected_user_eatris)

    print('EATRIS content manager has been created!')


    # BBMRI
    id_bbmri = 4
    username_bbmri = 'BBMRI_CM'
    password_bbmri = 'BBMRI_CM_12!'
    first_name_bbmri = ''
    last_name_bbmri = ''
    email_bbmri = ''

    user_bbmri = ContentManager(
        id=id_bbmri,
        username=username_bbmri,
        first_name=first_name_bbmri,
        last_name=last_name_bbmri,
        email=email_bbmri
    )
    user_bbmri.is_staff = True
    user_bbmri.is_superuser = True
    user_bbmri.is_active = True
    user_bbmri.set_password(password_bbmri)
    user_bbmri.save()

    selected_user_bbmri = ContentManager.objects.get(id=id_bbmri)
    group.user_set.add(selected_user_bbmri)

    print('BBMRI content manager has been created!')


    # EMBRC
    id_embrc = 5
    username_embrc = 'EMBRC_CM'
    password_embrc = 'EMBRC_CM_!12'
    first_name_embrc = ''
    last_name_embrc = ''
    email_embrc = ''

    user_embrc = ContentManager(
        id=id_embrc,
        username=username_embrc,
        first_name=first_name_embrc,
        last_name=last_name_embrc,
        email=email_embrc
    )
    user_embrc.is_staff = True
    user_embrc.is_superuser = True
    user_embrc.is_active = True
    user_embrc.set_password(password_embrc)
    user_embrc.save()

    selected_user_embrc = ContentManager.objects.get(id=id_embrc)
    group.user_set.add(selected_user_embrc)

    print('EMBRC content manager has been created!')


    # ERINHA
    id_erinha = 6
    username_erinha = 'ERINHA_CM'
    password_erinha = 'ERINHA_CM_121!@'
    first_name_erinha = ''
    last_name_erinha = ''
    email_erinha = ''

    user_erinha = ContentManager(
        id=id_erinha,
        username=username_erinha,
        first_name=first_name_erinha,
        last_name=last_name_erinha,
        email=email_erinha
    )
    user_erinha.is_staff = True
    user_erinha.is_superuser = True
    user_erinha.is_active = True
    user_erinha.set_password(password_erinha)
    user_erinha.save()

    selected_user_erinha = ContentManager.objects.get(id=id_erinha)
    group.user_set.add(selected_user_erinha)

    print('ERINHA content manager has been created!')


    # BIO IMAGING
    id_bio_imaging = 7
    username_bio_imaging = 'EURO_BI_CM'
    password_bio_imaging = 'EURO_BI_CM_!@!1'
    first_name_bio_imaging = ''
    last_name_bio_imaging = ''
    email_bio_imaging = ''

    user_bio_imaging = ContentManager(
        id=id_bio_imaging,
        username=username_bio_imaging,
        first_name=first_name_bio_imaging,
        last_name=last_name_bio_imaging,
        email=email_bio_imaging
    )
    user_bio_imaging.is_staff = True
    user_bio_imaging.is_superuser = True
    user_bio_imaging.is_active = True
    user_bio_imaging.set_password(password_bio_imaging)
    user_bio_imaging.save()

    selected_user_bio_imaging = ContentManager.objects.get(id=id_bio_imaging)
    group.user_set.add(selected_user_bio_imaging)

    print('EURO BIO IMAGING content manager has been created!')


    print('Content managers have been created!')
