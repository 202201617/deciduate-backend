# Generated by Django 5.0.4 on 2024-05-06 06:38

import django.db.models.deletion
import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(choices=[('M', '전공'), ('L', '교양')], max_length=2, verbose_name='개설영역')),
                ('grade', models.IntegerField(verbose_name='학년')),
                ('code', models.CharField(max_length=11, verbose_name='학수번호')),
                ('name', models.CharField(max_length=30, verbose_name='과목명')),
                ('professor', models.CharField(max_length=30, verbose_name='교수')),
                ('credit', models.IntegerField(verbose_name='학점')),
            ],
            options={
                'db_table': 'subject',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='전공명')),
                ('campus', models.CharField(choices=[('S', '서울'), ('G', '글로벌')], max_length=1, verbose_name='캠퍼스')),
                ('college', models.CharField(max_length=30, verbose_name='단과대학')),
            ],
            options={
                'db_table': 'major',
            },
        ),
        migrations.CreateModel(
            name='LiberalCompulsory',
            fields=[
                ('subject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.subject')),
                ('compulsory', models.BooleanField(verbose_name='교양 필수')),
            ],
            options={
                'db_table': 'liberal_compulsory',
            },
            bases=('users.subject',),
        ),
        migrations.CreateModel(
            name='MajorCompulsory',
            fields=[
                ('subject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.subject')),
                ('main_compulsory', models.BooleanField(verbose_name='본전공 필수')),
                ('sub_compulsory', models.BooleanField(verbose_name='이중/부전공 필수')),
            ],
            options={
                'db_table': 'major_compulsory',
            },
            bases=('users.subject',),
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='이메일')),
                ('nickname', models.CharField(max_length=20, unique=True, verbose_name='닉네임')),
                ('student_no', models.CharField(max_length=10, unique=True, verbose_name='학번')),
                ('major_type', models.IntegerField(choices=[(1, '전공심화'), (2, '이중전공'), (3, '부전공'), (4, '전공심화+부전공')], verbose_name='전공유형')),
                ('transfer', models.BooleanField(blank=True, default=False, verbose_name='편입생')),
                ('foreign', models.BooleanField(blank=True, default=False, verbose_name='외국인전형')),
                ('is_superuser', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('double_major', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users_double', to='users.major', verbose_name='이중전공')),
                ('main_major', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users_main', to='users.major', verbose_name='본전공')),
                ('minor_major', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users_minor', to='users.major', verbose_name='부전공')),
            ],
            options={
                'db_table': 'user',
            },
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24')], verbose_name='학년')),
                ('liberal_compulsory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='users.liberalcompulsory', verbose_name='교양 필수')),
                ('major_compulsory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='users.majorcompulsory', verbose_name='전공 필수')),
            ],
            options={
                'db_table': 'grade',
            },
        ),
    ]
