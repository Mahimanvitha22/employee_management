import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(editable=False, help_text='Auto-generated unique employee identifier.', max_length=20, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('department', models.CharField(choices=[('HR', 'Human Resources'), ('IT', 'Information Technology'), ('FINANCE', 'Finance'), ('MARKETING', 'Marketing'), ('SALES', 'Sales'), ('OPERATIONS', 'Operations'), ('LEGAL', 'Legal'), ('SUPPORT', 'Customer Support')], max_length=20)),
                ('designation', models.CharField(max_length=100)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(0)])),
                ('joining_date', models.DateField()),
                ('address', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
                'ordering': ['-created_at'],
            },
        ),
    ]
