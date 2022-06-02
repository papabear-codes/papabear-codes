# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aueberweisung(models.Model):
    konto = models.ForeignKey('Konto', models.DO_NOTHING)
    empfaenger_konto = models.CharField(max_length=40)
    empfaenger_name = models.CharField(max_length=140)
    empfaenger_bic = models.CharField(max_length=15, blank=True, null=True)
    betrag = models.FloatField()
    zweck = models.CharField(max_length=140, blank=True, null=True)
    termin = models.DateField()
    banktermin = models.IntegerField(blank=True, null=True)
    umbuchung = models.IntegerField(blank=True, null=True)
    instantpayment = models.IntegerField(blank=True, null=True)
    ausgefuehrt = models.IntegerField()
    ausgefuehrt_am = models.DateTimeField(blank=True, null=True)
    endtoendid = models.CharField(max_length=35, blank=True, null=True)
    pmtinfid = models.CharField(max_length=35, blank=True, null=True)
    purposecode = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aueberweisung'

class Budget(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    budget = models.FloatField()

    class Meta:
        managed = True
        db_table = 'budget'

class Dauerauftrag(models.Model):
    konto = models.ForeignKey('Konto', models.DO_NOTHING)
    empfaenger_konto = models.CharField(max_length=15)
    empfaenger_blz = models.CharField(max_length=15)
    empfaenger_name = models.CharField(max_length=255, blank=True, null=True)
    betrag = models.FloatField()
    zweck = models.CharField(max_length=27)
    zweck2 = models.CharField(max_length=27, blank=True, null=True)
    zweck3 = models.TextField(blank=True, null=True)
    erste_zahlung = models.DateField()
    letzte_zahlung = models.DateField(blank=True, null=True)
    orderid = models.CharField(max_length=100, blank=True, null=True)
    zeiteinheit = models.IntegerField()
    intervall = models.IntegerField()
    tag = models.IntegerField()
    typ = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dauerauftrag'


class Empfaenger(models.Model):
    kontonummer = models.CharField(max_length=15, blank=True, null=True)
    blz = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=255)
    iban = models.CharField(max_length=40, blank=True, null=True)
    bic = models.CharField(max_length=15, blank=True, null=True)
    bank = models.CharField(max_length=140, blank=True, null=True)
    kommentar = models.TextField(blank=True, null=True)
    kategorie = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empfaenger'


class Konto(models.Model):
    kontonummer = models.CharField(max_length=15)
    unterkonto = models.CharField(max_length=30, blank=True, null=True)
    blz = models.CharField(max_length=15)
    name = models.CharField(max_length=255)
    bezeichnung = models.CharField(max_length=255, blank=True, null=True)
    kundennummer = models.CharField(max_length=255)
    waehrung = models.CharField(max_length=6)
    passport_class = models.TextField(blank=True, null=True)
    saldo = models.FloatField(blank=True, null=True)
    saldo_datum = models.DateTimeField(blank=True, null=True)
    kommentar = models.TextField(blank=True, null=True)
    flags = models.IntegerField(blank=True, null=True)
    iban = models.CharField(max_length=40, blank=True, null=True)
    bic = models.CharField(max_length=15, blank=True, null=True)
    saldo_available = models.FloatField(blank=True, null=True)
    kategorie = models.CharField(max_length=255, blank=True, null=True)
    backend_class = models.TextField(blank=True, null=True)
    acctype = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'konto'


