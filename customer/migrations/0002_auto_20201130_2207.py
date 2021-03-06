# Generated by Django 3.1.2 on 2020-11-30 14:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='audit',
            options={'verbose_name': '审核记录', 'verbose_name_plural': '审核记录'},
        ),
        migrations.AlterModelOptions(
            name='detail',
            options={'verbose_name': '凭证', 'verbose_name_plural': '凭证'},
        ),
        migrations.AlterModelOptions(
            name='hospital',
            options={'verbose_name': '医院', 'verbose_name_plural': '医院'},
        ),
        migrations.AlterModelOptions(
            name='manager',
            options={'verbose_name': '员工', 'verbose_name_plural': '员工'},
        ),
        migrations.AlterModelOptions(
            name='ratio',
            options={'verbose_name': '报销比例', 'verbose_name_plural': '报销比例'},
        ),
        migrations.AlterModelOptions(
            name='record',
            options={'verbose_name': '报销记录', 'verbose_name_plural': '报销记录'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name': '科室', 'verbose_name_plural': '科室'},
        ),
        migrations.AlterModelOptions(
            name='usertype',
            options={'verbose_name': '人员类型', 'verbose_name_plural': '人员类型'},
        ),
        migrations.AddField(
            model_name='apply',
            name='atime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='申请时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manager',
            name='count',
            field=models.IntegerField(default=0, verbose_name='处理数量'),
        ),
        migrations.AddField(
            model_name='manager',
            name='right',
            field=models.IntegerField(default=0, verbose_name='有效数量'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='aid',
            field=models.CharField(max_length=18, verbose_name='申请编号'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='astatus',
            field=models.CharField(choices=[('0', '未提交'), ('1', '申请中'), ('2', '待确认'), ('3', '待报销'), ('4', '已报销')], default='未提交', max_length=20, verbose_name='申请状态'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='isDelete',
            field=models.BooleanField(default=False, null=True, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.user', verbose_name='发起人'),
        ),
        migrations.AlterField(
            model_name='audit',
            name='aid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.apply', verbose_name='申请编号'),
        ),
        migrations.AlterField(
            model_name='audit',
            name='auid',
            field=models.CharField(max_length=10, verbose_name='审核编号'),
        ),
        migrations.AlterField(
            model_name='audit',
            name='austatus',
            field=models.CharField(choices=[('1', '完成'), ('0', '撤销')], default='完成', max_length=20, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='audit',
            name='autime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='审核时间'),
        ),
        migrations.AlterField(
            model_name='audit',
            name='mid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.manager', verbose_name='审核人'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='did',
            field=models.CharField(max_length=10, verbose_name='凭证编号'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='dstatus',
            field=models.CharField(choices=[('0', '验证'), ('1', '合格'), ('-1', '不合格')], default='验证', max_length=20, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='dtime',
            field=models.DateField(verbose_name='时间'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='folder',
            field=models.ImageField(upload_to='images', verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='hname',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='医院'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='money',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='金额'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='rid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.record', verbose_name='报销编号'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='sid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='customer.section', verbose_name='科室'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='type',
            field=models.CharField(choices=[('0', '转诊单'), ('1', '挂号费'), ('2', '发票'), ('3', '补充')], max_length=20, verbose_name='类型'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hid',
            field=models.CharField(max_length=20, verbose_name='医院编号'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hname',
            field=models.CharField(max_length=100, verbose_name='医院名称'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='isDelete',
            field=models.BooleanField(default=False, null=True, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='isDelete',
            field=models.BooleanField(default=False, null=True, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='mid',
            field=models.CharField(max_length=20, verbose_name='账户'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='mname',
            field=models.CharField(max_length=20, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='pw',
            field=models.CharField(max_length=16, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='type',
            field=models.CharField(choices=[('0', '管理员'), ('1', '审核负责人'), ('2', '审核人'), ('3', '收单员')], max_length=20, verbose_name='身份'),
        ),
        migrations.AlterField(
            model_name='ratio',
            name='percent',
            field=models.IntegerField(default=70, verbose_name='报销比例'),
        ),
        migrations.AlterField(
            model_name='ratio',
            name='sid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.section', verbose_name='科室'),
        ),
        migrations.AlterField(
            model_name='ratio',
            name='utype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.usertype', verbose_name='人员类型'),
        ),
        migrations.AlterField(
            model_name='record',
            name='aid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.apply', verbose_name='申请编号'),
        ),
        migrations.AlterField(
            model_name='record',
            name='money',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='金额'),
        ),
        migrations.AlterField(
            model_name='record',
            name='msg',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='record',
            name='rid',
            field=models.CharField(max_length=10, verbose_name='记录编号'),
        ),
        migrations.AlterField(
            model_name='record',
            name='rtime',
            field=models.DateField(auto_now=True, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='section',
            name='isDelete',
            field=models.BooleanField(default=False, null=True, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='section',
            name='sid',
            field=models.CharField(max_length=20, verbose_name='科室编号'),
        ),
        migrations.AlterField(
            model_name='section',
            name='stype',
            field=models.CharField(max_length=20, verbose_name='科室'),
        ),
        migrations.AlterField(
            model_name='user',
            name='isDelete',
            field=models.BooleanField(default=False, null=True, verbose_name='删除状态'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('1', '男'), ('0', '女')], max_length=20, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='user',
            name='utype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.usertype', verbose_name='人员类型'),
        ),
        migrations.AlterField(
            model_name='usertype',
            name='change',
            field=models.IntegerField(default=10, verbose_name='变化幅度/%'),
        ),
        migrations.AlterField(
            model_name='usertype',
            name='limit',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='金额标准'),
        ),
        migrations.AlterField(
            model_name='usertype',
            name='utype',
            field=models.CharField(max_length=20, verbose_name='人员类型'),
        ),
    ]
