from django.db import models

class Contract_pr(models.Model):
    n_contract = models.CharField(max_length=30, verbose_name='Номер')
    d_contract = models.DateField(verbose_name='Дата')
    name_work = models.CharField(max_length=300, verbose_name='Предмет договора')
    summa = models.FloatField(verbose_name='Сумма', default=0)
    spr_kind = models.ForeignKey('Spr_kind', default='', null=True, on_delete=models.SET_NULL, related_name='spr_kind', verbose_name='Вид договора')
    spr_sign = models.ForeignKey('Spr_sign', default='', null=True, on_delete=models.SET_NULL, related_name='spr_sign', verbose_name='Признак договора')
    create_at = models.DateTimeField(auto_now_add=True, db_index=True)
    update_at = models.DateTimeField(auto_now=True)
    spr_user_cr = models.ForeignKey('Spr_user', default='', null=True, on_delete=models.SET_NULL, related_name='spr_user', verbose_name='Куратор оформления')
    d_cr = models.DateField(verbose_name='Дата отправки на согласование', null=True)
    spr_smeta = models.ForeignKey('Spr_smeta', default='', null=True, on_delete=models.SET_NULL, related_name='spr_smeta_main', verbose_name='Смета')
    spr_smeta_item = models.ForeignKey('Spr_smeta_item', default='', null=True, on_delete=models.SET_NULL, related_name='spr_smeta_item', verbose_name='Пункты сметы')
    spr_user_ow = models.ForeignKey('Spr_user', default='', null=True, on_delete=models.SET_NULL, related_name='spr_user_ow', verbose_name='Куратор')
    d_ow = models.DateField(verbose_name='Дата отправки на согласование', null=True)
    spr_user_nach = models.ForeignKey('Spr_user', default='', null=True, on_delete=models.SET_NULL, related_name='spr_user_nach', verbose_name='Начальник подразделения')
    d_nach = models.DateField(verbose_name='Дата согласования', null=True)
    spr_user_peo = models.ForeignKey('Spr_user', default='', null=True, on_delete=models.SET_NULL, related_name='spr_user_peo', verbose_name='Начальник ПЭО')
    d_peo = models.DateField(verbose_name='Дата согласования', null=True)
    spr_user_smeta = models.ForeignKey('Spr_user', default='', null=True, on_delete=models.SET_NULL, related_name='spr_user_smeta', verbose_name='Отвественный за смету')
    d_smeta = models.DateField(verbose_name='Дата согласования', null=True)
    spr_user_kazna = models.ForeignKey('Spr_user', default='', null=True, on_delete=models.SET_NULL, related_name='spr_user_kazna', verbose_name='Начальник Казначейства')
    d_kazna = models.DateField(verbose_name='Дата согласования', null=True)
    spr_user_zdef = models.ForeignKey('Spr_user', default='', null=True, on_delete=models.SET_NULL, related_name='spr_user_zdef', verbose_name='ЗДЭФ')
    d_zdef = models.DateField(verbose_name='Дата согласования', null=True)
    spr_user_uks = models.ForeignKey('Spr_user', default='', null=True, on_delete=models.SET_NULL, related_name='spr_user_uks', verbose_name='УКС. ЗН по учету поставок оборудования')
    d_uks = models.DateField(verbose_name='Дата согласования', null=True)
    spr_user_oimo = models.ForeignKey('Spr_user', default='', null=True, on_delete=models.SET_NULL, related_name='spr_user_oimo', verbose_name='Начальник ОИМО')
    d_oimo = models.DateField(verbose_name='Дата согласования', null=True)
    spr_user_uz = models.ForeignKey('Spr_user', default='', null=True, on_delete=models.SET_NULL, related_name='spr_user_uz', verbose_name='Начальник УЗ')
    d_uz = models.DateField(verbose_name='Дата согласования', null=True)
    spr_user_oeb = models.ForeignKey('Spr_user', default='', null=True, on_delete=models.SET_NULL, related_name='spr_user_oeb', verbose_name='Начальник ОЭБ')
    d_oeb = models.DateField(verbose_name='Дата согласования', null=True)
    spr_user_dop = models.ForeignKey('Spr_user', default='', null=True, on_delete=models.SET_NULL, related_name='spr_user_dop', verbose_name='Дополнительный согласователь')
    d_dop = models.DateField(verbose_name='Дата согласования', null=True)
    spr_user_gbuh = models.ForeignKey('Spr_user', default='', null=True, on_delete=models.SET_NULL, related_name='spr_user_gbuh', verbose_name='Главный бухгалтер')
    d_gbuh = models.DateField(verbose_name='Дата согласования', null=True)
    spr_user_uo = models.ForeignKey('Spr_user', default='', null=True, on_delete=models.SET_NULL, related_name='spr_user_uo', verbose_name='Начальник ЮО')
    d_uo = models.DateField(verbose_name='Дата согласования', null=True)
    d_registration = models.DateField(verbose_name='Дата регистрации', null=True)

    class Meta:
        db_table = 'contract_pr'
        verbose_name = 'проект договора'
        verbose_name_plural = 'проекты'

class Spr_user(models.Model):
    fio = models.CharField(max_length=200, verbose_name='Пользователь')

    class Meta:
        db_table = 'spr_user'
        verbose_name = 'куратор'
        verbose_name_plural = 'кураторы'

    def __str__(self):
        return "%s" % (self.fio)

class Spr_kind(models.Model):
    name = models.CharField(max_length=200, verbose_name='Вид договора')

    class Meta:
        db_table = 'spr_kind'
        verbose_name = 'вид договора'
        verbose_name_plural = 'виды договоров'

    def __str__(self):
        return "%s" % (self.name)

class Spr_sign(models.Model):
    name = models.CharField(max_length=200, verbose_name='Признак договора')

    class Meta:
        db_table = 'spr_sign'
        verbose_name = 'признак договора'
        verbose_name_plural = 'признаки договоров'

    def __str__(self):
        return "%s" % (self.name)

class Spr_smeta(models.Model):
    year = models.IntegerField(verbose_name='Год')
    shifr = models.CharField(max_length=10, verbose_name='Шифр')
    name = models.CharField(max_length=300, verbose_name='Название')

    class Meta:
        db_table = 'spr_smeta'
        verbose_name = 'смета'
        verbose_name_plural = 'сметы'
        ordering = ('year', 'shifr',)

    def __str__(self):
        return f'{self.year}, {self.shifr}'

class Spr_smeta_item(models.Model):
    spr_smeta = models.ForeignKey('Spr_smeta', default='', null=True, on_delete=models.SET_NULL, related_name='spr_smeta', verbose_name='Смета')
    item = models.CharField(max_length=10, verbose_name='Пункт')
    name = models.CharField(max_length=300, verbose_name='Название')

    class Meta:
        db_table = 'spr_smeta_item'
        verbose_name = 'пункт сметы'
        verbose_name_plural = 'пункты сметы'
        ordering = ('spr_smeta', 'item',)

    def __str__(self):
        return f'{self.item}, {self.name}'