class Kontoauszug(models.Model):
    konto = models.ForeignKey(Konto, models.DO_NOTHING)
    ausgefuehrt_am = models.DateTimeField(blank=True, null=True)
    kommentar = models.TextField(blank=True, null=True)
    pfad = models.TextField(blank=True, null=True)
    dateiname = models.TextField(blank=True, null=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    format = models.CharField(max_length=5, blank=True, null=True)
    erstellungsdatum = models.DateField(blank=True, null=True)
    von = models.DateField(blank=True, null=True)
    bis = models.DateField(blank=True, null=True)
    jahr = models.IntegerField(blank=True, null=True)
    nummer = models.IntegerField(blank=True, null=True)
    name1 = models.CharField(max_length=255, blank=True, null=True)
    name2 = models.CharField(max_length=255, blank=True, null=True)
    name3 = models.CharField(max_length=255, blank=True, null=True)
    quittungscode = models.TextField(blank=True, null=True)
    quittiert_am = models.DateTimeField(blank=True, null=True)
    gelesen_am = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kontoauszug'


class Lastschrift(models.Model):
    konto = models.ForeignKey(Konto, models.DO_NOTHING)
    empfaenger_konto = models.CharField(max_length=15)
    empfaenger_blz = models.CharField(max_length=15)
    empfaenger_name = models.CharField(max_length=255, blank=True, null=True)
    betrag = models.FloatField()
    zweck = models.CharField(max_length=27)
    zweck2 = models.CharField(max_length=27, blank=True, null=True)
    zweck3 = models.TextField(blank=True, null=True)
    termin = models.DateField()
    ausgefuehrt = models.IntegerField()
    typ = models.CharField(max_length=2, blank=True, null=True)
    ausgefuehrt_am = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lastschrift'


class Property(models.Model):
    name = models.TextField(unique=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'property'


class Protokoll(models.Model):
    konto = models.ForeignKey(Konto, models.DO_NOTHING)
    kommentar = models.TextField()
    datum = models.DateTimeField()
    typ = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'protokoll'


class Reminder(models.Model):
    uuid = models.CharField(unique=True, max_length=255)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'reminder'


class Sepadauerauftrag(models.Model):
    konto = models.ForeignKey(Konto, models.DO_NOTHING)
    empfaenger_konto = models.CharField(max_length=40)
    empfaenger_name = models.CharField(max_length=140)
    empfaenger_bic = models.CharField(max_length=15, blank=True, null=True)
    betrag = models.FloatField()
    zweck = models.CharField(max_length=140, blank=True, null=True)
    erste_zahlung = models.DateField()
    letzte_zahlung = models.DateField(blank=True, null=True)
    orderid = models.CharField(max_length=100, blank=True, null=True)
    endtoendid = models.CharField(max_length=35, blank=True, null=True)
    zeiteinheit = models.IntegerField()
    intervall = models.IntegerField()
    tag = models.IntegerField()
    canchange = models.IntegerField(blank=True, null=True)
    candelete = models.IntegerField(blank=True, null=True)
    pmtinfid = models.CharField(max_length=35, blank=True, null=True)
    purposecode = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sepadauerauftrag'


class Sepalastschrift(models.Model):
    konto = models.ForeignKey(Konto, models.DO_NOTHING)
    empfaenger_konto = models.CharField(max_length=40)
    empfaenger_name = models.CharField(max_length=140)
    empfaenger_bic = models.CharField(max_length=15, blank=True, null=True)
    betrag = models.FloatField()
    zweck = models.CharField(max_length=140, blank=True, null=True)
    termin = models.DateField()
    ausgefuehrt = models.IntegerField()
    ausgefuehrt_am = models.DateTimeField(blank=True, null=True)
    endtoendid = models.CharField(max_length=35, blank=True, null=True)
    creditorid = models.CharField(max_length=35)
    mandateid = models.CharField(max_length=35)
    sigdate = models.DateField()
    sequencetype = models.CharField(max_length=8)
    sepatype = models.CharField(max_length=8, blank=True, null=True)
    targetdate = models.DateField(blank=True, null=True)
    orderid = models.CharField(max_length=255, blank=True, null=True)
    pmtinfid = models.CharField(max_length=35, blank=True, null=True)
    purposecode = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sepalastschrift'


class Sepaslast(models.Model):
    konto = models.ForeignKey(Konto, models.DO_NOTHING)
    bezeichnung = models.CharField(max_length=255)
    sequencetype = models.CharField(max_length=8)
    sepatype = models.CharField(max_length=8, blank=True, null=True)
    targetdate = models.DateField(blank=True, null=True)
    termin = models.DateField()
    ausgefuehrt = models.IntegerField()
    ausgefuehrt_am = models.DateTimeField(blank=True, null=True)
    orderid = models.CharField(max_length=255, blank=True, null=True)
    pmtinfid = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sepaslast'


class Sepaslastbuchung(models.Model):
    sepaslast = models.ForeignKey(Sepaslast, models.DO_NOTHING)
    empfaenger_konto = models.CharField(max_length=40)
    empfaenger_name = models.CharField(max_length=140)
    empfaenger_bic = models.CharField(max_length=15, blank=True, null=True)
    betrag = models.FloatField()
    zweck = models.CharField(max_length=140, blank=True, null=True)
    endtoendid = models.CharField(max_length=35, blank=True, null=True)
    creditorid = models.CharField(max_length=35)
    mandateid = models.CharField(max_length=35)
    sigdate = models.DateField()
    purposecode = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sepaslastbuchung'


class Sepasueb(models.Model):
    konto = models.ForeignKey(Konto, models.DO_NOTHING)
    bezeichnung = models.CharField(max_length=255)
    termin = models.DateField()
    banktermin = models.IntegerField(blank=True, null=True)
    ausgefuehrt = models.IntegerField()
    ausgefuehrt_am = models.DateTimeField(blank=True, null=True)
    pmtinfid = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sepasueb'


class Sepasuebbuchung(models.Model):
    sepasueb = models.ForeignKey(Sepasueb, models.DO_NOTHING)
    empfaenger_konto = models.CharField(max_length=40)
    empfaenger_name = models.CharField(max_length=140)
    empfaenger_bic = models.CharField(max_length=15, blank=True, null=True)
    betrag = models.FloatField()
    zweck = models.CharField(max_length=140, blank=True, null=True)
    endtoendid = models.CharField(max_length=35, blank=True, null=True)
    purposecode = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sepasuebbuchung'


class Slastbuchung(models.Model):
    slastschrift = models.ForeignKey('Slastschrift', models.DO_NOTHING)
    gegenkonto_nr = models.CharField(max_length=15)
    gegenkonto_blz = models.CharField(max_length=15)
    gegenkonto_name = models.CharField(max_length=255, blank=True, null=True)
    betrag = models.FloatField()
    zweck = models.CharField(max_length=27)
    zweck2 = models.CharField(max_length=27, blank=True, null=True)
    zweck3 = models.TextField(blank=True, null=True)
    typ = models.CharField(max_length=2, blank=True, null=True)
    warnung = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'slastbuchung'


class Slastschrift(models.Model):
    konto = models.ForeignKey(Konto, models.DO_NOTHING)
    bezeichnung = models.CharField(max_length=255)
    termin = models.DateField()
    ausgefuehrt = models.IntegerField()
    ausgefuehrt_am = models.DateTimeField(blank=True, null=True)
    warnungen = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'slastschrift'


class Sueberweisung(models.Model):
    konto = models.ForeignKey(Konto, models.DO_NOTHING)
    bezeichnung = models.CharField(max_length=255)
    termin = models.DateField()
    ausgefuehrt = models.IntegerField()
    ausgefuehrt_am = models.DateTimeField(blank=True, null=True)
    warnungen = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sueberweisung'


class Sueberweisungbuchung(models.Model):
    sueberweisung = models.ForeignKey(Sueberweisung, models.DO_NOTHING)
    gegenkonto_nr = models.CharField(max_length=15)
    gegenkonto_blz = models.CharField(max_length=15)
    gegenkonto_name = models.CharField(max_length=255, blank=True, null=True)
    betrag = models.FloatField()
    zweck = models.CharField(max_length=27)
    zweck2 = models.CharField(max_length=27, blank=True, null=True)
    zweck3 = models.TextField(blank=True, null=True)
    typ = models.CharField(max_length=2, blank=True, null=True)
    warnung = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sueberweisungbuchung'


class Systemnachricht(models.Model):
    blz = models.CharField(max_length=15)
    nachricht = models.TextField()
    datum = models.DateField()
    gelesen = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'systemnachricht'


class Turnus(models.Model):
    zeiteinheit = models.IntegerField()
    intervall = models.IntegerField()
    tag = models.IntegerField()
    initial = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'turnus'


class Ueberweisung(models.Model):
    konto = models.ForeignKey(Konto, models.DO_NOTHING)
    empfaenger_konto = models.CharField(max_length=15)
    empfaenger_blz = models.CharField(max_length=15)
    empfaenger_name = models.CharField(max_length=255, blank=True, null=True)
    betrag = models.FloatField()
    zweck = models.CharField(max_length=27)
    zweck2 = models.CharField(max_length=27, blank=True, null=True)
    zweck3 = models.TextField(blank=True, null=True)
    termin = models.DateField()
    banktermin = models.IntegerField(blank=True, null=True)
    umbuchung = models.IntegerField(blank=True, null=True)
    ausgefuehrt = models.IntegerField()
    typ = models.CharField(max_length=2, blank=True, null=True)
    ausgefuehrt_am = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ueberweisung'


class Umsatz(models.Model):
    konto = models.ForeignKey(Konto, models.DO_NOTHING)
    empfaenger_konto = models.CharField(max_length=40, blank=True, null=True)
    empfaenger_blz = models.CharField(max_length=15, blank=True, null=True)
    empfaenger_name = models.CharField(max_length=255, blank=True, null=True)
    betrag = models.FloatField()
    zweck = models.CharField(max_length=255, blank=True, null=True)
    zweck2 = models.CharField(max_length=35, blank=True, null=True)
    zweck3 = models.TextField(blank=True, null=True)
    datum = models.DateField()
    valuta = models.DateField()
    saldo = models.FloatField(blank=True, null=True)
    primanota = models.CharField(max_length=100, blank=True, null=True)
    art = models.CharField(max_length=500, blank=True, null=True)
    customerref = models.CharField(max_length=100, blank=True, null=True)
    kommentar = models.TextField(blank=True, null=True)
    checksum = models.BigIntegerField(blank=True, null=True)
    umsatztyp = models.ForeignKey('Umsatztyp', models.DO_NOTHING, blank=True, null=True)
    flags = models.IntegerField(blank=True, null=True)
    gvcode = models.CharField(max_length=3, blank=True, null=True)
    addkey = models.CharField(max_length=3, blank=True, null=True)
    txid = models.CharField(max_length=100, blank=True, null=True)
    purposecode = models.CharField(max_length=10, blank=True, null=True)
    endtoendid = models.CharField(max_length=100, blank=True, null=True)
    mandateid = models.CharField(max_length=100, blank=True, null=True)
    empfaenger_name2 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'umsatz'


class Umsatztyp(models.Model):
    name = models.CharField(max_length=255)
    nummer = models.CharField(max_length=5, blank=True, null=True)
    pattern = models.TextField(blank=True, null=True)
    isregex = models.IntegerField(blank=True, null=True)
    umsatztyp = models.IntegerField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, related_name='+')
    color = models.CharField(max_length=11, blank=True, null=True)
    customcolor = models.IntegerField(blank=True, null=True)
    kommentar = models.TextField(blank=True, null=True)
    konto = models.ForeignKey(Konto, models.DO_NOTHING, blank=True, null=True)
    konto_kategorie = models.CharField(max_length=255, blank=True, null=True)
    flags = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'umsatztyp'


class Version(models.Model):
    name = models.CharField(max_length=255)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'version'
