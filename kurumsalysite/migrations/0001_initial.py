# Generated by Django 2.1.3 on 2019-01-30 22:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iletisim_adsoyad', models.CharField(max_length=100, verbose_name='Gönderenin Ad-Soyadı')),
                ('iletisim_ulasim', models.CharField(max_length=100, verbose_name='Ulaşım Bilgileri')),
                ('iletisim_mesaj', models.TextField(verbose_name='Mesaj')),
                ('iletisim_tarihi', models.DateTimeField(auto_now_add=True, verbose_name='İletişim Formu Gönderilme Tarihi')),
            ],
            options={
                'verbose_name': 'İletişim Talebi',
                'verbose_name_plural': 'İletişim Talepleri',
                'ordering': ('-iletisim_tarihi',),
            },
        ),
        migrations.CreateModel(
            name='Makaleler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('makale_baslik', models.CharField(max_length=150, verbose_name='Makale Başlığı')),
                ('makale_yayintarihi', models.DateField(verbose_name='Makale Yayın Tarihi')),
                ('makale_mesaj', ckeditor.fields.RichTextField()),
                ('makale_slug', models.SlugField(default='', unique=True)),
                ('makale_meta_keywords', models.CharField(max_length=200, verbose_name='Makale Anahtar Kelimeleri')),
                ('makale_meta_description', models.CharField(max_length=350, verbose_name='Makale Meta Açıklaması(SEO İÇİN)')),
                ('makale_author_seo', models.CharField(max_length=50, verbose_name='Makale Yazarı(SEO için kendimiz yazılacak)')),
            ],
            options={
                'verbose_name': 'Makale',
                'verbose_name_plural': 'Makaleler',
                'ordering': ('-makale_yayintarihi',),
            },
        ),
    ]
