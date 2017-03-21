# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.contenttypes.fields import (GenericRelation, GenericForeignKey)
from django.contrib.contenttypes.models import ContentType
from django.db import models
# TODO: remove if Django versions < 1.10 are not supported anymore
try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse

from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _
from model_utils.models import TimeStampedModel

GENDER_CHOICES = (
    ('M', _('Male')),
    ('F', _('Female')),
    (' ', _('N/A')),
)


@python_2_unicode_compatible
class Company(TimeStampedModel):
    """ A model which describes a Company """
    companyname = models.CharField(_('companyname'), max_length=200)
    shortname = models.SlugField(_('shortname'), max_length=50, unique=True)
    contact_number = GenericRelation('ContactNumber')
    email_address = GenericRelation('EmailAddress')
    web_site = GenericRelation('WebSite')
    street_address = GenericRelation('StreetAddress')

    class Meta:
        verbose_name = _('company')
        verbose_name_plural = _('companies')

    def __str__(self):
        return "%s" % self.companyname

    def get_absolute_url(self):
        return reverse('bcm:company_detail', kwargs={'pk': self.pk})


@python_2_unicode_compatible
class Person(TimeStampedModel):
    """ A model which describes a single Person. """
    title = models.CharField(_('title'), max_length=200, blank=True)
    first_name = models.CharField(_('first name'), max_length=100)
    last_name = models.CharField(_('last name'), max_length=200)
    nickname = models.CharField(_('nickname'), max_length=50, blank=True)
    gender = models.CharField(_('gender'), max_length=1, choices=GENDER_CHOICES, blank=True)
    # TODO: photo = models.ImageField(_('photo'), upload_to='bcm/person/', blank=True)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True, null=True, verbose_name=_('user'))

    contact_number = GenericRelation('ContactNumber')
    email_address = GenericRelation('EmailAddress')
    web_site = GenericRelation('WebSite')
    street_address = GenericRelation('StreetAddress')

    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('persons')

    def __str__(self):
        return self.fullname

    def get_absolute_url(self):
        return reverse('bcm:person_detail', kwargs={'pk': self.pk})

    @property
    def fullname(self):
        return "%s %s" % (self.first_name, self.last_name)


@python_2_unicode_compatible
class ContactNumber(TimeStampedModel):
    """ Model which describes contactnumbers i.e. Phone, Fax, Pager """
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # TODO: maybe use twilio to check validity
    number_readable = models.CharField(_('readable number'), max_length=20)
    number_raw = models.CharField(_('E.164 number'), max_length=16, unique=True,
                                  help_text=_('i.e. +4930123456 for the number 1234'))
    number_type = models.ForeignKey('NumberType')

    def __str__(self):
        return "%s (%s)" % (self.phone_number, self.number_type)

    class Meta:
        verbose_name = _('contact number')
        verbose_name_plural = _('contact numbers')


@python_2_unicode_compatible
class NumberType(TimeStampedModel):
    """ Model which defines the Type of a number i.e. Fax/Phone/Mobile """
    shortname = models.SlugField(_('shortname'), max_length=50, unique=True)
    description = models.TextField(_('description'), blank=True)

    def __str__(self):
        return "%s" % self.shortname

    class Meta:
        verbose_name = _('number type')
        verbose_name_plural = _('number types')


@python_2_unicode_compatible
class EmailAddress(TimeStampedModel):
    """ Model which describes an Emailaddress. """
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    email_address = models.EmailField(_('email'), unique=True)
    email_type = models.ForeignKey('EmailType')

    def __str__(self):
        return "%s (%s)" % (self.email_address, self.email_type)

    class Meta:
        verbose_name = _('email address')
        verbose_name_plural = _('email addresses')


@python_2_unicode_compatible
class EmailType(TimeStampedModel):
    """ Model which defines the Type of an emailaddress i.e Work/Home """
    shortname = models.SlugField(_('shortname'), max_length=50, unique=True)
    description = models.TextField(_('description'), blank=True)

    def __str__(self):
        return "%s" % self.shortname

    class Meta:
        verbose_name = _('email type')
        verbose_name_plural = _('email types')


@python_2_unicode_compatible
class WebSite(TimeStampedModel):
    """ Model which describes a Website """
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    url = models.URLField(_('url'), unique=True)

    def __str__(self):
        return "%s" % self.url

    class Meta:
        verbose_name = _('website')
        verbose_name_plural = _('websites')


@python_2_unicode_compatible
class StreetAddress(TimeStampedModel):
    """ Model which describes a (postal) address """
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    street = models.TextField(_('street'), blank=True)
    city = models.CharField(_('city'), max_length=200, blank=True)
    province = models.CharField(_('province'), max_length=200, blank=True)
    zipcode = models.CharField(_('zip code'), max_length=10, blank=True)
    country = models.CharField(_('country'), max_length=100)

    address_type = models.ForeignKey('StreetAddressType')

    def __str__(self):
        return "%s (%s)" % (self.city, self.location)

    class Meta:
        verbose_name = _('street address')
        verbose_name_plural = _('street addresses')


@python_2_unicode_compatible
class StreetAddressType(TimeStampedModel):
    """ Model which defines the type of an address (i.e Work/Home/Branchoffice)"""
    shortname = models.SlugField(_('shortname'), max_length=50, unique=True)
    description = models.TextField(_('description'), blank=True)

    def __str__(self):
        return "%s" % self.shortname

    class Meta:
        verbose_name = _('address type')
        verbose_name_plural = _('address types')


@python_2_unicode_compatible
class PersonCompanyRelation(TimeStampedModel):
    """ Model which describes relations Persons ahev with companies """
    person = models.ForeignKey(Person)
    company = models.ForeignKey(Company)
    jobtitle = models.CharField(_('job title'), max_length=100, blank=True)
    description = models.TextField(_('description'), blank=True)

    def __str__(self):
        return _("%s at %s") % (self.person, self.company)

    class Meta:
        verbose_name = _('person company relation')
        verbose_name_plural = _('persons companies relations')
