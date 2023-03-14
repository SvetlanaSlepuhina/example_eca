from datetime import *
from django.contrib import admin
from app_eca.models import Contract_pr, Spr_kind, Spr_sign, Spr_smeta, Spr_smeta_item

# class ContractInLine(admin.StackedInline):
#     model = Contract_pr
#     actions = ['registration', 'un_registration']
#
#     def registration(self, request, queryset):
#         queryset.update(d_registration=datetime.now())
#
#     def un_registration(self, request, queryset):
#         queryset.update(d_registration=None)
#
#     registration.short_description = 'Зарегистрировать'
#     un_registration.short_description = 'Отменить регистрацию'

@admin.register(Contract_pr)
class Contract_prAdmin(admin.ModelAdmin):
    list_display = ['n_contract', 'd_contract', 'name_work', 'spr_sign', 'spr_kind', 'summa', 'spr_user_cr', 'd_registration']
    list_filter = ['spr_sign', 'spr_kind', 'spr_user_cr']
    search_fields = ['n_contract', 'd_contract', 'name_work']
    # inlines = [ContractInLine]
    actions = ['registration', 'un_registration']

    def registration(self, request, queryset):
        queryset.update(d_registration=datetime.now())

    def un_registration(self, request, queryset):
        queryset.update(d_registration=None)

    registration.short_description = 'Зарегистрировать'
    un_registration.short_description = 'Отменить регистрацию'

    fieldsets = (
        ('Карточка проекта договора', {
            'fields': ('n_contract', 'd_contract', 'name_work', 'spr_sign', 'spr_kind', 'summa'),
            'description': 'Основная информация по проекту договора'
        }),
        ('Отправка на согласование', {
            'fields': ('spr_user_cr', 'd_cr', 'spr_user_ow', 'd_ow', 'spr_user_nach', 'd_nach')
            # 'description': 'Штамп согласования'
        }),
        ('Штамп параллельного согласования', {
            'fields': ('spr_user_peo', 'd_peo', 'spr_user_smeta', 'd_smeta', 'spr_user_kazna', 'd_kazna',
                     'spr_user_zdef', 'd_zdef', 'spr_user_uks', 'd_uks', 'spr_user_oimo', 'd_oimo',
                     'spr_user_uz', 'd_uz',  'spr_user_oeb', 'd_oeb', 'spr_user_dop', 'd_dop'),
            # 'description': 'Паралелельное согласования',
            'classes': ['collapse']
        }),
        ('Штамп последовательного согласования', {
            'fields': ('spr_user_gbuh', 'd_gbuh', 'spr_user_uo', 'd_uo'),
            # 'description': 'Последовательное согласования',
            'classes': ['collapse']
        })


    )

@admin.register(Spr_kind)
class Spr_kindAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Spr_sign)
class Spr_signAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class Spr_smeta_itemInLine(admin.TabularInline):
    model = Spr_smeta_item

@admin.register(Spr_smeta)
class Spr_smetaAdmin(admin.ModelAdmin):
    list_display = ('year','shifr','name',)
    search_fields = ('year','shifr',)
    inlines = [Spr_smeta_itemInLine]

@admin.register(Spr_smeta_item)
class Spr_smeta_itemAdmin(admin.ModelAdmin):
    list_display = ('item','name',)
    search_fields = ('item','name',)

