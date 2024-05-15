# Generated by Django 5.0.4 on 2024-05-05 20:58

import applibreria.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id_aut', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
                'db_table': 'autor',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id_cont', models.AutoField(primary_key=True, serialize=False)),
                ('email_cont', models.CharField(max_length=100)),
                ('fullname', models.CharField(max_length=100)),
                ('menssenger', models.TextField(max_length=1500)),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id_gen', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
                'db_table': 'genre',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id_pub', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Publisher',
                'verbose_name_plural': 'Publishers',
                'db_table': 'publisher',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id_sal', models.AutoField(primary_key=True, serialize=False)),
                ('sale_date', models.DateField(auto_now=True)),
                ('delivery_type', models.BooleanField(default=False)),
                ('payment_type', models.BooleanField(default=False)),
                ('total_quantity', models.IntegerField(default=0)),
                ('total_cost', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
            options={
                'verbose_name': 'Sale',
                'verbose_name_plural': 'Sales',
                'db_table': 'sale',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id_book', models.AutoField(primary_key=True, serialize=False)),
                ('isbn', models.IntegerField(blank=True)),
                ('title', models.CharField(max_length=100)),
                ('pages', models.IntegerField(blank=True)),
                ('releaseyear', models.IntegerField(blank=True)),
                ('bookcover', models.CharField(blank=True, max_length=150)),
                ('stock', models.IntegerField()),
                ('synopsis', models.TextField(max_length=2000)),
                ('price', models.DecimalField(decimal_places=2, default=1, max_digits=10)),
                ('id_aut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applibreria.autor')),
                ('id_pub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applibreria.publisher')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='BookGenre',
            fields=[
                ('id_bg', models.AutoField(primary_key=True, serialize=False)),
                ('id_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applibreria.book')),
                ('id_gen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applibreria.genre')),
            ],
            options={
                'verbose_name': 'GenreOfBook',
                'verbose_name_plural': 'GenresOfBooks',
                'db_table': 'book_genre',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id_pro', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('id_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applibreria.book')),
                ('id_sal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applibreria.sale')),
            ],
            options={
                'verbose_name': 'Products',
                'verbose_name_plural': 'Products',
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('dni', models.IntegerField(blank=True)),
                ('address_province', models.CharField(blank=True, max_length=30)),
                ('address_location', models.CharField(blank=True, max_length=30)),
                ('address_street', models.CharField(blank=True, max_length=50)),
                ('address_number', models.IntegerField(blank=True)),
                ('id_rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applibreria.role')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'user',
            },
        ),
        migrations.AddField(
            model_name='sale',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applibreria.user'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id_pay', models.AutoField(primary_key=True, serialize=False)),
                ('namecard', models.CharField(max_length=30)),
                ('numbercard', models.IntegerField()),
                ('exp_date', applibreria.models.MonthYearField()),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applibreria.user')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
                'db_table': 'payment',
            },
        ),
        migrations.CreateModel(
            name='Credential',
            fields=[
                ('id_cred', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100)),
                ('psw', models.CharField(max_length=255)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applibreria.user')),
            ],
            options={
                'verbose_name': 'Credential',
                'verbose_name_plural': 'Credentials',
                'db_table': 'credential',
            },
        ),
    ]
