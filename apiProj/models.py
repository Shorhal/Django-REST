from django.db import models

# Create your models here.

class Tarif(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="Название", max_length=64, unique=True)
    startDate = models.DateField(verbose_name="Дата начала действия")
    endDate = models.DateField(verbose_name="Дата конца действия")
    minutesCount = models.IntegerField(verbose_name="Объем минут")
    smsCount = models.IntegerField(verbose_name="Объем смс")
    traficCount = models.IntegerField(verbose_name="Объем трафика (мб)")

class Abonent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="Имя", max_length=64)
    currentBalance = models.CharField(verbose_name="Текущий баланс", max_length=100)
    addDate = models.DateField(verbose_name="Дата добавления")
    age = models.IntegerField(verbose_name="Возраст")
    city = models.CharField(verbose_name="Город проживания", max_length=100)
    lastActivity = models.DateField(verbose_name="Временная метка последней активности")
    activeTarif = models.ForeignKey(Tarif, verbose_name="Активный тариф", on_delete=models.CASCADE)


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField(verbose_name="Метка времени")
    abonent = models.ForeignKey(Abonent, verbose_name="id абонента", on_delete=models.CASCADE)
    operationTypes = (
        (1, 'Звонок'),
        (2, 'смс'),
        (3, 'Трафик'),
    )
    operationType = models.CharField(verbose_name="Тип услуги(звонок, смс, трафик)", max_length=16, choices=operationTypes)
    spentValue = models.IntegerField(verbose_name="Объем затраченных единиц")

