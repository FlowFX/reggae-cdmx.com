"""Model factories for calendar app."""
from app.events.models import Event
from app.venues.factories import VenueFactory

import factory
from factory.django import DjangoModelFactory


def faker(provider, **kwargs):
    """Create localized factory.Faker function."""
    return factory.Faker(provider, locale='es_MX', **kwargs)


class EventFactory(DjangoModelFactory):
    """ModelFactory for the Event object.

    >>> e = EventFactory.build()
    >>> assert e.title
    >>> assert e.date
    >>> assert e.description
    >>> assert e.venue
    >>> assert e.fb_event_url
    """

    class Meta:  # noqa
        model = Event

    id = factory.Sequence(lambda n: n+1)
    title = faker('sentence', nb_words=4)
    date = faker('future_date', end_date="+60d")
    venue = factory.SubFactory(VenueFactory)
    description = faker('paragraph')
    fb_event_url = faker('url')
