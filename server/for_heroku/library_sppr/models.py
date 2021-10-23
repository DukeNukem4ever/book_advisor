from django.db import models


class Book(models.Model):
    name = models.CharField("date created", max_length=100, null = True)
    author = models.CharField("date created", max_length=100, null = True)


class Catalog(models.Model):
    recId = models.CharField("Идентификатор каталожной записи", max_length=100, null = True)
    aut = models.CharField("Идентификатор каталожной записи", max_length=100, null = True)
    title = models.CharField("Идентификатор каталожной записи", max_length=100, null = True)
    place = models.CharField("Идентификатор каталожной записи", max_length=100, null = True)
    publ = models.CharField("Идентификатор каталожной записи", max_length=100, null = True)
    yea = models.CharField("Идентификатор каталожной записи", max_length=100, null = True)
    lan = models.CharField("Идентификатор каталожной записи", max_length=100, null = True)
    rubrics = models.CharField("Идентификатор каталожной записи", max_length=100, null = True)
    person = models.CharField("Идентификатор каталожной записи", max_length=100, null = True)
    serial = models.CharField("Идентификатор каталожной записи", max_length=100, null = True)
    material = models.CharField("Идентификатор каталожной записи", max_length=100, null = True)
    biblevel = models.CharField("Идентификатор каталожной записи", max_length=100, null = True)
    ager = models.CharField("Идентификатор каталожной записи", max_length=100, null = True)


class Fund(models.Model):
    fundID = models.CharField("Идентификатор каталожной записи", max_length=100, null = True)
    catalogueRecordID = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    siglaID = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    inventoryNumber = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    barCode = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    trackIndex = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)


class Readers(models.Model):
    abis_id = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    dateOfBirth = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    Address = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)


class Circulaton(models.Model):
    circulationID = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    catalogueRecordID = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    barcode = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    Address = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    startDate = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    finishDate = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    readerID = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    bookpointID = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    state = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)


class Authors(models.Model):
    id = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    author = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)


class Languages(models.Model):
    id = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    lan_short = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    lan_full = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)


class Persons(models.Model):
    id = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    person = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)


class Places(models.Model):
    id = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    place = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)


class Publishers(models.Model):
    id = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    publisher = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)


class Rubrics(models.Model):
    id = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    rubrics = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)


class Series(models.Model):
    id = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    serial = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)


class Cbs(models.Model):
    id = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    name = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)


class Bookpoints(models.Model):
    id = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    cbs = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    name = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    address = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    eisk = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)


class Siglas(models.Model):
    id = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    cbs = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    name = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    address = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    eisk = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)


class Siglaslink(models.Model):
    Sigla = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
    Bookpoint = models.CharField("Идентификатор каталожной записи", max_length=100, null=True)
